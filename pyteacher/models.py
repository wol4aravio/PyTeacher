from pydantic import BaseModel


class User(BaseModel):
    telegram_user_id: str
    repo_url: str = None
    access_token: str = None
    is_admin: bool = False
