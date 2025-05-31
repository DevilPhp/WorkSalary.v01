from app.ui.widgets.ui_customYesNowDialog import *
from PySide6.QtWidgets import QGraphicsDropShadowEffect


class CustomYesNowDialog(QDialog, Ui_CustomYesNoDialog):
    ADDING = 'adding'
    DELETING = 'deleting'
    ACCEPT = 'accept'
    EDITING = 'editing'
    WARNING = 'warning'

    def __init__(self, isNormalIcon=True, parent=None):
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
        self.warningIcon.setHidden(True)
        self.isNormalIcon = isNormalIcon
        if not self.isNormalIcon:
            self.normalIcon.setHidden(True)
            self.warningIcon.setHidden(False)
        self.yesBtn.clicked.connect(self.accept)
        self.noBtn.clicked.connect(self.reject)

    def setMessage(self, name: str,  message: str, mode: str):
        self.questionTextLabel.setText(message)
        self.nameTextLabel.setText(name)
        if mode == self.ADDING:
            self.mainTextLabel.setText("ДОБАВЯНЕ")
        elif mode == self.EDITING:
            self.mainTextLabel.setText("РЕДАКТИРАНЕ")
        elif mode == self.DELETING:
            self.mainTextLabel.setText("ПРЕМАХВАНЕ")
        elif mode == self.ACCEPT:
            self.mainTextLabel.setText("ПРИЕМАНЕ")
        elif mode == self.WARNING:
            self.mainTextLabel.setText("ВНИМАНИЕ!")
