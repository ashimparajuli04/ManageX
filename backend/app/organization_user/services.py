from sqlalchemy.orm import Session

from app.organization_user.models import OrganizationUser
from app.organization_user.schemas import OrganizationUserCreate


def create_organization_user(
    session: Session, org_user_data: OrganizationUserCreate, commit: bool = True
):
    organization_user = OrganizationUser(
        user_id=org_user_data.user_id,
        organization_id=org_user_data.organization_id,
    )
    session.add(organization_user)
    if commit:
        session.commit()
    return organization_user

def membership(session: Session, organization_id: int, user_id: int) -> bool:
    membership = session.query(OrganizationUser).filter(
        OrganizationUser.organization_id == organization_id,
        OrganizationUser.user_id == user_id,
        OrganizationUser.is_active == True
    ).first()
    if not membership:
        raise ValueError("The user is not a member of the organization")
    return True
