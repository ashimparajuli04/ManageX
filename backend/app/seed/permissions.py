from sqlalchemy import select

from app.core.database import SessionLocal
from app.role_management.permission.models import (
    Action,
    Permission,
    SystemFeature,
    Type,
)

SYSTEM_PERMISSIONS = [
    # Roles
    ("system", "role", None, "view"),
    ("system", "role", None, "create"),
    ("system", "role", None, "edit"),
    ("system", "role", None, "delete"),
    
    ("system", "member", None,"view"),
    ("system", "member", None, "edit"),
    ("system", "member", None, "remove"),
    ("system", "member", None, "invite"),
]


def seed_permissions():
    session = SessionLocal()
    try:
        for type, system_feature, instance_id, action in SYSTEM_PERMISSIONS:
            exists = session.scalar(
                select(Permission).where(
                    Permission.type == Type(type),
                    Permission.system_feature == SystemFeature(system_feature),
                    Permission.instance_id == instance_id,
                    Permission.action == Action(action),
                )
            )
            if not exists:
                session.add(
                    Permission(
                        type=Type(type),
                        system_feature=SystemFeature(system_feature),
                        instance_id=instance_id,
                        action=Action(action),
                    ),
                )
        session.commit()
    finally:
        session.close()
