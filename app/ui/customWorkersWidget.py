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
        self.proxyModelWorkers = CaseInsensitiveProxyModel(numericColumns=[0], parent=self)
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

        self.addNewWorkerBtn.clicked.connect(self.openCustomWorkerDialog)
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
            self.editSelectedWorker(position)

    def editSelectedWorker(self, position):
        index = self.workersTableView.currentIndex()
        workerId = index.siblingAtColumn(0).data()
        if workerId:
            dialog = CustomWorkerDialog(workerId, self)
            dialog.show()
            dialog.yesBtn.clicked.connect(lambda: self.editWorker(workerId, dialog))

    def editWorker(self, workerId, dialog):
        if dialog.isDialogChanged:
            startDate = datetime.strptime(dialog.startDateEdit.date().toString('yyyy-MM-dd'), '%Y-%m-%d') \
                if dialog.startDateEdit.date().isValid() and dialog.startCheckBox.isChecked() else None
            endDate = datetime.strptime(dialog.leaveDateEdit.date().toString('yyyy-MM-dd'), '%Y-%m-%d') \
                if dialog.leaveDateEdit.date().isValid() and dialog.leavingCheckBox.isChecked() else None

            worker = {
                'id': workerId,
                'firstName': dialog.workerName.text() if dialog.workerName.text() != '' else None,
                'middleName': dialog.workerSirname.text() if dialog.workerSirname.text() != '' else None,
                'lastName': dialog.workerLastname.text() if dialog.workerLastname.text() != '' else None,
                'cehId': dialog.cehoveComboBox.currentIndex() + 1 if dialog.cehoveComboBox.currentIndex() >= 0 else None,
                'positionId': dialog.positionComboBox.currentIndex() + 1
                if dialog.positionComboBox.currentIndex() >= 0 else None,
                'EGN': dialog.workerEGN.text() if dialog.workerEGN.text() != '' else None,
                'paymentTypeId': dialog.paymentTypeComboBox.currentIndex(),
                'workerPhone': dialog.workerTel.text() if dialog.workerTel.text() != '' else None,
                'startDate': startDate,
                'endDate': endDate,
                'town': dialog.workerTownAdress.text() if dialog.workerTownAdress.text() != '' else None,
                'address': dialog.workerStreetAdress.text() if dialog.workerStreetAdress.text() != '' else None,
            }

            yesNoDialog = CustomYesNowDialog()
            yesNoDialog.setMessage(f'{worker["firstName"]} {worker["lastName"]}', 'Промяна на работник?',
                                   'accept')
            result = yesNoDialog.exec()
            if result == QDialog.DialogCode.Accepted:
                isWorkerUpdated = WoS.updateWorker(worker)
                if isWorkerUpdated:
                    MM.showOnWidget(self,
                                    f'Работникът {worker["firstName"]} {worker["lastName"]} е променен успешно.',
                                    'success')
                dialog.close()

        else:
            dialog.close()
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

    def refreshWorkersTable(self):
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

    def openCustomWorkerDialog(self):
        dialog = CustomWorkerDialog()
        result = dialog.exec_()
