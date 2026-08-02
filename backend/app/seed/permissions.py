from sqlalchemy import select

from app.core.database import SessionLocal
from app.role_management.system.system_permission.models import (
    Action,
    Feature,
    SystemPermission,
)

SYSTEM_PERMISSIONS = [
    # Roles
    ("role", "view"),
    ("role", "create"),
    ("role", "edit"),
    ("role", "delete"),
    ("member", "view"),
    ("member", "edit"),
    ("member", "remove"),
    ("member", "invite"),
]


def seed_permissions():
    session = SessionLocal()
    try:
        for feature, action in SYSTEM_PERMISSIONS:
            exists = session.scalar(
                select(SystemPermission).where(
                    SystemPermission.feature == Feature(feature),
                    SystemPermission.action == Action(action),
                )
            )
            if not exists:
                session.add(
                    SystemPermission(
                        feature=Feature(feature),
                        action=Action(action),
                    ),
                )
        session.commit()
    finally:
        session.close()
