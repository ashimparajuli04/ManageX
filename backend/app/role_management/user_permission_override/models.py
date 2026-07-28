from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.role_management.system_permission.models import Permission
from app.user.models import User


class UserPermissionOverride(Base):
    __tablename__ = "user_permission_override"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    permission_id: Mapped[int] = mapped_column(ForeignKey(Permission.id))
    effect: Mapped[bool] = mapped_column()
