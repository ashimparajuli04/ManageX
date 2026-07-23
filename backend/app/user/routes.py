from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.user.schemas import UserCreate
from app.user.services import create_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

SessionDep = Annotated[Session, Depends(get_session)]

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def create_new_user(user_data: UserCreate, session: SessionDep):
    try:
        return create_user(session, user_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.args[0],
        )
