from sqlalchemy.orm import Session

from app.role_management.role.models import Role
from app.role_management.role.schemas import RoleInfo


def create_role(session: Session, organization_id: int, name: str) -> RoleInfo:

    role = Role(
        name=name,
        organization_id=organization_id,
    )
    session.add(role)
    session.commit()
    session.refresh(role)
    return RoleInfo.model_validate(role, from_attributes=True)