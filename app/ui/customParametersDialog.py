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
            labelItem = self.addParametersLayout.itemAt(i, QFormLayout.LabelRole)
            fieldItem = self.addParametersLayout.itemAt(i, QFormLayout.FieldRole)

            if labelItem and fieldItem:
                nameWidget = labelItem.widget()
                inputWidget = fieldItem.widget()  # This is the CustomParametersRowWidget
            # if row:
                name = nameWidget.text()
                userInput = inputWidget.inputLineEdit.text()
                if name == "SupervisorNo":
                    userInput = inputWidget.inputComboBox.currentText()
                    newEntry[name] = int(userInput.split(':  ')[0])

                elif name == "ВидОперация":
                    userInput = inputWidget.inputComboBox.currentText()
                    newEntry[name] = int(userInput.split(':  ')[0])

                elif name == "Ниво":
                    userInput = inputWidget.inputComboBox.currentText()
                    newEntry[name] = userInput

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
        try:
            userId = info[2]
        except IndexError:
            userId = None
        # print(param, info[1])
        # print(userId)
        row = CustomParametersRowWidget(info[1])
        nameLabel = QLabel(param)
        nameLabel.setObjectName('nameLabel')
        if param == "SupervisorNo" or param == "ВидОперация" or param == "Ниво":
            self.setComboBox(param, row, userId)
            row.inputComboBox.setVisible(True)
            row.inputLineEdit.setVisible(False)
        else:
            row.inputComboBox.setVisible(False)
            row.inputLineEdit.setVisible(True)

        # row.nameLabel.setText(param)
        self.addParametersLayout.addRow(nameLabel, row)

    def setComboBox(self, param, row, userId):
        # print(userId)
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

        elif param == "Ниво":
            userRols = ["guest", "user", "admin"]
            for userRole in userRols:
                row.inputComboBox.addItem(userRole)
            if userId:
                # user = Ws.getUserById(userId)
                row.inputComboBox.setCurrentIndex(userRols.index(userId))
            else:
                row.inputComboBox.setCurrentIndex(0)
