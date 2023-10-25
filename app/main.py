import json
import os

from flask import Flask
import google.cloud.logging      

from dotenv import load_dotenv
from app.src.etl import extract
from app.src.utils import build_logger


# Set up the Google Cloud Logging python client library
client = google.cloud.logging.Client()
client.setup_logging()
logger = build_logger()


# Load env variables
load_dotenv("app/src/.env")
bucket_name = os.getenv("BUCKET_NAME")
gcp_runtime = os.getenv("GCP_RUNTIME")

# Initialize Flask object
app = Flask(__name__)

# Index API
@app.route("/")
def hello_world():
    return "Welcome to the Airbnb data pipeline!"

# ETL API
@app.route("/etl")
def etl():
    logger.info("Starting ETL process...")
    df = extract.read_csv(bucket_name, "listings.csv", "tmp.csv")
    logger.info(f"Finished ETL process...\n Data sample: {df.head(10)}")

    return json.dumps(df.to_dict(orient='records'))


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
