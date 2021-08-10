import logging
from google.cloud import storage

logger = logging.getLogger('airflow.task')

def list_blobs(bucket_name: str):
    """
    Get list of blobs.
    Args:
        bucket_name: Name of the bucket.
    """
    client = storage.Client()
    logger.info('Connect to Google Cloud Storage! v1')
    blobs = [blob.name for blob in client.list_blobs(bucket_name)]
    logger.info(blobs)