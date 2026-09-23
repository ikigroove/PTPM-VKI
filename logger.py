import logging
import sys

class Logger:
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    def setup() -> logging.Logger:
        logging.basicConfig(
            level=logging.DEBUG,
            format=Logger.LOG_FORMAT,
            datefmt=Logger.DATE_FORMAT,
            handlers=[
                logging.StreamHandler(sys.stdout),
                logging.FileHandler("app.log", encoding="utf-8"),
            ],
        )
        return logging.getLogger(__name__)