from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    telegram_user_id: str
    date_joined: datetime = datetime.utcnow()
    repo_url: str = None
    access_token: str = None
    is_admin: bool = False
