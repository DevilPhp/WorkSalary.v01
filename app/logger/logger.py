import logging
import os
import datetime
from logging.handlers import RotatingFileHandler


class Logger:
    def __init__(self, log_level=logging.INFO, log_to_console=True):
        # Create logs directory if it doesn't exist
        if not os.path.exists("logs"):
            os.makedirs("logs")

        # Format: YYYY-MM-DD.log
        currentDate = datetime.datetime.now().strftime("%d-%m-%Y")
        logFile = f"logs/{currentDate}.log"

        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%d-%m-%Y %H:%M:%S'
        )

        # Create logger
        self.logger = logging.getLogger("Knitex-96")
        self.logger.setLevel(log_level)

        # Clear any existing handlers to prevent duplicates
        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        # Create file handler with rotating logs (5 MB max size, keep 10 backup files)
        fileHandler = RotatingFileHandler(
            logFile,
            maxBytes=5 * 1024 * 1024,  # 5 MB
            backupCount=5,
            encoding='utf-8'
        )
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)

        # Add console handler if enabled
        if log_to_console:
            consoleHandler = logging.StreamHandler()
            consoleHandler.setFormatter(formatter)
            self.logger.addHandler(consoleHandler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def exception(self, message):
        self.logger.exception(message)


# Create a singleton instance
_logger = None


def getLogger(log_level=logging.INFO, log_to_console=True):
    global _logger
    if _logger is None:
        _logger = Logger(log_level, log_to_console)
    return _logger
