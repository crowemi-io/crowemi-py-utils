import base64
import json
from pydantic import BaseModel


class CrowemiConfig(BaseModel):
    client_name: str
    client_id: str
    client_secret_key: str
    uri: dict

class CrowemiHeaders(BaseModel):
    crowemi_client_name: str | None = None
    crowemi_client_id: str
    crowemi_client_secret_key: str
    crowemi_session_id: str | None = None

class Helper():
    @staticmethod
    def convert_config(b64: str | None) -> dict | None:
        if b64:
            try:
                config = base64.b64decode(b64).decode("utf-8")
                return json.loads(config)
            except Exception as e:
                print(f"crowemi-py-utils: Error reading config file: {e}")
                raise e
