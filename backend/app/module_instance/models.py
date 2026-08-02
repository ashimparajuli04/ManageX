from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class ModuleInstance(Base):
    __tablename__ = "module_instances"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    template: Mapped[str] = mapped_column(String)
    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.id"), index=True
    )

    __table_args__ = (
        UniqueConstraint(
            "name",
            "organization_id",
            name="unique_module_instance_name_organization",
        ),
    )
