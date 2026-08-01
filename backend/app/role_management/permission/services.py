from app.organization_user.services import get_organization_user


# def has_permission(session, organization_id: int, current_user_id: int) -> bool:
#     organization = session.get(Organization, organization_id)
#     if current_user_id == organization.owner_id:
#         return True
#     elif user_info = get_organization_user(session, organization_id, current_user_id):
#         return True
#     return False
