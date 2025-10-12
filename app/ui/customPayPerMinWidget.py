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
        self.payPerMinNight = Ps.getPayPerMin(False)
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

        self.refreshPayPerMinTable(self.payPerMin)

        self.payPerMinNightCheckBox.stateChanged.connect(self.showPayPerMinNight)


    def refreshPayPerMinTable(self, data):
        self.payPerMinModel.setRowCount(0)
        row = []
        for payPerMin in data:
            row = [
                QStandardItem(str(payPerMin['id'])),
                QStandardItem(str(payPerMin['valueLeva'])),
                QStandardItem(str(round(payPerMin['valueEUR'], 4))),
                QStandardItem(datetime.strftime(payPerMin['dateActive'], '%d.%m.%Y')),
                QStandardItem(datetime.strftime(payPerMin['lastUpdated'], '%d.%m.%Y')),
                QStandardItem(payPerMin['updatedBy']),
                QStandardItem(payPerMin['comment'])
            ]
            self.payPerMinModel.appendRow(row)

    def showPayPerMinNight(self):
        if self.payPerMinNightCheckBox.isChecked():
            self.pageTitle.setText("ПЛАЩАНЕ ЗА МИН. НОЩЕН ТРУД")
            self.refreshPayPerMinTable(self.payPerMinNight)
        else:
            self.pageTitle.setText("ПЛАЩАНЕ ЗА МИН.")
            self.refreshPayPerMinTable(self.payPerMin)
