from enum import Enum

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class UserRole(str, Enum):
    ADMIN = "admin"
    EMPLOYEE = "employee"
    USER = "user"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True,
    )

    username: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True,
    )

    first_name: Mapped[str] = mapped_column(String)

    middle_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    last_name: Mapped[str] = mapped_column(String)

    password_hash: Mapped[str] = mapped_column(String)

    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole),
        default=UserRole.EMPLOYEE,
    )

    is_active: Mapped[bool] = mapped_column(default=True)