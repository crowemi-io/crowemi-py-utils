from datetime import datetime, UTC
import base64
import json
from pydantic import BaseModel

from cloud.gcp import get_default_credential_token
from model.log import LogMessage, LogLevel


class CrowemiConfig(BaseModel):
    """
    A class to represent the configuration of a Crowemi client.
    Attributes:
        crowemi_client_name (str): The name of the Crowemi client.
        crowemi_client_id (str): The client ID associated with the Crowemi service.
        crowemi_client_secret_key (str): The secret key for the Crowemi client.
        uri (dict): A dictionary containing the URIs for the Crowemi client.
    """
    client_name: str
    client_id: str
    client_secret_key: str
    uri: dict

    def create_headers(self, include_default_credentials: bool) -> dict:
        """
        Creates and returns a dictionary of headers for HTTP requests within the crowemi eco-system.
        The headers include:
        - `crowemi-client-id`: The client ID associated with the crowemi service.
        - `crowemi-client-secret-key`: The secret key for the crowemi client.
        - `crowmei-client-name`: The name of the Crowemi client.
        - `Content-Type`: Specifies the content type as JSON.
        Returns:
            dict: A dictionary containing the headers for HTTP requests.
        """

        headers = {
            "crowemi-client-id": self.client_id,
            "crowemi-client-secret-key": self.client_secret_key,
            "crowemi-client-name": self.client_name,
            "Content-Type": "application/json"
        }
        if include_default_credentials:
            token = get_default_credential_token()
            headers["Authorization"] = f"Bearer {token}"
        return headers

class CrowemiConfigBase(BaseModel):
    crowemi: CrowemiConfig
    gcp_project_id: str
    gcp_log_topic: str

    @staticmethod
    def convert_config(b64: str | None) -> dict | None:
        if b64:
            try:
                config = base64.b64decode(b64).decode("utf-8")
                return json.loads(config)
            except Exception as e:
                print(f"Error reading config file: {e}")
                return None

    def log(self, message: str, level: LogLevel, session_id: str = "", path: str = None, obj: any = None):
        LogMessage(**{"created_at": datetime.now(UTC), "app": self.crowemi.client_name, "message": message, "level": level.value, "session": session_id, "path": path, "obj": obj}).log(self.gcp_project_id, self.gcp_log_topic)



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
