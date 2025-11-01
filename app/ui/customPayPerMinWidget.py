from datetime import datetime

from PySide6.QtCore import Signal
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QDialog, QMenu

from app.models.sortingModel import CaseInsensitiveProxyModel
from app.ui.customYesNoMessage import CustomYesNowDialog
from app.ui.widgets.ui_customPayPerMinWidget import *
from app.services.paymentsServices import PaymentServices as Ps
from app.ui.customPayPerMinDialog import CustomPayPerTimeDialog
from app.ui.messagesManager import MessageManager as MM
from app.utils.utils import Utils


class CustomPayPerMinWidget(QWidget, Ui_customPayPerMinWidget):
    logoutSignal = Signal(bool)

    def __init__(self, mainWindow, user, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle("Плашане за Мин.")
        self.usernameLabel.setText(user)
        self.user = user
        self.payPerMin = Ps.getPayPerMin()
        self.payPerMinNight = Ps.getPayPerMin(False)
        self.payPerMinModel = QStandardItemModel()
        self.payPerMinHeaderNames = ['ID', 'Коеф. в лв', 'Коеф. в €', 'лв/€',
                                     'Активно', 'Активно за', 'Модификации', 'Профил', 'Коментар']
        for i, tableHeaderName in enumerate(self.payPerMinHeaderNames):
            self.payPerMinModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.payPerMinModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.payPerMinModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelPayPerMin = CaseInsensitiveProxyModel(numericColumns=[0, 1, 2, 3],
                                                             dateColumns=[5, 6],
                                                             parent=self)

        self.proxyModelPayPerMin.setSourceModel(self.payPerMinModel)
        self.payPerMinTableView.setModel(self.proxyModelPayPerMin)
        self.payPerMinTableView.setSortingEnabled(True)
        self.payPerMinTableView.horizontalHeader().setStretchLastSection(True)
        self.payPerMinTableView.horizontalHeader().setMinimumWidth(120)
        self.payPerMinTableView.setColumnWidth(0, 50)
        self.payPerMinTableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.payPerMinTableView.customContextMenuRequested.connect(self.showCustomContextMenu)

        self.payPerMinModel.itemChanged.connect(self.onCheckboxChanged)
        self.checkedItemRow = 0

        self.refreshPayPerMinTable(self.payPerMin)

        self.payPerMinNightCheckBox.stateChanged.connect(self.showPayPerMinNight)
        self.addNewPayPerMinEntryBtn.clicked.connect(self.addNewPayPerMinEntry)

        self.logoutBtn.clicked.connect(self.logout)

    def refreshPayPerMinTable(self, data):
        self.payPerMinModel.setRowCount(0)
        count = 1
        row = []
        for payPerMin in data:
            idCell = QStandardItem(str(count))
            idCell.setData(payPerMin['id'], Qt.ItemDataRole.UserRole)

            activeCell = QStandardItem()
            activeCell.setCheckable(True)

            if payPerMin['active']:
                activeCell.setCheckState(Qt.CheckState.Checked)
                activeCell.setData('Активно', Qt.ItemDataRole.DisplayRole)
                activeCell.setData(payPerMin['id'], Qt.ItemDataRole.UserRole)
                self.checkedItemRow = count - 1
            else:
                activeCell.setCheckState(Qt.CheckState.Unchecked)
                activeCell.setData('Неактивно', Qt.ItemDataRole.DisplayRole)
                activeCell.setData(payPerMin['id'], Qt.ItemDataRole.UserRole)

            row = [
                idCell,
                QStandardItem(str(payPerMin['valueLeva'])),
                QStandardItem(str(round(payPerMin['valueEUR'], 4))),
                QStandardItem(str(round(payPerMin['levaPerEuro'], 4))),
                activeCell,
                QStandardItem(datetime.strftime(payPerMin['dateActive'], '%d.%m.%Y')),
                QStandardItem(datetime.strftime(payPerMin['lastUpdated'], '%d.%m.%Y')),
                QStandardItem(payPerMin['updatedBy']),
                QStandardItem(payPerMin['comment'])
            ]
            self.payPerMinModel.appendRow(row)
            count += 1

    def clearCheckedPayPerMinCheckbox(self):
        if 0 <= self.checkedItemRow < self.payPerMinModel.rowCount():
            currentItem = self.payPerMinModel.item(self.checkedItemRow, 4)
            if currentItem:
                # Temporarily block signals to prevent recursive calls
                self.payPerMinModel.blockSignals(True)
                currentItem.setCheckState(Qt.CheckState.Unchecked)
                currentItem.setData('Неактивно', Qt.ItemDataRole.DisplayRole)
                self.payPerMinModel.blockSignals(False)

                # Force the view to update this specific cell
                modelIndex = self.payPerMinModel.index(self.checkedItemRow, 4)
                self.payPerMinTableView.update(self.proxyModelPayPerMin.mapFromSource(modelIndex))

        # self.payPerMinModel.blockSignals(False)

    def onCheckboxChanged(self, item):
        # print(item.checkState())
        if item.column() == 4:
            if item.checkState() == Qt.CheckState.Checked:
                if self.checkedItemRow != item.row():
                    currentItemId = self.payPerMinModel.item(
                        self.checkedItemRow, 4).data(Qt.ItemDataRole.UserRole)
                    # self.clearCheckedPayPerMinCheckbox()
                    # self.checkedItemRow = item.row()
                    # item.setCheckState(Qt.CheckState.Checked)
                    # item.setData('Активно', Qt.ItemDataRole.DisplayRole)
                    # # self.checkedItemRow = item.row()
                    itemId = item.data(Qt.ItemDataRole.UserRole)
                    if self.payPerMinNightCheckBox.isChecked():
                        print(itemId, currentItemId)
                        # print(f'Checked item row NIGHT: {self.checkedItemRow}')
                        Ps.updatePayPerMinNight(itemId, currentItemId, self.user)
                        self.payPerMinNight = Ps.getPayPerMin(False)
                        self.refreshPayPerMinTable(self.payPerMinNight)
                        MM.showOnWidget(self, f'Активен платеж за Мин. за нощен труд!', 'success')
                    else:
                        # print(f'Checked item row DAY: {self.checkedItemRow}')
                        Ps.updatePayPerMin(itemId, currentItemId, self.user)
                        self.payPerMin = Ps.getPayPerMin()
                        self.refreshPayPerMinTable(self.payPerMin)
                        MM.showOnWidget(self, f'Активен платеж за Мин.', 'success')
                    # print(self.checkedItemRow)
                # print(f'Checked item row: {self.checkedItemRow}')
            elif item.checkState() == Qt.CheckState.Unchecked:
                if self.checkedItemRow == item.row():
                    self.payPerMinModel.blockSignals(True)
                    item.setCheckState(Qt.CheckState.Checked)
                    item.setData('Активно', Qt.ItemDataRole.DisplayRole)
                    self.payPerMinModel.blockSignals(False)

        # print(item.checkState())
        # if item.column() == 3 and item.checkState() == Qt.CheckState.Unchecked:
        #     print(item.data(Qt.ItemDataRole.UserRole))
        # elif item.column() == 3:
        #     item.setCheckState(Qt.CheckState.Checked)

    def showPayPerMinNight(self):
        if self.payPerMinNightCheckBox.isChecked():
            self.pageTitle.setText("ПЛАЩАНЕ ЗА МИН. НОЩЕН ТРУД")
            self.refreshPayPerMinTable(self.payPerMinNight)
        else:
            self.pageTitle.setText("ПЛАЩАНЕ ЗА МИН.")
            self.refreshPayPerMinTable(self.payPerMin)

    def addNewPayPerMinEntry(self):
        currentLev = float(self.payPerMinModel.item(self.checkedItemRow, 1).data(Qt.ItemDataRole.DisplayRole))
        currentEuro = float(self.payPerMinModel.item(self.checkedItemRow, 2).data(Qt.ItemDataRole.DisplayRole))
        dialog = CustomPayPerTimeDialog(currentLev, currentEuro)
        dialog.newEntryInfo.connect(self.aceptNewPayPerMinEntry)
        dialog.exec_()

    def aceptNewPayPerMinEntry(self, newEntry):
        if self.payPerMinNightCheckBox.isChecked():
            result = Ps.addPayPerMin(self.user, newEntry, False)
            if result:
                self.payPerMinNight = Ps.getPayPerMin(False)
                self.refreshPayPerMinTable(self.payPerMinNight)
        else:
            result = Ps.addPayPerMin(self.user, newEntry, True)
            if result:
                self.payPerMin = Ps.getPayPerMin()
                self.refreshPayPerMinTable(self.payPerMin)

    def showCustomContextMenu(self, position):
        menu = QMenu(self.payPerMinTableView)
        editAction = menu.addAction("Редактиране")
        deleteAction = menu.addAction("Изтриване")
        action = menu.exec_(self.payPerMinTableView.mapToGlobal(position))

        if action == deleteAction:
            selectedRow = self.payPerMinTableView.selectionModel().selectedRows()
            if selectedRow:
                selectedId = self.proxyModelPayPerMin.data(selectedRow[0].siblingAtColumn(0), Qt.ItemDataRole.UserRole)
                selectedName = self.proxyModelPayPerMin.data(selectedRow[0].siblingAtColumn(0),
                                                             Qt.ItemDataRole.DisplayRole)
                selectedLeva = self.proxyModelPayPerMin.data(selectedRow[0].siblingAtColumn(1),
                                                             Qt.ItemDataRole.DisplayRole)
                selectedEuro = self.proxyModelPayPerMin.data(selectedRow[0].siblingAtColumn(2),
                                                             Qt.ItemDataRole.DisplayRole)
                dialog = CustomYesNowDialog()
                message = f'Изтриване на: {selectedName} - лв{selectedLeva} / €{selectedEuro}'
                dialog.setMessage(name='', message=message, mode='deleting')
                result = dialog.exec()
                if result == QDialog.Accepted:
                    if self.payPerMinNightCheckBox.isChecked():
                        if Ps.deletePayPerMin(self.user, selectedId, False):
                            self.payPerMinNight = Ps.getPayPerMin(False)
                            self.refreshPayPerMinTable(self.payPerMinNight)
                            MM.showOnWidget(self, 'Изтриването е успешно!', 'success')
                        else:
                            MM.showOnWidget(self, 'Изтриването не е успешно!', 'error')
                            return
                    else:
                        if Ps.deletePayPerMin(self.user, selectedId):
                            self.payPerMin = Ps.getPayPerMin()
                            self.refreshPayPerMinTable(self.payPerMin)
                            MM.showOnWidget(self, 'Изтриването е успешно!', 'success')
                        else:
                            MM.showOnWidget(self, 'Изтриването не е успешно!', 'error')
                            return

        elif action == editAction:
            print('Edit entry')

    def logout(self):
        self.logoutSignal.emit(True)
