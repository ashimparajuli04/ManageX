import os
from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from sqlalchemy.orm import Session

from app.auth.schemas import TokenData
from app.auth.utils import verify_password
from app.core.database import get_session
from app.user.models import User, UserRole
from app.user.services import get_user_by_email

load_dotenv()


SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

SessionDep = Annotated[Session, Depends(get_session)]


def authenticate_user(
    email: str,
    password: str,
    session: Session,  # ✅ plain Session
):

    user = get_user_by_email(session, email)
    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user


def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None,
):
    to_encode = data.copy()

    expire = (
        datetime.now(timezone.utc) + expires_delta
        if expires_delta
        else datetime.now(timezone.utc) + timedelta(minutes=15)
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: SessionDep,
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],  # type: ignore
        )
        email = payload.get("sub")
        if email is None:
            raise credentials_exception

        token_data = TokenData(email=email)

    except PyJWTError:
        raise credentials_exception

    user = get_user_by_email(session, token_data.email)
    if not user:
        raise credentials_exception

    return user


def get_current_active_user(
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_active:
        raise HTTPException(
            status_code=400,
            detail="Inactive user",
        )
    return current_user


# def require_role(*roles: UserRole):
#     def checker(user: User = Depends(get_current_active_user)):
#         print("USER ROLE:", user.role)
#         print("REQUIRED ROLES:", roles)

#         if user.role not in roles:
#             raise HTTPException(status_code=403, detail="Forbidden")
#         return user

#     return checker


def require_admin(user: User = Depends(get_current_active_user)):
    if user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Forbidden")
    return user


# def require_staff():
#     return Depends(require_role(UserRole.ADMIN, UserRole.EMPLOYEE))
