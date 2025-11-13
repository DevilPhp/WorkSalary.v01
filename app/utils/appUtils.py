import requests
from functools import wraps
from PySide6.QtCore import QObject, Signal
from app.logger import logger


class ApiSignalEmitter(QObject):
    server_disconnected = Signal()


# Global instance of the emitter
api_signal_emitter = ApiSignalEmitter()


def handle_api_connection(func):
    """
    A decorator to handle API connection errors for service methods.
    It wraps a function that makes an API call. If a requests.RequestException
    is caught, it logs the error and emits a global signal.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as e:
            logger.error(f"API Connection Error in '{func.__name__}': {e}")
            api_signal_emitter.server_disconnected.emit()
            # Return a default value that indicates failure
            # This should be consistent with what the calling code expects on failure
            if "delete" in func.__name__ or "update" in func.__name__ or "add" in func.__name__ or "set" in func.__name__:
                return False
            if "get" in func.__name__:
                if "Info" in func.__name__ or "Data" in func.__name__:
                    return {}
                return []
            return None
    return wrapper
