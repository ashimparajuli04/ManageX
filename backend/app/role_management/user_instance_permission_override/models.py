from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.role_management.system_permission.models import Action


class UserInstancePermissionOverride(Base):
    __tablename__ = "user_instance_permission_override"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    instance_id: Mapped[int] = mapped_column()
    action: Mapped[Action] = mapped_column(String)
    effect: Mapped[bool] = mapped_column()
