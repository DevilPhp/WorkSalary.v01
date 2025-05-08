from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QDialog

from app.logger import logger
from app.ui.messagesManager import MessageManager
from app.ui.customYesNoMessage import CustomYesNowDialog
from app.ui.widgets.ui_operToModelTypeCustomWidget import *
from app.ui.customWidgetForDefaultOper import CustomCheckboxWidget
from app.services.operationServices import OperationsServices as OpS
from app.services.modelServices import ModelService as Ms
from app.utils.utils import Utils
import datetime


class CustomWidgetForModelOper(QWidget, Ui_customWidgetForModelOper):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle('Операции за модели')
        self.operationsGroupsHolder.setVisible(False)
        self.operationsGroupsReturnBtn.setVisible(False)
        validatorInt = QDoubleValidator(0, 999999, 0)
        validatorFloat = QDoubleValidator(0.1, float('inf'), 1)
        validatorInt.setNotation(QDoubleValidator.Notation.StandardNotation)
        validatorFloat.setNotation(QDoubleValidator.Notation.StandardNotation)
        validatorFloat.setLocale(QLocale.English)
        validatorInt.setLocale(QLocale.English)
        self.piecesLineEdit.setValidator(validatorInt)
        self.machineGaugeLineEdit.setValidator(validatorFloat)
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
        self.groupOperations = OpS.getOperationsGroups()
        self.selectedOperForGroup = []
        self.addOperationsForNewModel = {}
        self.newModel = {}
        # print(self.geometry())
        self.setCheckBox()
        self.setupClientAndModelLineEdit()
        self.setupNewModelInfo()
        self.selectAllCheckbox.stateChanged.connect(lambda: self.selectAllOperations())
        self.actualCheckBox.stateChanged.connect(self.updateActualCheckBox)
        self.newModelCheckBox.stateChanged.connect(self.updateNewModelInfo)
        self.modelTypeComboBox.currentIndexChanged.connect(self.updateModelTypeCheckBox)
        self.saveNewModel.clicked.connect(self.checkAcceptAddingNewModel)
        self.piecesLineEdit.textChanged.connect(self.updatePiecesLineEdit)
        self.machineComboBox.currentIndexChanged.connect(self.updateMachineComboBox)
        self.operationsGroupViewBtn.clicked.connect(self.showOperationsGroupView)
        self.operationsGroupsReturnBtn.clicked.connect(self.returnToModelOpersView)
        self.saveOpertaionsGroupsBtn.clicked.connect(self.saveOperationsGroups)
        Utils.setupCompleter(self.groupOperations.keys(), self.operationGroupLineEdit)
        self.operationGroupLineEdit.editingFinished.connect(self.updateGroupOperations)

        self.clientsLineEdit.setFocus()

        # logger.info('Models and Operations Page initialized successfully!')
        # MessageManager.showOnWidget(self, 'Models and Operations Page initialized successfully!',
        #                             'info')

    def updateGroupOperations(self):
        name = self.operationGroupLineEdit.text()
        if name in self.groupOperations.keys():
            self.selectedOperForGroup.clear()
            self.resetAllOperations(True)
            for operation in self.groupOperations[name]['operations']:
                if operation in self.comboBoxItems.keys():
                    self.comboBoxItems[operation][0].setCheckState(Qt.CheckState.Checked)
                    self.selectedOperForGroup.append(operation)
        if name == '':
            self.resetAllOperations(True)
        self.operationGroupLineEdit.clearFocus()

    def saveOperationsGroups(self):
        name = self.operationGroupLineEdit.text()
        if name == '':
            MessageManager.showOnWidget(self, 'Моля въведете име за група операции!', 'error')
            self.operationGroupLineEdit.setFocus()
            return

        if not self.selectedOperForGroup and name in self.groupOperations.keys():
            result = OpS.addOperationToGroup(self.selectedOperForGroup, groupId=(self.groupOperations[name]['id']))
            if result:
                MessageManager.showOnWidget(self, f'Група {name} е премахната!', 'success')
                self.resetGroupOperInfo()
                return
        elif not self.selectedOperForGroup and name:
            MessageManager.showOnWidget(self, 'Моля изберете операции за група!', 'error')
            return

        if name in self.groupOperations.keys():
            result = OpS.addOperationToGroup(self.selectedOperForGroup, groupId=(self.groupOperations[name]['id']))
        else:
            result = OpS.addOperationToGroup(self.selectedOperForGroup, name=name)

        if result:
            MessageManager.showOnWidget(self, f'Група {name} е запазена успешно!', 'success')
            self.resetGroupOperInfo()
        else:
            MessageManager.showOnWidget(self, 'Група операции не беше запазена успешно!', 'error')
            self.operationGroupLineEdit.clear()
            self.resetAllOperations(True)

    def resetGroupOperInfo(self):
        self.operationGroupLineEdit.clear()
        self.groupOperations = OpS.getOperationsGroups()
        Utils.setupCompleter(self.groupOperations.keys(), self.operationGroupLineEdit)
        self.resetAllOperations(True)

    def showOperationsGroupView(self):
        self.modelInfoHolder.setVisible(False)
        self.operationsGroupsHolder.setVisible(True)
        self.resetAllOperations(True)
        self.operationsGroupViewBtn.setVisible(False)
        self.saveBtn.setVisible(False)
        self.operationsGroupsReturnBtn.setVisible(True)

    def returnToModelOpersView(self):
        self.operationsGroupsHolder.setVisible(False)
        self.modelInfoHolder.setVisible(True)
        self.resetAllOperations(True)
        self.operationsGroupViewBtn.setVisible(True)
        self.saveBtn.setVisible(True)
        self.operationsGroupsReturnBtn.setVisible(False)
        self.selectedOperForGroup.clear()

    def checkAcceptAddingNewModel(self):
        if self.newModelLineEdit.text() == '':
            MessageManager.showOnWidget(self, 'Моля въведете Поръчка№!', 'error')
            self.newModelLineEdit.setFocus()
            return
        elif self.newModelLineEdit.text() in self.modelNames.keys():
            MessageManager.showOnWidget(self, 'Поръчка с такъв номер вече съществъва!', 'error')
            self.newModelLineEdit.setFocus()
            return

        for checkbox in self.comboBoxItems.values():
            if checkbox[0].isChecked():
                self.addOperationsForNewModel[int(checkbox[0].objectName())] = [checkbox[0].text().split(':  ')[1],
                                                                                float(checkbox[1].text())
                                                                                if checkbox[1].text() != '' else 0]

        if not self.addOperationsForNewModel:
            MessageManager.showOnWidget(self, 'Моля изберете поне една операция', 'error')
            return

        self.newDialog = CustomYesNowDialog()
        message = 'Добавяне на нова поръчка?'
        self.newDialog.setMessage(name=self.newModelLineEdit.text(), message=message, mode='adding')
        result = self.newDialog.exec()
        if result == QDialog.Accepted:
            self.saveModelWithOperations()
        else:
            return

    def saveModelWithOperations(self):
        orderNo = self.newModelLineEdit.text()
        orderPieces = None
        machineId = None
        vidObleklo = None
        yarnId = None

        try:
            orderPieces = int(self.piecesLineEdit.text())
        except ValueError:
            pass

        try:
            machineId = int(self.machines[self.machineComboBox.currentText().split(' :  ')[0]][0])
        except KeyError:
            pass

        try:
            vidObleklo = int(self.vidOblekla[self.modelTypeComboBox.currentText()])
        except KeyError:
            pass

        try:
            yarnId = int(self.yarns[self.yarnComboBox.currentText().split(' :  ')[0]][0])
        except KeyError:
            pass

        fain = self.machineGaugeLineEdit.text()
        if fain == '':
            if self.machineComboBox.currentText() != '':
                fain = self.machines[self.machineComboBox.currentText().split(' :  ')[0]][1]

        self.newModel = {
            'orderNo': orderNo,
            'orderPieces': orderPieces,
            'clientId': self.clientNames[self.clientsLineEdit.text()],
            'actual': self.actualCheckBox.isChecked(),
            'machineId': machineId,
            'fain': fain,
            'wearType': vidObleklo,
            'yarnId': yarnId,
            'pieces': orderPieces,
            'dateCreated': datetime.datetime.now(),
            'targetDate': datetime.datetime.now() + datetime.timedelta(days=30),
            'userCreated': self.usernameLabel.text(),
            'descr': self.descrLineEdit.text()
        }

        newModelAdded = Ms.addNewModel(self.newModel, self.addOperationsForNewModel)
        if newModelAdded:
            MessageManager.showOnWidget(self, f'Успешно добавен модел: {newModelAdded}',
                                        'success')
            logger.info(f'Model Added: {newModelAdded}')
            self.resetNewModelInfo()
            self.newModelCheckBox.setCheckState(Qt.CheckState.Unchecked)
            self.resetAllOperations(True)
            self.setModelsForClient()
            self.modelsLineEdit.clear()
            self.modelsLineEdit.setFocus()

        else:
            MessageManager.showOnWidget(self, 'Неуспешно добавен модел!', 'error')
            logger.error(f'Failed to add Model: {self.newModel}')
            return

    def updateMachineComboBox(self):
        machineFine = self.machineComboBox.currentText().split(' :  ')[1].strip('E')
        self.machineGaugeLineEdit.setText(machineFine)

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
            self.machineComboBox.addItem(f'{machine} :  {self.machines[machine][1]}E')
        self.machineComboBox.setCurrentIndex(-1)

        for vidObleklo in self.vidOblekla.keys():
            self.modelTypeComboBox.addItem(vidObleklo)
        self.modelTypeComboBox.setCurrentIndex(-1)
        for yarn in self.yarns.keys():
            self.yarnComboBox.addItem(f'{yarn} :  {self.yarns[yarn][1]}')
        self.yarnComboBox.setCurrentIndex(-1)

    def setupClientAndModelLineEdit(self):
        for client in self.clients:
            self.clientNames[client.Клиент] = client.ClientID
        Utils.setupCompleter(self.clientNames.keys(), self.clientsLineEdit)
        self.clientsLineEdit.editingFinished.connect(self.selectClient)

    def selectClient(self):
        if self.newModelCheckBox.isChecked():
            self.newModelCheckBox.setCheckState(Qt.CheckState.Unchecked)
            self.resetNewModelInfo()
        self.modelNames.clear()
        self.modelsLineEdit.clear()
        self.dataUpdatedLabel.setText('')
        self.modelActualCheckBox.setCheckState(Qt.CheckState.Unchecked)
        self.resetAllOperations()
        if self.clientsLineEdit.text() == '':
            return
        if self.clientsLineEdit.text() not in self.clientNames:
            MessageManager.showOnWidget(self, 'Не е намерен клиент с такова име!', 'warning')
            self.clientsLineEdit.selectAll()
            self.clientsLineEdit.setFocus()
            return
        self.setModelsForClient()
        self.modelsLineEdit.setFocus()
        self.modelsLineEdit.editingFinished.connect(self.selectModel)

    def setModelsForClient(self):
        self.models = Ms.getModelsForClient(self.clientNames[self.clientsLineEdit.text()])
        for model in self.models:
            if model.ClientID == self.clientNames[self.clientsLineEdit.text()]:
                self.modelNames[model.ПоръчкаNo] = [model.id, model.Actual, model.DateCreated]
        Utils.setupCompleter(self.modelNames.keys(), self.modelsLineEdit)

    def selectModel(self):
        self.resetAllOperations(True)
        self.modelExistingOperations.clear()
        if self.modelsLineEdit.text() == '':
            self.resetAllOperations()
            self.dataUpdatedLabel.setText('')
            self.modelActualCheckBox.setCheckState(Qt.CheckState.Unchecked)
            return
        if self.modelsLineEdit.text() not in self.modelNames:
            MessageManager.showOnWidget(self, 'Не е намерен модел с такова Поръчка№!', 'warning')
            self.modelsLineEdit.selectAll()
            self.modelsLineEdit.setFocus()
            return
        operationsForModel = OpS.getOperationsForModel(self.modelNames[self.modelsLineEdit.text()][0])
        actualState = self.modelNames[self.modelsLineEdit.text()][1]
        self.dataUpdatedLabel.setText(self.modelNames[self.modelsLineEdit.text()][2].strftime('%d.%m.%Y'))
        if actualState:
            self.modelActualCheckBox.setCheckState(Qt.CheckState.Checked)
        else:
            self.modelActualCheckBox.setCheckState(Qt.CheckState.Unchecked)

        if self.newModelCheckBox.isChecked():
            self.setModelInfoIfExists()

        for operation in operationsForModel:
            self.modelExistingOperations.append(operation.ОперацияNo)
            if not int(self.comboBoxItems[operation.ОперацияNo][0].objectName()) in self.newModelOperations:
                self.comboBoxItems[operation.ОперацияNo][0].setChecked(True)
                self.comboBoxItems[operation.ОперацияNo][0].setText(
                    f'{operation.ОперацияNo}:  {operation.Операция}'
                )
                self.comboBoxItems[operation.ОперацияNo][1].setText(str(round(operation.TimeForOper, 2)))

    def resetAllOperations(self, clearOperations=False):
        for checkbox in self.comboBoxItems.values():
            if int(checkbox[0].objectName()) in self.newModelOperations and not clearOperations:
                checkbox[0].setCheckState(Qt.CheckState.Checked)
            else:
                if int(checkbox[0].objectName()) in self.operations.keys():
                    checkbox[0].setText(
                        f'{checkbox[0].objectName()}:  {self.operations[int(checkbox[0].objectName())]["name"]}'
                    )
                checkbox[0].setChecked(False)
                checkbox[1].setText('')

        if clearOperations:
            self.newModelOperations = []

    def updateActualCheckBox(self):
        if self.actualCheckBox.isChecked():
            self.label_11.setStyleSheet("QLabel { color: #008b69; }")
        else:
            self.label_11.setStyleSheet("")

    def updateNewModelInfo(self):
        self.resetNewModelInfo()
        if self.clientsLineEdit.text() == '' or self.clientsLineEdit.text() not in self.clientNames.keys():
            MessageManager.showOnWidget(self, 'Моля изберете първо клиент', 'warning')
            self.newModelCheckBox.setCheckState(Qt.CheckState.Unchecked)
            return

        if self.modelsLineEdit.text() != '' and self.modelsLineEdit.text() in self.modelNames.keys():
            self.setModelInfoIfExists()

        if self.newModelCheckBox.isChecked():
            self.saveBtn.setEnabled(False)
            self.newModelInfoHolder.setEnabled(True)
            self.actualCheckBox.setCheckState(Qt.CheckState.Checked)
        else:
            self.resetNewModelInfo()
            self.saveBtn.setEnabled(True)
            self.newModelInfoHolder.setEnabled(False)
            self.actualCheckBox.setCheckState(Qt.CheckState.Unchecked)

    def setModelInfoIfExists(self):
        modelInfo = Ms.getModelInfo(self.modelNames[self.modelsLineEdit.text()][0])
        if modelInfo[1]:
            self.machineComboBox.setCurrentText(modelInfo[1])
        if modelInfo[2]:
            self.yarnComboBox.setCurrentText(modelInfo[2])
        if modelInfo[3]:
            self.modelTypeComboBox.blockSignals(True)
            self.modelTypeComboBox.setCurrentText(modelInfo[3])
            self.modelTypeComboBox.blockSignals(False)
        if modelInfo[0]:
            self.machineGaugeLineEdit.setText(modelInfo[0])

    def resetNewModelInfo(self):
        self.machineComboBox.blockSignals(True)
        self.machineComboBox.setCurrentIndex(-1)
        self.machineComboBox.blockSignals(False)
        self.yarnComboBox.setCurrentIndex(-1)
        self.machineGaugeLineEdit.clear()
        self.newModelLineEdit.clear()
        self.piecesLineEdit.clear()
        self.descrLineEdit.clear()
        self.modelTypeComboBox.blockSignals(True)
        self.modelTypeComboBox.setCurrentIndex(-1)
        self.modelTypeComboBox.blockSignals(False)

    def setCheckBox(self):
        for index, operation in enumerate(self.operations):
            operName = self.operations[operation]['name']
            operType = self.operations[operation]['operationType']
            newCustomComboBoxItem = CustomCheckboxWidget()
            name = f'{operation}:  {operName}'

            newCustomComboBoxItem.checkBox.setText(name)

            newCustomComboBoxItem.checkBox.setObjectName(str(operation))
            newCustomComboBoxItem.checkBox.clicked.connect(self.updateNewModelOperations)
            row = index % 20
            col = index // 20
            self.operationsLayout.addWidget(newCustomComboBoxItem, row, col)
            self.comboBoxItems[operation] = [newCustomComboBoxItem.checkBox,
                                             newCustomComboBoxItem.lineEdit,
                                             newCustomComboBoxItem.label]
            newCustomComboBoxItem.checkBox.stateChanged.connect(self.updateSelectAllBtn)

    def updateNewModelOperations(self):
        if isinstance(self.sender(), QCheckBox):
            if (self.sender().checkState() == Qt.CheckState.Checked and
                    int(self.sender().objectName()) not in self.newModelOperations and
                    not self.operationsGroupsHolder.isVisible()):
                self.newModelOperations.append(int(self.sender().objectName()))
            elif (self.sender().checkState() == Qt.CheckState.Unchecked and
                  int(self.sender().objectName()) in self.newModelOperations and
                  not self.operationsGroupsHolder.isVisible()):
                self.newModelOperations.remove(int(self.sender().objectName()))
            if (self.sender().checkState() == Qt.CheckState.Checked and
                    self.operationsGroupsHolder.isVisible()):
                self.selectedOperForGroup.append(int(self.sender().objectName()))
            elif (self.sender().checkState() == Qt.CheckState.Unchecked and
                  self.operationsGroupsHolder.isVisible()):
                self.selectedOperForGroup.remove(int(self.sender().objectName()))
        print(self.selectedOperForGroup)
        print(self.newModelOperations)
        # print(self.selectedOperForGroup)
        # print(self.newModelOperations)

    def selectAllOperations(self):
        # self.selectAllCheckbox.blockSignals(True)
        if self.operationsGroupsHolder.isVisible():
            self.selectedOperForGroup.clear()
        else:
            self.newModelOperations.clear()
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
                    if self.operationsGroupsHolder.isVisible():
                        self.selectedOperForGroup.append(int(widget.objectName()))
                    else:
                        self.newModelOperations.append(int(widget.objectName()))
                else:
                    if int(widget.objectName()) in self.modelExistingOperations:
                        # print(widget.text().split(':  ')[0])
                        widget.setCheckState(Qt.CheckState.Checked)
                        lineEdit.setEnabled(True)
                        label.setStyleSheet("QLabel { color: #008b69; }")
                    else:
                        lineEdit.setEnabled(False)
                        label.setStyleSheet("")

                    if self.operationsGroupsHolder.isVisible():
                        self.selectedOperForGroup.clear()
                    else:
                        self.newModelOperations.clear()

                    self.newModelOperations.clear()
                widget.blockSignals(False)
        # print(self.selectedOperForGroup)

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

    def updatePiecesLineEdit(self):
        text = self.piecesLineEdit.text()
        if ',' in text:
            text = text.split(',')[0]
        elif '.' in text:
            text = text.split('.')[0]
        self.piecesLineEdit.setText(text)
