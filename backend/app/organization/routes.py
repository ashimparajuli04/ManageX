from typing import Annotated
from webbrowser import get

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.services import get_current_active_user
from app.core.database import get_session
from app.organization.schemas import OrganizationCreate, OrganizationInfo
from app.organization.services import create_organization
from app.user.models import User

router = APIRouter(
    prefix="/organizations",
    tags=["organizations"],
)
SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/", response_model=OrganizationInfo)
def create_new_organization(session: SessionDep, organization: OrganizationCreate, current_user: Annotated[User, Depends(get_current_active_user)]):
    return create_organization(session, organization, current_user)
