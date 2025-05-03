from PySide6.QtGui import QStandardItemModel, QStandardItem

from app.ui.widgets.ui_customPaymentsDetailsWidget import *
from app.services.workerServices import WorkerServices as WoS
from app.models.tableModel import CustomTableViewWithMultiSelection
from app.models.customTreeView import CustomTreeView
from app.models.sortingModel import CaseInsensitiveProxyModel


class CustomPaymentsDetailsWidget(QWidget, Ui_customPaymentsDetailsWidget):
    def __init__(self, mainWindow, workerId, startDate, endDate, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.mainWindow = mainWindow
        self.workerId = workerId
        self.startDate = startDate
        self.endDate = endDate
        self.workerDetalsTreeView = CustomTreeView(self)

        self.setupWindowInfo()

        self.paymentsDetailsTableHolder.layout().addWidget(self.workerDetalsTreeView)
        self.tablePaymentDetailsModel = QStandardItemModel()
        self.tablePaymentDetailsNames = ['ID', 'Дата', 'Смяна', 'Поръчки', 'Операции',
                                         'Време', 'Поч. Раб.', 'Бройки', 'Ефект.', 'Нач. лв.', 'Нач. €']
        for i, tableHeaderName in enumerate(self.tablePaymentDetailsNames):
            self.tablePaymentDetailsModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.tablePaymentDetailsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.tablePaymentDetailsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelPaymentsDetailsTree = CaseInsensitiveProxyModel(numericColumns=[0, 5, 6, 7, 8, 9],
                                                                       parent=self)
        self.setProxyModel(self.proxyModelPaymentsDetailsTree, self.tablePaymentDetailsModel, self.workerDetalsTreeView)
        # self.timePapersForDayTableView.setModel(self.tablePaymentsModel)
        self.workerDetalsTreeView.header().setDefaultSectionSize(80)
        self.workerDetalsTreeView.header().setStretchLastSection(True)
        self.workerDetalsTreeView.setColumnWidth(3, 150)
        self.workerDetalsTreeView.setColumnWidth(2, 120)
        self.workerDetalsTreeView.setColumnWidth(1, 120)
        self.refreshPaymentsDetailsTreeView()

    # ['ID', 'Дата', 'Смяна', 'Поръчки', 'Операции',
    #  'Време', 'Поч. Раб.' 'Ефект.', 'Нач. лв.', 'Нач. €']
    def refreshPaymentsDetailsTreeView(self):
        self.tablePaymentDetailsModel.setRowCount(0)
        paymentsData = WoS.getPaymentsDetailsForWorker(self.workerId, self.startDate, self.endDate)
        if paymentsData:
            for payment, details in paymentsData.items():
                row = [
                    QStandardItem(str(payment)),
                    QStandardItem(details['date']),
                    QStandardItem(details['shift']),
                    QStandardItem(str(details['ordersCount'])),
                    QStandardItem(str(details['operationsCount'])),
                    QStandardItem(str(details['totalTime'])),
                    QStandardItem(str(details['isHourly'])),
                    QStandardItem(str(details['totalPieces'])),
                    QStandardItem(str(round(details['totalTime'] / details['totalPieces'], 2))),
                    QStandardItem('0'),
                    QStandardItem('0')
                ]
                self.tablePaymentDetailsModel.appendRow(row)

    def setProxyModel(self, proxyModel, model, table):
        proxyModel.setSourceModel(model)
        # filterableHeaderView = FilterableHeaderView(Qt.Orientation.Horizontal, table)
        # table.setHorizontalHeader(filterableHeaderView)
        # filterableHeaderView.filterRequested.connect(partial(self.updateFilter, proxyModel, filterableHeaderView))
        table.setModel(proxyModel)
        table.setSortingEnabled(True)

    def setupWindowInfo(self):
        workerData = WoS.getWorkerDataForPayments(self.workerId)
        self.workerNameLabel.setText(workerData['firstName'])
        self.workerLastNameLabel.setText(workerData['lastName'])
        self.workerNumberLabel.setText(str(workerData['id']))
        self.workerPlaceLabel.setText(workerData['place'])
        self.workerPositionLabel.setText(workerData['position'])
