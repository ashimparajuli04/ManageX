from pydantic import BaseModel, Field


class OrganizationCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)


class OrganizationInfo(BaseModel):
    id: int
    name: str
