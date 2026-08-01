from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.invite.models import Invite, InviteStatus
from app.invite.schemas import InviteCreate
from app.organization_user.services import membership
from app.user.services import get_user_by_email_username


def send_invite(session: Session, invite_data: InviteCreate, user_id: int):
    user = get_user_by_email_username(session, invite_data.user_identifier)
    if user and membership(session, invite_data.organization_id, user.id):
        raise ValueError("User is already a member of this organization")
    if "@" not in invite_data.user_identifier and not user:
        raise ValueError("User with this username does not exist")
    if user:
        invite_data.user_identifier = user.email
    existing_invite = session.scalar(
        select(Invite).where(
            Invite.user_identifier == invite_data.user_identifier,
            Invite.organization_id == invite_data.organization_id,
            Invite.invited_by == user_id,
        )
    )
    if existing_invite:
        existing_invite.status = InviteStatus.PENDING
        existing_invite.created_at = datetime.now(UTC)
        session.commit()
        return existing_invite
    invite = Invite(
        user_identifier=invite_data.user_identifier,
        organization_id=invite_data.organization_id,
        invited_by=user_id,
    )
    session.add(invite)
    session.commit()
    return invite
