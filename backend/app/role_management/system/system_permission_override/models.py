from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class SystemPermissionOverride(Base):
    __tablename__ = "system_permission_override"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    permission_id: Mapped[int] = mapped_column(ForeignKey("system_permissions.id"))
    effect: Mapped[bool] = mapped_column()
