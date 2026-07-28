from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class RolePermissions(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
