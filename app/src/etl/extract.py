import os

from dotenv import load_dotenv
from google.cloud import storage
import pandas as pd

from app.src.utils import build_logger


def setup_client():
    """Setup client to interact with Cloud Storage."""

    load_dotenv("app/src/.env")

    project_id = os.getenv("PROJECT_ID")

    client = storage.Client(project_id)

    return client


def read_csv(bucket_name, file_name, destination_file_name):
    """Loads CSV from bucket in a pandas df"""

    logger = build_logger()

    storage_client = setup_client()

    bucket = storage_client.bucket(bucket_name) 

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(file_name)
    local_file_path = f"app/src/etl/tmp_data/{destination_file_name}"
    blob.download_to_filename(local_file_path)

    logger.info(
        f"Downloaded storage object {file_name} from bucket {bucket_name} to local file {local_file_path}..")
    
    # Load csv into pandas df
    df = pd.read_csv(local_file_path)

    # Clean workspace
    os.remove(local_file_path)

    return df
