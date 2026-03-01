from functools import partial

from PySide6.QtCore import Signal
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
from app.models.customLineEditWidget import CustomLineEdit
import datetime


class CustomWidgetForModelOper(QWidget, Ui_customWidgetForModelOper):
    logoutSignal = Signal(bool)
    pageClosedSignal = Signal(bool)

    def __init__(self, mainWindow, user, isCalling=False, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle('Операции за модели')
        self.usernameLabel.setText(user)
        self.user = user
        self.isCalling = isCalling

        self.clientsLineEdit = CustomLineEdit(self)
        self.modelsLineEdit = CustomLineEdit(self)
        self.clientsWidget.layout().insertWidget(0, self.clientsLineEdit)
        self.modelsWidget.layout().insertWidget(0, self.modelsLineEdit)

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
        self.effectChangesWidget.setVisible(False)
        self.effectChangesComboBox.setEnabled(False)
        self.operations = OpS.getAllOperations()
        self.clients = Ms.getClients()
        self.machines = Ms.getMachines()
        self.vidOblekla = Ms.getVidObjekla()
        self.yarns = Ms.getYarns()
        self.models = None
        self.modelsForGroup = Ms.getForModelsGroups()
        self.clientNames = {}
        self.modelNames = {}
        self.comboBoxItems = {}
        self.modelExistingOperations = []
        self.removedOperations = []
        self.newModelOperations = []
        self.changedOperTimes = {}
        self.operationsForModel = None
        self.groupOperations = OpS.getOperationsGroups()
        self.groupOperationsForModel = {}
        self.selectedOperForGroup = []
        self.addOperationsForNewModel = {}
        self.newModel = {}
        self.isNewModel = False
        self.lastSelectedClient = None
        self.lastSelectedModel = None

        # print(self.geometry())
        self.setCheckBox()
        self.isOperationsReseted = True
        self.setupClientAndModelLineEdit()
        self.clientsLineEdit.editingFinished.connect(self.selectClient)
        self.modelsLineEdit.editingFinished.connect(self.selectModel)
        # self.modelsLineEdit.doubleClicked.connect(print('double clicked'))

        self.setupNewModelInfo()

        self.editModelHolder.setVisible(False)
        self.operationsHolder.setEnabled(False)

        self.editModelCheckBox.stateChanged.connect(self.updateEditModelInfo)
        self.selectAllCheckbox.stateChanged.connect(lambda: self.selectAllOperations())
        self.actualCheckBox.stateChanged.connect(self.updateActualCheckBox)
        self.newModelCheckBox.stateChanged.connect(self.updateNewModelInfo)
        self.effectChangesCheckBox.stateChanged.connect(self.setEffectChangesComboBox)
        self.modelTypeComboBox.currentIndexChanged.connect(self.updateModelTypeCheckBox)
        self.saveNewModel.clicked.connect(self.checkBtnSender)
        self.piecesLineEdit.textChanged.connect(self.updatePiecesLineEdit)
        self.machineComboBox.currentIndexChanged.connect(self.updateMachineComboBox)
        self.operationsGroupViewBtn.clicked.connect(self.showOperationsGroupView)
        self.operationsGroupsReturnBtn.clicked.connect(self.returnToModelOpersView)
        self.saveOpertaionsGroupsBtn.clicked.connect(self.saveOperationsGroups)
        self.deleteOperetionGroupsBtn.clicked.connect(self.deleteOperationsGroups)
        # Utils.setupCompleter(self.groupOperations.keys(), self.operationGroupLineEdit)
        self.operationGroupLineEdit.editingFinished.connect(self.updateGroupOperations)
        self.forModelCheckBox.stateChanged.connect(self.updateForModelLineEdit)
        self.forModelLineEdit.editingFinished.connect(self.forModelLineEditChange)
        self.deleteModelBtn.clicked.connect(self.deleteModel)

        self.clientsLineEdit.setFocus()

        self.closeBtn.clicked.connect(self.close)
        self.logoutBtn.clicked.connect(self.logout)

    def setEffectChangesComboBox(self):
        if self.effectChangesCheckBox.isChecked():
            self.effectChangesComboBox.setEnabled(True)
        else:
            self.effectChangesComboBox.setEnabled(False)

    def updateEditModelInfo(self):
        if self.editModelCheckBox.isChecked():
            self.setModelInfoIfExists()
            self.newModelInfoHolder.setEnabled(True)
            self.newModelCheckBox.setEnabled(False)
            self.newModelLineEdit.setReadOnly(True)
            self.actualCheckBox.setEnabled(True)
            self.saveNewModel.setText("Запазване")
            self.operationsHolder.setEnabled(True)
            self.modelsLineEdit.setReadOnly(True)
            self.effectChangesWidget.setVisible(True)
        else:
            self.resetNewModelInfo()
            self.setOperationsForModel(self.operationsForModel)
            self.newModelCheckBox.setEnabled(True)
            self.newModelLineEdit.setReadOnly(False)
            self.actualCheckBox.setEnabled(True)
            self.newModelInfoHolder.setEnabled(False)
            self.operationsHolder.setEnabled(False)
            self.modelsLineEdit.setReadOnly(False)
            self.effectChangesWidget.setVisible(False)
            self.effectChangesCheckBox.setCheckState(Qt.CheckState.Unchecked)

    def setEditModelVisible(self, visible):
        if visible:
            self.editModelHolder.setVisible(True)
            self.modelNameLabel.setText(self.modelsLineEdit.text())

    def setWindowsForTimePapersCall(self):
        self.showOperationsGroupView()
        self.operationsGroupsReturnBtn.setVisible(False)

    def setWindowForTimePapersReturn(self, clientName, modelName, modelId, currentMonth):
        self.modelsLineEdit.blockSignals(True)
        self.clientsLineEdit.blockSignals(True)
        self.effectChangesComboBox.setCurrentIndex(currentMonth - 1)
        self.widget_4.setVisible(False)
        self.widget_3.setVisible(False)
        self.modelInfoWidget.setVisible(False)
        self.newModelInfoHolder.setEnabled(True)
        self.clientsLineEdit.setText(clientName)
        self.clientsLineEdit.setEnabled(False)
        self.modelsLineEdit.setText(modelName)
        self.modelsLineEdit.setEnabled(False)
        self.effectChangesWidget.setVisible(True)
        self.saveNewModel.setText("Запазване")
        self.effectChangesCheckBox.setCheckState(Qt.CheckState.Checked)
        self.effectChangesCheckBox.setEnabled(False)
        self.selectAllCheckbox.setVisible(False)
        self.operationsHolder.setEnabled(True)
        self.saveNewModel.clicked.disconnect()
        self.saveNewModel.clicked.connect(lambda: self.checkAcceptAddingNewModel(self.isCalling, modelId))
        self.operationsForModel = OpS.getOperationsForModel(modelId)
        self.setOperationsForModel(self.operationsForModel, True)

    def updateGroupOperations(self):
        # if (self.operationGroupLineEdit.text() != '' and
        #         self.operationGroupLineEdit.text() in self.groupOperations.keys()):
        #     completer = self.operationGroupLineEdit.completer()
        #     self.operationGroupLineEdit.setText(Utils.setReturnBtnForCompleter(completer))
        name = self.operationGroupLineEdit.text()
        if not self.forModelCheckBox.isChecked():
            if name in self.groupOperations.keys():
                self.selectedOperForGroup.clear()
                # if not self.isOperationsReseted:
                self.resetAllOperations(True)
                for operation in self.groupOperations[name]['operations']:
                    if operation in self.comboBoxItems.keys():
                        self.comboBoxItems[operation][0].setCheckState(Qt.CheckState.Checked)
                        self.selectedOperForGroup.append(operation)
            else:
                # if not self.isOperationsReseted:
                self.resetAllOperations(True)
            self.operationGroupLineEdit.clearFocus()
        else:
            if name in self.groupOperationsForModel.keys():
                self.selectedOperForGroup.clear()
                # if not self.isOperationsReseted:
                self.resetAllOperations(resetNames=False, resetActual=False)
                for operation in self.groupOperationsForModel[name]['operations']:
                    if operation in self.comboBoxItems.keys():
                        self.comboBoxItems[operation][0].setCheckState(Qt.CheckState.Checked)
                        self.selectedOperForGroup.append(operation)
                self.operationGroupLineEdit.clearFocus()
            else:
                if not self.forModelCheckBox.isChecked():
                    self.selectedOperForGroup.clear()
                    self.resetAllOperations(resetNames=False)
        self.operationGroupLineEdit.clearFocus()

        # if name in self.groupOperations.keys() or name in self.groupOperationsForModel.keys():
        #     self.isOperationsReseted = False

    def saveOperationsGroups(self):
        # print(self.selectedOperForGroup)
        name = self.operationGroupLineEdit.text()
        print(name)
        if name == '':
            MessageManager.showOnWidget(self, 'Моля въведете име за група операции!', 'error')
            self.operationGroupLineEdit.setFocus()
            return

        # if not self.selectedOperForGroup and name in self.groupOperations.keys():
        #     result = OpS.addOperationToGroup(self.selectedOperForGroup, groupId=(self.groupOperations[name]['id']))
        #     if result:
        #         MessageManager.showOnWidget(self, f'Група {name} е премахната!', 'success')
        #         self.resetGroupOperInfo()
        #         return
        if not self.selectedOperForGroup and name:
            MessageManager.showOnWidget(self, 'Моля изберете операции за група!', 'error')
            return

        if not self.forModelCheckBox.isChecked():
            result = self.saveDefaultGroups(name)
        else:
            result = self.saveForModelGroups(name)

        if result:
            MessageManager.showOnWidget(self, f'Група {name} е запазена успешно!', 'success')
            self.resetGroupOperInfo()
        else:
            MessageManager.showOnWidget(self, 'Група операции не беше запазена успешно!', 'error')
            self.operationGroupLineEdit.clear()
            self.resetAllOperations(True)

    def deleteOperationsGroups(self):
        groupName = self.operationGroupLineEdit.text()
        if groupName == '':
            MessageManager.showOnWidget(self, 'Моля изберете група за изтриване!', 'error')
            self.operationGroupLineEdit.setFocus()
            return
        else:
            if not self.forModelCheckBox.isChecked():
                groupId = self.groupOperations[groupName]['id']
            else:
                groupId = self.groupOperationsForModel[groupName]['id']

            if groupId:
                newDialog = CustomYesNowDialog()
                message = 'Изтриване на група операции?'
                mode = 'deleting'
                name = groupName

                newDialog.setMessage(name=name, message=message, mode=mode)
                result = newDialog.exec()
                if result == QDialog.Accepted:
                    if not self.forModelCheckBox.isChecked():
                        result = OpS.deleteOperationsGroup(groupId, name)
                    else:
                        result = OpS.deleteOperationsGroupFromModel(groupId, name)
                    if result:
                        MessageManager.showOnWidget(self, f'Група {name} е изтрита успешно!', 'success')
                        self.resetGroupOperInfo()
                        return
                    else:
                        MessageManager.showOnWidget(self, 'Група операции не беше изтрита успешно!', 'error')
                        return


    def saveForModelGroups(self, name):
        modelId = self.forModelLineEdit.text().split(' - ')[0]
        modelName = self.forModelLineEdit.text().split(' - ')[1]
        # print(self.selectedOperForGroup)
        if name in self.groupOperationsForModel.keys():
            result = OpS.addOperationsGroupToModel(
                modelId, modelName, self.selectedOperForGroup, self.groupOperationsForModel[name]['id']
            )
        else:
            result = OpS.addOperationsGroupToModel(modelId, modelName, self.selectedOperForGroup, name=name)
        return result

    def saveDefaultGroups(self, name):
        if name in self.groupOperations.keys():
            result = OpS.addOperationToGroup(self.selectedOperForGroup, groupId=(self.groupOperations[name]['id']))
        else:
            result = OpS.addOperationToGroup(self.selectedOperForGroup, name=name)
        return result

    def resetGroupOperInfo(self):
        self.operationGroupLineEdit.clear()
        if not self.forModelCheckBox.isChecked():
            self.groupOperations = OpS.getOperationsGroups()
            Utils.setupCompleter(self.groupOperations.keys(), self.operationGroupLineEdit)
            self.forModelCheckBox.setChecked(False)
            self.resetAllOperations(True)
        else:
            self.groupOperationsForModel = OpS.getGroupOperationsForModel(self.forModelLineEdit.text().split(' - ')[0])
            Utils.setupCompleter(self.groupOperationsForModel.keys(), self.operationGroupLineEdit)
            self.resetAllOperations(resetNames=False, resetActual=False)
        self.operationGroupLineEdit.setFocus()

    def showOperationsGroupView(self):
        self.operationsHolder.setEnabled(True)
        self.modelInfoHolder.setVisible(False)
        self.operationsGroupsHolder.setVisible(True)
        if not self.isOperationsReseted:
            self.resetAllOperations(True)
        self.operationsGroupViewBtn.setVisible(False)
        self.operationsGroupsReturnBtn.setVisible(True)
        self.operationGroupLineEdit.setFocus()
        self.operationsHolder.setEnabled(True)
        self.forModelCheckBox.setChecked(False)
        self.forModelLineEdit.setReadOnly(True)
        self.selectAllCheckbox.setVisible(False)
        self.setModelsLineEditForGroups()
        self.setCompleterForGroups()

    def setCompleterForGroups(self):
        if self.forModelCheckBox.isChecked() and self.forModelLineEdit.text() != '':
            modelId = self.forModelLineEdit.text().split(' - ')[0]
            self.groupOperationsForModel = OpS.getGroupOperationsForModel(modelId)
            Utils.setupCompleter(self.groupOperationsForModel.keys(), self.operationGroupLineEdit)
        else:
            Utils.setupCompleter(self.groupOperations.keys(), self.operationGroupLineEdit)

    def updateForModelLineEdit(self):
        # if not self.isOperationsReseted:
        #     self.resetAllOperations()
        if self.forModelCheckBox.isChecked():
            self.forModelLineEdit.setReadOnly(False)
            self.forModelLineEdit.setFocus()
            if self.operationGroupLineEdit.text() != '':
                self.operationGroupLineEdit.clear()
                self.resetAllOperations(True)
        else:
            self.forModelLineEdit.setReadOnly(True)
            if self.forModelLineEdit.text() != '':
                self.forModelLineEdit.clear()
                self.resetAllOperations(True)
            self.operationGroupLineEdit.clear()
            self.operationGroupLineEdit.setFocus()
            Utils.setupCompleter(self.groupOperations.keys(), self.operationGroupLineEdit)

    def returnToModelOpersView(self):
        self.operationsGroupsHolder.setVisible(False)
        self.selectAllCheckbox.setVisible(True)
        self.modelInfoHolder.setVisible(True)
        self.operationsHolder.setEnabled(False)
        if not self.isOperationsReseted:
            self.resetAllOperations(True)
        self.operationsGroupViewBtn.setVisible(True)
        self.operationsGroupsReturnBtn.setVisible(False)
        self.selectedOperForGroup.clear()
        self.operationsHolder.setEnabled(False)
        self.modelsLineEdit.clear()
        self.dataUpdatedLabel.setText('')
        if self.newModelCheckBox.isChecked():
            self.newModelCheckBox.setChecked(False)
        if self.editModelCheckBox.isChecked():
            self.editModelCheckBox.setChecked(False)
        self.editModelHolder.setVisible(False)

    def setModelsLineEditForGroups(self):
        Utils.setupCompleter(self.modelsForGroup, self.forModelLineEdit)
        if self.modelsLineEdit.text() != '':
            completer = self.forModelLineEdit.completer()
            self.forModelLineEdit.setText(Utils.setReturnBtnForCompleter(completer))
            modelName = f'{self.modelNames[self.modelsLineEdit.text()][0]} - {self.modelsLineEdit.text()}'
            if modelName in self.modelsForGroup:
                self.forModelLineEdit.setText(self.modelsForGroup[self.modelsForGroup.index(modelName)])
                self.forModelCheckBox.setChecked(True)
                self.forModelLineEditChange()
        else:
            self.forModelLineEdit.clear()

    def forModelLineEditChange(self):
        selectedText = self.forModelLineEdit.text()
        if selectedText in self.modelsForGroup:
            operationsForModel = OpS.getOperationsForModel(selectedText.split(' - ')[0])
            self.groupOperationsForModel = OpS.getGroupOperationsForModel(selectedText.split(' - ')[0])
            Utils.setupCompleter(self.groupOperationsForModel.keys(), self.operationGroupLineEdit)

            operationsNumbers = [operation['ОперацияNo'] for operation in operationsForModel]
            # print(operationsNumbers)

            for opId, widgets in self.comboBoxItems.items():
                checkbox = widgets[0]
                lineEdit = widgets[1]
                label = widgets[2]

                if opId not in operationsNumbers:
                    if opId in self.operations:
                        checkbox.setText(f'{opId}:  {self.operations[opId]["name"]}')
                        checkbox.setEnabled(False)
                        checkbox.setStyleSheet('color: #87b0a6;')
                        lineEdit.setEnabled(False)
                        label.setEnabled(False)
                else:
                    checkbox.setEnabled(True)
                    checkbox.setStyleSheet('')
                    lineEdit.setEnabled(True)
                    label.setEnabled(True)

            for operation in operationsForModel:
                self.comboBoxItems[operation['ОперацияNo']][0].setText(
                    f'{operation["ОперацияNo"]}:  {operation["Операция"]}'
                )
                self.comboBoxItems[operation['ОперацияNo']][1].setText('')
                # self.comboBoxItems[operation.ОперацияNo][1].setText(str(round(operation.TimeForOper, 2)))
            # self.operationGroupLineEdit.clear()
            self.operationGroupLineEdit.setFocus()
        else:
            self.forModelLineEdit.clear()
            self.operationGroupLineEdit.clear()
            Utils.setupCompleter(self.groupOperations.keys(), self.operationGroupLineEdit)

            # Re-enable all checkboxes since no model is selected
            for opId, widgets in self.comboBoxItems.items():
                widgets[0].setEnabled(True)
                widgets[1].setEnabled(False)  # LineEdit starts disabled until checkbox is checked

            if not self.isOperationsReseted:
                self.resetAllOperations()
            # Utils.setupCompleter(self.groupOperations.keys(), self.operationGroupLineEdit)
            # self.resetAllOperations()
        if selectedText in self.modelsForGroup:
            self.isOperationsReseted = False

    def checkBtnSender(self):
        if self.newModelCheckBox.isChecked():
            self.isNewModel = True

        elif self.editModelCheckBox.isChecked():
            self.isNewModel = False

        self.checkAcceptAddingNewModel()

    def checkAcceptAddingNewModel(self, isCalling=False, modelId=None):
        # print(self.isNewModel)
        if not isCalling:
            if self.isNewModel:
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
                if checkbox[1].text() == '' or float(checkbox[1].text()) == 0:
                    MessageManager.showOnWidget(self,
                                                f"Моля въведете време за опер. {checkbox[0].text().split(':  ')[1]}!",
                                                'error')
                    checkbox[1].setFocus()
                    checkbox[1].selectAll()
                    return
                self.addOperationsForNewModel[int(checkbox[0].objectName())] = [checkbox[0].text().split(':  ')[1],
                                                                                float(checkbox[1].text())]
        # print(self.addOperationsForNewModel)

        if not self.addOperationsForNewModel:
            MessageManager.showOnWidget(self, 'Моля изберете поне една операция', 'error')
            return

        print(self.changedOperTimes)

        newDialog = CustomYesNowDialog()
        if self.isNewModel:
            message = 'Добавяне на нова поръчка?'
            mode = 'adding'
            name = self.newModelLineEdit.text()
        elif not self.isNewModel or isCalling:
            message = f'Редактиране на поръчка?'
            mode = 'editing'
            name = self.modelsLineEdit.text()
        newDialog.setMessage(name=name, message=message, mode=mode)
        result = newDialog.exec()
        if result == QDialog.Accepted:
            self.saveModelWithOperations(isCalling, modelId)
        else:
            return

    def saveModelWithOperations(self, isCalling, modelId):
        if not isCalling:
            if self.isNewModel:
                orderNo = self.newModelLineEdit.text()
            else:
                orderNo = self.modelNames[self.modelsLineEdit.text()][0]
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

            targetDate = datetime.datetime.now() + datetime.timedelta(days=30)

            self.newModel = {
                'isNew': self.isNewModel,
                'orderNo': orderNo,
                'orderPieces': orderPieces,
                'clientId': self.clientNames[self.clientsLineEdit.text()],
                'actual': self.actualCheckBox.isChecked(),
                'machineId': machineId,
                'fain': fain,
                'wearType': vidObleklo,
                'yarnId': yarnId,
                'pieces': orderPieces,
                'dateCreated': datetime.datetime.now().strftime('%Y-%m-%d'),
                'targetDate': targetDate.strftime('%Y-%m-%d'),
                'userCreated': self.user,
                'descr': self.descrLineEdit.text()
            }
            if self.isNewModel:
                newModelAdded = Ms.addNewModel(self.newModel, self.addOperationsForNewModel)
                self.modelsForGroup = Ms.getForModelsGroups()
            else:
                if self.checkOperations():
                    if self.effectChangesCheckBox.isChecked():
                        Ms.effectChangedOperTimes(self.changedOperTimes,
                                                  self.effectChangesComboBox.currentIndex() + 1,
                                                  self.modelNames[self.modelsLineEdit.text()][0])
                    newModelAdded = Ms.updateModel(self.newModel, None,
                                                   self.addOperationsForNewModel, self.removedOperations, None)
                    self.changedOperTimes.clear()
                else:
                    self.selectModel()
                    return
            if newModelAdded:
                if self.isNewModel:
                    message = f'Успешно добавен нов модел: {newModelAdded}'
                else:
                    message = f'Успешно редактиран модел: {self.modelsLineEdit.text()}'

                MessageManager.showOnWidget(self, message,
                                            'success')
                self.resetInformation()


            else:
                MessageManager.showOnWidget(self, 'Неуспешно добавен модел!', 'error')
                # logger.error(f'Failed to add Model: {self.newModel}')
                return
        else:
            if self.changedOperTimes:
                if Ms.effectChangedOperTimes(self.changedOperTimes,
                                             self.effectChangesComboBox.currentIndex() + 1,
                                             modelId):
                    Ms.updateModel(None, modelId,
                                   self.addOperationsForNewModel, self.removedOperations, self.usernameLabel.text())
                    # message = f'Успешно редактирано време за операции в модел: {self.modelsLineEdit.text()}'
                    # MessageManager.showOnWidget(self, message, 'success')
                    self.pageClosedSignal.emit(True)
                    self.close()
                else:
                    message = f'Неуспешно редактирано време за операции в модел: {self.modelsLineEdit.text()}'
                    MessageManager.showOnWidget(self, message, 'error')
                    return

    def deleteModel(self):
        modelId = self.modelNames[self.modelsLineEdit.text()][0]
        if modelId:

            newDialog = CustomYesNowDialog()
            message = 'Изтриване на модел?'
            mode = 'deleting'
            name = self.modelsLineEdit.text()

            newDialog.setMessage(name=name, message=message, mode=mode)
            result = newDialog.exec()
            if result == QDialog.Accepted:
                result = Ms.deleteModel(modelId)
                if result == 1:
                    MessageManager.showOnWidget(self, 'Успешно изтрит модел!', 'success')
                    self.resetInformation()
                    self.modelsForGroup = Ms.getForModelsGroups()
                    # self.editModelHolder.setVisible(False)
                elif result == 2:
                    MessageManager.showOnWidget(self, 'Не можете изтриете модел, съществуват листове за време!',
                                                'error')
                else:
                    MessageManager.showOnWidget(self, 'Неуспешно изтрит модел!', 'error')
            else:
                return

        else:
            MessageManager.showOnWidget(self, 'Моля изберете модел!', 'error')
            return

    def resetInformation(self):
        self.resetNewModelInfo()
        self.newModelCheckBox.setCheckState(Qt.CheckState.Unchecked)
        self.editModelCheckBox.setCheckState(Qt.CheckState.Unchecked)
        self.resetAllOperations(True)
        self.setModelsForClient()
        self.modelsLineEdit.clear()
        # self.modelsLineEdit.setFocus()
        self.clientsLineEdit.setFocus()
        self.clientsLineEdit.selectAll()
        self.editModelHolder.setVisible(False)
        self.effectChangesWidget.setVisible(False)
        self.effectChangesCheckBox.setCheckState(Qt.CheckState.Unchecked)

    def checkOperations(self):
        # print(self.modelExistingOperations)
        # print(self.addOperationsForNewModel)
        operations = Ms.checkIfOperationsCanBeDeleted(self.newModel,
                                                      self.removedOperations)
        # print(operations)
        # return False
        # print(operations)
        if operations:
            newDialog = CustomYesNowDialog(isNormalIcon=False)
            message = 'Не можете да изтриете следните операции:\n' + ', '.join(operations)
            newDialog.setMessage(name='', message=message, mode='warning')
            result = newDialog.exec()
            if result == QDialog.Accepted:
                return False
            else:
                return False
        else:
            return True

    def updateMachineComboBox(self):
        machineFine = self.machineComboBox.currentText().split(' :  ')[1].strip('E')
        self.machineGaugeLineEdit.setText(machineFine)

    def updateModelTypeCheckBox(self):
        if self.modelsLineEdit != '':
            self.resetAllOperations()
            modelTypeOper = Ms.getDfaultOperations(int(self.vidOblekla[self.modelTypeComboBox.currentText()]))
            if modelTypeOper:
                for operation in modelTypeOper:
                    if not self.comboBoxItems[operation[0]][0].isChecked():
                        self.comboBoxItems[operation[0]][0].setCheckState(Qt.CheckState.Checked)
                        self.comboBoxItems[operation[0]][1].setText(str(operation[1]))

    def setupNewModelInfo(self):
        sortedMachines = sorted(self.machines.keys(), key=lambda x: int(x.split(':')[0]))
        for machine in sortedMachines:
            self.machineComboBox.addItem(f'{machine} :  {self.machines[machine][1]}E')
        self.machineComboBox.setCurrentIndex(-1)

        sortedVidOblekla = sorted(self.vidOblekla.keys(), key=lambda x: int(x.split(':')[0]))
        for vidObleklo in sortedVidOblekla:
            self.modelTypeComboBox.addItem(vidObleklo)
        self.modelTypeComboBox.setCurrentIndex(-1)

        sortedYearns = sorted(self.yarns.keys(), key=lambda x: int(x.split(':')[0]))
        for yarn in sortedYearns:
            self.yarnComboBox.addItem(f'{yarn} :  {self.yarns[yarn][1]}')
        self.yarnComboBox.setCurrentIndex(-1)

    def setupClientAndModelLineEdit(self):
        for clientId, client in self.clients.items():
            self.clientNames[client] = int(clientId)
        Utils.setupCompleter(self.clientNames.keys(), self.clientsLineEdit)

    def selectClient(self):
        selectedText = self.clientsLineEdit.text()
        if hasattr(self, 'lastSelectedClient') and self.lastSelectedClient == selectedText and selectedText != '':
            self.modelsLineEdit.setFocus()
            return
        if self.clientsLineEdit.text() != '':
            # self.isOperationsReseted = False
            completer = self.clientsLineEdit.completer()
            self.clientsLineEdit.setText(Utils.setReturnBtnForCompleter(completer))
        selectedText = self.clientsLineEdit.text()
        self.modelNames.clear()
        self.modelsLineEdit.clear()
        self.dataUpdatedLabel.setText('')

        if self.newModelCheckBox.isChecked():
            self.newModelCheckBox.setCheckState(Qt.CheckState.Unchecked)
            self.resetNewModelInfo()
        if selectedText == '':
            if not self.isOperationsReseted:
                self.resetAllOperations()
            Utils.setupCompleter([], self.modelsLineEdit)
            return
        if selectedText not in self.clientNames:
            MessageManager.showOnWidget(self, 'Не е намерен клиент с такова име!', 'warning')
            self.clientsLineEdit.selectAll()
            self.clientsLineEdit.setFocus()
            return
        self.lastSelectedClient = selectedText
        self.setModelsForClient()
        self.modelsLineEdit.setFocus()
        if not self.isOperationsReseted:
            self.resetAllOperations(True)
        # if self.modelsLineEdit.receivers("editingFinished()") > 0:
        #     self.modelsLineEdit.editingFinished.disconnect(self.selectModel)
        # self.editModelHolder.setVisible(False)

    def setModelsForClient(self):
        self.models = Ms.getModelsForClient(self.clientNames[self.clientsLineEdit.text()])
        for model, value in self.models.items():
            if value[1] == self.clientNames[self.clientsLineEdit.text()]:
                self.modelNames[model] = [value[0], value[2]]
            # if model.ClientID == self.clientNames[self.clientsLineEdit.text()]:
            #     self.modelNames[model.ПоръчкаNo] = [model.id, model.DateCreated]
        Utils.setupCompleter(self.modelNames.keys(), self.modelsLineEdit)

    def selectModel(self):
        selectedText = self.modelsLineEdit.text()
        if hasattr(self, 'lastSelectedClient') and self.lastSelectedModel == selectedText and selectedText != '':
            self.modelsLineEdit.clearFocus()
            return
        print('selectModel')
        # if not self.isOperationsReseted:
        # self.resetAllOperations(True)
        self.changedOperTimes.clear()
        self.modelExistingOperations.clear()
        self.removedOperations.clear()
        self.modelsLineEdit.blockSignals(True)
        if self.modelsLineEdit.text() != '':
            completer = self.modelsLineEdit.completer()
            self.modelsLineEdit.setText(Utils.setReturnBtnForCompleter(completer))
        selectedText = self.modelsLineEdit.text()
        self.modelsLineEdit.blockSignals(False)
        if selectedText == '':
            if not self.isOperationsReseted:
                self.resetAllOperations()
            self.dataUpdatedLabel.setText('')
            self.editModelHolder.setVisible(False)
            return
        if selectedText not in self.modelNames.keys():
            MessageManager.showOnWidget(self, 'Не е намерен модел с такова Поръчка№!', 'warning')
            self.modelsLineEdit.selectAll()
            self.modelsLineEdit.setFocus()
            self.editModelHolder.setVisible(False)
            return

        self.lastSelectedModel = selectedText
        self.operationsForModel = OpS.getOperationsForModel(self.modelNames[selectedText][0])
        self.dataUpdatedLabel.setText(self.modelNames[selectedText][1])

        if self.newModelCheckBox.isChecked():
            self.setModelInfoIfExists()

        self.newModelOperations.clear()
        self.setEditModelVisible(True)

        self.setOperationsForModel(self.operationsForModel)
        if selectedText in self.modelNames.keys():
            self.isOperationsReseted = False
        self.modelsLineEdit.clearFocus()

    def setOperationsForModel(self, operations, isCalledFromTimePapers=False):
        if not isCalledFromTimePapers:
            self.newModelOperations.clear()
            for operation in operations:
                if self.modelExistingOperations:
                    self.modelExistingOperations.append(operation['ОперацияNo'])
                if not int(self.comboBoxItems[operation['ОперацияNo']][0].objectName()) in self.newModelOperations:
                    self.comboBoxItems[operation['ОперацияNo']][0].setChecked(True)
                    self.comboBoxItems[operation['ОперацияNo']][0].setText(
                        f'{operation["ОперацияNo"]}:  {operation["Операция"]}'
                    )
                    self.comboBoxItems[operation['ОперацияNo']][1].setText(str(round(operation['TimeForOper'], 2)))
                    self.comboBoxItems[operation['ОперацияNo']][3].setText(str(round(operation['TimeForOper'], 2)))
                    self.newModelOperations.append(int(operation['ОперацияNo']))
        else:
            for checkbox, value in self.comboBoxItems.items():
                value[0].setEnabled(False)
            for operation in operations:
                self.comboBoxItems[operation['ОперацияNo']][0].setChecked(True)
                self.comboBoxItems[operation['ОперацияNo']][0].setText(
                    f'{operation["ОперацияNo"]}:  {operation["Операция"]}'
                )
                self.comboBoxItems[operation['ОперацияNo']][1].setText(str(round(operation['TimeForOper'], 2)))
                self.comboBoxItems[operation['ОперацияNo']][3].setText(str(round(operation['TimeForOper'], 2)))

    def resetAllOperations(self, clearOperations=False, resetNames=True, resetActual=True):
        print('OPERATIONS RESETED')
        for checkbox in self.comboBoxItems.values():
            if int(checkbox[0].objectName()) in self.newModelOperations and not clearOperations:
                checkbox[0].setCheckState(Qt.CheckState.Checked)
            else:
                if resetNames:
                    if int(checkbox[0].objectName()) in self.operations.keys():
                        checkbox[0].setText(
                            f'{checkbox[0].objectName()}:  {self.operations[int(checkbox[0].objectName())]["name"]}'
                        )

            if resetActual:
                checkbox[0].setEnabled(True)
                checkbox[0].setStyleSheet("")

            checkbox[0].setChecked(False)
            checkbox[1].setText('')
            checkbox[3].setText('')

        if clearOperations:
            self.newModelOperations = []

        # self.isOperationsReseted = True

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

        if (self.modelsLineEdit.text() != '' and
                self.modelsLineEdit.text() in self.modelNames.keys() and
                self.newModelCheckBox.isChecked()):
            self.setModelInfoIfExists()

        if self.newModelCheckBox.isChecked():
            self.saveNewModel.setText("Добавяне")
            self.newModelInfoHolder.setEnabled(True)
            self.actualCheckBox.setCheckState(Qt.CheckState.Checked)
            self.editModelHolder.setEnabled(False)
            self.operationsHolder.setEnabled(True)
            self.modelsLineEdit.setReadOnly(True)
        else:
            self.resetNewModelInfo()
            self.editModelHolder.setEnabled(True)
            self.newModelInfoHolder.setEnabled(False)
            self.actualCheckBox.setCheckState(Qt.CheckState.Unchecked)
            self.operationsHolder.setEnabled(False)
            self.modelsLineEdit.setReadOnly(False)

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
        if self.sender().objectName() == 'editModelCheckBox':
            self.piecesLineEdit.setText(str(modelInfo[4]))
            if modelInfo[5]:
                self.actualCheckBox.setCheckState(Qt.CheckState.Checked)
            else:
                self.actualCheckBox.setCheckState(Qt.CheckState.Unchecked)

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
        self.actualCheckBox.setCheckState(Qt.CheckState.Unchecked)
        self.dataUpdatedLabel.setText('')

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
                                             newCustomComboBoxItem.label,
                                             newCustomComboBoxItem.currentOperTime]
            newCustomComboBoxItem.checkBox.stateChanged.connect(self.updateSelectAllBtn)
            newCustomComboBoxItem.operTime.connect(self.operTimeChanged)
            # print(self.comboBoxItems)

    def operTimeChanged(self, value):
        self.changedOperTimes[int(self.sender().checkBox.objectName())] = [float(self.sender().currentOperTime.text()),
                                      value]
        # print(self.sender().checkBox.objectName())
        # print(self.sender().currentOperTime.text())
        # print(value)

    def updateNewModelOperations(self):
        if isinstance(self.sender(), QCheckBox):
            if (self.sender().checkState() == Qt.CheckState.Checked and
                    int(self.sender().objectName()) not in self.newModelOperations and
                    not self.operationsGroupsHolder.isVisible() and self.editModelCheckBox.isChecked()):
                self.newModelOperations.append(int(self.sender().objectName()))
                if int(self.sender().objectName()) in self.removedOperations:
                    self.removedOperations.remove(int(self.sender().objectName()))
            elif (self.sender().checkState() == Qt.CheckState.Checked and
                    int(self.sender().objectName()) not in self.newModelOperations and
                    not self.operationsGroupsHolder.isVisible()):
                self.newModelOperations.append(int(self.sender().objectName()))
            elif (self.sender().checkState() == Qt.CheckState.Unchecked and
                  int(self.sender().objectName()) in self.newModelOperations and not
                    self.operationsGroupsHolder.isVisible() and self.editModelCheckBox.isChecked()):
                self.newModelOperations.remove(int(self.sender().objectName()))
                self.removedOperations.append(int(self.sender().objectName()))
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
            # print(self.selectedOperForGroup)
            # print(self.newModelOperations)
            # print(self.removedOperations)

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

    def logout(self):
        self.logoutSignal.emit(True)