from datetime import datetime
from functools import partial

from PySide6.QtCore import QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem, QDoubleValidator
from PySide6.QtWidgets import QMenu, QDialog

from app.ui.widgets.ui_customTimePapersWidget import *
from app.utils.utils import Utils
from app.services.workerServices import WorkerServices as WoS
from app.services.modelServices import ModelService as MoS
from app.services.operationServices import OperationsServices as OpS
from app.ui.customCalendarWidget import CustomCalendarDialog
from app.models.sortingModel import CaseInsensitiveProxyModel, FilterableHeaderView
from app.models.tableModel import CustomTableViewWithMultiSelection
from app.ui.messagesManager import MessageManager as MM
from app.ui.customSortingMenuWidget import CustomSortingMenuWidget
from app.ui.customYesNoMessage import CustomYesNowDialog


class CustomTimePapersWidget(QWidget, Ui_customTimePapersWidget):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle("Листове за време")
        self.workers = WoS.getWorkers()
        self.models = MoS.getClientsAndModels()
        self.overtimeWarning.setVisible(False)
        self.clientModels = {}
        self.modelOperations = {}
        self.workingShifts = WoS.getWorkingShifts()
        self.workersInfo = []
        self.existingTimePapers = {}
        self.checkBoxFiltering = {}
        self.initialCheckBoxes = {}
        self.operationsGroups = OpS.getOperationsGroups()
        self.operationsGroupsHolder.setEnabled(False)
        self.operationsGroupsForModel = None
        # self.setOperationsGroups()
        self.lastSelectedModel = None
        self.setupWorkerAndModelsCompleter()
        self.timePaperDateEdit.setDate(QDate.currentDate())
        self.setupWorkingTimeWidgets()
        self.timePapersForDayTableView = CustomTableViewWithMultiSelection(self)
        self.timePaperTableHolder.layout().addWidget(self.timePapersForDayTableView)
        self.tableTimePapersModel = QStandardItemModel()
        self.tableTimePapersHeadersNames = ['ID', 'Номер', 'ПоръчкаNo', 'ОперацияNo', 'Операция', 'Бройки', 'Време']
        for i, tableHeaderName in enumerate(self.tableTimePapersHeadersNames):
            self.tableTimePapersModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.tableTimePapersModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.tableTimePapersModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelWorkers = CaseInsensitiveProxyModel(numericColumns=[0, 1, 3, 5, 6],
                                                           parent=self)
        self.setProxyModel(self.proxyModelWorkers, self.tableTimePapersModel, self.timePapersForDayTableView)
        self.timePapersForDayTableView.horizontalHeader().setStretchLastSection(True)
        self.timePapersForDayTableView.horizontalHeader().setMinimumWidth(80)
        self.totalWorkingMinsHolder.setVisible(False)
        self.refreshTimePapersForToday()
        self.timePapersForDayTableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.timePapersForDayTableView.customContextMenuRequested.connect(self.showCustomContextMenu)
        self.timePapersForDayTableView.selectedRows.connect(self.showTimePaperDetails)
        self.timePapersForDayTableView.clearCurrentSelection.connect(self.resetSelectedInfo)
        self.workerShiftsHolder.setEnabled(False)
        self.modelAndOperationHolder.setVisible(False)
        validatorInt = QDoubleValidator(0, 999999, 0)
        self.modelPiecesLineEdit.setValidator(validatorInt)

        self.operationsGroupComboBox.setEnabled(False)
        self.operationsGroupsBtn.setEnabled(False)
        self.operationsGroupsCheckBox.stateChanged.connect(self.showOperationsGroups)
        self.operationsGroupComboBox.currentIndexChanged.connect(self.setOperationsGroupForDB)
        self.operationsGroupsBtn.clicked.connect(self.openOperationsGroupsWindow)
        self.refreshOpersGroupBtn.clicked.connect(self.refreshOpersGroup)

        self.isDefaultTimeCheckBox.stateChanged.connect(self.setDefaultTime)
        self.shiftStart.timeChanged.connect(self.updateDuration)
        self.shiftEnd.timeChanged.connect(self.updateDuration)
        self.shiftStart.editingFinished.connect(self.checkForExistingShift)
        self.shiftEnd.editingFinished.connect(self.checkForExistingShift)
        self.overtimeStart.timeChanged.connect(self.updateDuration)
        self.overtimeEnd.timeChanged.connect(self.updateDuration)
        self.hourlyStart.timeChanged.connect(self.updateDuration)
        self.hourlyEnd.timeChanged.connect(self.updateDuration)
        # self.hourlyStart.editingFinished.connect(self.checkIfTimeIsValid)
        # self.hourlyEnd.editingFinished.connect(self.checkIfTimeIsValid)
        # self.overtimeStart.editingFinished.connect(self.checkIfTimeIsValid)
        # self.overtimeEnd.editingFinished.connect(self.checkIfTimeIsValid)

        self.calendarBtn.clicked.connect(self.showCustomCalendaDialog)
        self.modelPiecesLineEdit.returnPressed.connect(self.addTimePaperOperation)
        self.addNewTimePaperBtn.clicked.connect(self.addTimePaperOperation)
        self.addNewShiftBtn.clicked.connect(self.setShiftsWindow)
        self.refreshShiftsBtn.clicked.connect(self.refreshShifts)

        self.clearWorkerNameBtn.setVisible(False)
        self.workerNameLineEdit.textChanged.connect(self.showClearWorkerNameBtn)
        self.clearWorkerNameBtn.clicked.connect(self.clearWorkerName)
        self.showAllCheckBox.stateChanged.connect(self.showAllWorkersForDate)

        self.workerNameLineEdit.returnPressed.connect(self.updateWorkerInfo)
        self.clientModelsLineEdit.returnPressed.connect(self.updateModelInfo)

        # self.workerNameLineEdit.editingFinished.connect(self.checkWorker)
        # self.clientModelsLineEdit.editingFinished.connect(self.checkModel)

        # completer = self.clientModelsLineEdit.completer()
        # self.clientModelsLineEdit.setText(Utils.setReturnBtnForCompleter(completer))
        # self.clientModelsLineEdit.setText('')

        self.modelPiecesLineEdit.textChanged.connect(self.updateModelPieces)
        self.timeForPieceLineEdit.textChanged.connect(self.updateModelPieces)
        self.modelOperationLineEdit.editingFinished.connect(self.updateModelOperation)
        # print('here')

    def showAllWorkersForDate(self):
        if self.showAllCheckBox.checkState() == Qt.CheckState.Checked:
            self.refreshTimePapersForToday(showAll=True)
        else:
            if self.workerNameLineEdit.text() != '':
                self.refreshTimePapersForToday(workerId=int(self.workerNumberLineEdit.text()))
            else:
                self.refreshTimePapersForToday()

    def clearWorkerName(self):
        self.workerNameLineEdit.clear()
        self.clearWorker()
        self.clearOperationInfo()
        self.modelAndOperationHolder.setVisible(False)
        self.refreshTimePapersForToday()
        self.workerNameLineEdit.setFocus()

    def showClearWorkerNameBtn(self, text):
        if text != '':
            self.clearWorkerNameBtn.setVisible(True)
        else:
            self.clearWorkerNameBtn.setVisible(False)

    def showCustomContextMenu(self, pos):
        menu = QMenu(self)
        deleteAction = menu.addAction("Изтрий")
        action = menu.exec_(self.timePapersForDayTableView.viewport().mapToGlobal(pos))

        if action == deleteAction:
            selectedIds = []
            selectedOperations = []
            selectedRow = self.timePapersForDayTableView.selectionModel().selectedRows(0)
            selectedOper = self.timePapersForDayTableView.selectionModel().selectedRows(4)
            selectedOvertimesAndHorlis = self.timePapersForDayTableView.selectionModel().selectedRows(2)
            for selectedRow in selectedRow:
                if self.tableTimePapersModel.item(selectedRow.row(), 2).text() == 'Почасова работа':
                    key = f'{selectedRow.data(Qt.ItemDataRole.UserRole)}_hourlyPay'
                elif self.tableTimePapersModel.item(selectedRow.row(), 2).text() == 'Извънредна работа':
                    key = f'{selectedRow.data(Qt.ItemDataRole.UserRole)}_overtimePay'
                else:
                    key = f'{selectedRow.data(Qt.ItemDataRole.UserRole)}_operation'
                selectedIds.append(key)
            for selectedOperation in selectedOper:
                selectedOperations.append(selectedOperation.data(Qt.ItemDataRole.DisplayRole))
            for selectedOvertimeAndHorly in selectedOvertimesAndHorlis:
                if (selectedOvertimeAndHorly.data(Qt.ItemDataRole.DisplayRole) == 'Почасова работа' or
                        selectedOvertimeAndHorly.data(Qt.ItemDataRole.DisplayRole) == 'Извънредна работа'):
                    selectedOperations.append(selectedOvertimeAndHorly.data(Qt.ItemDataRole.DisplayRole))
            dialog = CustomYesNowDialog()
            message = 'Изтриване на:\n\n' + '\n'.join(selectedOperations)
            dialog.setMessage(name='', message=message, mode='deleting')
            result = dialog.exec()
            if result == QDialog.Accepted:
                if WoS.deleteTimePapers(selectedIds):
                    self.refreshTimePapersForToday(int(self.workerNumberLineEdit.text()))
                    self.clearOperationInfo(False)
                    MM.showOnWidget(self, 'Успешно изтрити записи', 'success')
                else:
                    MM.showOnWidget(self, 'Грешка при изтриване', 'error')
            else:
                return

    def refreshOpersGroup(self):
        self.operationsGroups = OpS.getOperationsGroups()
        self.setOperationsGroups()

    def openOperationsGroupsWindow(self):
        self.mainWindow.setModelOperPage(True)

    def setOperationsGroupForDB(self):
        self.clearOperationInfo(False)
        if self.operationsGroupComboBox.currentIndex() > -1 and self.operationsGroupsCheckBox.isChecked():
            self.modelPiecesLineEdit.setReadOnly(False)
            self.modelOperationLineEdit.blockSignals(True)
            self.modelOperationLineEdit.setReadOnly(True)
            self.modelOperationLineEdit.setText('Група операции')
            self.modelOperationLineEdit.blockSignals(False)
            self.modelPiecesLineEdit.setFocus()
            return
        else:
            self.modelPiecesLineEdit.setReadOnly(True)
            self.modelOperationLineEdit.blockSignals(True)
            self.modelOperationLineEdit.setReadOnly(False)
            self.modelOperationLineEdit.clear()
            self.modelOperationLineEdit.blockSignals(False)
            self.modelPiecesLineEdit.clear()
            return

    def setOperationsGroups(self, modelId=None):
        self.operationsGroupComboBox.clear()
        print(self.operationsGroups)
        if len(self.operationsGroups) > 0:
            for group, value in self.operationsGroups.items():
                name = f'{value["id"]}: {group}'
                self.operationsGroupComboBox.addItem(name)
                self.operationsGroupComboBox.setCurrentIndex(-1)
        if modelId:
            self.operationsGroupsForModel = OpS.getGroupOperationsForModel(modelId)
            # print(operationsGroupsForModel)
            self.operationsGroupComboBox.insertSeparator(self.operationsGroupComboBox.count())
            for group, value in self.operationsGroupsForModel.items():
                name = f'{value["id"]}: {group}'
                self.operationsGroupComboBox.addItem(name)
                self.operationsGroupComboBox.setCurrentIndex(-1)

    def showOperationsGroups(self):
        self.operationsGroupComboBox.setEnabled(self.operationsGroupsCheckBox.isChecked())
        self.operationsGroupsBtn.setEnabled(self.operationsGroupsCheckBox.isChecked())

        if not self.operationsGroupsCheckBox.isChecked():
            self.operationsGroupComboBox.setCurrentIndex(-1)
            self.clearOperationInfo(False)

    def checkForExistingShift(self):
        for key, value in self.workingShifts.items():
            if value[1] == self.shiftStart.time() and value[2] == self.shiftEnd.time():
                self.shiftNameLineEdit.setCurrentText(key)
                break
            else:
                self.shiftNameLineEdit.setCurrentIndex(-1)

    def setShiftsWindow(self):
        data = [
            self.shiftNameLineEdit.currentText(),
            self.shiftStart.time(),
            self.shiftEnd.time()
        ]
        self.mainWindow.setWorkingShiftsPage(data)

    def showTimePaperDetails(self, selectedRows):
        numberSelectedRows = len(selectedRows['pieces'])
        totalSelectedPieces = 0
        totalSelectedTime = 0
        # pass
        for key, row in selectedRows.items():
            if key == 'pieces':
                for item in row:
                    totalSelectedPieces += int(item.data())
            else:
                for item in row:
                    totalSelectedTime += float(item.data())
        avrTimePerPiece = round(totalSelectedTime / totalSelectedPieces, 2) if totalSelectedPieces > 0 else 0
        self.avrTimePerPiece.setText(str(avrTimePerPiece))
        self.totalSelectedRows.setText(str(numberSelectedRows))
        self.totalSelectedPieces.setText(str(totalSelectedPieces))
        self.totalSelectedTime.setText(str(round(totalSelectedTime, 2)))

    def resetSelectedInfo(self):
        self.totalSelectedRows.setText("0")
        self.totalSelectedPieces.setText("0")
        self.totalSelectedTime.setText("0.0")
        self.avrTimePerPiece.setText("0.0")

    def setDefaultTime(self):
        if self.modelOperationLineEdit.text() == '':
            self.isDefaultTimeCheckBox.setCheckState(Qt.CheckState.Checked)
            MM.showOnWidget(self, "Не е избрана операция", 'error')
            return
        elif self.modelOperationLineEdit.text() == 'Група операции':
            self.isDefaultTimeCheckBox.setCheckState(Qt.CheckState.Checked)
            MM.showOnWidget(self, "Не можете да промените време за група операции", 'warning')
            return

        if self.isDefaultTimeCheckBox.isChecked():
            self.timeForPieceLineEdit.setReadOnly(True)
            self.timeForPieceLineEdit.setText(str(self.modelOperations[self.modelOperationLineEdit.text()][0]))
        else:
            self.timeForPieceLineEdit.setReadOnly(False)
            self.timeForPieceLineEdit.setFocus()
            self.timeForPieceLineEdit.selectAll()

    def refreshTimePapersForToday(self, workerId=None, showAll=False):
        totalWorkingMins = 0
        totalProdPieces = 0
        self.existingTimePapers.clear()
        self.initialCheckBoxes.clear()
        searchedDate = self.timePaperDateEdit.date().toString('yyyy-MM-dd')
        formatedDate = datetime.strptime(searchedDate, '%Y-%m-%d').date()
        data = WoS.getTimePapersForDate(formatedDate, workerId, showAll)
        self.tableTimePapersModel.setRowCount(0)
        self.totalViewRows.setText(str(len(data)))
        self.resetSelectedInfo()
        for item in data:
            timePaperId = QStandardItem(str(item[0]))
            timePaperId.setData(item[7], Qt.ItemDataRole.UserRole)
            if not workerId and item[3] == 49:
                totalProdPieces += item[5]
            elif workerId:
                totalWorkingMins += item[6]

            if item[7] == -1:
                totalWorkingMins += item[8]
                item[6] = item[8]
                timePaperId.setData(item[9], Qt.ItemDataRole.UserRole)

            row = [
                timePaperId,
                QStandardItem(str(item[1])),
                QStandardItem(item[2]),
                QStandardItem(str(item[3])),
                QStandardItem(item[4]),
                QStandardItem(str(item[5])),
                QStandardItem(Utils.setFloatToStr(item[6])),
            ]
            self.tableTimePapersModel.appendRow(row)
            self.existingTimePapers[item[1]] = item[0]
        if workerId:
            self.totalProdPiecesHolder.setVisible(False)
            self.totalWorkingMinsHolder.setVisible(True)
            self.totalWorkingMins.setText(str(round(totalWorkingMins, 2)))
        else:
            self.totalProdPiecesHolder.setVisible(True)
            self.totalWorkingMinsHolder.setVisible(False)
            self.totalProdPieces.setText(str(totalProdPieces))

        self.checkForExistingShiftInTimePaper(workerId)

        self.setTotalMinsColor()

    def checkForExistingShiftInTimePaper(self, workerId):
        if workerId:
            if self.existingTimePapers:
                timePaperId = self.existingTimePapers[int(workerId)]
                shift = WoS.getExistingTimePaperShift(timePaperId)
                if shift:
                    self.shiftNameLineEdit.setCurrentText(shift[0])
                    self.shiftStart.setTime(QTime(shift[1].hour, shift[1].minute))
                    self.shiftEnd.setTime(QTime(shift[2].hour, shift[2].minute))
                    self.addNewShiftBtn.setEnabled(False)
                    self.refreshShiftsBtn.setEnabled(False)
                    self.shiftNameLineEdit.setEnabled(False)
                    self.shiftStart.setEnabled(False)
                    self.shiftEnd.setEnabled(False)
            else:
                self.shiftNameLineEdit.setCurrentIndex(0)
                self.shiftStart.setTime(QTime(8, 0))
                self.shiftEnd.setTime(QTime(17, 0))
                self.addNewShiftBtn.setEnabled(True)
                self.refreshShiftsBtn.setEnabled(True)
                self.shiftNameLineEdit.setEnabled(True)
                self.shiftStart.setEnabled(True)
                self.shiftEnd.setEnabled(True)

    def setTotalMinsColor(self):
        totalWorkingMins = float(self.totalWorkingMins.text())
        shiftWorkingTime = int(self.shiftTotalMins.text()) + int(self.overtimeTotalMins.text())
        if totalWorkingMins > shiftWorkingTime:
            self.totalWorkingMins.setStyleSheet("color: #c75f59;")
            self.overtimeWarning.setVisible(True)
        else:
            self.totalWorkingMins.setStyleSheet("color: #324b4c;")
            self.overtimeWarning.setVisible(False)

    def setProxyModel(self, proxyModel, model, table):
        proxyModel.setSourceModel(model)
        filterableHeaderView = FilterableHeaderView(Qt.Orientation.Horizontal, table)
        table.setHorizontalHeader(filterableHeaderView)
        filterableHeaderView.filterRequested.connect(partial(self.updateFilter, proxyModel, filterableHeaderView))
        table.setModel(proxyModel)
        table.setSortingEnabled(True)

    def updateFilter(self, proxyModel, header, column):
        if column < 5:
            # Create dictionaries to store column values and checked states if they don't exist
            if not hasattr(self, 'columnValues'):
                self.columnValues = {}
            if not hasattr(self, 'checkedStates'):
                self.checkedStates = {}
            if column not in self.checkBoxFiltering:
                self.checkBoxFiltering[column] = []

            items = []
            self.columnValues[column] = []

            for row in range(proxyModel.rowCount()):
                index = proxyModel.index(row, column)
                value = proxyModel.data(index, Qt.ItemDataRole.DisplayRole)
                if value not in self.columnValues[column]:
                    self.columnValues[column].append(value)
                    if value not in self.initialCheckBoxes:
                        self.initialCheckBoxes[value] = column

            for value in self.columnValues[column]:
                items.append(value)

            if items:
                menu = CustomSortingMenuWidget(header)
                for item in items:
                    checked = item in self.checkBoxFiltering[column]
                    menu.addItem(item, checked)
                menu.setMenuSize(len(items))
                menu.move(self.cursor().pos())
                menu.checkedCheckbox.connect(partial(self.applyFilter, proxyModel))

    def applyFilter(self, proxyModel, item):
        col = self.initialCheckBoxes[item.text()]
        if item.isChecked() and item.text() not in self.checkBoxFiltering[col]:
            self.checkBoxFiltering[col].append(item.text())
        elif not item.isChecked() and item.text() in self.checkBoxFiltering[col]:
            self.checkBoxFiltering[col].remove(item.text())

        if not self.checkBoxFiltering[col]:
            if col in proxyModel.columnFilters:
                del proxyModel.columnFilters[col]
        else:
            proxyModel.setFilterForColumn(col, self.checkBoxFiltering)
        proxyModel.invalidateFilter()
        self.totalViewRows.setText(str(proxyModel.rowCount()))

    def showCustomCalendaDialog(self):
        calendarDialog = CustomCalendarDialog()
        calendarDialog.calendarCustomWidget.setSelectedDate(self.timePaperDateEdit.date())
        Utils.calculatingIdealDialogShowPos(self, calendarDialog)
        calendarDialog.dateSelected.connect(self.updateDateLabel)
        calendarDialog.exec_()

    def updateDateLabel(self, formattedDate):
        self.timePaperDateEdit.setDate(formattedDate)
        if self.workerNumberLineEdit.text() != '':
            self.refreshTimePapersForToday(int(self.workerNumberLineEdit.text()))
        else:
            self.refreshTimePapersForToday()
        self.clearOperationInfo()

    def updateDuration(self):
        if self.sender() == self.shiftStart or self.sender() == self.shiftEnd:
            duration = Utils.calculateMinutes(self.shiftStart, self.shiftEnd)
            if duration < 0:
                self.shiftStart.setTime(self.shiftEnd.time().addSecs(-1800))
                duration = Utils.calculateMinutes(self.shiftStart, self.shiftEnd)
            self.shiftTotalMins.setText(str(duration))
            self.setTotalMinsColor()

        if self.sender() == self.hourlyStart or self.sender() == self.hourlyEnd:
            duration = Utils.calculateMinutes(self.hourlyStart, self.hourlyEnd)
            if duration < 0:
                self.hourlyStart.setTime(self.hourlyEnd.time().addSecs(-1800))
                duration = Utils.calculateMinutes(self.hourlyStart, self.hourlyEnd)
            self.hourlyTotalMins.setText(str(duration))

        if self.sender() == self.overtimeStart or self.sender() == self.overtimeEnd:
            duration = Utils.calculateMinutes(self.overtimeStart, self.overtimeEnd)
            if duration < 0:
                self.overtimeStart.setTime(self.overtimeEnd.time().addSecs(-1800))
                duration = Utils.calculateMinutes(self.overtimeStart, self.overtimeEnd)
            self.overtimeTotalMins.setText(str(duration))
            self.setTotalMinsColor()

    def checkIfTimeIsValid(self):
        if self.isHourlyWorking.isChecked():
            # Get all times as QTime objects
            shiftStart = self.shiftStart.time()
            shiftEnd = self.shiftEnd.time()
            hourlyStart = self.hourlyStart.time()
            hourlyEnd = self.hourlyEnd.time()

            # Check if shift crosses midnight
            isOvernightShift = shiftEnd <= shiftStart

            if isOvernightShift:
                # For overnight shifts (e.g., 22:30-5:30)
                # Hourly time is valid if:
                # 1. It's between shift start and midnight, OR
                # 2. It's between midnight and shift end
                isStartValid = hourlyStart >= shiftStart or hourlyStart <= shiftEnd
                isEndValid = hourlyEnd >= shiftStart or hourlyEnd <= shiftEnd

                # Check if hourly shift is contained within the working shift
                if not (isStartValid and isEndValid):
                    self.hourlyStart.setTime(shiftStart)
                    self.hourlyEnd.setTime(shiftEnd)
                    MM.showOnWidget(self, 'Почасовото време не е валидно за работна смяна!', 'warning')
                    return False

                # Check if hourly shift itself is valid (doesn't cross midnight in wrong direction)
                if hourlyEnd <= hourlyStart and not (hourlyStart >= shiftStart and hourlyEnd <= shiftEnd):
                    self.hourlyStart.setTime(shiftStart)
                    self.hourlyEnd.setTime(shiftEnd)
                    MM.showOnWidget(self, 'Почасовото време не е валидно - начало и край са разменени!', 'warning')
                    return False

                return True
            else:
                # For regular shifts (e.g., 8:00-17:00)
                # Both hourly start and end must be within shift times
                if not (shiftStart <= hourlyStart <= shiftEnd and shiftStart <= hourlyEnd <= shiftEnd):
                    self.hourlyStart.setTime(shiftStart)
                    self.hourlyEnd.setTime(shiftEnd)
                    MM.showOnWidget(self, 'Почасовото време не е валидно за работна смяна!', 'warning')
                    return False

                # Check if hourly start is before hourly end
                if hourlyEnd < hourlyStart:
                    self.hourlyStart.setTime(shiftStart)
                    self.hourlyEnd.setTime(shiftEnd)
                    MM.showOnWidget(self, 'Почасовото време не е валидно - начало и край са разменени!', 'warning')
                    return False

                return True

        elif self.isOvertimeWorking.isChecked():
            # Get all times as QTime objects
            shiftStart = self.shiftStart.time()
            shiftEnd = self.shiftEnd.time()
            overtimeStart = self.overtimeStart.time()
            overtimeEnd = self.overtimeEnd.time()

            # Check if shift crosses midnight
            isOvernightShift = overtimeEnd <= overtimeStart
            print(isOvernightShift)

            if isOvernightShift:
                print('here')

                # For overnight shifts (where overtime crosses midnight)

                # Create a helper function to check if a time is within the shift
                def is_time_in_shift(time_to_check):
                    if shiftEnd <= shiftStart:  # If shift also crosses midnight
                        return time_to_check >= shiftStart or time_to_check <= shiftEnd
                    else:  # Regular shift
                        return shiftStart <= time_to_check <= shiftEnd

                # Check if overtime start or end overlaps with shift
                if is_time_in_shift(overtimeStart) or is_time_in_shift(overtimeEnd):
                    MM.showOnWidget(self, 'Извънредно време не е валидно за работна смяна!', 'warning')
                    return False

                return True
            else:
                # For regular shifts, overtime must be outside the shift hours
                # Either before shift start or after shift end
                if (shiftStart <= overtimeStart <= shiftEnd) or (shiftStart <= overtimeEnd <= shiftEnd):
                    MM.showOnWidget(self, 'Извънредно време не е валидно за работна смяна!', 'warning')
                    return False

            # Check if overtime shift itself is valid
            if overtimeEnd < overtimeStart and not isOvernightShift:
                MM.showOnWidget(self, 'Извънредно време не е валидно - начало и край са разменени!', 'warning')
                return False

            return True

        return True  # If neither hourly nor overtime is checked, validation passes

    def setupWorkingTimeWidgets(self):
        self.hourlyEndWidget.setEnabled(False)
        self.hourlyStartWidget.setEnabled(False)
        self.overtimeEndWidget.setEnabled(False)
        self.overtimeStartWidget.setEnabled(False)
        self.isHourlyWorking.stateChanged.connect(self.toggleHourlyWorking)
        self.isOvertimeWorking.stateChanged.connect(self.toggleOvertimeWorking)
        for shift in self.workingShifts.keys():
            self.shiftNameLineEdit.addItem(shift)
        self.shiftNameLineEdit.setCurrentIndex(0)
        Utils.setupCompleter(self.workingShifts.keys(), self.shiftNameLineEdit)
        self.shiftNameLineEdit.currentIndexChanged.connect(self.updateShiftInfo)

    def updateShiftInfo(self):
        shiftName = self.shiftNameLineEdit.currentText()
        if shiftName in self.workingShifts:
            shift = self.workingShifts[shiftName]
            self.shiftStart.setTime(shift[1])
            self.shiftEnd.setTime(shift[2])

    def refreshShifts(self):
        self.workingShifts = WoS.getWorkingShifts()
        self.shiftNameLineEdit.clear()
        for shift in self.workingShifts.keys():
            self.shiftNameLineEdit.addItem(shift)
        Utils.setupCompleter(self.workingShifts.keys(), self.shiftNameLineEdit)
        self.shiftNameLineEdit.setCurrentIndex(0)

    def toggleHourlyWorking(self):
        if self.isHourlyWorking.isChecked():
            self.hourlyStartWidget.setEnabled(True)
            self.hourlyEndWidget.setEnabled(True)
            self.hourlyStart.setTime(self.shiftStart.time())
            self.hourlyEnd.setTime(self.shiftEnd.time())
            if self.isOvertimeWorking.isChecked():
                self.isOvertimeWorking.setChecked(False)
        else:
            self.hourlyStartWidget.setEnabled(False)
            self.hourlyEndWidget.setEnabled(False)
            self.hourlyStart.setTime(QTime(0, 0))
            self.hourlyEnd.setTime(QTime(0, 0))

    def toggleOvertimeWorking(self):
        if self.isOvertimeWorking.isChecked():
            self.overtimeStartWidget.setEnabled(True)
            self.overtimeEndWidget.setEnabled(True)
            if self.isHourlyWorking.isChecked():
                self.isHourlyWorking.setChecked(False)
        else:
            self.overtimeStartWidget.setEnabled(False)
            self.overtimeEndWidget.setEnabled(False)
            self.overtimeStart.setTime(QTime(0, 0))
            self.overtimeEnd.setTime(QTime(0, 0))

    def setupWorkerAndModelsCompleter(self):
        for worker in self.workers:
            self.workersInfo.append(f"{worker[0].Име} {worker[0].Фамилия} - {worker[0].Номер}")
        Utils.setupCompleter(self.workersInfo, self.workerNameLineEdit)

        for client in self.models:
            self.clientModels[f'{client[1].ПоръчкаNo} : {client[0].Клиент}'] = client[1].id
        Utils.setupCompleter(self.clientModels.keys(), self.clientModelsLineEdit)

    def checkModel(self):
        if not self.clientModelsLineEdit.text() in self.clientModels.keys():
            self.clientModelsLineEdit.clear()
            self.clientModelsLineEdit.setFocus()
            MM.showOnWidget(self, "Избран е несъществуващ модел", 'error')
            return

    def updateModelInfo(self):
        if self.clientModelsLineEdit.text() != '':
            completer = self.clientModelsLineEdit.completer()
            self.clientModelsLineEdit.setText(Utils.setReturnBtnForCompleter(completer))
        selectedText = self.clientModelsLineEdit.text()

        if selectedText in self.clientModels.keys():
            modelId = self.clientModels[selectedText]
            self.setOperationsGroups(modelId)
            # print(self.operationsGroupComboBox)
            if self.operationsGroupComboBox.count() > 1:
                self.operationsGroupsHolder.setEnabled(True)
            self.modelOperations.clear()
            modelData = MoS.getModelOperations(modelId)
            self.modelTotalPiecesLineEdit.setText(str(modelData[1]) if modelData[1] else '0')
            operations = modelData[0]
            for operation in operations:
                self.modelOperations[f'{operation.ОперацияNo} : {operation.Операция}'] = [
                    round(operation.TimeForOper, 2), operation.id, operation.ProducedPieces
                ]
            Utils.setupCompleter(self.modelOperations.keys(), self.modelOperationLineEdit)
            self.modelOperationLineEdit.setReadOnly(False)
            self.modelOperationLineEdit.setFocus()
        else:
            self.clientModelsLineEdit.clear()
            self.clientModelsLineEdit.setFocus()
            self.operationsGroupsHolder.setEnabled(False)
            self.modelTotalPiecesLineEdit.clear()

    def updateModelOperation(self):
        if self.modelOperationLineEdit.text() != '':
            completer = self.modelOperationLineEdit.completer()
            self.modelOperationLineEdit.setText(Utils.setReturnBtnForCompleter(completer))
        selectedText = self.modelOperationLineEdit.text()

        if selectedText not in self.modelOperations.keys() or selectedText == '':
            self.modelOperationLineEdit.setFocus()
            self.modelOperationLineEdit.selectAll()
            MM.showOnWidget(self, "Не е избрана операция", 'error')
            self.modelPiecesLineEdit.setReadOnly(True)
            self.modelPiecesLineEdit.clear()
            return

        if selectedText in self.modelOperations.keys():

            self.piecesForProdLineEdit.setText(str(
                int(self.modelTotalPiecesLineEdit.text()) - self.modelOperations[selectedText][2]
            ))
            if int(self.piecesForProdLineEdit.text()) < 0:
                self.piecesForProdLineEdit.setStyleSheet('color: #c75f59;')
            else:
                self.piecesForProdLineEdit.setStyleSheet('color: #324b4c;')
            self.piecesProducedLineEdit.setText(str(self.modelOperations[selectedText][2]))
            self.timeForPieceLineEdit.setText(str(self.modelOperations[selectedText][0]))
            self.modelPiecesLineEdit.setReadOnly(False)
            self.modelPiecesLineEdit.setFocus()

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
        if self.clientModelsLineEdit.text() == '' or self.modelOperationLineEdit.text() == '':
            if not self.isHourlyWorking.isChecked() and not self.isOvertimeWorking.isChecked():
                MM.showOnWidget(self,
                                'Не сте избрали клиент и/или операция',
                                'error')
                return
            else:
                if not self.checkIfTimeIsValid():
                    return
        count = 1
        operationsGroupForAdd = {}
        timePaper = None
        if (self.modelOperationLineEdit.text() == 'Група операции' and
                self.operationsGroupsCheckBox.isChecked() and
                self.operationsGroupComboBox.currentIndex() > -1):
            try:
                operations = self.operationsGroups[
                    self.operationsGroupComboBox.currentText().split(': ')[1]
                ]['operations']
            except KeyError:
                operations = self.operationsGroupsForModel[
                    self.operationsGroupComboBox.currentText().split(': ')[1]
                ]['operations']
            for operation in operations:
                for key in self.modelOperations.keys():
                    if operation == int(key.split(': ')[0]):
                        operationsGroupForAdd[self.modelOperations[key][1]] = self.modelOperations[key][0]
                        break
            count = len(operationsGroupForAdd.keys())

        if count < 1:
            MM.showOnWidget(self,
                            f"Избраните операции не съществуват за {self.clientModelsLineEdit.text()}",
                            'error')
            return

        for i in range(count):
            if operationsGroupForAdd:
                modelOperationId = list(operationsGroupForAdd.keys())[i]
                modelOperationTime = round(
                    operationsGroupForAdd[modelOperationId] * int(self.modelPiecesLineEdit.text()), 2
                )
                orderId = self.clientModels[self.clientModelsLineEdit.text()]
            elif ((self.modelOperationLineEdit.text() == '' or
                  self.clientModelsLineEdit.text() == '') and
                  self.isHourlyWorking.isChecked()):
                modelOperationId = None
                modelOperationTime = 0
                orderId = None
            elif ((self.modelOperationLineEdit.text() == '' or
                  self.clientModelsLineEdit.text() == '') and
                  self.isOvertimeWorking.isChecked()):
                modelOperationId = None
                modelOperationTime = 0
                orderId = None
            else:
                modelOperationId = self.modelOperations[self.modelOperationLineEdit.text()][1]
                modelOperationTime = float(self.piecesTimeLineEdit.text())
                orderId = self.clientModels[self.clientModelsLineEdit.text()]

            overtime = [Utils.convertQtimeToTime(self.overtimeStart.time()),
                        Utils.convertQtimeToTime(self.overtimeEnd.time()),
                        float(self.overtimeTotalMins.text())] if self.isOvertimeWorking.isChecked() else None

            hourlyPay = [Utils.convertQtimeToTime(self.hourlyStart.time()),
                         Utils.convertQtimeToTime(self.hourlyEnd.time()),
                         float(self.hourlyTotalMins.text())] if self.isHourlyWorking.isChecked() else None
            nightMins = 0
            if overtime:
                nightMins += Utils.checkNightShiftMins(self.overtimeStart.time(), self.overtimeEnd.time())
            elif hourlyPay:
                nightMins += Utils.checkNightShiftMins(self.hourlyStart.time(), self.hourlyEnd.time())
            else:
                nightMins += Utils.checkNightShiftMins(self.shiftStart.time(), self.shiftEnd.time())

            currentShiftNightMins = Utils.checkNightShiftMins(self.shiftStart.time(), self.shiftEnd.time())

            # if nightMins > 240:
            #     nightMins -= 60

            print(f'nightMins: {nightMins}')
            print(f'currentShiftNightMins: {currentShiftNightMins}')

            if int(self.workerNumberLineEdit.text()) not in self.existingTimePapers.keys():
                date = datetime.strptime(self.timePaperDateEdit.date().toString('yyyy-MM-dd'), '%Y-%m-%d').date()
                timePaperData = {
                    'Date': date,
                    'WeekDay': date.isoweekday(),
                    'ShiftId': self.workingShifts[self.shiftNameLineEdit.currentText()][0],
                    'IsHourlyPaid': hourlyPay,
                    'IsOvertime': overtime,
                    'WorkerId': int(self.workerNumberLineEdit.text()),
                    'user': self.usernameLabel.text(),
                    'OrderId': orderId,
                    'ModelOperationId': modelOperationId,
                    'Pieces': int(self.modelPiecesLineEdit.text()) if modelOperationId else 0,
                    'WorkingTimeMinutes': modelOperationTime,
                    'nightMins': nightMins,
                    'currentShiftNightMins': currentShiftNightMins,
                }
                timePaper = WoS.addNewTimePaperAndOperation(timePaperData)
                if operationsGroupForAdd:
                    self.existingTimePapers[int(self.workerNumberLineEdit.text())] = timePaper
                # print(self.existingTimePapers)
            else:
                # print(self.existingTimePapers[int(self.workerNumberLineEdit.text())])
                timePaperData = {
                    'TimePaperId': self.existingTimePapers[int(self.workerNumberLineEdit.text())],
                    'OrderId': orderId,
                    'ModelOperationId': modelOperationId,
                    'Pieces': int(self.modelPiecesLineEdit.text()) if modelOperationId else 0,
                    'IsHourlyPaid': hourlyPay,
                    'IsOvertime': overtime,
                    'WorkingTimeMinutes': modelOperationTime,
                    'user': self.usernameLabel.text(),
                    'nightMins': nightMins,
                    'currentShiftNightMins': currentShiftNightMins,
                }
                # print(f'TimePaperData: {timePaperData}')
                # return
                timePaper = WoS.updateTimePaperAndOperation(timePaperData)

        if timePaper:
            if operationsGroupForAdd:
                message = f'Успешно добавен лист за време за група операций {self.operationsGroupComboBox.currentText()}'
            else:
                message = 'Успешно добавен лист за време'
            MM.showOnWidget(self, message, 'success')
            self.refreshTimePapersForToday(int(self.workerNumberLineEdit.text()))
            self.clearOperationInfo(False)
            self.operationsGroupsCheckBox.setCheckState(Qt.CheckState.Unchecked)

    def checkIsHourlyWorking(self):
        if self.isHourlyWorking.isChecked():
            if self.hourlyStart.time() == self.shiftStart.time() and self.hourlyEnd.time() == self.shiftEnd.time():
                print('FullHourlyWork')
                return 'FullHourlyWork'
            else:
                print('HourlyWork')
                return 'HourlyWork'
        else:
            return None

    def checkWorker(self):
        if not self.workerNameLineEdit.text() in self.workersInfo:
            self.workerNameLineEdit.clear()
            self.workerNameLineEdit.setFocus()
            MM.showOnWidget(self, "Избран е несъществуващ работник", 'error')
            return

    def updateWorkerInfo(self):
        self.clearOperationInfo(False)
        if self.workerNameLineEdit.text() != '':
            completer = self.workerNameLineEdit.completer()
            self.workerNameLineEdit.setText(Utils.setReturnBtnForCompleter(completer))
        selectedText = self.workerNameLineEdit.text()
        if selectedText in self.workersInfo:
            workerId = selectedText.split(" - ")[1]
            workerName = selectedText.split(" - ")[0].split(" ")[0]
            workerLastName = selectedText.split(" - ")[0].split(" ")[1]
            self.workerNameLineEdit.setText(workerName)
            self.workerLastNameLineEdit.setText(workerLastName)
            self.workerNumberLineEdit.setText(workerId)

            # self.checkForWorkerTimePaper(int(workerId))

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
                self.workerPositionLineEdit.setText('Не е указано')
            self.clientModelsLineEdit.setFocus()
            self.clientModelsLineEdit.selectAll()
            self.showAllCheckBox.blockSignals(True)
            self.showAllCheckBox.setCheckState(Qt.CheckState.Unchecked)
            self.showAllCheckBox.blockSignals(False)
            self.refreshTimePapersForToday(int(workerId))
        else:
            self.workerNameLineEdit.clear()
            self.workerNameLineEdit.setFocus()
            self.clearWorker()

        # if self.existingTimePapers:
        #     timePaperId = self.existingTimePapers[int(workerId)]
        #     shift = WoS.getExistingTimePaperShift(timePaperId)
        #     if shift:
        #         self.shiftNameLineEdit.setCurrentText(shift[0])
        #         self.shiftStart.setTime(QTime(shift[1].hour, shift[1].minute))
        #         self.shiftEnd.setTime(QTime(shift[2].hour, shift[2].minute))
        #         self.shiftNameLineEdit.setEnabled(False)
        #         self.shiftStart.setEnabled(False)
        #         self.shiftEnd.setEnabled(False)
        # else:
        #     self.shiftNameLineEdit.setCurrentIndex(0)
        #     self.shiftNameLineEdit.setEnabled(True)
        #     self.shiftStart.setEnabled(True)
        #     self.shiftEnd.setEnabled(True)

    def clearWorker(self):
        self.workerShiftsHolder.setEnabled(False)
        self.clearWorkerInfo()
        self.workerLastNameLineEdit.clear()
        self.workerNumberLineEdit.clear()
        self.modelAndOperationHolder.setVisible(False)
        self.workerPlaceLineEdit.setText('Не е указано')
        self.workerPositionLineEdit.setText('Не е указано')

    def clearWorkerInfo(self):
        self.shiftNameLineEdit.setCurrentIndex(0)
        self.shiftStart.setTime(QTime(8, 0))
        self.shiftEnd.setTime(QTime(17, 0))
        self.isOvertimeWorking.setCheckState(Qt.CheckState.Unchecked)
        self.isHourlyWorking.setCheckState(Qt.CheckState.Unchecked)
        self.overtimeStart.setTime(QTime(0, 0))
        self.overtimeEnd.setTime(QTime(0, 0))
        self.hourlyStart.setTime(QTime(0, 0))
        self.hourlyEnd.setTime(QTime(0, 0))

    def clearOperationInfo(self, model=True):
        if model:
            self.clientModelsLineEdit.clear()
        else:
            self.clientModelsLineEdit.setFocus()
            self.clientModelsLineEdit.selectAll()

        if self.isHourlyWorking.isChecked():
            self.isHourlyWorking.setChecked(False)

        if self.isOvertimeWorking.isChecked():
            self.isOvertimeWorking.setChecked(False)

        self.modelOperationLineEdit.clear()
        self.modelPiecesLineEdit.clear()
        self.timeForPieceLineEdit.clear()
        self.piecesTimeLineEdit.setText('0')
        self.isDefaultTimeCheckBox.blockSignals(True)
        self.isDefaultTimeCheckBox.setCheckState(Qt.CheckState.Checked)
        self.isDefaultTimeCheckBox.blockSignals(False)
        self.piecesForProdLineEdit.clear()
        self.piecesProducedLineEdit.clear()
