from app.logger import logger
from app.ui.messagesManager import MessageManager
from app.ui.widgets.ui_operToModelTypeCustomWidget import *
from app.ui.customWidgetForDefaultOper import CustomCheckboxWidget
from app.services.operationServices import OperationsServices as OpS
from app.services.modelServices import ModelService as Ms
from app.utils.utils import Utils


class CustomWidgetForModelOper(QWidget, Ui_customWidgetForModelOper):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.newModelInfoHolder.setEnabled(False)
        self.likeModelCheckBox.setEnabled(False)
        self.operations = OpS.getAllOperations()
        self.clients = Ms.getClients()
        self.models = Ms.getAllModels()
        self.clientNames = {}
        self.modelNames = {}
        self.comboBoxItems = {}
        # print(self.geometry())
        self.setCheckBox()
        self.setupClientAndModelLineEdit()
        self.selectAllCheckbox.stateChanged.connect(lambda: self.selectAllOperations())
        self.actualCheckBox.stateChanged.connect(self.updateActualCheckBox)
        self.newModelCheckBox.stateChanged.connect(self.updateNewModelInfo)
        # logger.info('Models and Operations Page initialized successfully!')
        # MessageManager.showOnWidget(self, 'Models and Operations Page initialized successfully!',
        #                             'info')

    def setupClientAndModelLineEdit(self):
        for client in self.clients:
            self.clientNames[client.Клиент] = client.ClientID
        Utils.setupCompleter(self.clientNames.keys(), self.clientsLineEdit)
        self.clientsLineEdit.editingFinished.connect(self.selectClient)

    def selectClient(self):
        self.modelNames.clear()
        self.modelsLineEdit.clear()
        for model in self.models:
            if model.ClientID == self.clientNames[self.clientsLineEdit.text()]:
                self.modelNames[model.ПоръчкаNo] = model.id
        Utils.setupCompleter(self.modelNames.keys(), self.modelsLineEdit)
        self.modelsLineEdit.editingFinished.connect(self.selectModel)

    def selectModel(self):
        operationsForModel

    def updateActualCheckBox(self):
        if self.actualCheckBox.isChecked():
            self.label_11.setStyleSheet("QLabel { color: #008b69; }")
        else:
            self.label_11.setStyleSheet("")

    def updateNewModelInfo(self):
        if self.newModelCheckBox.isChecked():
            self.newModelInfoHolder.setEnabled(True)
            self.likeModelCheckBox.setEnabled(True)
            self.actualCheckBox.setCheckState(Qt.CheckState.Checked)
        else:
            self.newModelInfoHolder.setEnabled(False)
            self.likeModelCheckBox.setEnabled(False)
            self.actualCheckBox.setCheckState(Qt.CheckState.Unchecked)

    def setCheckBox(self):
        for index, operation in enumerate(self.operations):
            newCustomComboBoxItem = CustomCheckboxWidget()
            name = f'{operation.ОперацияNo}:  {operation.Операция}'

            newCustomComboBoxItem.checkBox.setText(name)

            newCustomComboBoxItem.checkBox.setObjectName(str(operation.ОперацияNo))
            row = index % 20
            col = index // 20
            self.operationsLayout.addWidget(newCustomComboBoxItem, row, col)
            self.comboBoxItems[operation.ОперацияNo] = [newCustomComboBoxItem.checkBox,
                                                        newCustomComboBoxItem.lineEdit,
                                                        newCustomComboBoxItem.label]
            newCustomComboBoxItem.checkBox.stateChanged.connect(self.updateSelectAllBtn)

    def selectAllOperations(self):
        # self.selectAllCheckbox.blockSignals(True)

        for index in self.comboBoxItems.keys():
            widget = self.comboBoxItems[index][0]
            lineEdit = self.comboBoxItems[index][1]
            label = self.comboBoxItems[index][2]
            if isinstance(widget, QCheckBox):
                widget.blockSignals(True)
                widget.setCheckState(self.selectAllCheckbox.checkState())
                if widget.checkState() == Qt.CheckState.Checked:
                    lineEdit.setEnabled(True)
                    label.setStyleSheet("QLabel { color: #008b69; }")
                else:
                    lineEdit.setEnabled(False)
                    label.setStyleSheet("")
                widget.blockSignals(False)

        # self.selectAllCheckbox.blockSignals(False)

    def updateSelectAllBtn(self):
        self.selectAllCheckbox.blockSignals(True)
        operId = int(self.sender().objectName())
        lineEdit = self.comboBoxItems[operId][1]
        if isinstance(self.sender(), QCheckBox):
            if self.sender().checkState() == Qt.CheckState.Checked:
                lineEdit.setEnabled(True)
            else:
                lineEdit.setEnabled(False)

        # Check if all boxes are checked
        allChecked = True
        isUnchecked = False

        for index in self.comboBoxItems.keys():
            widget = self.comboBoxItems[index][0]
            if isinstance(widget, QCheckBox):
                if widget.checkState() != Qt.CheckState.Checked:
                    isUnchecked = True
        if isUnchecked:
            allChecked = False

        # Set the state of the "Select All" checkbox
        if allChecked:
            self.selectAllCheckbox.setCheckState(Qt.CheckState.Checked)
        else:
            self.selectAllCheckbox.setCheckState(Qt.CheckState.Unchecked)

        # Reconnect signal
        self.selectAllCheckbox.blockSignals(False)
