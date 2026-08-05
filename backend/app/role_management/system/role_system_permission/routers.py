from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.role_management.role.models import Role
from app.role_management.service import check_permission
from app.role_management.system.role_system_permission.models import (
    RoleSystemPermission,
)
from app.role_management.system.role_system_permission.schemas import (
    RoleSystemPermissionCreate,
)
from app.role_management.system.system_permission.models import SystemPermission

router = APIRouter(
    prefix="/organizations/{organization.id}/roles/{role_id}/system-permissions",
    tags=["role-system-permissions"],
)

SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/", dependencies=[Depends(check_permission)])
def get_role_system_permissions(
    session: SessionDep, system_permission_id: RoleSystemPermissionCreate, role_id: int
):
    if session.get(Role, role_id) is None:
        return {"error": "Role not found"}
    if session.get(SystemPermission, system_permission_id) is None:
        return {"error": "Please enter a valid system permission ID"}
    if session.get(RoleSystemPermission, (role_id, system_permission_id)) is not None:
        return {"error": "Role system permission already exists"}
    role_system_permission = RoleSystemPermission(
        role_id=role_id,
        system_permission_id=system_permission_id,
    )
    session.add(role_system_permission)
    session.commit()
    return {"message": "Role system permission added successfully"}
