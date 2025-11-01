from PySide6.QtCore import Signal
from PySide6.QtGui import QStandardItemModel, QStandardItem

from app.ui.widgets.ui_customPaymentsDetailsWidget import *
from app.services.workerServices import WorkerServices as WoS
from app.models.customTreeView import CustomTreeView
from app.models.sortingModel import CaseInsensitiveProxyModel
from app.utils.utils import Utils


class CustomPaymentsDetailsWidget(QWidget, Ui_customPaymentsDetailsWidget):
    logoutSignal = Signal(bool)

    def __init__(self, mainWindow, workerId, startDate, endDate, totalPayInLeva, totalPayInEuro, user, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle(f'Детайли за работник с ID: {workerId}')
        self.mainWindow = mainWindow
        self.usernameLabel.setText(user)
        self.user = user

        self.workerId = workerId
        self.startDate = startDate
        self.endDate = endDate
        self.workerDetalsTreeView = CustomTreeView(self)
        self.totalPayInLeva = totalPayInLeva
        self.totalPayInEuro = totalPayInEuro

        self.fromDateLineEdit.setText(self.startDate.toString('dd.MM.yyyy'))
        self.toDateLineEdit.setText(self.endDate.toString('dd.MM.yyyy'))

        self.setupWindowInfo()

        self.paymentsDetailsTableHolder.layout().addWidget(self.workerDetalsTreeView)
        self.tablePaymentDetailsModel = QStandardItemModel()
        self.tablePaymentDetailsNames = ['ID', 'Дата', 'Смяна', 'Поръчки', 'Опер.',
                                         'Вр. мин.', 'Поч./Празн. дни', 'Поч. Раб.', 'Изв. Раб.', 'Нощен труд',
                                         'Бр.', 'Ефект.', 'Нач. лв.', 'Нач. €']
        for i, tableHeaderName in enumerate(self.tablePaymentDetailsNames):
            self.tablePaymentDetailsModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.tablePaymentDetailsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.tablePaymentDetailsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelPaymentsDetailsTree = CaseInsensitiveProxyModel(numericColumns=[0, 4, 5, 7, 8, 9,
                                                                                       10, 11, 12, 13],
                                                                       dateColumns=[1],
                                                                       parent=self)
        self.setProxyModel(self.proxyModelPaymentsDetailsTree, self.tablePaymentDetailsModel, self.workerDetalsTreeView)
        # self.timePapersForDayTableView.setModel(self.tablePaymentsModel)
        self.workerDetalsTreeView.header().setDefaultSectionSize(80)
        self.workerDetalsTreeView.header().setStretchLastSection(True)
        self.setColumnWidths()
        self.refreshPaymentsDetailsTreeView()
        self.setInitialColumns()

        self.workerDetalsTreeView.selectedRows.connect(self.showPaymentDetails)
        self.workerDetalsTreeView.clearCurrentSelection.connect(self.resetSelectedInfo)

        self.hourlyCheckBox.stateChanged.connect(self.onHourlyStateChanged)
        self.overtimeCheckBox.stateChanged.connect(self.onOvertimeStateChanged)
        self.nightTimeCheckBox.stateChanged.connect(self.onNightTimeStateChanged)
        self.selectAllCheckBox.stateChanged.connect(self.onSelectAllStateChanged)
        self.weekendHolidaysCheckBox.stateChanged.connect(self.onWeekendHolidaysStateChanged)

        self.logoutBtn.clicked.connect(self.logout)

    def showPaymentDetails(self, selectedRows):
        numberSelectedRows = len(selectedRows['payInEuro'])
        totalPayInLeva = 0
        totalPayInEuro = 0
        avrLeva = 0
        avrEuro = 0

        for key, row in selectedRows.items():
            if key == 'payInEuro':
                for item in row:
                    totalPayInEuro += float(item.data())
            else:
                for item in row:
                    totalPayInLeva += float(item.data())

        if len(selectedRows['payInLeva']) > 0:
            avrLeva = round(totalPayInLeva / len(selectedRows['payInLeva']), 2)
            avrEuro = round(totalPayInEuro / len(selectedRows['payInEuro']), 2)

        self.totalSelectedRows.setText(str(numberSelectedRows))
        self.totalLevaLabel.setText(str(round(totalPayInLeva, 2)))
        self.totalEuroLabel.setText(str(round(totalPayInEuro, 2)))
        self.avrLevaLabel.setText(str(avrLeva))
        self.avrEuroLabel.setText(str(avrEuro))

    def resetSelectedInfo(self):
        self.totalSelectedRows.setText("0")
        self.totalLevaLabel.setText("0.0")
        self.totalEuroLabel.setText("0.0")
        self.avrLevaLabel.setText("0.0")
        self.avrEuroLabel.setText("0.0")

    def setColumnWidths(self):
        self.workerDetalsTreeView.setColumnWidth(1, 100)
        self.workerDetalsTreeView.setColumnWidth(3, 100)
        self.workerDetalsTreeView.setColumnWidth(4, 60)
        self.workerDetalsTreeView.setColumnWidth(5, 80)
        self.workerDetalsTreeView.setColumnWidth(6, 100)
        self.workerDetalsTreeView.setColumnWidth(7, 85)
        self.workerDetalsTreeView.setColumnWidth(8, 85)
        self.workerDetalsTreeView.setColumnWidth(9, 50)
        self.workerDetalsTreeView.setColumnWidth(10, 70)

    def setInitialColumns(self):
        self.workerDetalsTreeView.setColumnHidden(6, True)
        self.workerDetalsTreeView.setColumnHidden(7, True)
        self.workerDetalsTreeView.setColumnHidden(8, True)
        self.workerDetalsTreeView.setColumnHidden(9, True)

    def checkAllstate(self):
        if (self.hourlyCheckBox.isChecked() and
                self.overtimeCheckBox.isChecked() and
                self.nightTimeCheckBox.isChecked() and
                self.weekendHolidaysCheckBox.isChecked()):
            self.selectAllCheckBox.setChecked(True)
        else:
            self.selectAllCheckBox.blockSignals(True)
            self.selectAllCheckBox.setChecked(False)
            self.selectAllCheckBox.blockSignals(False)

    def onSelectAllStateChanged(self, state):
        self.hourlyCheckBox.setChecked(state)
        self.overtimeCheckBox.setChecked(state)
        self.nightTimeCheckBox.setChecked(state)
        self.weekendHolidaysCheckBox.setChecked(state)

    def onWeekendHolidaysStateChanged(self, state):
        self.workerDetalsTreeView.setColumnHidden(6, not state)
        self.checkAllstate()

    def onHourlyStateChanged(self, state):
        self.workerDetalsTreeView.setColumnHidden(7, not state)
        self.checkAllstate()

    def onOvertimeStateChanged(self, state):
        self.workerDetalsTreeView.setColumnHidden(8, not state)
        self.checkAllstate()

    def onNightTimeStateChanged(self, state):
        self.workerDetalsTreeView.setColumnHidden(9, not state)
        self.checkAllstate()

    def refreshPaymentsDetailsTreeView(self):
        self.tablePaymentDetailsModel.setRowCount(0)
        totalRows = 0
        startDate = Utils.convertQDateToDate(self.startDate)
        endDate = Utils.convertQDateToDate(self.endDate)
        paymentsData = WoS.getPaymentsDetailsForWorker(self.workerId, startDate, endDate)
        paymentPerMinute = WoS.getPaymentForMin()
        paymentForNightMin = WoS.getPaymentForNightMin()
        paymentInLv = paymentPerMinute.PaymentValue
        paymentInEuro = paymentPerMinute.PaymentInEuro
        nightPayInLeva = paymentForNightMin.NightPaymentValue + paymentInLv
        nightPayInEuro = paymentForNightMin.NightPaymentInEuro + paymentInEuro
        self.levaPerMinDayLabel.setText(str(paymentInLv))
        self.euroPerMinDayLabel.setText(str(paymentInEuro))
        self.levaPerMinNightLabel.setText(str(nightPayInLeva))
        self.euroPerMinNightLabel.setText(str(nightPayInEuro))
        self.paymentLevaLabel.setText(f'{self.totalPayInLeva} лв')
        self.paymentEuroLabel.setText(f'{self.totalPayInEuro} €')

        if paymentsData:
            for payment, details in paymentsData.items():
                totalHourlyTime = 0
                totalOvertime = 0
                totalNightTime = 0
                totalPaymentInLev = 0
                totalPaymentInEuro = 0
                if details['hourly']:
                    data = self.calculatePayment(details['hourly'], details['paymentRatio'], paymentInLv,
                                                 paymentInEuro, nightPayInLeva, nightPayInEuro)
                    totalPaymentInLev += data[0]
                    totalPaymentInEuro += data[1]
                    totalNightTime += data[2]
                    totalHourlyTime += data[3]

                if details['overtime']:
                    data = self.calculatePayment(details['overtime'], details['paymentRatio'], paymentInLv,
                                                 paymentInEuro, nightPayInLeva, nightPayInEuro)
                    totalPaymentInLev += data[0]
                    totalPaymentInEuro += data[1]
                    totalNightTime += data[2]
                    totalOvertime += data[3]
                if details['nightMins'] > 0:
                    totalNightTime += details['nightMins']
                    totalPaymentInLev += Utils.calculatePayment(details['nightMins'], details['paymentRatio'],
                                                            1, nightPayInLeva)
                    totalPaymentInEuro += Utils.calculatePayment(details['nightMins'], details['paymentRatio'],
                                                             1, nightPayInEuro)

                totalPaymentInLev += Utils.calculatePayment(details['totalTime'] - details['nightMins'],
                                                            details['paymentRatio'], 1, paymentInLv)
                totalPaymentInEuro += Utils.calculatePayment(details['totalTime'] - details['nightMins'],
                                                            details['paymentRatio'], 1, paymentInEuro)

                weekendHolidays = QStandardItem('')
                if details['paymentRatio'] >= 1.75:
                    weekendHolidays.setText('Почивен ден')

                if details['paymentRatio'] >= 2:
                    weekendHolidays.setText('Празничен ден')

                parentRow = QStandardItem(str(payment))
                row = [
                    parentRow,
                    QStandardItem(details['date']),
                    QStandardItem(details['shift']),
                    QStandardItem(str(details['ordersCount'])),
                    QStandardItem(str(details['operationsCount'])),
                    QStandardItem(str(details['totalTime'])),
                    weekendHolidays,
                    QStandardItem(str(round(totalHourlyTime, 2))),
                    QStandardItem(str(round(totalOvertime, 2))),
                    QStandardItem(str(round(totalNightTime, 2))),
                    QStandardItem(str(details['totalPieces'])),
                    QStandardItem(str(round(details['totalTime'] / details['totalPieces'], 2))
                                  if details['totalPieces'] > 0 else '0'),
                    QStandardItem(str(round(totalPaymentInLev, 2))),
                    QStandardItem(str(round(totalPaymentInEuro, 2)))
                ]
                self.tablePaymentDetailsModel.appendRow(row)
                totalRows += 1

                if details['hourly']:
                    for hourlyPay in details['hourly']:

                        data = self.calculatePaymentNoRepeat(hourlyPay, details['paymentRatio'], paymentInLv,
                                                             paymentInEuro, nightPayInLeva, nightPayInEuro)

                        subRow = self.makeSubRowForTreeView([hourlyPay[2], details['date'], details['shift'],
                                                             'Почасово', 0, 0, weekendHolidays, hourlyPay[0], 0,
                                                             round(hourlyPay[3], 2), 0, 0,
                                                             round(data[0], 2), round(data[1], 2)
                                                             ])
                        parentRow.appendRow(subRow)

                if details['overtime']:
                    for overtimePay in details['overtime']:

                        data = self.calculatePaymentNoRepeat(overtimePay, details['paymentRatio'], paymentInLv,
                                                             paymentInEuro, nightPayInLeva, nightPayInEuro)

                        subRow = self.makeSubRowForTreeView([overtimePay[2], details['date'], details['shift'],
                                                             'Извънреден', 0, 0, weekendHolidays, 0, overtimePay[0],
                                                             round(overtimePay[3], 2), 0, 0,
                                                             round(data[0], 2), round(data[1], 2)
                                                             ])
                        parentRow.appendRow(subRow)

                if details['operations']:
                    # nightMins = details['nightMins']
                    for operation in details['operations'].keys():
                        operPayInLev = 0
                        operPayInEuro = 0
                        operTime = details['operations'][operation]['time']
                        oprerPieces = details['operations'][operation]['pieces']
                        nightMins = details['operations'][operation]['nightMins']

                        if nightMins > 0:
                            if nightMins < operTime:
                                operPayInLev += Utils.calculatePayment(operTime - nightMins, 1,
                                                                       details['paymentRatio'], paymentInLv)
                                operPayInEuro += Utils.calculatePayment(operTime - nightMins, 1,
                                                                        details['paymentRatio'], nightPayInEuro)
                            operPayInLev += Utils.calculatePayment(nightMins, 1,
                                                                   details['paymentRatio'], nightPayInLeva)
                            operPayInEuro += Utils.calculatePayment(nightMins, 1,
                                                                    details['paymentRatio'], nightPayInEuro)
                        else:
                            operPayInLev += Utils.calculatePayment(operTime, 1,
                                                                   details['paymentRatio'], paymentInLv)
                            operPayInEuro += Utils.calculatePayment(operTime, 1,
                                                                    details['paymentRatio'], paymentInEuro)

                        subRow = self.makeSubRowForTreeView([operation,
                                                             details['date'], details['shift'],
                                                             details['operations'][operation]['order'],
                                                             details['operations'][operation]['operation'],
                                                             round(details['operations'][operation]['time'], 2),
                                                             weekendHolidays, '0', '0', round(nightMins, 2),
                                                             details['operations'][operation]['pieces'],
                                                             round(operTime / oprerPieces, 2),
                                                             round(operPayInLev, 2),
                                                             round(operPayInEuro, 2)
                                                             ])
                        parentRow.appendRow(subRow)
        self.totalViewRows.setText(str(totalRows))
        self.proxyModelPaymentsDetailsTree.sort(1, Qt.SortOrder.DescendingOrder)

    def makeSubRowForTreeView(self, rows):
        returnedRow = [
            QStandardItem(str(rows[0])),  #'ID'
            QStandardItem(str(rows[1])),  #'Дата'
            QStandardItem(str(rows[2])),  #'Смяна'
            QStandardItem(str(rows[3])),  #'Поръчки'
            QStandardItem(str(rows[4])),  #'Опер.'
            QStandardItem(str(rows[5])),  #'Вр. мин.'
            rows[6],  #'Поч./Празн. дни'
            QStandardItem(str(rows[7])),  #'Поч. Раб.'
            QStandardItem(str(rows[8])),  #'Изв. Раб.'
            QStandardItem(str(rows[9])),  #'Нощен труд'
            QStandardItem(str(rows[10])),  #'Бр.'
            QStandardItem(str(rows[11])),  #'Ефект.'
            QStandardItem(str(rows[12])),  #'Нач. лв.'
            QStandardItem(str(rows[13])),  #'Нач. €'
        ]
        return returnedRow

    def calculatePayment(self, data, mainPaymentRation, paymentInLv,
                         paymentInEuro, nightPayInLeva, nightPayInEuro):
        totalPaymentInLev = 0
        totalPaymentInEuro = 0
        totalNightTime = 0
        totalTime = 0

        for pay in data:
            efficient = pay[0]
            ratio = pay[1]
            nightMins = pay[3]

            totalPaymentInLev += Utils.calculatePayment(efficient - nightMins, ratio,
                                                        mainPaymentRation, paymentInLv)
            totalPaymentInEuro += Utils.calculatePayment(efficient - nightMins, ratio,
                                                         mainPaymentRation, paymentInEuro)
            if nightMins > 0:
                totalNightTime += nightMins
                totalPaymentInLev += Utils.calculatePayment(nightMins, ratio,
                                                            mainPaymentRation, nightPayInLeva)
                totalPaymentInEuro += Utils.calculatePayment(nightMins, ratio,
                                                             mainPaymentRation, nightPayInEuro)
            totalTime += efficient

        return totalPaymentInLev, totalPaymentInEuro, totalNightTime, totalTime

    def calculatePaymentNoRepeat(self, data, mainPaymentRation, paymentInLv,
                                 paymentInEuro, nightPayInLeva, nightPayInEuro):
        totalPayLv = 0
        totalPayEuro = 0
        totalPayLv += Utils.calculatePayment((data[0] - data[3]),
                                             data[1], mainPaymentRation, paymentInLv)
        totalPayEuro += Utils.calculatePayment((data[0] - data[3]),
                                               data[1], mainPaymentRation, paymentInEuro)

        if data[3] > 0:
            totalPayLv += Utils.calculatePayment(data[3], data[1],
                                                 mainPaymentRation, nightPayInLeva)
            totalPayEuro += Utils.calculatePayment(data[3], data[1],
                                                   mainPaymentRation, nightPayInEuro)
        return totalPayLv, totalPayEuro

    def setProxyModel(self, proxyModel, model, table):
        proxyModel.setSourceModel(model)
        table.setModel(proxyModel)
        table.setSortingEnabled(True)

    def setupWindowInfo(self):
        workerData = WoS.getWorkerDataForPayments(self.workerId)
        self.workerNameLabel.setText(workerData['firstName'])
        self.workerLastNameLabel.setText(workerData['lastName'])
        self.workerNumberLabel.setText(str(workerData['id']))
        self.workerPlaceLabel.setText(workerData['place'])
        self.workerPositionLabel.setText(workerData['position'])

    def logout(self):
        self.logoutSignal.emit(True)
