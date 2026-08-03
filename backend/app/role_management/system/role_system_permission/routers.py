from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.role_management.role.models import Role
from app.role_management.service import check_permission
from app.role_management.system.role_system_permission.models import (
    RoleSystemPermission,
)

router = APIRouter(
    prefix="{organization.id}/role-system-permissions",
    tags=["role-system-permissions"],
)

SessionDep = Annotated[Session, Depends(get_session)]


@router.get("/", dependencies=[Depends(check_permission)])
def get_role_system_permissions(
    session: SessionDep, organization_id: int, role_id: int
):
    pass
