from enum import Enum
from turtle import back

from sqlalchemy import Enum as SQLEnum, UniqueConstraint
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.organization.models import Organization
from app.user.models import User


class UserRole(str, Enum):
    ADMIN = "admin"
    EMPLOYEE = "employee"
    USER = "user"


class OrganizationUser(Base):
    __tablename__ = "organization_users"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "organization_id",
            name="unique_user_organization",
        ),
    )

    user: Mapped[User] = relationship(back_populates="organization_users")
    organization: Mapped[Organization] = relationship(back_populates="organization_users")
