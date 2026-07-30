from typing import Annotated
from webbrowser import get

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.services import get_current_active_user
from app.core.database import get_session
from app.invite.schemas import InviteCreate
from app.invite.services import send_invite
from app.organization_user.services import membership
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
        if invite_data.user_identifier == current_user.email or invite_data.user_identifier == current_user.username:
            raise ValueError("You cannot invite yourself")
        membership(session, invite_data.organization_id, current_user.id)
        send_invite(session, invite_data, current_user.id)
        return {"message": f"invite has been successfully sent to {invite_data.user_identifier}"}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.args[0])
