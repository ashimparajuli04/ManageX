from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth.services import get_current_active_user
from app.core.database import get_session
from app.invite.schemas import InviteCreate
from app.invite.services import send_invite
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
    send_invite(session, invite_data, current_user.id)
    return {"message": f"invite has been cussessfully sent to {invite_data.email}"}
