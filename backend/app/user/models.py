from sqlalchemy import Enum as SQLEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.organization_user.models import OrganizationUser


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

    is_active: Mapped[bool] = mapped_column(default=True)

    organization_users: Mapped[list[OrganizationUser]] = relationship(
        back_populates="user"
    )
