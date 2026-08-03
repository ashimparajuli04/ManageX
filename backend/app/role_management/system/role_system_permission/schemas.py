from pydantic import BaseModel


class RoleSystemPermission(BaseModel):
    role_id: int
    system_permission_id: int
