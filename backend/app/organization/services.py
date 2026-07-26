from sqlalchemy.orm import Session

from app.organization.models import Organization
from app.organization.schemas import OrganizationCreate


def create_organization(session: Session, organization_data: OrganizationCreate):
    organization = Organization(
        name=organization_data.name
    )
    session.add(organization)
    session.commit()
    session.refresh(organization)
    return organization
