from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.services import get_current_active_user
from app.core.database import get_session
from app.user.models import User
from app.user.schemas import UserCreate, UserInfo
from app.user.services import create_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

SessionDep = Annotated[Session, Depends(get_session)]

@router.post("/signup",
    status_code=status.HTTP_201_CREATED,
)
def create_new_user(user_data: UserCreate, session: SessionDep):
    try:
        create_user(session, user_data)
        return {"message": "User has been successfully created"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.args[0],
        )

@router.get("/", response_model=UserInfo)
def get_my_info(session: SessionDep, current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user
