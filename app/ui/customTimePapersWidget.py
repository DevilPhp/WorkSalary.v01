from datetime import datetime
from functools import partial

from PySide6.QtGui import QStandardItemModel, QStandardItem

from app.ui.widgets.ui_customTimePapersWidget import *
from app.utils.utils import Utils
from app.services.workerServices import WorkerServices as WoS
from app.services.modelServices import ModelService as MoS
from app.ui.customCalendarWidget import CustomCalendarDialog
from app.models.tableModel import TableModel
from app.models.sortingModel import CaseInsensitiveProxyModel

class CustomTimePapersWidget(QWidget, Ui_customTimePapersWidget):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.workers = WoS.getWorkers()
        self.models = MoS.getClientsAndModels()
        self.clientModels = []
        self.workersInfo = []
        self.setupWorkerAndModelsCompleter()
        self.timePaperDateEdit.setDate(QDate.currentDate())
        self.setupWorkingTimeWidgets()
        self.tableTimePapersModel = QStandardItemModel()
        self.tableTimePapersHeadersNames = ['Номер', 'ПоръчкаNo', 'ОперацияNo', 'Операция', 'Бройки', 'Време']
        for i, tableHeaderName in enumerate(self.tableTimePapersHeadersNames):
            self.tableTimePapersModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.tableTimePapersModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.tableTimePapersModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelWorkers = CaseInsensitiveProxyModel(numericColumns=[0, 2, 4, 5],
                                                           parent=self)
        self.setProxyModel(self.proxyModelWorkers, self.tableTimePapersModel, self.timePapersForDayTableView)
        # self.timePapersForDayTableView.setModel(self.tableTimePapersModel)
        self.timePapersForDayTableView.horizontalHeader().setStretchLastSection(True)
        self.timePapersForDayTableView.horizontalHeader().setMinimumWidth(80)
        # self.timePapersForDayTableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.refreshTimePapersForToday()

        self.shiftStart.editingFinished.connect(self.updateDuration)
        self.shiftEnd.editingFinished.connect(self.updateDuration)
        self.overtimeStart.editingFinished.connect(self.updateDuration)
        self.overtimeEnd.editingFinished.connect(self.updateDuration)
        self.hourlyStart.editingFinished.connect(self.updateDuration)
        self.hourlyEnd.editingFinished.connect(self.updateDuration)

        self.calendarBtn.clicked.connect(self.showCustomCalendaDialog)

    def refreshTimePapersForToday(self):
        searchedDate = self.timePaperDateEdit.date().toString('yyyy-MM-dd')
        formatedDate = datetime.strptime(searchedDate, '%Y-%m-%d').date()
        # print(formatedDate, searchedDate)
        data = WoS.getTimePapersForDate(formatedDate)
        self.tableTimePapersModel.setRowCount(0)
        # print(data)
        for item in data:
            row = [
                QStandardItem(str(item[0])),
                QStandardItem(item[1]),
                QStandardItem(str(item[2])),
                QStandardItem(item[3]),
                QStandardItem(str(item[4])),
                QStandardItem(Utils.setFloatToStr(item[5])),
            ]
            self.tableTimePapersModel.appendRow(row)
        # model = TableModel(data)
        # self.timePapersForDayTableView.setModel(model)
        #
        # self.timePapersForDayTableView.resizeColumnsToContents()
        # self.timePapersForDayTableView.sortByColumn(0, Qt.SortOrder.AscendingOrder)

    def setProxyModel(self, proxyModel, model, table):
        proxyModel.setSourceModel(model)
        table.setModel(proxyModel)
        table.setSortingEnabled(True)

    def showCustomCalendaDialog(self):
        calendarDialog = CustomCalendarDialog()
        calendarDialog.calendarCustomWidget.setSelectedDate(self.timePaperDateEdit.date())
        Utils.calculatingIdealDialogShowPos(self, calendarDialog)
        calendarDialog.dateSelected.connect(self.updateDateLabel)
        calendarDialog.exec_()

    def updateDateLabel(self, formattedDate):
        # print(f'Selected date: {formattedDate}')
        self.timePaperDateEdit.setDate(formattedDate)
        self.refreshTimePapersForToday()

    def updateDuration(self):
        if self.sender() == self.shiftStart or self.sender() == self.shiftEnd:
            duration = Utils.calculateMinutes(self.shiftStart, self.shiftEnd)
            self.shiftTotalMins.setText(str(duration))
        if self.sender() == self.hourlyStart or self.sender() == self.hourlyEnd:
            duration = Utils.calculateMinutes(self.hourlyStart, self.hourlyEnd)
            self.hourlyTotalMins.setText(str(duration))
        if self.sender() == self.overtimeStart or self.sender() == self.overtimeEnd:
            duration = Utils.calculateMinutes(self.overtimeStart, self.overtimeEnd)
            self.overtimeTotalMins.setText(str(duration))


    def setupWorkingTimeWidgets(self):
        self.hourlyEndWidget.setEnabled(False)
        self.hourlyStartWidget.setEnabled(False)
        self.overtimeEndWidget.setEnabled(False)
        self.overtimeStartWidget.setEnabled(False)
        self.isHourlyWorking.stateChanged.connect(self.toggleHourlyWorking)
        self.isOvertimeWorking.stateChanged.connect(self.toggleOvertimeWorking)

    def toggleHourlyWorking(self):
        if self.isHourlyWorking.isChecked():
            self.hourlyStartWidget.setEnabled(True)
            self.hourlyEndWidget.setEnabled(True)
        else:
            self.hourlyStartWidget.setEnabled(False)
            self.hourlyEndWidget.setEnabled(False)
            self.hourlyStart.setTime(QTime(0, 0))
            self.hourlyEnd.setTime(QTime(0, 0))

    def toggleOvertimeWorking(self):
        if self.isOvertimeWorking.isChecked():
            self.overtimeStartWidget.setEnabled(True)
            self.overtimeEndWidget.setEnabled(True)
        else:
            self.overtimeStartWidget.setEnabled(False)
            self.overtimeEndWidget.setEnabled(False)
            self.overtimeStart.setTime(QTime(0, 0))
            self.overtimeEnd.setTime(QTime(0, 0))

    def setupWorkerAndModelsCompleter(self):
        for worker in self.workers:
            self.workersInfo.append(f"{worker[0].Име} {worker[0].Фамилия} - {worker[0].Номер}")
        Utils.setupCompleter(self.workersInfo, self.workerNameLineEdit)
        self.workerNameLineEdit.editingFinished.connect(self.updateWorkerInfo)

        for client in self.models:
            self.clientModels.append(f'{client[1].ПоръчкаNo} : {client[0].Клиент}')
        Utils.setupCompleter(self.clientModels, self.clientModelsLineEdit)


    def updateWorkerInfo(self):
        selectedText = self.workerNameLineEdit.text()
        if selectedText in self.workersInfo:
            workerId = selectedText.split(" - ")[1]
            workerName = selectedText.split(" - ")[0].split(" ")[0]
            workerLastName = selectedText.split(" - ")[0].split(" ")[1]
            self.workerNameLineEdit.setText(workerName)
            self.workerLastNameLineEdit.setText(workerLastName)
            self.workerNumberLineEdit.setText(workerId)
            workerPlace = None
            workerPosition = None
            for worker in self.workers:
                if worker[0].Номер == int(workerId):
                    workerPlace = worker[1]
                    workerPosition = worker[2]
                # print(worker[1])
                # print(worker[0].Номер)
                # print(workerId)
            # workerPlace = [worker.cehove.Група for worker in self.workers if worker.Номер == workerId]
            #     workerPlace = worker[1] if worker[0].Номер == int(workerId) else None
            #     workerPosition = worker[2] if worker[0].Номер == int(workerId)else None
            # print(workerPlace)
            if workerPlace:
                self.workerPlaceLineEdit.setText(workerPlace)
            else:
                self.workerPlaceLineEdit.setText('Не е указано')

            if workerPosition:
                self.workerPositionLineEdit.setText(workerPosition)

            else:
                self.workerPlaceLineEdit.setText('Не е указано')
