from datetime import datetime
from typing import Literal

from pydantic import BaseModel

from app.invite.models import InviteStatus


class InviteInfo(BaseModel):
    id: int
    organization_id: int
    invited_by: int
    status: InviteStatus
    created_at: datetime


class InviteCreate(BaseModel):
    user_identifier: str
    organization_id: int


class InviteResponse(BaseModel):
    invite_id: int
    status: Literal["accepted", "rejected"]
