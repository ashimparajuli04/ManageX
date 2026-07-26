from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.organization.schemas import OrganizationCreate, OrganizationInfo
from app.organization.services import create_organization

router = APIRouter(
    prefix="/organizations",
    tags=["organizations"],
)
SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/", response_model=OrganizationInfo)
def create_new_organization(session: SessionDep, organization: OrganizationCreate):
    return create_organization(session, organization)
