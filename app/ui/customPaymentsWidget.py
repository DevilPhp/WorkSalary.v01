from functools import partial

from PySide6.QtGui import QStandardItemModel, QStandardItem

from app.ui.widgets.ui_customPaymentsWidget import *
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
        self.tablePaymentsNames = ['ID', '№', 'Дата', 'ПоръчкаNo', 'Бр.',
                                   'Време', 'Ефект.', 'Нач. лв.', 'Нач. €']
        for i, tableHeaderName in enumerate(self.tablePaymentsNames):
            self.tablePaymentsModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.tablePaymentsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.tablePaymentsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelPaymentsTable = CaseInsensitiveProxyModel(numericColumns=[0, 1, 3, 5, 6],
                                                           parent=self)
        self.setProxyModel(self.proxyModelPaymentsTable, self.tablePaymentsModel, self.paymentsTableView)
        # self.timePapersForDayTableView.setModel(self.tablePaymentsModel)
        self.paymentsTableView.horizontalHeader().setStretchLastSection(True)
        self.paymentsTableView.setColumnWidth(0, 60)
        self.paymentsTableView.setColumnWidth(1, 60)
        self.paymentsTableView.setColumnWidth(2, 150)
        self.paymentsTableView.setColumnWidth(3, 250)
        self.paymentsTableView.setColumnWidth(4, 70)
        self.paymentsTableView.setColumnWidth(5, 70)
        self.paymentsTableView.setColumnWidth(6, 70)
        self.paymentsTableView.setColumnWidth(7, 80)
        self.paymentsTableView.setColumnWidth(8, 80)
        self.fromDateEdit.setDate(QDate.currentDate().addDays(-7))
        self.toDateEdit.setDate(QDate.currentDate())
        
        self.refreshPaymentsTable()
    
    def refreshPaymentsTable(self):
        workerNumber = self.workerNumberLineEdit.text()
        startDate = Utils.convertQDateToDate(self.fromDateEdit.date())
        endDate = Utils.convertQDateToDate(self.toDateEdit.date())
        paymentsData = WoS.getInfoForPayments(workerNumber, startDate, endDate)
    
    def setProxyModel(self, proxyModel, model, table):
        proxyModel.setSourceModel(model)
        filterableHeaderView = FilterableHeaderView(Qt.Orientation.Horizontal, table)
        table.setHorizontalHeader(filterableHeaderView)
        # filterableHeaderView.filterRequested.connect(partial(self.updateFilter, proxyModel, filterableHeaderView))
        table.setModel(proxyModel)
        table.setSortingEnabled(True)
    
    