from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"), index=True)
    __table_args__ = (
        UniqueConstraint(
            "name",
            "organization_id",
            name="unique_name_organization",
        ),
    )
