from sqlalchemy.orm import Session

from app.role.models import Role
from app.role.schemas import RoleCreate


def create_role(session: Session, role_data: RoleCreate):
    role = Role(
        name=role_data.name,
        organization_id=role_data.organization_id,
    )
    session.add(role)
    session.commit()
    session.refresh(role)
    return role