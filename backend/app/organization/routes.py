from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.services import get_current_active_user
from app.core.database import get_session
from app.organization.models import Organization
from app.organization.schemas import OrganizationCreate, OrganizationInfo
from app.organization.services import create_organization
from app.organization_user.models import OrganizationUser
from app.organization_user.schemas import OrganizationUserCreate
from app.organization_user.services import create_organization_user
from app.user.models import User

router = APIRouter(
    prefix="/organizations",
    tags=["organizations"],
)
SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/", response_model=OrganizationInfo)
def create_new_organization(
    session: SessionDep,
    organization: OrganizationCreate,
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    org_data = create_organization(session, organization, current_user.id)
    organization_user = OrganizationUserCreate(
        user_id=current_user.id,
        organization_id=org_data.id,
    )
    create_organization_user(session, organization_user, commit=False)
    session.commit()
    return org_data


@router.get("/", response_model=list[OrganizationInfo])
def get_organizations(
    session: SessionDep, current_user: Annotated[User, Depends(get_current_active_user)]
):
    organizations = (
        session.query(Organization)
        .join(
            OrganizationUser, OrganizationUser.organization_id == Organization.id
        )
        .where(
            OrganizationUser.user_id == current_user.id,
            OrganizationUser.is_active == True,
        )
        .all()
    )
    return organizations
