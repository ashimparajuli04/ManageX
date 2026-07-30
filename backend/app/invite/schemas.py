from datetime import datetime

from pydantic import BaseModel

from app.invite.models import InviteStatus


class InviteInfo(BaseModel):
    organization_id: int
    invited_by: int
    status: InviteStatus
    created_at: datetime

class InviteCreate(BaseModel):
    user_identifier: str
    organization_id: int
