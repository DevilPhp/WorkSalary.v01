from PySide6.QtCore import Signal

from app.ui.widgets.ui_customAddOperationDialog import *

from PySide6.QtWidgets import QGraphicsDropShadowEffect
from app.services.workerServices import WorkerServices as Ws
from app.utils.utils import Utils


class CustomAddOperationDialog(QDialog, Ui_customAddOperationDialog):
    operInfo = Signal(list)

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
        self.operTypes = Ws.getOperationTypes()
        self.operTypeComboBox.setEditable(True)
        Utils.setupCompleter(self.operTypes, self.operTypeComboBox.lineEdit())
        for oper in self.operTypes:
            self.operTypeComboBox.addItem(oper)
        self.operTypeComboBox.setCurrentIndex(-1)

        self.operationNameLineEdit.editingFinished.connect(self.operNameChanged)

        self.yesBtn.clicked.connect(self.acceptOper)

    def operNameChanged(self):
        self.operTypeComboBox.setFocus()

    def acceptOper(self):
        if self.operationNameLineEdit.text() == "":
            self.operationNameLineEdit.setFocus()
            return
        returnedData = [self.operationNameLineEdit.text(), self.operTypeComboBox.currentText().split(':  ')[0]]
        self.operInfo.emit(returnedData)
        self.close()

