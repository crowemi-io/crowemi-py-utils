import base64
import json
from pydantic import BaseModel


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

    def create_headers(self) -> dict:
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

        return {
            "crowemi-client-id": self.crowemi_client_id,
            "crowemi-client-secret-key": self.crowemi_client_secret_key,
            "crowmei-client-name": self.crowemi_client_name,
            "Content-Type": "application/json"
        }

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
