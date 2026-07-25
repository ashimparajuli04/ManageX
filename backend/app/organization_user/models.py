from enum import Enum

from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.properties import ForeignKey

from app.core.database import Base
from app.organization.models import Organization
from app.user.models import User


class UserRole(str, Enum):
    ADMIN = "admin"
    EMPLOYEE = "employee"
    USER = "user"


class OrganizationUsers(Base):
    __tablename__ = "organization_users"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))
    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole),
        default=UserRole.EMPLOYEE,
    )
    user: Mapped[User] = relationship()
    organization: Mapped[Organization] = relationship()
