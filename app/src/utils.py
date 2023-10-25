import logging


# Use Python’s standard logging library to send logs to GCP
def build_logger() -> logging.Logger:

    # Set config
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Add handlers
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler = logging.FileHandler("app/src/logs.log", mode="w")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
