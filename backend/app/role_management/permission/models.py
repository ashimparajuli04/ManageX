from enum import Enum

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class SystemFeature(str, Enum):
    ORGANIZATION = "organization"
    ROLE = "role"
    USER = "user"

class Type(str, Enum):
    SYSTEM = "system"
    INSTANCE = "instance"

class Action(str, Enum):
    VIEW = "view"
    CREATE = "create"
    EDIT = "edit"
    DELETE = "delete"


class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[Type] = mapped_column(SQLEnum(Type))
    system_feature: Mapped[SystemFeature] = mapped_column(SQLEnum(SystemFeature), nullable=True)
    instance_id: Mapped[str] = mapped_column(nullable=True)
    action: Mapped[Action] = mapped_column(SQLEnum(Action))

    __table_args__ = (
        UniqueConstraint(
            "type",
            "action",
            "system_feature",
            "instance_id",
            name="uc_type_action_system_feature_instance_id",
        ),
    )
