from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class InstancePermissionOverride(Base):
    __tablename__ = "instance_permission_override"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    instance_permission_id: Mapped[int] = mapped_column(
        ForeignKey("instance_permissions.id")
    )
    effect: Mapped[bool] = mapped_column()
