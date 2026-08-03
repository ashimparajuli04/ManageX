from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.role_management.role.models import Role
from app.role_management.role.schemas import RoleCreate, RoleInfo
from app.role_management.role.services import create_role
from app.role_management.service import check_permission

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(
    prefix="/{organization_id}/roles",
    tags=["roles"],
)


@router.post("",dependencies=[Depends(check_permission)])
def create_new_role(
    session: SessionDep, organization_id: int, role_data: RoleCreate
):
    if session.query(Role).filter_by(organization_id=organization_id, name=role_data.name).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Role already exists")
    create_role(session, organization_id, role_data.name)
    return HTTPException(status_code=status.HTTP_201_CREATED, detail="Role created successfully")

@router.get("", dependencies=[Depends(check_permission)], response_model=list[RoleInfo])
def get_roles(
    session: SessionDep, organization_id: int
):
    roles = session.query(Role).filter_by(organization_id=organization_id).all()
    return RoleInfo.model_validate(roles, from_attributes=True)

@router.get("/{role_id}", dependencies=[Depends(check_permission)], response_model=RoleInfo)
def get_role(
    session: SessionDep, organization_id: int, role_id: int
):
    role = session.query(Role).filter_by(organization_id=organization_id, id=role_id).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    return RoleInfo.model_validate(role, from_attributes=True)
