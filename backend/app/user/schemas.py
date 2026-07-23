from pydantic import BaseModel, EmailStr, Field, field_validator


class UserCreate(BaseModel):
    first_name: str = Field(min_length=1, max_length=20)
    middle_name: str | None = Field(default=None, max_length=20)
    last_name: str = Field(min_length=1, max_length=20)
    email: EmailStr
    username: str = Field(max_length=20, min_length=3, pattern=r"^[a-zA-Z0-9_]+$")
    password: str = Field(min_length=8, max_length=64)

    @field_validator("first_name", "middle_name", "last_name")
    @classmethod
    def strip_names(cls, value: str | None):
        return value.strip() if value is not None else value

class UserInfo(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    middle_name: str | None
    last_name: str
    username: str
