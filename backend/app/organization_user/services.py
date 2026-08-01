from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.organization_user.models import OrganizationUser
from app.organization_user.schemas import OrganizationUserCreate, OrganizationUserInfo


def create_organization_user(
    session: Session, org_user_data: OrganizationUserCreate, commit: bool = True
):
    if (
        session.query(OrganizationUser)
        .filter(
            OrganizationUser.user_id == org_user_data.user_id,
            OrganizationUser.organization_id == org_user_data.organization_id,
        )
        .first()
    ):
        raise ValueError("Organization user already exists")
    organization_user = OrganizationUser(
        user_id=org_user_data.user_id,
        organization_id=org_user_data.organization_id,
    )
    session.add(organization_user)
    if commit:
        session.commit()
    return organization_user


def membership(session: Session, organization_id: int, user_id: int) -> bool:
    ## This function checks whether the person is a member of the organization or not.
    membership = (
        session.query(OrganizationUser)
        .filter(
            OrganizationUser.organization_id == organization_id,
            OrganizationUser.user_id == user_id,
            OrganizationUser.is_active == True,
        )
        .first()
    )
    return membership is not None


def get_organization_user(session: Session, organization_id: int, user_id: int) -> OrganizationUser:
    organization_user = session.scalar(
        select(OrganizationUser).where(
            OrganizationUser.organization_id == organization_id,
            OrganizationUser.user_id == user_id,
        )
    )
    if not organization_user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    if not organization_user.is_active:
        raise HTTPException(status.HTTP_403_FORBIDDEN)
    return organization_user
