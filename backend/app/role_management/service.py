from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.services import get_current_active_user
from app.core.database import get_session
from app.organization.models import Organization
from app.user.models import User

SessionDep = Annotated[Session, Depends(get_session)]
def has_permission(session, organization_id: int, current_user_id: int) -> bool:
    organization = session.get(Organization, organization_id)
    if not organization:
        return False
    if organization.owner_id == current_user_id:
        return True
    else:
        return False

def check_permission(
    session: SessionDep,
    organization_id: int,
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    if not has_permission(session, organization_id, current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You dont have permission")
