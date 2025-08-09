from functools import partial

from PySide6.QtGui import QStandardItemModel, QStandardItem

from app.ui.customSortingMenuWidget import CustomSortingMenuWidget
from app.ui.widgets.ui_customPaymentsWidget import *
from app.ui.customPaymentsDetailsWidget import CustomPaymentsDetailsWidget
from app.models.tableModel import CustomTableViewWithMultiSelection
from app.models.sortingModel import CaseInsensitiveProxyModel, FilterableHeaderView
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
                                   'Време', 'Бр./час', 'Лв.', '€']
        for i, tableHeaderName in enumerate(self.tablePaymentsNames):
            self.tablePaymentsModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.tablePaymentsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.tablePaymentsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelPaymentsTable = CaseInsensitiveProxyModel(numericColumns=[0, 1, 3, 4, 5, 6, 7, 8],
                                                           parent=self)
        self.setProxyModel(self.proxyModelPaymentsTable, self.tablePaymentsModel, self.paymentsTableView)
        # self.timePapersForDayTableView.setModel(self.tablePaymentsModel)
        self.paymentsTableView.horizontalHeader().setDefaultSectionSize(80)
        self.paymentsTableView.horizontalHeader().setStretchLastSection(True)
        self.paymentsTableView.setColumnWidth(2, 180)
        self.fromDateEdit.setDate(QDate.currentDate().addDays(-7))
        self.toDateEdit.setDate(QDate.currentDate())

        self.checkBoxFiltering = {}
        self.initialCheckBoxes = {}
        
        self.refreshPaymentsTable()

        self.searchBtn.clicked.connect(self.refreshPaymentsTable)
        self.paymentsTableView.doubleClicked.connect(self.openPaymentDetails)
    
    def refreshPaymentsTable(self):
        self.tablePaymentsModel.setRowCount(0)
        count = 0
        # workerNumber = self.workerNameLineEdit.text()
        startDate = Utils.convertQDateToDate(self.fromDateEdit.date())
        endDate = Utils.convertQDateToDate(self.toDateEdit.date())
        paymentsData = WoS.getInfoForPayments(startDate, endDate)
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
            totalHourlyMins = 0
            totalOvertimeMins = 0
            totalPieces = 0
            totalTime = 0
            workingPayInLeva = 0
            workingPayInEuro = 0
            hourlyPayInLeva = 0
            hourlyPayInEuro = 0
            overtimePayInLeva = 0
            overtimePayInEuro = 0
            # payInLeva = 0
            # payInEuro = 0
            # currentPayment = 0
            # currentPaymentInEuro = 0

            for timePaperPayment in paymentsData[workerPayment]:
                hourly = paymentsData[workerPayment][timePaperPayment]['hourly']
                overtime = paymentsData[workerPayment][timePaperPayment]['overtime']
                pieces = paymentsData[workerPayment][timePaperPayment]['totalPieces']
                workingTime = paymentsData[workerPayment][timePaperPayment]['totalTime']
                if hourly:
                    totalHourlyMins = round(totalHourlyMins + hourly[1], 2)
                if overtime:
                    totalOvertimeMins = round(totalOvertimeMins + overtime[1], 2)
                # currentPayment = workingTime * paymentInLeva * paymentsData[workerPayment][payment]['paymentRation']
                # currentPaymentInEuro = workingTime * paymentInEuro * paymentsData[workerPayment][payment]['paymentRation']



                # print(f'Payment: {workerName} {currentPayment}, Euro: {currentPaymentInEuro}')
                totalPieces += pieces
                totalTime = round(totalTime + workingTime, 2)
                # payInLeva = round(payInLeva + currentPayment, 2)
                # payInEuro = round(payInEuro + currentPaymentInEuro, 2)
                # print(paymentsData[workerPayment][payment]['paymentRation'])
            dispalyTime = '0'
            efficiency = 0
            totalTime = round(totalTime + totalHourlyMins + totalOvertimeMins, 2)
            if totalPieces != 0 or totalTime != 0:
                efficiency = round((totalTime / totalPieces), 2)
                dispalyTime = f'{int(totalTime / 60)}:{int(totalTime % 60)}' \
                    if totalTime % 60 > 0 else f'{int(totalTime / 60)}'
            # print(totalTime, totalMins)
            payInLeva = round(totalTime * paymentInLeva, 2)
            payInEuro = round(totalTime * paymentInEuro, 2)

            row = [
                QStandardItem(str(count)),
                QStandardItem(str(workerId)),
                QStandardItem(workerName),
                QStandardItem(str(workingDays)),
                QStandardItem(str(totalPieces)),
                QStandardItem(dispalyTime),
                QStandardItem(str(efficiency)),
                QStandardItem(str(payInLeva)),
                QStandardItem(str(payInEuro))
            ]
            self.tablePaymentsModel.appendRow(row)

    def closeEvent(self, event):
        self.mainWindow.closeAllPaymentsDetails()

    def openPaymentDetails(self, index):
        workerId = self.proxyModelPaymentsTable.mapToSource(index).siblingAtColumn(1).data(Qt.ItemDataRole.DisplayRole)
        startDate = Utils.convertQDateToDate(self.fromDateEdit.date())
        endDate = Utils.convertQDateToDate(self.toDateEdit.date())
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
    
    