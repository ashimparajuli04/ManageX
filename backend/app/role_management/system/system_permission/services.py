from fastapi import HTTPException, status

from app.organization.models import Organization


def has_permission(session, organization_id: int, current_user_id: int) -> bool:
    organization = session.get(Organization, organization_id)
    if organization.owner_id == current_user_id:
        return True
    else:
        return False

def check_permission(
    session,
    organization_id: int,
    current_user_id: int,
):
    
    pass
