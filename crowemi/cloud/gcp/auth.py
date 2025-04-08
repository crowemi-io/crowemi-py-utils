import google.auth
from google.auth.transport.requests import Request


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
