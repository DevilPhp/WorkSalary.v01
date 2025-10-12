from datetime import datetime
from PySide6.QtWidgets import QMenu, QGraphicsDropShadowEffect, QDialog
from app.ui.widgets.ui_customWorkersWidget import *
from PySide6.QtGui import QStandardItemModel, QStandardItem
from app.models.sortingModel import CaseInsensitiveProxyModel
from app.ui.customWorkerDialog import CustomWorkerDialog
from app.ui.customYesNoMessage import CustomYesNowDialog
from app.services.workerServices import WorkerServices as WoS
from app.ui.messagesManager import MessageManager as MM
from app.utils.utils import Utils


class CustomWorkersWidget(QWidget, Ui_customWorkersEditWidget):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle("Персонал")
        self.workersInfo = WoS.getWorkersInfo()
        self.existingWorkersId = [str(key) for key in self.workersInfo.keys()]
        self.workerDialog = None

        self.workersModel = QStandardItemModel()
        self.workersHeaderNames = [
            'Номер', 'Име', 'Презиме',
            'Фамилия', 'Цех', 'Длъжност',
            'Постъпване', 'Напускане', 'Заплащане',
            'ЕГН', 'гр/с', 'Адрес', 'Телефон',
            'Дата начало стаж', 'Стаж Год.', 'Стаж Месеци', 'Стаж Дни'
        ]
        for i, tableHeaderName in enumerate(self.workersHeaderNames):
            self.workersModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.workersModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.workersModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelWorkers = CaseInsensitiveProxyModel(numericColumns=[0], dateColumns=[6, 7, 13], parent=self)
        self.proxyModelWorkers.setSourceModel(self.workersModel)
        self.workersTableView.setModel(self.proxyModelWorkers)
        self.workersTableView.setSortingEnabled(True)
        # self.timePapersForDayTableView.setModel(self.tableTimePapersModel)
        self.workersTableView.horizontalHeader().setStretchLastSection(True)
        self.workersTableView.horizontalHeader().setMinimumWidth(80)
        self.setInitialColumns()
        self.refreshWorkersTable()
        self.setSearchInput()
        self.workersTableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.workersTableView.customContextMenuRequested.connect(self.showCustomMenu)

        self.addNewWorkerBtn.clicked.connect(self.editSelectedWorker)
        self.workerEGNCheckBox.stateChanged.connect(self.toggleEGN)
        self.adressCheckBox.stateChanged.connect(self.toggleAdress)
        self.expCheckBox.stateChanged.connect(self.toggleExp)
        self.allCheckBox.stateChanged.connect(self.toggleAll)

    def showCustomMenu(self, position):
        menu = QMenu(self)
        editAction = menu.addAction('Редактиране')
        deleteAction = menu.addAction('Изтриване')
        action = menu.exec_(self.workersTableView.viewport().mapToGlobal(position))

        if action == editAction:
            index = self.workersTableView.currentIndex()
            workerId = index.siblingAtColumn(0).data()
            self.editSelectedWorker(workerId)

        if action == deleteAction:
            index = self.workersTableView.currentIndex()
            workerId = index.siblingAtColumn(0).data()
            self.deleteSelectedWorker(workerId)

    def deleteSelectedWorker(self, workerId):
        if workerId:
            yesNoDialog = CustomYesNowDialog()
            yesNoDialog.setMessage(name=workerId, message='Изтриване на работник?', mode='deleting')
            result = yesNoDialog.exec()
            if result == QDialog.Accepted:
                if WoS.deleteWorker(workerId):
                    self.refreshWorkersTable(True)
                    MM.showOnWidget(self, f'Успешно изтриване на работника с ID: {workerId}', 'success')
                else:
                    MM.showOnWidget(self, f'Неуспешно изтриване: {workerId}! Моля проверете листове за време',
                                    'error')

    def editSelectedWorker(self, workerId=None):
        self.workerDialog = CustomWorkerDialog(workerId, self.existingWorkersId, self)
        self.workerDialog.show()
        self.workerDialog.workerInfo.connect(self.setWorker)

    def setWorker(self, workerData):
        if workerData:
            yesNoDialog = CustomYesNowDialog()
            if workerData['isNew']:
                message = 'Създаване на нов работник?'
                name = workerData['firstName'] + ' ' + workerData['lastName']
                mode = 'adding'
            else:
                message = 'Редактиране на работника?'
                name = workerData['firstName'] + ' ' + workerData['lastName']
                mode = 'editing'
            yesNoDialog.setMessage(name=name, message=message, mode=mode)
            result = yesNoDialog.exec()
            if result == QDialog.Accepted:
                worker = WoS.setWorker(workerData)
                if worker:
                    self.refreshWorkersTable(True)
                    MM.showOnWidget(self, f'Успешно добавяне/редактиране на {workerData["id"]}!', 'success')
                    self.workerDialog.close()
                    self.workerDialog = None
            else:
                return

    def setSearchInput(self):
        workers = []
        for worker, value in self.workersInfo.items():
            workers.append(f'{worker}: {value["firstName"]} {value["lastName"]}')
        Utils.setupCompleter(workers, self.searchLineEdit)
        self.searchLineEdit.returnPressed.connect(self.updateWorkersTable)
        self.searchLineEdit.textChanged.connect(self.showAllTableRows)

    def showAllTableRows(self, text):
        if text == '':
            self.proxyModelWorkers.clearFilters()

    def updateWorkersTable(self):
        if self.searchLineEdit.text() != '':
            completer = self.searchLineEdit.completer()
            self.searchLineEdit.setText(self.setReturnBtnForCompleter(completer))
        selectedText = self.searchLineEdit.text()
        filterText = {0: [selectedText.split(': ')[0]]}
        self.proxyModelWorkers.setFilterForColumn(0, filterText)

    def setReturnBtnForCompleter(self, completer):
        currentIndex = completer.popup().currentIndex()
        if currentIndex.isValid():
            selectedText = currentIndex.data()
        else:
            selectedText = completer.completionModel().index(0, 0).data()
        return selectedText

    def refreshWorkersTable(self, fetchData=False):
        if fetchData:
            self.workersInfo = WoS.getWorkersInfo()
        self.workersModel.setRowCount(0)
        for worker, value in self.workersInfo.items():
            row = [
                QStandardItem(str(worker)),
                QStandardItem(value['firstName']),
                QStandardItem(value['middleName']),
                QStandardItem(value['lastName']),
                QStandardItem(value['ceh']),
                QStandardItem(value['position']),
                QStandardItem(value['startDate']),
                QStandardItem(value['endDate']),
                QStandardItem(value['paymentType']),
                QStandardItem(value['workerEGN']),
                QStandardItem(value['town']),
                QStandardItem(value['address']),
                QStandardItem(value['phone']),
                QStandardItem(value['workerExpStart']),
                QStandardItem(str(value['workerExpYears'])),
                QStandardItem(str(value['workerExpMonths'])),
                QStandardItem(str(value['workerExpDays']))
            ]
            self.workersModel.appendRow(row)

    def setInitialColumns(self):
        self.workersTableView.setColumnHidden(2, True)  # Презиме
        self.workersTableView.setColumnHidden(9, True)  # ЕГН
        self.workersTableView.setColumnHidden(10, True)  # гр/с
        self.workersTableView.setColumnHidden(11, True)  # Адрес
        self.workersTableView.setColumnHidden(12, True)  # Телефон
        self.workersTableView.setColumnHidden(13, True)  # Стаж Год
        self.workersTableView.setColumnHidden(14, True)  # Стаж Месеци
        self.workersTableView.setColumnHidden(15, True)  # Стаж Дни
        self.workersTableView.setColumnHidden(16, True)  # Дата начало стаж

    def checkAllstate(self):
        if self.workerEGNCheckBox.isChecked() and self.adressCheckBox.isChecked() and self.expCheckBox.isChecked():
            self.allCheckBox.setChecked(True)
        else:
            self.allCheckBox.blockSignals(True)
            self.allCheckBox.setChecked(False)
            self.allCheckBox.blockSignals(False)

    def toggleAll(self, state):
        self.workerEGNCheckBox.setChecked(state)
        self.adressCheckBox.setChecked(state)
        self.expCheckBox.setChecked(state)

    def toggleExp(self, state):
        self.workersTableView.setColumnHidden(13, not state)  # Стаж Год
        self.workersTableView.setColumnHidden(14, not state)  # Стаж Месеци
        self.workersTableView.setColumnHidden(15, not state)  # Стаж Дни
        self.workersTableView.setColumnHidden(16, not state)  # Дата начало стаж
        self.checkAllstate()

    def toggleEGN(self, state):
        self.workersTableView.setColumnHidden(2, not state)  # Презиме
        self.workersTableView.setColumnHidden(9, not state)  # ЕГН
        self.checkAllstate()

    def toggleAdress(self, state):
        self.workersTableView.setColumnHidden(10, not state)  # гр/с
        self.workersTableView.setColumnHidden(11, not state)  # Адрес
        self.workersTableView.setColumnHidden(12, not state)  # Телефон
        self.checkAllstate()

