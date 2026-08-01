from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.role_management.system_permission.models import Action


class RoleInstancePermission(Base):
    __tablename__ = "role_instance_permissions"

    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id"),
        primary_key=True,
    )
    instance_id: Mapped[int] = mapped_column(
        ForeignKey("module_instances.id"),
        index=True,
        primary_key=True,
    )

    action: Mapped[Action] = mapped_column(String, primary_key=True)
