from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class RoleInstancePermission(Base):
    __tablename__ = "role_instance_permissions"

    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id"),
        primary_key=True,
    )

    instance_permission_id: Mapped[int] = mapped_column(
        ForeignKey("instance_permissions.id"),
        primary_key=True,
    )
