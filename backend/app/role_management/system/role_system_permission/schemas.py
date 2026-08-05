from pydantic import BaseModel

class RoleSystemPermissionCreate(BaseModel):
    system_permission_id: list[int]

