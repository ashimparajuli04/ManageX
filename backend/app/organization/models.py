from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.organization_user.models import OrganizationUser
    from app.role_management.role.models import Role
    from app.user.models import User


class Organization(Base):
    __tablename__ = "organizations"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    organization_users: Mapped[list[OrganizationUser]] = relationship(
        back_populates="organization"
    )
    owner: Mapped[User] = relationship(back_populates="owned_organizations")
    roles: Mapped[list[Role]] = relationship()
