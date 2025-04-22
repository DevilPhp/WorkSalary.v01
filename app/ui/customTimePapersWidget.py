from datetime import datetime
from functools import partial

from PySide6.QtGui import QStandardItemModel, QStandardItem, QDoubleValidator

from app.ui.widgets.ui_customTimePapersWidget import *
from app.utils.utils import Utils
from app.services.workerServices import WorkerServices as WoS
from app.services.modelServices import ModelService as MoS
from app.ui.customCalendarWidget import CustomCalendarDialog
from app.models.tableModel import TableModel
from app.models.sortingModel import CaseInsensitiveProxyModel
from app.ui.messagesManager import MessageManager as MM

class CustomTimePapersWidget(QWidget, Ui_customTimePapersWidget):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.workers = WoS.getWorkers()
        self.models = MoS.getClientsAndModels()
        self.clientModels = {}
        self.modelOperations = {}
        self.workersInfo = []
        self.existingTimePapers = {}
        self.setupWorkerAndModelsCompleter()
        self.timePaperDateEdit.setDate(QDate.currentDate())
        self.setupWorkingTimeWidgets()
        self.tableTimePapersModel = QStandardItemModel()
        self.tableTimePapersHeadersNames = ['ID', 'Номер', 'ПоръчкаNo', 'ОперацияNo', 'Операция', 'Бройки', 'Време']
        for i, tableHeaderName in enumerate(self.tableTimePapersHeadersNames):
            self.tableTimePapersModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.tableTimePapersModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.tableTimePapersModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelWorkers = CaseInsensitiveProxyModel(numericColumns=[0, 1, 3, 5, 6],
                                                           parent=self)
        self.setProxyModel(self.proxyModelWorkers, self.tableTimePapersModel, self.timePapersForDayTableView)
        # self.timePapersForDayTableView.setModel(self.tableTimePapersModel)
        self.timePapersForDayTableView.horizontalHeader().setStretchLastSection(True)
        self.timePapersForDayTableView.horizontalHeader().setMinimumWidth(80)
        # self.timePapersForDayTableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.refreshTimePapersForToday()
        self.modelAndOperationHolder.setVisible(False)
        validatorInt = QDoubleValidator(0, 999999, 0)
        self.modelPiecesLineEdit.setValidator(validatorInt)

        self.isDefaultTimeCheckBox.stateChanged.connect(self.setDefaultTime)
        self.shiftStart.editingFinished.connect(self.updateDuration)
        self.shiftEnd.editingFinished.connect(self.updateDuration)
        self.overtimeStart.editingFinished.connect(self.updateDuration)
        self.overtimeEnd.editingFinished.connect(self.updateDuration)
        self.hourlyStart.editingFinished.connect(self.updateDuration)
        self.hourlyEnd.editingFinished.connect(self.updateDuration)

        self.calendarBtn.clicked.connect(self.showCustomCalendaDialog)
        self.modelPiecesLineEdit.returnPressed.connect(self.addTimePaperOperation)

    def setDefaultTime(self):
        if self.clientModelsLineEdit.text() not in self.clientModels.keys():
            self.isDefaultTimeCheckBox.setCheckState(Qt.CheckState.Checked)
            MM.showOnWidget(self, "Не е избрана поръчка", 'error')
            return
        if self.isDefaultTimeCheckBox.isChecked():
            self.timeForPieceLineEdit.setReadOnly(True)
            self.timeForPieceLineEdit.setText(str(self.modelOperations[self.modelOperationLineEdit.text()]))
        else:
            self.timeForPieceLineEdit.setReadOnly(False)
            self.timeForPieceLineEdit.setFocus()

    def refreshTimePapersForToday(self):
        self.existingTimePapers.clear()
        searchedDate = self.timePaperDateEdit.date().toString('yyyy-MM-dd')
        formatedDate = datetime.strptime(searchedDate, '%Y-%m-%d').date()
        # print(formatedDate, searchedDate)
        data = WoS.getTimePapersForDate(formatedDate)
        self.tableTimePapersModel.setRowCount(0)
        # print(data)
        for item in data:
            row = [
                QStandardItem(str(item[0])),
                QStandardItem(str(item[1])),
                QStandardItem(item[2]),
                QStandardItem(str(item[3])),
                QStandardItem(item[4]),
                QStandardItem(str(item[5])),
                QStandardItem(Utils.setFloatToStr(item[6])),
            ]
            self.tableTimePapersModel.appendRow(row)
            self.existingTimePapers[item[1]] = item[0]
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
            self.clientModels[f'{client[1].ПоръчкаNo} : {client[0].Клиент}'] = client[1].id
        Utils.setupCompleter(self.clientModels.keys(), self.clientModelsLineEdit)
        self.clientModelsLineEdit.editingFinished.connect(self.updateModelInfo)

    def updateModelInfo(self):
        selectedText = self.clientModelsLineEdit.text()

        if selectedText in self.clientModels.keys():
            self.modelOperations.clear()
            modelId = self.clientModels[selectedText]
            operations = MoS.getModelOperations(modelId)
            for operation in operations:
                self.modelOperations[f'{operation.ОперацияNo} : {operation.Операция}'] = round(operation.TimeForOper, 2)
            Utils.setupCompleter(self.modelOperations.keys(), self.modelOperationLineEdit)
            self.modelOperationLineEdit.setReadOnly(False)
            self.modelOperationLineEdit.editingFinished.connect(self.updateModelOperation)
        # else:
            # self.modelShiftsHolder.setEnabled(False)
            # self.modelNumberLineEdit.clear()
            # self.modelNameLineEdit.clear()

    def updateModelOperation(self):
        if self.modelOperationLineEdit.text() not in self.modelOperations.keys() or self.modelOperationLineEdit.text() == '':
            self.modelOperationLineEdit.setFocus()
            self.modelOperationLineEdit.selectAll()
            MM.showOnWidget(self, "Не е избрана операция", 'error')
            self.modelPiecesLineEdit.setReadOnly(True)
            self.modelPiecesLineEdit.clear()
            return

        if self.modelOperationLineEdit.text() in self.modelOperations.keys():
            self.timeForPieceLineEdit.setText(str(self.modelOperations[self.modelOperationLineEdit.text()]))
            self.modelPiecesLineEdit.setReadOnly(False)
            self.modelPiecesLineEdit.textChanged.connect(self.updateModelPieces)
            self.timeForPieceLineEdit.textChanged.connect(self.updateModelPieces)

    def updateModelPieces(self):
        if self.sender() == self.modelPiecesLineEdit:
            text = self.modelPiecesLineEdit.text()
            if ',' in text:
                text = text.strip(',')
            self.modelPiecesLineEdit.setText(text)
        if self.modelPiecesLineEdit.text() != '' and self.timeForPieceLineEdit.text() != '':
            pieces = int(self.modelPiecesLineEdit.text())
            timeForPiece = float(self.timeForPieceLineEdit.text())
            self.piecesTimeLineEdit.setText(str(round(pieces * timeForPiece, 2)))

    def addTimePaperOperation(self):
        if int(self.workerNumberLineEdit.text()) not in self.existingTimePapers.keys():
            print('New Time Paper created')

        else:
            print('Time Paper updated')
            print(self.existingTimePapers[int(self.workerNumberLineEdit.text())])


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
            self.modelAndOperationHolder.setVisible(True)
            self.workerShiftsHolder.setEnabled(True)
            if workerPlace:
                self.workerPlaceLineEdit.setText(workerPlace)
            else:
                self.workerPlaceLineEdit.setText('Не е указано')

            if workerPosition:
                self.workerPositionLineEdit.setText(workerPosition)

            else:
                self.workerPlaceLineEdit.setText('Не е указано')
        else:
            self.workerShiftsHolder.setEnabled(False)
            self.workerLastNameLineEdit.clear()
            self.workerNumberLineEdit.clear()
            self.modelAndOperationHolder.setVisible(False)
