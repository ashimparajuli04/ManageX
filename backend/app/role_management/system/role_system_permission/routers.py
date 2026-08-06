import sys
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
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
    session: SessionDep, payload: RoleSystemPermissionCreate, role_id: int
):
    if session.get(Role, role_id) is None:
        return {"error": "Role not found"}

    system_permission_ids = [id[0] for id in session.query(SystemPermission.id).all()]

    for item in payload.permissions:
        if item.system_permission_id not in system_permission_ids:
            session.rollback()
            return {"error": "System permission not found"}
        if item.verdict and session.get(
            RoleSystemPermission, (role_id, item.system_permission_id)
        ):
            continue
        if (
            item.verdict is False
            and session.get(RoleSystemPermission, (role_id, item.system_permission_id)) is None
        ):
            continue
        if item.verdict == True:
            session.add(
                RoleSystemPermission(
                    role_id=role_id, system_permission_id=item.system_permission_id
                )
            )
        else:
            session.delete(
                session.get(RoleSystemPermission, (role_id, item.system_permission_id))
            )

    session.commit()
    return {"message": "Role system permissions updated successfully"}


@router.get("/", dependencies=[Depends(check_permission)])
def get_role_system_permissions(
    session: SessionDep,
    role_id: int,
):
    role_system_permissions = session.query(RoleSystemPermission).filter_by(role_id=role_id).all()
    return [
        {"system_permission_id": permission.system_permission_id}
        for permission in role_system_permissions
    ]
