from datetime import datetime

from PySide6.QtGui import QStandardItemModel, QStandardItem

from app.models.sortingModel import CaseInsensitiveProxyModel
from app.ui.widgets.ui_customPayPerMinWidget import *
from app.services.paymentsServices import PaymentServices as Ps


class CustomPayPerMinWidget(QWidget, Ui_customPayPerMinWidget):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle("Плашане за Мин.")
        self.payPerMin = Ps.getPayPerMin()
        self.payPerMinModel = QStandardItemModel()
        self.payPerMinHeaderNames = ['ID', 'Коеф. в лв', 'Коеф. в €',
                                     'Активно за', 'Модификации', 'Профил', 'Коментар']
        for i, tableHeaderName in enumerate(self.payPerMinHeaderNames):
            self.payPerMinModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.payPerMinModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.payPerMinModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelPayPerMin = CaseInsensitiveProxyModel(numericColumns=[0, 1, 2], dateColumns=[3, 4], parent=self)
        self.proxyModelPayPerMin.setSourceModel(self.payPerMinModel)
        self.payPerMinTableView.setModel(self.proxyModelPayPerMin)
        self.payPerMinTableView.setSortingEnabled(True)
        self.payPerMinTableView.horizontalHeader().setStretchLastSection(True)
        self.payPerMinTableView.horizontalHeader().setMinimumWidth(120)
        self.payPerMinTableView.setColumnWidth(0, 50)
        # self.payPerMinTableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.refreshPayPerMinTable()


    def refreshPayPerMinTable(self):
        self.payPerMinModel.setRowCount(0)
        row = []
        for payPerMin in self.payPerMin:
            row = [
                QStandardItem(str(payPerMin.id)),
                QStandardItem(str(payPerMin.PaymentValue)),
                QStandardItem(str(round(payPerMin.PaymentInEuro, 4))),
                QStandardItem(datetime.strftime(payPerMin.DateActive, '%d.%m.%Y')),
                QStandardItem(datetime.strftime(payPerMin.LastUpdated, '%d.%m.%Y')),
                QStandardItem(payPerMin.UpdatedBy),
                QStandardItem(payPerMin.Comment)
            ]
            self.payPerMinModel.appendRow(row)

