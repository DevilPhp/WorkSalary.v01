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
        self.operations = OpS.getAllOperations()
        self.clients = Ms.getClients()
        self.machines = Ms.getMachines()
        self.vidOblekla = Ms.getVidObjekla()
        self.yarns = Ms.getYarns()
        self.models = None
        self.clientNames = {}
        self.modelNames = {}
        self.comboBoxItems = {}
        self.modelExistingOperations = []
        self.newModelOperations = []
        # print(self.geometry())
        self.setCheckBox()
        self.setupClientAndModelLineEdit()
        self.setupNewModelInfo()
        self.selectAllCheckbox.stateChanged.connect(lambda: self.selectAllOperations())
        self.actualCheckBox.stateChanged.connect(self.updateActualCheckBox)
        self.newModelCheckBox.stateChanged.connect(self.updateNewModelInfo)
        self.modelTypeComboBox.currentIndexChanged.connect(self.updateModelTypeCheckBox)
        # logger.info('Models and Operations Page initialized successfully!')
        # MessageManager.showOnWidget(self, 'Models and Operations Page initialized successfully!',
        #                             'info')

    def updateModelTypeCheckBox(self):
        if self.modelsLineEdit != '':
            self.resetAllOperations()
            # print(int(self.vidOblekla[self.modelTypeComboBox.currentText()]))
            modelTypeOper = Ms.getDfaultOperations(int(self.vidOblekla[self.modelTypeComboBox.currentText()]))
            for operation in modelTypeOper:
                if not self.comboBoxItems[operation.ОперацияNo][0].isChecked():
                    self.comboBoxItems[operation.ОперацияNo][0].setCheckState(Qt.CheckState.Checked)
                    self.comboBoxItems[operation.ОперацияNo][1].setText(str(operation.defaultTime))

    def setupNewModelInfo(self):
        for machine in self.machines.keys():
            self.machineComboBox.addItem(machine)
        self.machineComboBox.setCurrentIndex(-1)

        for vidObleklo in self.vidOblekla.keys():
            self.modelTypeComboBox.addItem(vidObleklo)
        self.modelTypeComboBox.setCurrentIndex(-1)

        for yarn in self.yarns.keys():
            self.yarnComboBox.addItem(yarn)
        self.yarnComboBox.setCurrentIndex(-1)

    def setupClientAndModelLineEdit(self):
        for client in self.clients:
            self.clientNames[client.Клиент] = client.ClientID
        Utils.setupCompleter(self.clientNames.keys(), self.clientsLineEdit)
        self.clientsLineEdit.editingFinished.connect(self.selectClient)

    def selectClient(self):
        self.modelNames.clear()
        self.modelsLineEdit.clear()
        self.dataUpdatedLabel.setText('')
        self.modelActualCheckBox.setCheckState(Qt.CheckState.Unchecked)
        self.resetAllOperations()
        if self.clientsLineEdit.text() == '':
            return
        if self.clientsLineEdit.text() not in self.clientNames:
            MessageManager.showOnWidget(self, 'Не е намерен клиент с такова име!', 'warning')
            return
        self.models = Ms.getModelsForClient(self.clientNames[self.clientsLineEdit.text()])
        for model in self.models:
            if model.ClientID == self.clientNames[self.clientsLineEdit.text()]:
                self.modelNames[model.ПоръчкаNo] = [model.id, model.Actual, model.DateCreated]
        Utils.setupCompleter(self.modelNames.keys(), self.modelsLineEdit)
        self.modelsLineEdit.editingFinished.connect(self.selectModel)

    def selectModel(self):
        self.modelExistingOperations.clear()
        if self.modelsLineEdit.text() == '':
            return
        operationsForModel = OpS.getOperationsForModel(self.modelsLineEdit.text())
        actualState = self.modelNames[self.modelsLineEdit.text()][1]
        self.dataUpdatedLabel.setText(self.modelNames[self.modelsLineEdit.text()][2].strftime('%d.%m.%Y'))
        if actualState:
            self.modelActualCheckBox.setCheckState(Qt.CheckState.Checked)
        else:
            self.modelActualCheckBox.setCheckState(Qt.CheckState.Unchecked)
        for operation in operationsForModel:
            self.modelExistingOperations.append(operation.ОперацияNo)
            self.comboBoxItems[operation.ОперацияNo][0].setChecked(True)
            self.comboBoxItems[operation.ОперацияNo][1].setText(str(round(operation.TimeForOper, 2)))

    def resetAllOperations(self):
        for checkbox in self.comboBoxItems.values():
            checkbox[0].setChecked(False)
            checkbox[1].setText('')

    def updateActualCheckBox(self):
        if self.actualCheckBox.isChecked():
            self.label_11.setStyleSheet("QLabel { color: #008b69; }")
        else:
            self.label_11.setStyleSheet("")

    def updateNewModelInfo(self):
        if self.clientsLineEdit.text() == '' or self.clientsLineEdit.text() not in self.clientNames.keys():
            MessageManager.showOnWidget(self, 'Моля изберете първо клиент', 'warning')
            self.newModelCheckBox.setCheckState(Qt.CheckState.Unchecked)
            return

        if self.newModelCheckBox.isChecked():
            self.newModelInfoHolder.setEnabled(True)
            self.actualCheckBox.setCheckState(Qt.CheckState.Checked)
        else:
            self.newModelInfoHolder.setEnabled(False)
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
                    if int(widget.text().split(':  ')[0]) in self.modelExistingOperations:
                        # print(widget.text().split(':  ')[0])
                        widget.setCheckState(Qt.CheckState.Checked)
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
