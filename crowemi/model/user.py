from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    email: str
    first_name: str
    last_name: str
    phone: str

    session: str | None = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    is_deleted: bool = False
