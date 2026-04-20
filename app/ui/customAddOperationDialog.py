from functools import partial

from PySide6.QtCore import Signal
from PySide6.QtGui import QIntValidator, QDoubleValidator

from app.ui.widgets.ui_customAddOperationDialog import *

from PySide6.QtWidgets import QGraphicsDropShadowEffect
from app.services.workerServices import WorkerServices as Ws
from app.services.groupOperServices import GroupOperationsService as GoS
from app.utils.utils import Utils


class CustomAddOperationDialog(QDialog, Ui_customAddOperationDialog):
    operInfo = Signal(list)
    isInputs = Signal(bool)

    def __init__(self, isNewOper=False, oper=None, operations=None, parent=None):
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

        validator = QDoubleValidator(0.01, float(999), 2)
        validator.setNotation(QDoubleValidator.StandardNotation)
        validator.setLocale(QLocale.English)

        self.operNumLineEdit.setValidator(QIntValidator(1, 1000000))
        self.operTimeLineEdit.setValidator(validator)

        self.isNewOper = isNewOper
        self.oper = oper
        if self.oper:
            self.operationNameLineEdit.setText(self.oper.get("name"))
            self.operTimeLineEdit.setText(self.oper.get("time"))
        self.groupsList = []
        self.operations = operations
        self.operNums = [oper[1] for name, oper in operations.items()] if operations else []

        self.operTypeComboBox.setEditable(True)

        if not self.isNewOper:
            self.operTypes = Ws.getOperationTypes()
            Utils.setupCompleter(self.operTypes, self.operTypeComboBox.lineEdit())
            for oper in self.operTypes:
                self.operTypeComboBox.addItem(oper)
        else:
            self.operTypes = GoS.getGroups()
            sortedGroups = sorted(self.operTypes.items(), key=lambda x: x[1])
            for group, id in sortedGroups:
                item = f"{id}:  {group}"
                self.groupsList.append(item)
                self.operTypeComboBox.addItem(item)
            Utils.setupCompleter(self.groupsList, self.operTypeComboBox.lineEdit())
            self.operTypeComboBox.setCurrentIndex(-1)

        self.operTypeComboBox.currentTextChanged.connect(self.operGroupSelected)

        if self.oper:
            self.operTypeComboBox.setCurrentIndex(self.oper.get("groupId") - 1)
        else:
            self.operTypeComboBox.setCurrentIndex(-1)

        self.operationNameLineEdit.editingFinished.connect(self.operNameChanged)
        self.operTimeLineEdit.textChanged.connect(self.operTimeChanged)
        self.operTimeLineEdit.editingFinished.connect(self.operTimeEdited)

        self.operationNameLineEdit.setFocus()
        self.operationNameLineEdit.selectAll()

        self.yesBtn.clicked.connect(self.acceptOper)
        self.noBtn.clicked.connect(self.reject)

    def getFirstAvailableOperNumber(self, groupId):
        """
            Returns the first free operation number for the selected group.

            Examples:
            groupId = "5"  -> checks 501, 502, 503, ...
            groupId = "12" -> checks 1201, 1202, 1203, ...

            self.operNums contains all already existing operation numbers as strings.
        """
        # Start from suffix 1 => 01, 02, 03...
        suffix = 1

        while True:
            candidate = int(f"{groupId}{suffix:02d}")

            if candidate not in self.operNums:
                return str(candidate)
            suffix += 1

    def operGroupSelected(self, text):
        try:
            self.operNumLineEdit.textChanged.disconnect()
        except RuntimeError:
            pass

        if not text.strip():
            return

        groupId = text.split(':  ')[0].strip()
        availableNumber = self.getFirstAvailableOperNumber(groupId)
        if self.oper and self.oper.get("number") > 0:
            self.operNumLineEdit.setText(str(self.oper.get("number")))
        else:
            self.operNumLineEdit.setText(availableNumber)
        self.operNumLineEdit.textChanged.connect(partial(self.operNumChanged, groupId))

    def operNumChanged(self, groupId, numText):
        self.operNumLineEdit.blockSignals(True)

        groupId = str(groupId)

        numText = numText.strip()

        if not numText:
            self.operNumLineEdit.setText(groupId)
            self.operNumLineEdit.blockSignals(False)
            return

        if numText.startswith(groupId):
            suffixPart = numText[len(groupId):]
        else:
            # Keep only the extra typed part after the prefix length
            suffixPart = numText[len(groupId):] if len(numText) > len(groupId) else ""

        self.operNumLineEdit.setText(groupId + suffixPart)
        self.operNumLineEdit.blockSignals(False)

    def operNameChanged(self):
        self.operTypeComboBox.setFocus()

    def acceptOper(self):
        if self.operationNameLineEdit.text() == "":
            self.operationNameLineEdit.setFocus()
            self.isInputs.emit(False)
            return

        if self.operNumLineEdit.text() == "":
            self.operNumLineEdit.setText("0")

        if not self.isNewOper:
            returnedData = [self.operationNameLineEdit.text(), self.operTypeComboBox.currentText().split(':  ')[0]]
        else:
            defaultTime = float(self.operTimeLineEdit.text())
            if defaultTime < 0.01:
                defaultTime = 0.01
            if self.oper:
                returnedData = [self.oper.get("id"),
                                self.operationNameLineEdit.text(),
                                int(self.operNumLineEdit.text()),
                                defaultTime]
            else:
                returnedData = [self.operationNameLineEdit.text(),
                                int(self.operNumLineEdit.text()),
                                defaultTime]
        self.operInfo.emit(returnedData)
        self.close()

    def operTimeChanged(self, text):
        currentText = text.replace(",", ".")
        self.operTimeLineEdit.setText(currentText)

    def operTimeEdited(self):
        convertedTime = float(self.operTimeLineEdit.text())
        # if convertedTime < 0.01:
        #     self.operTimeLineEdit.setText("0.01")
        # else:
        self.operTimeLineEdit.setText(str(convertedTime))
