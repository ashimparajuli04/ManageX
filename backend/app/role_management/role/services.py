from sqlalchemy.orm import Session

from app.role_management.role.models import Role
from app.role_management.role.schemas import RoleCreate, RoleInfo


def create_role(session: Session, role_data: RoleCreate) -> RoleInfo:

    role = Role(
        name=role_data.name,
        organization_id=role_data.organization_id,
    )
    session.add(role)
    session.commit()
    session.refresh(role)
    return RoleInfo.model_validate(role, from_attributes=True)