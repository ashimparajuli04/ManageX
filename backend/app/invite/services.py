from sqlalchemy.orm import Session

from app.invite.models import Invite
from app.invite.schemas import InviteCreate
from app.organization_user.services import membership


def send_invite(session: Session, invite_data: InviteCreate, user_id: int):
    membership(session, invite_data.organization_id, user_id)
    invite = Invite(
        email=invite_data.email,
        organization_id=invite_data.organization_id,
        user_id= user_id,
    )
    session.add(invite)
    session.commit()
    return invite
