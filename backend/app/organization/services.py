from sqlalchemy.orm import Session

from app.organization.models import Organization
from app.organization.schemas import OrganizationCreate


def create_organization(
    session: Session, organization_data: OrganizationCreate, owner_id: int):
    organization = Organization(
        name=organization_data.name,
        owner_id=owner_id
    )
    session.add(organization)
    session.flush()
    return organization
