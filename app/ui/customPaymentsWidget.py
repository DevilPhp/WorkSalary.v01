from functools import partial

from PySide6.QtGui import QStandardItemModel, QStandardItem

from app.ui.customSortingMenuWidget import CustomSortingMenuWidget
from app.ui.widgets.ui_customPaymentsWidget import *
from app.models.tableModel import CustomTableViewWithMultiSelection
from app.models.sortingModel import CaseInsensitiveProxyModel, FilterableHeaderView
from app.ui.customCalendarWidget import CustomCalendarDialog
from app.services.workerServices import WorkerServices as WoS
from app.utils.utils import Utils


class CustomPaymentsWidget(QWidget, Ui_customPaymentsWidget):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.paymentsTableView = CustomTableViewWithMultiSelection()
        self.paymentsTableHolder.layout().addWidget(self.paymentsTableView)
        self.tablePaymentsModel = QStandardItemModel()
        self.tablePaymentsNames = ['ID', '№', 'Име', 'Зар. дни', 'Бр.',
                                   'Вр. Опер. в ч.', 'Почас. в ч.', 'Извънр. в ч.', 'Бр./час', 'Лв.', '€']
        for i, tableHeaderName in enumerate(self.tablePaymentsNames):
            self.tablePaymentsModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.tablePaymentsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.tablePaymentsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelPaymentsTable = CaseInsensitiveProxyModel(numericColumns=[0, 1, 3, 4, 5, 6, 7, 8, 9, 10],
                                                                    parent=self)
        self.setProxyModel(self.proxyModelPaymentsTable, self.tablePaymentsModel, self.paymentsTableView)
        # self.timePapersForDayTableView.setModel(self.tablePaymentsModel)
        self.paymentsTableView.horizontalHeader().setDefaultSectionSize(80)
        self.paymentsTableView.horizontalHeader().setStretchLastSection(True)
        self.setColumnWidths()
        self.fromDateEdit.setDate(QDate.currentDate().addDays(-7))
        self.toDateEdit.setDate(QDate.currentDate())

        self.checkBoxFiltering = {}
        self.initialCheckBoxes = {}

        # self.setPayPerMinComboBox()
        
        self.refreshPaymentsTable()

        self.fromCalendarBtn.clicked.connect(self.showCalendarDialog)
        self.toCalendarBtn.clicked.connect(self.showCalendarDialog)

        self.fromDateEdit.dateChanged.connect(self.checkFromDate)
        self.toDateEdit.dateChanged.connect(self.checkToDate)

        self.searchBtn.clicked.connect(self.refreshPaymentsTable)
        self.paymentsTableView.doubleClicked.connect(self.openPaymentDetails)

    # def setPayPerMinComboBox(self):
    #     paymentsPerMin = WoS.getPaymentsForMin()
    #     self.payPerMinComboBox.clear()


    def showCalendarDialog(self):
        calendarDialog = CustomCalendarDialog()
        Utils.calculatingIdealDialogShowPos(self, calendarDialog)
        if self.sender() == self.fromCalendarBtn:
            calendarDialog.calendarCustomWidget.setSelectedDate(self.fromDateEdit.date())
            calendarDialog.dateSelected.connect(self.updateFromDateLabel)
        elif self.sender() == self.toCalendarBtn:
            calendarDialog.calendarCustomWidget.setSelectedDate(self.toDateEdit.date())
            calendarDialog.dateSelected.connect(self.updateToDateLabel)

        calendarDialog.exec_()

    def updateFromDateLabel(self, selectedDate):
        self.fromDateEdit.setDate(selectedDate)

    def updateToDateLabel(self, selectedDate):
        self.toDateEdit.setDate(selectedDate)

    def checkFromDate(self):
        if self.fromDateEdit.date() > self.toDateEdit.date():
            self.toDateEdit.setDate(self.fromDateEdit.date())

    def checkToDate(self):
        if self.toDateEdit.date() < self.fromDateEdit.date():
            self.fromDateEdit.setDate(self.toDateEdit.date())

    def setColumnWidths(self):
        self.paymentsTableView.setColumnWidth(0, 20)
        self.paymentsTableView.setColumnWidth(1, 40)
        self.paymentsTableView.setColumnWidth(2, 180)
        self.paymentsTableView.setColumnWidth(4, 50)
        self.paymentsTableView.setColumnWidth(5, 120)
        self.paymentsTableView.setColumnWidth(6, 100)
        self.paymentsTableView.setColumnWidth(7, 110)

    def refreshPaymentsTable(self):
        self.tablePaymentsModel.setRowCount(0)
        count = 0
        # workerNumber = self.workerNameLineEdit.text()
        startDate = Utils.convertQDateToDate(self.fromDateEdit.date())
        endDate = Utils.convertQDateToDate(self.toDateEdit.date())
        paymentsData = WoS.getInfoForPayments(startDate, endDate)
        # for pay in paymentsData:
        #     print(pay, paymentsData[pay])
        #     return
        paymentForMin = WoS.getPaymentForMin()
        paymentForNightMin = WoS.getPaymentForNightMin()
        paymentInLeva = paymentForMin.PaymentValue
        paymentInEuro = paymentForMin.PaymentInEuro
        nightPayInLeva = paymentForNightMin.NightPaymentValue
        nightPayInEuro = paymentForNightMin.NightPaymentInEuro

        for workerPayment in paymentsData:
            count += 1
            workerId = workerPayment.split(' : ')[0]
            workerName = workerPayment.split(' : ')[1]
            workingDays = len(paymentsData[workerPayment])
            totalPayInLev = 0
            totalPayInEuro = 0

            for timePaperPayment in paymentsData[workerPayment]:
                totalHourlyMins = 0
                totalOvertimeMins = 0
                totalPieces = 0
                totalTime = 0
                currentPayment = 0
                currentPaymentInEuro = 0
                hourly = paymentsData[workerPayment][timePaperPayment]['hourly']
                overtime = paymentsData[workerPayment][timePaperPayment]['overtime']
                nightMins = paymentsData[workerPayment][timePaperPayment]['nightMins']
                pieces = paymentsData[workerPayment][timePaperPayment]['totalPieces']
                workingTime = paymentsData[workerPayment][timePaperPayment]['totalTime']
                paymentRatio = paymentsData[workerPayment][timePaperPayment]['paymentRatio']
                if hourly:
                    for hourlyPayment in hourly:
                        totalHourlyMins += hourly[hourlyPayment][0]
                        currentPayment += (hourly[hourlyPayment][0] *
                                           hourly[hourlyPayment][1] *
                                           paymentRatio *
                                           paymentInLeva)
                        currentPaymentInEuro += (hourly[hourlyPayment][0] *
                                                 hourly[hourlyPayment][1] *
                                                 paymentRatio *
                                                 paymentInEuro)
                if overtime:
                    for overtimePayment in overtime:
                        totalOvertimeMins += overtime[overtimePayment][0]
                        currentPayment += overtime[overtimePayment][0]*overtime[overtimePayment][1]*paymentInLeva
                        currentPaymentInEuro += overtime[overtimePayment][0]*overtime[overtimePayment][1]*paymentInEuro

                if nightMins:
                    if workingTime > nightMins:
                        nightWorking = nightMins
                        currentPayment += (nightWorking *
                                           nightPayInLeva *
                                           paymentRatio)
                        currentPaymentInEuro += (nightWorking *
                                                 nightPayInEuro *
                                                 paymentRatio)
                        workingTime = workingTime - nightWorking

                    else:
                        nightWorking = workingTime
                        currentPayment += (nightWorking *
                                           nightPayInLeva *
                                           paymentRatio)
                        currentPaymentInEuro += (nightWorking *
                                                 nightPayInEuro *
                                                 paymentRatio)
                        currentPayment += (workingTime *
                                           paymentInLeva *
                                           paymentRatio)
                        currentPaymentInEuro += (workingTime *
                                                 paymentInEuro *
                                                 paymentRatio)
                else:
                    currentPayment += (workingTime *
                                       paymentInLeva *
                                       paymentRatio)
                    currentPaymentInEuro += (workingTime *
                                             paymentInEuro *
                                             paymentRatio)
                totalPieces += pieces
                totalTime = round(totalTime + workingTime, 2)

                totalPayInLev += currentPayment
                totalPayInEuro += currentPaymentInEuro
            displayOperTime = '0'
            displayHourlyTime = '0'
            displayOverTime = '0'
            efficiency = 0
            totalTime = round(totalTime, 2)
            if totalPieces != 0 or totalTime != 0:
                efficiency = round((totalTime / totalPieces), 2)
                displayOperTime = Utils.makeDispalyMins(totalTime)

            if totalOvertimeMins > 0:
                displayOverTime = Utils.makeDispalyMins(totalOvertimeMins)

            if totalHourlyMins > 0:
                displayHourlyTime = Utils.makeDispalyMins(totalHourlyMins)

            payInLeva = round(totalPayInLev, 2)
            payInEuro = round(totalPayInEuro, 2)

            row = [
                QStandardItem(str(count)),
                QStandardItem(str(workerId)),
                QStandardItem(workerName),
                QStandardItem(str(workingDays)),
                QStandardItem(str(totalPieces)),
                QStandardItem(displayOperTime),
                QStandardItem(displayHourlyTime),
                QStandardItem(displayOverTime),
                QStandardItem(str(efficiency)),
                QStandardItem(str(payInLeva)),
                QStandardItem(str(payInEuro))
            ]
            self.tablePaymentsModel.appendRow(row)

    def closeEvent(self, event):
        self.mainWindow.closeAllPaymentsDetails()

    def openPaymentDetails(self, index):
        workerId = self.proxyModelPaymentsTable.mapToSource(index).siblingAtColumn(1).data(Qt.ItemDataRole.DisplayRole)
        startDate = self.fromDateEdit.date()
        endDate = self.toDateEdit.date()
        self.mainWindow.setPaymentsDetailsPage(workerId, startDate, endDate)

    def setProxyModel(self, proxyModel, model, table):
        proxyModel.setSourceModel(model)
        filterableHeaderView = FilterableHeaderView(Qt.Orientation.Horizontal, table)
        table.setHorizontalHeader(filterableHeaderView)
        filterableHeaderView.filterRequested.connect(partial(self.updateFilter, proxyModel, filterableHeaderView))
        table.setModel(proxyModel)
        table.setSortingEnabled(True)

    def updateFilter(self, proxyModel, header, column):
        if column < 3:
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
    
    