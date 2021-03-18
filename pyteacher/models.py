from pydantic import BaseModel


class User(BaseModel):
    telegram_user_id: str
    repo_url: str
    access_token: str
    is_admin: bool = False
