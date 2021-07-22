import sys
import logging
from google.cloud import storage

logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
logging.getLogger().setLevel(logging.INFO)


def list_blobs(bucket_name: str):
    """
    Get list of blobs.
    Args:
        bucket_name: Name of the bucket.
    """
    client = storage.Client()
    logging.info('Connect to Google Cloud Storage')
    blobs = [blob.name for blob in client.list_blobs(bucket_name)]
    logging.info(blobs)