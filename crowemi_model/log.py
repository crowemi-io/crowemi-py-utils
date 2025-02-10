from datetime import datetime
from enum import Enum

import pydantic

class LogLevel(Enum):
    INFO = "info"
    ERROR = "error"
    WARNING = "warning"
    DEBUG = "debug"


class LogMessage(pydantic.BaseModel):
    created_at: datetime = datetime.now()
    app: str
    message: str
    level: str = LogLevel.INFO
    obj: dict = {}
    session: str = ""
