import google.oauth2.id_token
import google.auth
from google.auth.transport.requests import Request


def get_gcp_id_token(audience: str) -> str:
    """
    Get the ID token for the default credentials.
    Args:
        audience (str): The audience for which the ID token is requested.
    Returns:
        str: the ID token for the default credentials.
    """
    try:
        credentials, _ = google.auth.default()
        request = Request()
        id_token = google.oauth2.id_token.fetch_id_token(request, audience)
        return id_token
    except Exception as e:
        raise e
