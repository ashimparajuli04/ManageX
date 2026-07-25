from sqlalchemy import select
from sqlalchemy.orm import Session

from app.auth.utils import get_password_hash
from app.user.models import User
from app.user.schemas import UserCreate


def get_user_by_email(session: Session, email: str):
    statement = select(User).where(User.email == email)
    return session.scalar(statement)

def get_user_by_username(session: Session, username: str):
    statement = select(User).where(User.username == username)
    return session.scalar(statement)

def get_email_by_username(session: Session, username: str):
    statement = select(User.email).where(User.username == username)
    return session.scalar(statement)


def create_user(session: Session, user_data: UserCreate):
    errors = {}
    
    if get_user_by_email(session, user_data.email):
        errors["email"] = "User with this email already exists"
    if get_user_by_username(session, user_data.username):
        errors["username"] = "User with this username already exists"
    if errors:
        raise ValueError(errors)
    

    user = User(
        email=user_data.email,
        username=user_data.username,
        first_name=user_data.first_name,
        middle_name=user_data.middle_name,
        last_name=user_data.last_name,
        password_hash=get_password_hash(user_data.password),
    )
    
    session.add(user)
    session.commit()