from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    module: Mapped[str] = mapped_column()
    action: Mapped[str] = mapped_column()

    __table_args__ = (UniqueConstraint
        (
        "module",
        "action",
        name="uc_module_action"
        ),
    )
    
