from enum import Enum

from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class SystemFeature(str, Enum):
    ORGANIZATION = "organization"
    ROLE = "role"
    USER = "user"
    MEMBER = "member"


class Type(str, Enum):
    SYSTEM = "system"
    INSTANCE = "instance"


class Action(str, Enum):
    VIEW = "view"
    CREATE = "create"
    EDIT = "edit"
    DELETE = "delete"

    INVITE = "invite"
    REMOVE = "remove"


class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[Type] = mapped_column(String)
    system_feature: Mapped[SystemFeature] = mapped_column(String, nullable=True)
    instance_id: Mapped[str] = mapped_column(nullable=True, index=True)
    action: Mapped[Action] = mapped_column(String)

    __table_args__ = (
        UniqueConstraint(
            "type",
            "action",
            "system_feature",
            "instance_id",
            name="uc_type_action_system_feature_instance_id",
        ),
    )
