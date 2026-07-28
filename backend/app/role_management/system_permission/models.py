from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class SystemPermission(Base):
    __tablename__ = "system_permissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column()
    action: Mapped[str] = mapped_column()

    __table_args__ = (
        UniqueConstraint(
            "type",
            "action",
            name="uc_type_action",
        ),
    )
    
