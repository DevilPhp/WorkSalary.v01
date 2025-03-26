from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer, Property
from PySide6.QtWidgets import QGraphicsOpacityEffect

from app.ui.widgets.ui_customMessageWidget import *

class CustomMessageBox(QWidget, Ui_customMessageWidget):
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.timeout = 3000
        self._opacity = 0.0

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)


        # Set up animations
        self.opacityEffect = QGraphicsOpacityEffect(self)
        self.opacityEffect.setOpacity(0.0)
        self.setGraphicsEffect(self.opacityEffect)

        self.animation = QPropertyAnimation(self, b"opacity")
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.setDuration(300)  # 300ms for fade in/out

        # Timer for auto-hiding
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.hideAnimation)

        # Current notification type
        self.currentType = self.INFO

    def setOpacity(self, opacity):
        self._opacity = opacity
        self.opacityEffect.setOpacity(opacity)

    def getОpacity(self):
        return self._opacity

        # Property for QPropertyAnimation

    opacity = Property(float, getОpacity, setOpacity)

    def showМessage(self, message, msgТype=INFO, timeout=None):
        """Show notification with the given message and type"""
        if timeout is not None:
            self.timeout = timeout

        self.currentType = msgТype
        self.textHolder.setText(message)
        self.textHolder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        if self.currentType == 'success':
            self.iconHolder.setIcon(QIcon("app/assets/icons/Check-Square--Streamline-Solar-Broken-#008b69.svg"))
            self.iconHolder.setIconSize(QSize(36, 36))
            self.label.setStyleSheet("QLabel { color: #008B69; }")

        # Adjust widget size based on text
        self.adjustSize()

        # Position at the bottom center of the parent
        if self.parent():
            print(self.parent().geometry().x())
            print(self.width())
            parentРect = self.parent().geometry()
            x = parentРect.x() + (parentРect.width() - self.width()) // 2
            y = parentРect.y() + parentРect.height() - self.height() - 50  # 50px from bottom
            self.setGeometry(x, y, self.width(), self.height())
            print(f"Positioned at ({x}, {y})")

        # Show the widget and start animations
        self.show()
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.start()

        # Start timer for auto-hiding
        self.timer.start(self.timeout)

    def hideAnimation(self):
        """Start fade-out animation"""
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.finished.connect(self.hide)
        self.animation.start()
