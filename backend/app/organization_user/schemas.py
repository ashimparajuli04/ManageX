from pydantic import BaseModel


class OrganizationUserCreate(BaseModel):
    organization_id: int
    user_id: int