from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.organization_user.models import OrganizationUser
from app.organization_user.schemas import OrganizationUserInfo
from app.role_management.service import check_permission

router = APIRouter(
    prefix="/organizations/{organization_id}/organization-users",
    tags=["organizaiton_user"],
)

SessionDep = Annotated[Session, Depends(get_session)]

@router.patch("/{organization_user_id}/roles", dependencies=[Depends(check_permission)])
def update_organization_user_roles(
    session: SessionDep,
    organization_id: int,
    organization_user_id: int,
    role_id: int,
):
    organization_user = session.get(OrganizationUser, organization_user_id)
    if organization_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organization user not found")
    
    organization_user.role_id = role_id
    session.commit()
    return {"message": "Role updated successfully"}

@router.get("", response_model=list[OrganizationUserInfo])
def get_organization_users(
    session: SessionDep,
    organization_id: int,
):
    organization_users = session.query(OrganizationUser).filter(OrganizationUser.organization_id == organization_id).all()
    return [OrganizationUserInfo.model_validate(org_users, from_attributes=True) for org_users in organization_users]
