from sqlalchemy import select
from sqlalchemy.orm import Session

from app.user.models import User


def get_user_by_email(session: Session, email: str):
    statement = select(User).where(User.email == email)
    return session.scalar(statement)