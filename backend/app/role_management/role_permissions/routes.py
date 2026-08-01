from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.services import get_current_active_user
from app.core.database import get_session

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(
    prefix = "/role-permissions",
    tags = ["role-permissions"]
)

@router.post("/")
def provide_permissions(session = SessionDep, organization_id: int, current_user = Depends(get_current_active_user)):
    