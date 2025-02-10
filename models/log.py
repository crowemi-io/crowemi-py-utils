import pydantic
from datetime import datetime

class LogLevel:
    INFO = "info"
    ERROR = "error"
    WARNING = "warning"
    DEBUG = "debug"


class LogMessages(pydantic.BaseModel):
    created_at: datetime
    app: str
    message: str
    level: str = LogLevel.INFO
    obj: dict
    session: str
