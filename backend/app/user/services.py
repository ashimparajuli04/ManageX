from sqlalchemy import inspect, select
from sqlalchemy.orm import Session

from app.user.models import User
from app.user.schemas import UserCreate
from app.auth.utils import get_password_hash


def get_user_by_email(session: Session, email: str):
    statement = select(User).where(User.email == email)
    return session.scalar(statement)

def get_user_by_username(session: Session, username: str):
    statement = select(User).where(User.username == username)
    return session.scalar(statement)


def create_user(session: Session, user_data: UserCreate):

    if get_user_by_email(session, user_data.email):
        raise ValueError("User with this email already exists")

    user = User(
        email=user_data.email,
        first_name=user_data.first_name,
        middle_name=user_data.middle_name,
        last_name=user_data.last_name,
        password_hash=get_password_hash(user_data.password),
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return inspect(user).dict