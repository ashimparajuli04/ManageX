from sqlalchemy.orm import Session

from app.organization.models import Organization
from app.organization.schemas import OrganizationCreate
from app.organization_user.services import create_organization_user
from app.user.models import User


def create_organization(
    session: Session, organization_data: OrganizationCreate):
    organization = Organization(
        name=organization_data.name,
    )
    session.add(organization)
    session.flush()
    return organization
