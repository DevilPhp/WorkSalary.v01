from PySide6.QtGui import QDoubleValidator

from app.logger import logger
from app.ui.messagesManager import MessageManager
from app.ui.widgets.ui_defaultOperToModelTypeCustomWidget import *
from app.ui.widgets.ui_customCheckBoxWidget import Ui_customCheckBoxWidget
from app.services.operationServices import OperationsServices as OpS
from app.services.modelServices import ModelService as Ms
from PySide6.QtWidgets import QCheckBox


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
            MessageManager.showOnWidget(self, f'Успешно запаметяване на операции за вид {name}',
                                        'success')
            logger.info(f"Saved operations for model type {self.modelTypesDict[modelTypeIndex]}")
        else:
            MessageManager.showOnWidget(self, 'Не сте избрали операция', 'info')
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
        for modelType in self.modelTypes:
            self.modelTypesDict[modelType.OblekloVid] = modelType.OblekloName
            name = f'{modelType.OblekloVid}:  {modelType.OblekloName}'
            self.defaultModelTypeComboBox.addItem(name)
        self.defaultModelTypeComboBox.setMinimumWidth(self.defaultModelTypeComboBox.minimumWidth() + 50)
        self.defaultModelTypeComboBox.currentIndexChanged.connect(self.loadOperationsForModelType)

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
