import logging
import os
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, operation_name: str):
        self.operation_name = operation_name
        self.src_path = os.path
        self.src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.log_dir = os.path.join(self.src_path, "logs")

        # Ensure the logs directory exists
        os.makedirs(self.log_dir, exist_ok=True)

        # Create logger
        self.logger = logging.getLogger(self.operation_name)
        self.logger.setLevel(logging.DEBUG)

        # Create file handler which logs even debug messages
        log_file = os.path.join(self.log_dir, f"{self.operation_name}.log")
        file_handler = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
        file_handler.setLevel(logging.DEBUG)

        # Create console handler with a higher log level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger
