import logging
import os
from datetime import datetime


class Logger:

    def __init__(self):

        os.makedirs("logs", exist_ok=True)

        log_file = datetime.now().strftime("logs/app_%Y%m%d.log")

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(log_file, encoding="utf-8"),
                logging.StreamHandler()
            ]
        )

        self.logger = logging.getLogger("CAD_AI")

    ########################################################

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)


# GLOBAL LOGGER INSTANCE (THIS FIXES YOUR ERROR)
logger = Logger()