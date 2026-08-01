from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.auth.services import get_current_active_user
from app.core.database import get_session
from app.invite.models import Invite, InviteStatus
from app.invite.schemas import InviteCreate, InviteInfo, InviteResponse
from app.invite.services import send_invite
from app.organization_user.schemas import OrganizationUserCreate
from app.organization_user.services import create_organization_user, membership
from app.user.models import User
from app.user.schemas import UserInfo

router = APIRouter(
    prefix="/invite",
    tags=["invite"],
)

SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_invite(
    session: SessionDep,
    invite_data: InviteCreate,
    current_user: Annotated[UserInfo, Depends(get_current_active_user)],
):
    try:
        if (
            invite_data.user_identifier == current_user.email
            or invite_data.user_identifier == current_user.username
        ):
            raise ValueError("You cannot invite yourself")
        if membership(session, invite_data.organization_id, current_user.id):
            send_invite(session, invite_data, current_user.id)
            return {
                "message": f"invite has been successfully sent to {invite_data.user_identifier}"
            }
        else:
            raise ValueError("You are not a member of this organization")
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.args[0])


@router.get("/received", response_model=list[InviteInfo])
def get_received_invites(
    session: SessionDep,
    current_user: Annotated[UserInfo, Depends(get_current_active_user)],
):
    invites = (
        session.query(Invite)
        .filter(
            or_(
                Invite.status == InviteStatus.PENDING,
                Invite.status == InviteStatus.SEEN,
            ),
            or_(
                Invite.user_identifier == current_user.email,
            ),
        )
        .all()
    )
    return invites


@router.post("/flag-invites-seen")
def flag_invites_seen(
    session: SessionDep,
    current_user: Annotated[UserInfo, Depends(get_current_active_user)],
):
    invites = (
        session.query(Invite)
        .filter(
            Invite.status == InviteStatus.PENDING,
            Invite.user_identifier == current_user.email,
        )
        .all()
    )
    for invite in invites:
        invite.status = InviteStatus.SEEN
    session.commit()


@router.get("/new_invites_count")
def get_invites(
    session: SessionDep,
    current_user: Annotated[UserInfo, Depends(get_current_active_user)],
):
    count = (
        session.query(Invite)
        .filter(
            Invite.status == InviteStatus.PENDING,
            Invite.user_identifier == current_user.email,
        )
        .count()
    )
    return count


@router.post("/invite-response")
def invite_response(
    session: SessionDep,
    body: InviteResponse,
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    invite = session.get(Invite, body.invite_id)

    if not invite:
        raise HTTPException(404, "Invite not found")

    if not (
        invite.user_identifier == current_user.email
        or invite.user_identifier == current_user.username
    ):
        raise HTTPException(403, "This invite is not for you")

    if invite.status == InviteStatus.ACCEPTED or invite.status == InviteStatus.REJECTED:
        raise HTTPException(400, "Invite is already responded to")

    if body.status == InviteStatus.ACCEPTED:
        try:
            create_organization_user(
                session,
                OrganizationUserCreate(
                    user_id=current_user.id, organization_id=invite.organization_id
                ),
                commit=False,
            )
            invite.status = InviteStatus.ACCEPTED
        except ValueError:
            raise HTTPException(400, "Organization user already exists")
    elif body.status == InviteStatus.REJECTED:
        invite.status = InviteStatus.REJECTED

    session.commit()
    return {"message": f"Invite {body.status}"}
