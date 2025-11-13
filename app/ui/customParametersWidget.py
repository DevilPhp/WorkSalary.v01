from functools import partial

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMenu, QDialog

from app.ui.widgets.ui_customParametersWidget import *
from app.models.tableModel import TableModel
from app.services.tableServices import fetchDataFromDbWithRelations
from app.services.modelServices import ModelService as Ms
from app.services.workerServices import WorkerServices as Ws
from app.models.sortingModel import CaseInsensitiveProxyModel
from app.ui.customParametersDialog import CustomAddParametersDialog
from app.ui.customYesNoMessage import CustomYesNowDialog
from app.services.userServices import UserServices as Us
from app.ui.messagesManager import MessageManager as MM
import pandas as pd


class CustomParametersWidget(QWidget, Ui_customParametersWidget):
    logoutSignal = Signal(bool)

    def __init__(self, mainWindow, user, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle('Номенклатури')
        self.mainWindow = mainWindow
        self.proxyModel = None
        self.model = None
        self.usernameLabel.setText(user)
        self.user = user

        self.selectedTable = None
        self.selectedIndex = None
        self.originalDispayValue = None
        self.originalUserValue = None

        self.numericColumns = []
        self.dataColumns = []

        # self.loadTable('cehove')

        self.clientsBtn.clicked.connect(lambda: self.btnClicked('clients', self.clientsBtn))
        self.cehoveBtn.clicked.connect(lambda: self.btnClicked('cehove', self.cehoveBtn))
        self.machinesBtn.clicked.connect(lambda: self.btnClicked('machines', self.machinesBtn))
        self.workingPosBtn.clicked.connect(lambda: self.btnClicked('workerPositions', self.workingPosBtn))
        self.yarnsBtn.clicked.connect(lambda: self.btnClicked('yarns', self.yarnsBtn))
        self.usersBtn.clicked.connect(lambda: self.btnClicked('users', self.usersBtn))
        self.operTypesBtn.clicked.connect(lambda: self.btnClicked('operationTypes', self.operTypesBtn))

        self.addNewEntryBtn.clicked.connect(self.addNewEntry)

        self.parametersTableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.parametersTableView.customContextMenuRequested.connect(self.showContextMenu)
        self.parametersTableView.doubleClicked.connect(self.tableDoubleClicked)

        self.logoutBtn.clicked.connect(self.logout)

        self.btnClicked('clients', self.clientsBtn)

    def addNewEntry(self):
        headers = {}
        if self.selectedTable and self.model:
            for i in range(self.model.columnCount()):
                if i > 0:
                    name = self.checkHeadersNames(i)
                    if i in self.numericColumns:
                        headers[name] = [i, 'numeric']
                    elif i in self.dataColumns:
                        headers[name] = [i, 'date']
                    elif name == 'Парола':
                        headers[name] = [i, 'password']
                    else:
                        headers[name] = [i, 'str']
            # headers = [self.model.headerData(i, Qt.Orientation.Horizontal) for i in range(
            #     self.model.columnCount()) if i > 0]
            dialog = CustomAddParametersDialog(headers)
            dialog.newEntryInfo.connect(self.addNewEntryToDb)
            dialog.exec_()

    def addNewEntryToDb(self, data):
        if self.selectedTable == 'users':
            self.addNewUser(data)
        elif self.selectedTable == 'cehove':
            self.addNewCehove(data)
        elif self.selectedTable =='machines':
            self.addNewMachine(data)
        elif self.selectedTable == 'workerPositions':
            self.addNewWorkerPosition(data)
        elif self.selectedTable == 'operationTypes':
            self.addNewOperationType(data)
        elif self.selectedTable == 'yarns':
            self.addNewYarn(data)
        elif self.selectedTable == 'clients':
            self.addNewClient(data)
        else:
            return

    def addNewUser(self, data):
        result = Us.registerNewUser(data)
        if result == 1:
            MM.showOnWidget(self, f"потребител '{data['Потребител']}' е добавен успешно!", 'success')
            self.btnClicked('users', self.usersBtn)
        elif result == -1:
            MM.showOnWidget(self, f"потребител '{data['Потребител']}' вече съществува!", 'error')
        else:
            MM.showOnWidget(self, f"потребител '{data['Потребител']}' не може да бъде добавен", 'error')

    def addNewClient(self, data):
        result = Ms.addNewClient(data, self.model.rowCount())
        if result == 1:
            MM.showOnWidget(self, f"Клиент '{data['Клиент']}' е добавен успешно!",'success')
            self.btnClicked('clients', self.clientsBtn)
        elif result == -1:
            MM.showOnWidget(self, f"Клиент '{data['Клиент']}' вече съществува!", 'error')
        else:
            MM.showOnWidget(self, f"Клиент '{data['Клиент']}' не може да бъде добавен!", 'error')

    def addNewCehove(self, data):
        result = Ws.addNewCehove(data)
        if result:
            MM.showOnWidget(self, f"Работно място '{data['Група']}' е добавено успешно!",'success')
            self.btnClicked('cehove', self.cehoveBtn)
        else:
            MM.showOnWidget(self, f"Работно място '{data['Група']}' не може да бъде добавено!", 'error')

    def addNewMachine(self, data):
        result = Ms.addNewMachine(data, self.model.rowCount())
        if result:
            message = f"Машина '{data['MachineType']}': {data['MachineFine']}E е добавена успешно!"
            MM.showOnWidget(self, message,'success')
            self.btnClicked('machines', self.machinesBtn)
        else:
            MM.showOnWidget(self, f"Машина '{data['MachineType']}' не може да бъде добавена!", 'error')

    def addNewWorkerPosition(self, data):
        result = Ws.addNewWorkerPosition(data, self.model.rowCount())
        if result:
            MM.showOnWidget(self, f"Длъжност '{data['Длъжност']}' е добавена успешно!",'success')
            self.btnClicked('workerPositions', self.workingPosBtn)
        else:
            MM.showOnWidget(self, f"Длъжност '{data['Длъжност']}' не може да бъде добавена!", 'error')

    def addNewOperationType(self, data):
        result = Ws.addNewOperationType(data, self.model.rowCount())
        if result:
            MM.showOnWidget(self, f"Вид длъжност '{data['OperName']}' е добавен успешно!",'success')
            self.btnClicked('operationTypes', self.operTypesBtn)
        else:
            MM.showOnWidget(self, f"Вид длъжност '{data['OperName']}' не може да бъде добавен!", 'error')

    def addNewYarn(self, data):
        result = Ms.addNewYarn(data, self.model.rowCount())
        if result:
            MM.showOnWidget(self, f"Прежда '{data['ПреждаТип']}' е добавена успешно!",'success')
            self.btnClicked('yarns', self.yarnsBtn)
        else:
            MM.showOnWidget(self, f"Прежда '{data['ПреждаТип']}' не може да бъде добавена!", 'error')

    def checkHeadersNames(self, i):
        name = self.model.headerData(i, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole)
        if name == 'passwordHash':
            name = 'Парола'

        if name == 'username':
            name = 'Потребител'

        if name == 'userRole':
            name = 'Ниво'

        return name

    def btnClicked(self, tableName, btn):
        self.loadTable(tableName)
        if tableName != self.selectedTable:
            self.selectedTable = tableName

            for btns in self.widget_7.findChildren(QPushButton):
                btns.setStyleSheet("")

            btn.setStyleSheet("background-color: #92b1a8;")
        else:
            return

    def loadTable(self, tableName):
        self.proxyModel = None
        self.model = None
        data = fetchDataFromDbWithRelations(tableName)
        self.model = TableModel(data)

        editableColumns = []
        if tableName == 'users':
            editableColumns = []
        # if tableName == 'cehove':
        #     editableColumns = [2, 3]

        self.model.setEditableColumns(editableColumns)

        self.parametersTableView.setModel(self.model)
        self.numericColumns = [i for i, dtype in enumerate(data.dtypes) if pd.api.types.is_numeric_dtype(dtype)]
        self.dataColumns = [i for i, dtype in enumerate(data.dtypes) if pd.api.types.is_datetime64_any_dtype(dtype)]

        self.proxyModel = CaseInsensitiveProxyModel(numericColumns=self.numericColumns,
                                                    dateColumns=self.dataColumns,
                                                    parent=self)
        self.setProxyModel(self.proxyModel, self.model, self.parametersTableView)
        self.model.dataEdited.connect(self.tableDataChanged)
        # self.parametersTableView.resizeColumnsToContents()
        self.parametersTableView.sortByColumn(0, Qt.SortOrder.DescendingOrder)
        self.parametersTableView.horizontalHeader().setStretchLastSection(True)
        self.parametersTableView.horizontalHeader().setMinimumWidth(80)
        self.parametersTableView.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)

        if tableName == 'users':
            self.parametersTableView.setColumnHidden(2, True)
        else:
            self.parametersTableView.setColumnHidden(2, False)

    def showContextMenu(self, pos):
        menu = QMenu(self)
        deleteAction = menu.addAction("Изтрий")
        if self.selectedTable == 'users':
            editAction = menu.addAction("Редактиране")
        else:
            еditAction = None
        # editAction = menu.addAction("Редактиране")
        action = menu.exec_(self.parametersTableView.viewport().mapToGlobal(pos))

        if action == deleteAction:
            selectedId = self.parametersTableView.selectionModel().selectedRows(0)[0].data(Qt.ItemDataRole.DisplayRole)
            selectedName = self.parametersTableView.selectionModel().selectedRows(1)[0].data(Qt.ItemDataRole.DisplayRole)
            if selectedId and selectedName:

                dialog = CustomYesNowDialog()
                message = f'Изтриване на: {selectedId} - {selectedName}'
                dialog.setMessage(name='', message=message, mode='deleting')
                result = dialog.exec()
                if result == QDialog.Accepted:
                    # print(f"Изтриване на ред {selectedId}")
                    self.deleteRow(selectedId, selectedName)
        elif self.selectedTable == 'users':
            if action == editAction:
                userId = self.parametersTableView.selectionModel().selectedRows(0)[0].data(Qt.ItemDataRole.DisplayRole)
                username = self.parametersTableView.selectionModel().selectedRows(1)[0].data(Qt.ItemDataRole.DisplayRole)
                userRole = self.parametersTableView.selectionModel().selectedRows(3)[0].data(Qt.ItemDataRole.DisplayRole)

                # if username == self.user:
                #     MM.showOnWidget(self, f"Не можете да изтриете текущия потребител!", 'error')
                #     return

                headers = {
                    'Нова парола:': [0, 'password'],
                    'Парола отново:': [1, 'password'],
                    'Ниво': [2, 'str', userRole]
                }
                dialog = CustomAddParametersDialog(headers)
                dialog.dialogTitle.setText(f"Редактиране на:  {username}")
                dialog.newEntryInfo.connect(partial(self.editCurrentUser, userId))
                dialog.exec_()

    def editCurrentUser(self, userId, data):
        user = Us.editUser(userId, data)
        if user:
            if user == self.user:
                self.logout()
                window = self.mainWindow
            else:
                self.loadTable('users')
                window = self
            MM.showOnWidget(window, f"Потребител '{user}' е редактиран успешно!", 'success', 1500)
        else:
            MM.showOnWidget(self, f"Потребител '{userId}' не може да бъде редактиран!", 'error')

    def deleteRow(self, rowId, name):
        if self.selectedTable == 'users':
            self.deleteSelectedUser(rowId, name)
        elif self.selectedTable == 'cehove':
            self.deleteSelectedCehove(rowId, name)
        elif self.selectedTable =='machines':
            self.deleteSelectedMachine(rowId, name)
        elif self.selectedTable == 'workerPositions':
            self.deleteSelectedWorkerPosition(rowId, name)
        elif self.selectedTable == 'operationTypes':
            self.deleteSelectedOperationType(rowId, name)
        elif self.selectedTable == 'yarns':
            self.deleteSelectedYarn(rowId, name)
        elif self.selectedTable == 'clients':
            self.deleteSelectedClient(rowId, name)

    def deleteSelectedUser(self, rowId, name):
        if name == self.user:
            MM.showOnWidget(self, f"Не можете да изтриете текущия потребител!", 'error')
            return
        if Us.deleteUser(rowId):
            self.loadTable('users')
            MM.showOnWidget(self, f"Потребител '{name}' е изтрит успешно!", 'success', 1500)
        else:
            MM.showOnWidget(self, f"Потребител '{name}' не може да бъде изтрит!", 'error')

    def deleteSelectedClient(self, rowId, name):
        result = Ms.deleteClient(rowId, name)
        if result == 1:
            self.loadTable('clients')
            MM.showOnWidget(self, f"Клиент: '{name}' е изтрит успешно!", 'success', 1500)
        elif result == -1:
            MM.showOnWidget(self, f"Клиент: '{name}' има съществуващи врзки с произв. модел/модели!",
                            'warning', 3000)
        else:
            MM.showOnWidget(self, f"Клиент: '{name}' не може да бъде изтрит!", 'error')

    def deleteSelectedCehove(self, rowId, name):
        result = Ws.deleteSelectedCehove(rowId)
        if result == 1:
            self.loadTable('cehove')
            MM.showOnWidget(self, f"Работно място: '{name}' е изтрито успешно!", 'success', 1500)
        elif result == -1:
            MM.showOnWidget(self, f"Работно място: '{name}' има съществуващи врзки с работници!",
                            'warning', 3000)
        else:
            MM.showOnWidget(self, f"Работно място: '{name}' не може да бъде изтрито!", 'error')

    def deleteSelectedMachine(self, rowId, name):
        result = Ms.deleteSelectedMachine(rowId)
        if result == 1:
            self.loadTable('machines')
            MM.showOnWidget(self, f"Машина: '{name}' е изтрита успешно!", 'success', 1500)
        elif result == -1:
            MM.showOnWidget(self, f"Машина: '{name}' има съществуващи врзки с производ. модел/модели!",
                            'warning', 3000)
        else:
            MM.showOnWidget(self, f"Машина: '{name}' не може да бъде изтрита!", 'error')

    def deleteSelectedWorkerPosition(self, rowId, name):
        result = Ws.deleteSelectedWorkerPosition(rowId)
        if result == 1:
            self.loadTable('workerPositions')
            MM.showOnWidget(self, f"Длъжност: '{name}' е изтрита успешно!", 'success', 1500)
        elif result == -1:
            MM.showOnWidget(self, f"Длъжност: '{name}' има съществуващи врзки с работници и/или вид длъжност!",
                            'warning', 3000)
        else:
            MM.showOnWidget(self, f"Длъжност: '{name}' не може да бъде изтрита!", 'error')

    def deleteSelectedOperationType(self, rowId, name):
        result = Ws.deleteSelectedOperationType(rowId)
        if result == 1:
            self.loadTable('operationTypes')
            MM.showOnWidget(self, f"Вид операция: '{name}' е изтрит успешно!", 'success', 1500)
        elif result == -1:
            MM.showOnWidget(self, f"Вид операция: '{name}' има съществуващи врзки с длъжности/операции!",
                            'warning', 3000)
        else:
            MM.showOnWidget(self, f"Вид операция: '{name}' не може да бъде изтрита!", 'error')

    def deleteSelectedYarn(self, rowId, name):
        result = Ms.deleteSelectedYarn(rowId)
        if result == 1:
            self.loadTable('yarns')
            MM.showOnWidget(self, f"Прежда: '{name}' е изтрита успешно!", 'success', 1500)
        elif result == -1:
            MM.showOnWidget(self, f"Прежда: '{name}' има съществуващи врзки с поръчки!",
                            'warning', 3000)
        else:
            MM.showOnWidget(self, f"Прежда: '{name}' не може да бъде изтрита!", 'error')

    def setProxyModel(self, proxyModel, model, table):
        proxyModel.setSourceModel(model)
        table.setModel(proxyModel)
        table.setSortingEnabled(True)

    def tableDoubleClicked(self, row):
        # print(self.selectedTable)
        # print(row.column())
        if row.column() > 0:
            # if self.selectedTable == 'cehove':
            #     print('here')
            #     row.column()
            #     print(row.column())
            self.originalDispayValue = row.data(Qt.ItemDataRole.DisplayRole)
            self.originalUserValue = row.data(Qt.ItemDataRole.UserRole)
            self.selectedIndex = row
        else:
            self.originalDispayValue = None
            self.originalUserValue = None
            self.selectedIndex = None
            return

    def tableDataChanged(self, row, column, value):
        print(self.originalUserValue, self.originalDispayValue, self.selectedIndex)
        print(self.model.index(row, 0).data(Qt.ItemDataRole.DisplayRole))

        if isinstance(self.originalDispayValue, int):
            print('Digits')
        elif self.originalDispayValue.isdigit():
            print('Digits')

        rowId = self.model.index(row, 0).data(Qt.ItemDataRole.DisplayRole)
        newValue = value if value else self.originalDispayValue

        print(f"Cell at row {row}, column {column} changed to: {value}")
        print(self.selectedTable)
        # print(row.data(Qt.ItemDataRole.DisplayRole))
        # print(topLeft, bottomRight, roles)
        # self.proxyModel.dataChanged.disconnect(self.tableDataChanged)
    #     if self.selectedTable == 'cehove':
    #         self.updateCehoveTable()
    #
    # def updateCehoveTable(self):
    #     selectedRows = self.parametersTableView.selectionModel().selectedRows()
    #     print(selectedRows)

    def logout(self):
        self.logoutSignal.emit(True)
        # self.close()
