from google.cloud import secretmanager
import google.auth
from google.auth.transport.requests import Request


def get_secret(project_id: str, secret_name: str) -> str:
    client = secretmanager.SecretManagerServiceClient()
    secret_path = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(name=secret_path)
    return response.payload.data.decode("UTF-8")

def get_default_credential_token() -> str:
    """
    Get the default credentials for Google Cloud.
    Returns:
        str: The default credentials for Google Cloud.
    """
    try:
        credentials, project_id = google.auth.default()
        if not credentials.valid:
            credentials.refresh(Request())
        token = credentials.id_token
        return token
    except Exception as e:
        raise e
