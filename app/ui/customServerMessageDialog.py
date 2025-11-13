from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGraphicsDropShadowEffect

from app.ui.widgets.ui_customServerMessageDialog import *


class CustomServerMessageDialog(QDialog, Ui_customServerMessageDialog):
    """
    Create a custom dialog for displaying server messages.
    """
    serverSignal = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setXOffset(2)
        shadow.setYOffset(2)
        shadow.setColor(QColor("#7f7f7f"))
        self.setGraphicsEffect(shadow)

        self.yesBtn.clicked.connect(self.onBtnClicked)

    def onBtnClicked(self):
        # self.serverSignal.emit(False)
        self.close()

