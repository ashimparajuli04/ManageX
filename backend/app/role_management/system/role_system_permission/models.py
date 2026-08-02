from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class RoleSystemPermission(Base):
    __tablename__ = "role_system_permissions"

    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id"),
        primary_key=True,
    )

    system_permission_id: Mapped[int] = mapped_column(
        ForeignKey("system_permissions.id"),
        primary_key=True,
    )