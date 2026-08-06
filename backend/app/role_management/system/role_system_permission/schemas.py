from pydantic import BaseModel


class SystemPermissionVerdict(BaseModel):
    system_permission_id: int
    verdict: bool

class RoleSystemPermissionCreate(BaseModel):
    permissions: list[SystemPermissionVerdict]