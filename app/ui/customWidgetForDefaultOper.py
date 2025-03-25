from app.ui.widgets.ui_defaultOperToModelTypeCustomWidget import *
from app.ui.widgets.ui_customCheckBoxWidget import Ui_customCheckBoxWidget
from app.services.operationServices import OperationsServices as OpS
from app.services.modelServices import ModelService as MS
from PySide6.QtWidgets import QCheckBox


class DefaultOperToModelTypeCustomWidget(QWidget, Ui_customWidgetForDefaultOper):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.operations = OpS.getAllOperations()
        self.comboBoxItems = {}
        self.setCheckBox()
        self.selectAllCheckbox.stateChanged.connect(lambda: self.selectAllOperations())
        self.modelTypesDict = {}
        self.modelTypes = MS.getAllModelTypes()
        self.setComboBox()


    def setComboBox(self):
        for modelType in self.modelTypes:
            self.modelTypesDict[modelType.OblekloVid] = modelType.OblekloName
            name = f'{modelType.OblekloVid}- {modelType.OblekloName}'
            self.defaultModelTypeComboBox.addItem(name)
        self.defaultModelTypeComboBox.setMinimumWidth(self.defaultModelTypeComboBox.minimumWidth() + 50)

    def setCheckBox(self):
        for index, operation in enumerate(self.operations):
            newCustomComboBoxItem = CustomCheckboxWidget()
            name = f'{operation.ОперацияNo}- {operation.Операция}'
            newCustomComboBoxItem.checkBox.setText(name)
            newCustomComboBoxItem.checkBox.setObjectName(str(operation.ОперацияNo))
            row = index % 15
            col = index // 15
            self.operationsLayout.addWidget(newCustomComboBoxItem, row, col)
            self.comboBoxItems[operation.ОперацияNo] = [newCustomComboBoxItem.checkBox, newCustomComboBoxItem.lineEdit]
            newCustomComboBoxItem.checkBox.stateChanged.connect(self.updateSelectAllBtn)

    def selectAllOperations(self):
        # self.selectAllCheckbox.blockSignals(True)

        for index in self.comboBoxItems.keys():
            widget = self.comboBoxItems[index][0]
            lineEdit = self.comboBoxItems[index][1]
            if isinstance(widget, QCheckBox):
                widget.blockSignals(True)
                widget.setCheckState(self.selectAllCheckbox.checkState())
                if widget.checkState() == Qt.CheckState.Checked:
                    lineEdit.setEnabled(True)
                else:
                    lineEdit.setEnabled(False)
                widget.blockSignals(False)

        # self.selectAllCheckbox.blockSignals(False)

    def updateSelectAllBtn(self):
        # widget = self.comboBoxItems[operationNo][0]
        # print(widget)
        # if isinstance(widget, QCheckBox):
        #     if widget.checkState() != Qt.CheckState.Checked:
        #         self.selectAllCheckbox.setCheckState(Qt.CheckState.Unchecked)

        # Prevent recursion by temporarily disconnecting signal
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
