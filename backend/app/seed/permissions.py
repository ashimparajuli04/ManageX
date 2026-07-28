# from sqlalchemy import select

# from app.core.database import SessionLocal
# from app.system_permission.models import Permission

# PERMISSIONS = [
#     ("Roles", "view"),
#     ("Roles", "create"),
#     ("Roles", "edit"),
#     ("Roles", "delete"),
# ]


# def seed_permissions():
#     session = SessionLocal()
#     try:
#         for module, action in PERMISSIONS:
#             exists = session.scalar(
#                 select(Permission).where(
#                     Permission.module == module,
#                     Permission.action == action,
#                 )
#             )
#             if not exists:
#                 session.add(Permission(module=module, action=action))
#         session.commit()
#     finally:
#         session.close()
