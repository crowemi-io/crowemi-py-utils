from google.cloud import secretmanager


def get_secret(project_id: str, secret_name: str) -> str:
    client = secretmanager.SecretManagerServiceClient()
    secret_path = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(name=secret_path)
    return response.payload.data.decode("UTF-8")


