from PySide6.QtGui import QStandardItemModel, QStandardItem

from app.ui.widgets.ui_customPaymentsDetailsWidget import *
from app.services.workerServices import WorkerServices as WoS
from app.models.customTreeView import CustomTreeView
from app.models.sortingModel import CaseInsensitiveProxyModel
from app.utils.utils import Utils


class CustomPaymentsDetailsWidget(QWidget, Ui_customPaymentsDetailsWidget):
    def __init__(self, mainWindow, workerId, startDate, endDate, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle(f'Детайли за работник с ID: {workerId}')
        self.mainWindow = mainWindow
        self.workerId = workerId
        self.startDate = startDate
        self.endDate = endDate
        self.workerDetalsTreeView = CustomTreeView(self)

        self.fromDateLineEdit.setText(self.startDate.toString('dd.MM.yyyy'))
        self.toDateLineEdit.setText(self.endDate.toString('dd.MM.yyyy'))

        self.setupWindowInfo()

        self.paymentsDetailsTableHolder.layout().addWidget(self.workerDetalsTreeView)
        self.tablePaymentDetailsModel = QStandardItemModel()
        self.tablePaymentDetailsNames = ['ID', 'Дата', 'Смяна', 'Поръчки', 'Опер.',
                                         'Вр. мин.', 'Поч. Раб.', 'Изв. Раб.', 'Бр.', 'Ефект.', 'Нач. лв.', 'Нач. €']
        for i, tableHeaderName in enumerate(self.tablePaymentDetailsNames):
            self.tablePaymentDetailsModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.tablePaymentDetailsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.tablePaymentDetailsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelPaymentsDetailsTree = CaseInsensitiveProxyModel(parent=self)
        self.setProxyModel(self.proxyModelPaymentsDetailsTree, self.tablePaymentDetailsModel, self.workerDetalsTreeView)
        # self.timePapersForDayTableView.setModel(self.tablePaymentsModel)
        self.workerDetalsTreeView.header().setDefaultSectionSize(80)
        self.workerDetalsTreeView.header().setStretchLastSection(True)
        self.setColumnWidths()
        self.refreshPaymentsDetailsTreeView()

    def setColumnWidths(self):
        self.workerDetalsTreeView.setColumnWidth(1, 100)
        self.workerDetalsTreeView.setColumnWidth(3, 100)
        self.workerDetalsTreeView.setColumnWidth(4, 60)
        self.workerDetalsTreeView.setColumnWidth(5, 50)
        self.workerDetalsTreeView.setColumnWidth(6, 85)
        self.workerDetalsTreeView.setColumnWidth(7, 85)
        self.workerDetalsTreeView.setColumnWidth(8, 50)
        self.workerDetalsTreeView.setColumnWidth(9, 70)

    def refreshPaymentsDetailsTreeView(self):
        self.tablePaymentDetailsModel.setRowCount(0)
        startDate = Utils.convertQDateToDate(self.startDate)
        endDate = Utils.convertQDateToDate(self.endDate)
        paymentsData = WoS.getPaymentsDetailsForWorker(self.workerId, startDate, endDate)
        paymentPerMinute = WoS.getPaymentForMin()
        paymentInLv = paymentPerMinute.PaymentValue
        paymentInEuro = paymentPerMinute.PaymentInEuro
        # print(paymentsData)
        if paymentsData:
            for payment, details in paymentsData.items():
                totalHourlyTime = 0
                totalOvertime = 0
                totalPaymentInLev = 0
                totalPaymentInEuro = 0
                if details['hourly']:
                    for hourlyPay in details['hourly']:
                        totalHourlyTime += hourlyPay[0]
                        totalPaymentInLev += hourlyPay[0] * hourlyPay[1] * details['paymentRatio'] * paymentInLv
                        totalPaymentInEuro += hourlyPay[0] * hourlyPay[1] * details['paymentRatio'] * paymentInEuro

                if details['overtime']:
                    for overtimePay in details['overtime']:
                        totalOvertime += overtimePay[0]
                        totalPaymentInLev += overtimePay[0] * overtimePay[1] * details['paymentRatio'] * paymentInLv
                        totalPaymentInEuro += overtimePay[0] * overtimePay[1] * details['paymentRatio'] * paymentInEuro

                totalPaymentInLev += details['totalTime'] * details['paymentRatio'] * paymentInLv
                totalPaymentInEuro += details['totalTime'] * details['paymentRatio'] * paymentInEuro

                parentRow = QStandardItem(str(payment))
                row = [
                    parentRow,
                    QStandardItem(details['date']),
                    QStandardItem(details['shift']),
                    QStandardItem(str(details['ordersCount'])),
                    QStandardItem(str(details['operationsCount'])),
                    QStandardItem(str(details['totalTime'])),
                    QStandardItem(str(totalHourlyTime)),
                    QStandardItem(str(totalOvertime)),
                    QStandardItem(str(details['totalPieces'])),
                    QStandardItem(str(round(details['totalTime'] / details['totalPieces'], 2))
                                  if details['totalPieces'] > 0 else '0'),
                    QStandardItem(str(round(totalPaymentInLev, 2))),
                    QStandardItem(str(round(totalPaymentInEuro, 2)))
                ]
                self.tablePaymentDetailsModel.appendRow(row)

                if details['hourly']:
                    for hourlyPay in details['hourly']:
                        subRow = [
                            QStandardItem(str(hourlyPay[2])),
                            QStandardItem(details['date']),
                            QStandardItem(details['shift']),
                            QStandardItem('Почасово'),
                            QStandardItem('0'),
                            QStandardItem('0'),
                            QStandardItem(str(hourlyPay[0])),
                            QStandardItem('0'),
                            QStandardItem('0'),
                            QStandardItem('0'),
                            QStandardItem(str(round(hourlyPay[0] * hourlyPay[1] * details['paymentRatio'] * paymentInLv, 2))),
                            QStandardItem(str(round(hourlyPay[0] * hourlyPay[1] * details['paymentRatio'] * paymentInEuro, 2)))
                        ]
                        parentRow.appendRow(subRow)

                if details['overtime']:
                    for overtimePay in details['overtime']:
                        subRow = [
                            QStandardItem(str(overtimePay[2])),
                            QStandardItem(details['date']),
                            QStandardItem(details['shift']),
                            QStandardItem('Извънреден'),
                            QStandardItem('0'),
                            QStandardItem('0'),
                            QStandardItem('0'),
                            QStandardItem(str(overtimePay[0])),
                            QStandardItem('0'),
                            QStandardItem('0'),
                            QStandardItem(str(round(overtimePay[0] * overtimePay[1] * details['paymentRatio'] * paymentInLv, 2))),
                            QStandardItem(str(round(overtimePay[0] * overtimePay[1] * details['paymentRatio'] * paymentInEuro, 2)))
                        ]
                        parentRow.appendRow(subRow)

                if details['operations']:
                    for operation in details['operations'].keys():
                        subRow = [
                            QStandardItem(str(operation)),
                            QStandardItem(details['date']),
                            QStandardItem(details['shift']),
                            QStandardItem(details['operations'][operation]['order']),
                            QStandardItem(str(details['operations'][operation]['operation'])),
                            QStandardItem(str(round(details['operations'][operation]['time'], 2))),
                            QStandardItem('0'),
                            QStandardItem('0'),
                            QStandardItem(str(details['operations'][operation]['pieces'])),
                            QStandardItem(str(round(details['operations'][operation]['time']
                                                    / details['operations'][operation]['pieces'], 2))),
                            QStandardItem(
                                str(round(
                                    (details['operations'][operation]['time']*details['paymentRatio']*paymentInLv), 2))
                                ),
                            QStandardItem(
                                str(round(
                                    (details['operations'][operation]['time']*details['paymentRatio']*paymentInEuro), 2))
                            )
                        ]
                        parentRow.appendRow(subRow)
        self.proxyModelPaymentsDetailsTree.sort(1, Qt.SortOrder.DescendingOrder)

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
