from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.role_management.service import check_permission
from app.role_management.system.system_permission.models import SystemPermission
from app.role_management.system.system_permission.schemas import SystemPermissionInfo

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(
    prefix="/{organization_id}/system-role-permissions", tags=["role-permissions"]
)


@router.get(
    "",
    dependencies=[Depends(check_permission)],
    response_model=list[SystemPermissionInfo],
)
def get_system_role_permissions(session: SessionDep):
    system_role_permissions = session.query(SystemPermission).all()
    return system_role_permissions
