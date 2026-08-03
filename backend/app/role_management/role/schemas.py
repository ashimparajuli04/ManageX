from pydantic import BaseModel, Field


class RoleCreate(BaseModel):
    name: str = Field(min_length=1, max_length=30)

class RoleInfo(BaseModel):
    id: int
    name: str
