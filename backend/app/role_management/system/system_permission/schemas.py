from pydantic import BaseModel

from app.role_management.system.system_permission.models import Action, Feature



class SystemPermissionInfo(BaseModel):
    id: int
    feature: Feature
    action: Action
    