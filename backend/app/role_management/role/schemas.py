from pydantic import BaseModel


class RoleCreate(BaseModel):
    name: str
    organization_id: int

class RoleInfo(BaseModel):
    id: int
    name: str
