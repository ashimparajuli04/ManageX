from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.organization.models import Organization
    from app.user.models import User


class OrganizationUser(Base):
    __tablename__ = "organization_users"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))
    date_joined: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )
    role_id: Mapped[int] = mapped_column()
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "organization_id",
            name="unique_user_organization",
        ),
    )

    user: Mapped[User] = relationship(back_populates="organization_users")
    organization: Mapped[Organization] = relationship(
        back_populates="organization_users"
    )
