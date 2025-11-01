from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QLineEdit

from app.ui.widgets.ui_customAddParametersDialog import *
from app.ui.customParametersRowWidget import CustomParametersRowWidget
from app.services.workerServices import WorkerServices as Ws
from app.utils.utils import Utils


class CustomAddParametersDialog(Ui_customAddParametersDialog, QDialog):
    newEntryInfo = Signal(dict)

    def __init__(self, params, parent=None):
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

        self.parameters = params
        self.initializeParams()

        self.yesBtn.clicked.connect(self.acceptNewEntry)

    def acceptNewEntry(self):
        newEntry = {}
        for i in range(self.addParametersLayout.rowCount()):
            row = self.addParametersLayout.itemAt(i)
            if row:
                name = row.widget().nameLabel.text()
                userInput = row.widget().inputLineEdit.text()
                if name == "SupervisorNo":
                    userInput = row.widget().inputComboBox.currentText()
                    newEntry[name] = int(userInput.split(':  ')[0])

                elif name == "ВидОперация":
                    userInput = row.widget().inputComboBox.currentText()
                    newEntry[name] = int(userInput.split(':  ')[0])

                else:
                    newEntry[name] = userInput

                if userInput == '':
                    return
        # print(newEntry)
        if newEntry:
            self.newEntryInfo.emit(newEntry)
            self.close()
        else:
            return

    def initializeParams(self):
        for name, info in self.parameters.items():
            self.addParameter(name, info)

    def addParameter(self, param, info):
        if info[1] == "numeric":
            if param == "Коефициент":
                info[1] = "float"
        # print(param, info[1])
        row = CustomParametersRowWidget(info[1])
        if param == "SupervisorNo" or param == "ВидОперация":
            self.setComboBox(param, row)
            row.inputComboBox.setVisible(True)
            row.inputLineEdit.setVisible(False)
        else:
            row.inputComboBox.setVisible(False)
            row.inputLineEdit.setVisible(True)
        row.nameLabel.setText(param)
        self.addParametersLayout.addRow(row)

    def setComboBox(self, param, row):
        if param == "SupervisorNo":
            workers = Ws.getWorkersForCehove()
            for worker in workers:
                row.inputComboBox.addItem(worker)
            row.inputComboBox.setEditable(True)
            Utils.setupCompleter(workers, row.inputComboBox.lineEdit())

        elif param == "ВидОперация":
            operTypes = Ws.getOperationTypes()
            for operType in operTypes:
                row.inputComboBox.addItem(operType)
            row.inputComboBox.setEditable(True)
            Utils.setupCompleter(operTypes, row.inputComboBox.lineEdit())
