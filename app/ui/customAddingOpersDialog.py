from PySide6.QtCore import Signal
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QLineEdit
from app.models.customLineEditWidget import CustomLineEdit
from app.ui.widgets.ui_customDroppingOpersDialog import *


class CustomAddOperationDialog(QDialog, Ui_CustomDroppingOpersDialog):
    emitedData = Signal(dict)

    def __init__(self, operations, item, firstParent, secondParent, thirdParent, parent=None):
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

        self.currentItem = item
        self.firstParent = firstParent
        self.secondParent = secondParent
        self.thirdParent = thirdParent

        if self.thirdParent:
            text = (f"{self.thirdParent.text()} > {self.secondParent.text()} >"
                    f" {self.firstParent.text()} > {self.currentItem.text()}")
        else:
            text = f"{self.secondParent.text()} > {self.firstParent.text()} > {self.currentItem.text()}"

        self.operPositionLabel.setText(text)
        self.operations = operations
        self.validator = QDoubleValidator(0.01, float(999), 2)
        self.validator.setNotation(QDoubleValidator.StandardNotation)
        self.validator.setLocale(QLocale.English)

        self.setOpersForm()
        self.yesBtn.clicked.connect(self.emitAcceptedOpers)
        self.noBtn.clicked.connect(self.reject)

    def emitAcceptedOpers(self):
        emitedData = {}
        parentList = []
        operList = []
        if self.thirdParent:
            parentList.append({'nodeType': self.thirdParent.data(Qt.ItemDataRole.UserRole + 1),
                               'id': self.thirdParent.data(Qt.ItemDataRole.UserRole)})
        parentList.append({'nodeType': self.secondParent.data(Qt.ItemDataRole.UserRole + 1),
                           'id': self.secondParent.data(Qt.ItemDataRole.UserRole)})
        parentList.append({'nodeType': self.firstParent.data(Qt.ItemDataRole.UserRole + 1),
                           'id': self.firstParent.data(Qt.ItemDataRole.UserRole)})
        parentList.append({'nodeType': self.currentItem.data(Qt.ItemDataRole.UserRole + 1),
                           'id': self.currentItem.data(Qt.ItemDataRole.UserRole)})
        emitedData['parentList'] = parentList
        emitedData['currentNode'] = self.currentItem

        for index in range(len(self.operations)):
            operId = int(self.opersGridLayout.itemAtPosition(index, 0).widget().objectName())
            operMins = float(self.opersGridLayout.itemAtPosition(index, 1).widget().text())
            operList.append({'id': operId, 'mins': operMins})
        emitedData['operList'] = operList

        self.emitedData.emit(emitedData)
        self.close()

    def setOpersForm(self):
        for index, oper in enumerate(self.operations):
            operName = QLabel(oper['name'])
            operName.setObjectName(str(oper['id']))
            operMins = CustomLineEdit()
            operMins.setText("0.01")
            operMins.setMaximumWidth(40)
            operMins.textChanged.connect(self.updateLabel)
            operMins.editingFinished.connect(self.setMinsText)
            operMins.setValidator(self.validator)
            operMinsLabel = QLabel("мин.")
            self.opersGridLayout.addWidget(operName, index, 0)
            self.opersGridLayout.addWidget(operMins, index, 1)
            self.opersGridLayout.addWidget(operMinsLabel, index, 2)

    def setMinsText(self):
        sender = self.sender()
        if sender.text() == "":
            sender.setText("0")
        else:
            sender.setText(str(round(float(sender.text()), 2)))

    def updateLabel(self):
        text = self.sender().text()
        if ',' in text:
            text = text.split(',')[0]
            text = text + '.'
        self.sender().setText(text)
