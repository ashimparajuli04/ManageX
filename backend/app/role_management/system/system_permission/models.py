from enum import Enum

from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Feature(str, Enum):
    ORGANIZATION = "organization"
    ROLE = "role"
    USER = "user"
    MEMBER = "member"

class Action(str, Enum):
    VIEW = "view"
    CREATE = "create"
    EDIT = "edit"
    DELETE = "delete"
    INVITE = "invite"
    REMOVE = "remove"


class SystemPermission(Base):
    __tablename__ = "system_permissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    feature: Mapped[Feature] = mapped_column(String)
    action: Mapped[Action] = mapped_column(String)

    __table_args__ = (
        UniqueConstraint(
            "feature",
            "action",
            name="uc_feature_action",
        ),
    )
