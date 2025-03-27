from app.ui.customMessage import CustomMessageBox
from app.logger import logger


class MessageManager:
    """Singleton manager for application notifications"""
    _instance = None
    _notification = None
    _mainWindow = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MessageManager, cls).__new__(cls)
        return cls._instance

    @classmethod
    def initialize(cls, mainWindow):
        """Initialize the notification manager with the main window"""
        cls._mainWindow = mainWindow
        cls._notification = CustomMessageBox(mainWindow)

    @classmethod
    def showOnWidget(cls, widget, message, notification_type, timeout=3000):
        """Show notification on a specific widget"""
        if widget:
            # Create a temporary notification for this widget
            notification = CustomMessageBox(widget)
            notification.showМessage(message, notification_type, timeout)
        else:
            logger.warning("Cannot show notification: Invalid widget")

    @classmethod
    def info(cls, message, timeout=3000):
        """Show info notification"""
        if cls._notification:
            logger.info(f"Notification (INFO): {message}")
            cls._notification.showМessage(message, CustomMessageBox.INFO, timeout)
        else:
            logger.warning("Notification manager not initialized")

    @classmethod
    def success(cls, message, timeout=3000):
        """Show success notification"""
        if cls._notification:
            logger.info(f"Notification (SUCCESS): {message}")
            cls._notification.showМessage(message, CustomMessageBox.SUCCESS, timeout)
        else:
            logger.warning("Notification manager not initialized")

    @classmethod
    def warning(cls, message, timeout=3000):
        """Show warning notification"""
        if cls._notification:
            logger.warning(f"Notification (WARNING): {message}")
            cls._notification.showМessage(message, CustomMessageBox.WARNING, timeout)
        else:
            logger.warning("Notification manager not initialized")

    @classmethod
    def error(cls, message, timeout=4000):
        """Show error notification (longer timeout by default)"""
        if cls._notification:
            logger.error(f"Notification (ERROR): {message}")
            cls._notification.showМessage(message, CustomMessageBox.ERROR, timeout)
        else:
            logger.warning("Notification manager not initialized")
