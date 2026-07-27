from pydantic import BaseModel, Field

from app.organization_user.models import UserRole


class OrganizationUserCreate(BaseModel):
    organization_id: int
    user_id: int
