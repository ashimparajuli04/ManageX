from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.role_management.system.system_permission.models import Action


class InstancePermission(Base):
    __tablename__ = "instance_permissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    instance_id: Mapped[int] = mapped_column(
        ForeignKey("module_instances.id"), index=True
    )
    action: Mapped[Action] = mapped_column(String)

    __table_args__ = (
        UniqueConstraint(
            "instance_id",
            "action",
            name="uc_instance_action",
        ),
    )
