from pydantic import BaseModel


class OrganizationUserCreate(BaseModel):
    organization_id: int
    user_id: int


class OrganizationUserInfo(BaseModel):
    organization_id: int
    user_id: int
    role: str | None
