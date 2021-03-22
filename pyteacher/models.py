from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    telegram_user_id: str
    date_joined: str = datetime.utcnow().isoformat()
    repo_url: str = None
    access_token: str = None
    is_admin: bool = False
