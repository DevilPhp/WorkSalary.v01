from PySide6 import QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtGui import QDoubleValidator

from app.logger import logger
from app.ui.messagesManager import MessageManager as MM
from app.ui.widgets.ui_defaultOperToModelTypeCustomWidget import *
from app.ui.widgets.ui_customCheckBoxWidget import Ui_customCheckBoxWidget
from app.ui.customYesNoMessage import CustomYesNowDialog
from app.services.operationServices import OperationsServices as OpS
from app.services.modelServices import ModelService as Ms
from PySide6.QtWidgets import QCheckBox, QMenu, QDialog


class DefaultOperToModelTypeCustomWidget(QWidget, Ui_customWidgetForDefaultOper):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # MessageManager.initialize(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.operations = OpS.getAllOperations()
        self.comboBoxItems = {}
        # print(self.geometry())
        self.setCheckBox()
        self.selectAllCheckbox.stateChanged.connect(lambda: self.selectAllOperations())
        self.modelTypesDict = {}
        self.modelTypes = Ms.getAllModelTypes()
        self.setComboBox()
        self.loadOperationsForModelType()
        self.saveBtn.clicked.connect(self.saveOperationsForModelType)
        self.addNewOperation.clicked.connect(self.addNewOperationDialog)
        self.addNeModelType.clicked.connect(self.addNewModelTypeDialog)
        self.delDefModelTypeBtn.clicked.connect(self.deleteDefaultModelType)

    def deleteDefaultModelType(self):
        defaultModelType = int(self.defaultModelTypeComboBox.currentText().split(':  ')[0])
        dialog = CustomYesNowDialog()
        name = self.defaultModelTypeComboBox.currentText().split(':  ')[1]
        message = f'Изтриване на вид модел?'
        dialog.setMessage(name, message, 'deleting')
        if dialog.exec() == QDialog.Accepted:
            if Ms.deleteDefaultModelType(defaultModelType):
                self.modelTypes = Ms.getAllModelTypes()
                self.setComboBox()
                MM.showOnWidget(self, f'Успешно изтриване на вид модели: {defaultModelType}', 'success')
            else:
                MM.showOnWidget(self, 'Не е изтрит вид модели', 'error')

    def addNewModelTypeDialog(self):
        newText, ok = QtWidgets.QInputDialog.getText(self,"Добавяне", "Въведете име:")
        if ok and newText:
            newModelType = Ms.addNewDefaultModelType(newText)
            if newModelType:
                self.modelTypes = Ms.getAllModelTypes()
                self.setComboBox()
                MM.showOnWidget(self, f'Успешно добавяне на вид модели:\n {newText}', 'success')
            else:
                MM.showOnWidget(self, 'Не е добавен вид модели', 'error')

    def addNewOperationDialog(self):
        newText, ok = QtWidgets.QInputDialog.getText(self,"Добавяне", "Въведете име:")
        if ok and newText:
            newOperation = OpS.addNewDefaultOperations(newText)
            if newOperation:
                self.operations = OpS.getAllOperations()
                self.clearOperationsLayout()
                self.setCheckBox()
                MM.showOnWidget(self, f'Успешно добавяне на операция: {newText}', 'success')

    def saveOperationsForModelType(self):
        modelTypeIndex = self.defaultModelTypeComboBox.currentIndex() + 1
        selectedOperations = []
        for index, checkbox in self.comboBoxItems.items():
            if checkbox[0].isChecked():
                selectedOperations.append([
                    index,
                    checkbox[0].text().split(':  ')[1],
                    checkbox[1].text() if checkbox[1].text() != '' else 0
                ])
                # logger.info(f"Selected operation: {index}")
                # print(f"index: {index}, checkbox: {checkbox[0].isChecked()}")
        if selectedOperations:
            Ms.saveOperationsForModelType(modelTypeIndex, selectedOperations)
            name = self.defaultModelTypeComboBox.currentText().split(':  ')[1]
            MM.showOnWidget(self, f'Успешно запаметяване на операции за вид {name}',
                                        'success')
            logger.info(f"Saved operations for model type {self.modelTypesDict[modelTypeIndex]}")
        else:
            MM.showOnWidget(self, 'Не сте избрали операция', 'info')
            return

    def loadOperationsForModelType(self):
        self.resetAllOperations()
        defaultModelOpearions = Ms.getOperationsForModelType(
            self.defaultModelTypeComboBox.currentIndex() + 1
        )
        if defaultModelOpearions:
            for operation in defaultModelOpearions:
                self.comboBoxItems[operation.ОперацияNo][0].setChecked(True)
                self.comboBoxItems[operation.ОперацияNo][1].setText(str(operation.defaultTime)
                                                                    if operation.defaultTime else '')

    def resetAllOperations(self):
        for checkbox in self.comboBoxItems.values():
            checkbox[0].setChecked(False)
            checkbox[1].setText('')

    def setComboBox(self):
        self.defaultModelTypeComboBox.clear()
        for modelType in self.modelTypes:
            self.modelTypesDict[modelType.OblekloVid] = modelType.OblekloName
            name = f'{modelType.OblekloVid}:  {modelType.OblekloName}'
            self.defaultModelTypeComboBox.addItem(name)
        self.defaultModelTypeComboBox.setMinimumWidth(self.defaultModelTypeComboBox.minimumSizeHint().width() + 75)
        self.defaultModelTypeComboBox.currentIndexChanged.connect(self.loadOperationsForModelType)

    def setCheckBox(self):
        for index, operation in enumerate(self.operations):
            operName = self.operations[operation]['name']
            operType = self.operations[operation]['operationType']
            newCustomComboBoxItem = CustomCheckboxWidget()
            name = f'{operation}:  {operName}'

            newCustomComboBoxItem.checkBox.setText(name)

            newCustomComboBoxItem.checkBox.setObjectName(str(operation))
            row = index % 20
            col = index // 20
            self.operationsLayout.addWidget(newCustomComboBoxItem, row, col)
            self.comboBoxItems[operation] = [newCustomComboBoxItem.checkBox,
                                             newCustomComboBoxItem.lineEdit,
                                             newCustomComboBoxItem.label]
            newCustomComboBoxItem.checkBox.stateChanged.connect(self.updateSelectAllBtn)
            newCustomComboBoxItem.newOperName.connect(self.updateDBOperation)
            newCustomComboBoxItem.deleteWidget.connect(self.deleteSelectedOperation)

    def deleteSelectedOperation(self, widget):
        widgetName = widget.checkBox.text()
        operId = int(widgetName.split(':  ')[0])
        yesNoDialog = CustomYesNowDialog()
        message = 'Искате ли да изтриете операция:'
        mode = 'deleting'
        yesNoDialog.setMessage(name=widgetName, message=message, mode=mode)
        result = yesNoDialog.exec()
        if result == QDialog.Accepted:
            success = OpS.deleteOperation(operId)
            if success:
                widget.deleteLater()
                self.operationsLayout.removeWidget(widget)
                self.operations = OpS.getAllOperations()
                self.clearOperationsLayout()
                self.setCheckBox()
                MM.showOnWidget(self, f'Успешно изтриване на: {widgetName}', 'success')
            else:
                MM.showOnWidget(self,
                                f'Грешка при изтриване. Моля проверете връзки: {widgetName}',
                                'error'
                                )

    def updateDBOperation(self, text):
        if text:
            operId = int(text.split(':  ')[0])
            operName = text.split(':  ')[1]
            yesNoDialog = CustomYesNowDialog()
            message = 'Искате ли да промените операция:'
            yesNoDialog.setMessage(name=str(operId), message=message, mode='accept')
            result = yesNoDialog.exec()
            if result == QDialog.Accepted:
                success = OpS.updateOperationName(operId, operName)
                if success:
                    self.sender().checkBox.setText(text)
                    MM.showOnWidget(self,
                                                f'Успешно променихте операцията {operId}', 'success'
                                                )
                else:
                    MM.showOnWidget(self,
                                                f'Грешка при промяна на операцията {operId}', 'error'
                                                )
            else:
                return

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

    def clearOperationsLayout(self):
        for index in range(self.operationsLayout.count()):
            row = index % 20
            col = index // 20
            widget = self.operationsLayout.itemAtPosition(row, col).widget()
            if isinstance(widget, CustomCheckboxWidget):
                self.operationsLayout.removeWidget(widget)
                widget.deleteLater()
        self.comboBoxItems = {}

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
                    # lineEdit.setEnabled(False)
                # else:
                #     lineEdit.setEnabled(True)
        if isUnchecked:
            allChecked = False

        # Set the state of the "Select All" checkbox
        if allChecked:
            self.selectAllCheckbox.setCheckState(Qt.CheckState.Checked)
        else:
            self.selectAllCheckbox.setCheckState(Qt.CheckState.Unchecked)

        # Reconnect signal
        self.selectAllCheckbox.blockSignals(False)


class CustomCheckboxWidget(QWidget, Ui_customCheckBoxWidget):
    newOperName = Signal(str)
    deleteWidget = Signal(QWidget)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.lineEdit.setEnabled(False)
        self.checkBox.stateChanged.connect(self.toggleLabel)
        validator = QDoubleValidator(0.1, float('inf'), 2)
        validator.setNotation(QDoubleValidator.StandardNotation)
        validator.setLocale(QLocale.English)
        self.lineEdit.setValidator(validator)
        self.lineEdit.textChanged.connect(self.updateLabel)
        self.checkBox.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.checkBox.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self, pos):
        menu = QMenu(self)
        editAction = menu.addAction("Редактиране")
        deleteAction = menu.addAction("Изтриване")
        action = menu.exec_(self.checkBox.mapToGlobal(pos))

        if action == editAction:
            self.editCheckBoxName()
        elif action == deleteAction:
            self.deleteCheckBox()

    def deleteCheckBox(self):
        self.deleteWidget.emit(self)

    def editCheckBoxName(self):
        procedureId = self.checkBox.text().split(':  ')[0]
        newText, ok = QtWidgets.QInputDialog.getText(self,
                                                     "Редактиране", "Въведете име:",
                                                     text=self.checkBox.text().split(':  ')[1])
        newText = f'{procedureId}:  {newText}'
        if ok and self.window().objectName() == 'customWidgetForModelOper':
            self.checkBox.setText(newText)
        elif ok and self.window().objectName() == 'customWidgetForDefaultOper':
            self.newOperName.emit(newText)

    def updateLabel(self):
        text = self.lineEdit.text()
        if ',' in text:
            text = text.split(',')[0]
            text = text + '.'
        self.lineEdit.setText(text)

    def toggleLabel(self):
        if self.checkBox.checkState() == Qt.CheckState.Checked:
            self.label.setStyleSheet("QLabel { color: #008b69; }")
        else:
            self.label.setStyleSheet("")
