from google.cloud import storage

def write(bucket_name: str, prefix: str, file_name: str, content: str, content_type: str = 'application/jsonl'):
    try:
        # Initialize a storage client
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(f"{prefix}/{file_name}")
        # Upload the content to GCS
        blob.upload_from_string(content, content_type=content_type)
    except Exception as e:
        return e