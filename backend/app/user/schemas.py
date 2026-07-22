from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    first_name: str
    middle_name: str | None = None
    last_name: str
    password: str
