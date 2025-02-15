from datetime import datetime
from enum import Enum

import pydantic

from google.cloud import pubsub_v1

PUBLISHER = pubsub_v1.PublisherClient()


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
    obj: object | None = None
    session: str | None = ""

    def log(self, project: str, topic: str):
        try:
            data = self.model_dump_json()
            data = data.encode("utf-8")
            topic = PUBLISHER.topic_path(project, topic)
            future = PUBLISHER.publish(topic, data)
            print(future.result())
        except Exception as e:
            print("Failed writing message to pubsub.")
            print(e)
