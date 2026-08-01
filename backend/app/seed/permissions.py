from sqlalchemy import select

from app.core.database import SessionLocal
from app.role_management.system_permission.models import (
    Action,
    Feature,
    Permission,
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
                select(Permission).where(
                    Permission.feature == Feature(feature),
                    Permission.action == Action(action),
                )
            )
            if not exists:
                session.add(
                    Permission(
                        feature=Feature(feature),
                        action=Action(action),
                    ),
                )
        session.commit()
    finally:
        session.close()
