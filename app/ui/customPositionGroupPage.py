from PySide6.QtCore import Signal, QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem

from app.models.sortingModel import CaseInsensitiveProxyModel
from app.ui.widgets.ui_customPositionGroupWidget import *
from app.models.tableModel import CustomTableViewWithMultiSelection, ButtonDelegation
from app.services.workerServices import WorkerServices as WoS
from app.ui.addingCehoveDialog import CustomWorkingPlaceDialog
from app.ui.messagesManager import MessageManager as MM


class CustomPositionGroupWidget(QWidget, Ui_customPositionGroupWidget):

    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle('Групи към позиции')
        self.mainWindow = mainWindow
        self.postions = {}
        self.currentPositionId = None

        self.positionGroupTableView = CustomTableViewWithMultiSelection(singleSelection=True)
        self.posGroupsTableHolder.layout().addWidget(self.positionGroupTableView)
        self.posGroupsTableModel = QStandardItemModel()

        self.posGroupsTableNames = ['ID', 'Позиция', 'Групи']
        for i, column in enumerate(self.posGroupsTableNames):
            self.posGroupsTableModel.setHorizontalHeaderItem(i, QStandardItem(column))
            self.posGroupsTableModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.proxyModelPosGroups = CaseInsensitiveProxyModel(numericColumns=[0], parent=self)
        self.proxyModelPosGroups.setSourceModel(self.posGroupsTableModel)
        self.positionGroupTableView.setModel(self.proxyModelPosGroups)
        self.positionGroupTableView.setSortingEnabled(True)
        self.proxyModelPosGroups.sort(0, Qt.SortOrder.DescendingOrder)
        self.positionGroupTableView.setColumnWidth(0, 50)
        self.positionGroupTableView.setColumnWidth(1, 250)
        self.positionGroupTableView.setColumnWidth(0, 80)

        self.buttonDelegate = ButtonDelegation("Групи", self.positionGroupTableView)
        self.buttonDelegate.clickedRow.connect(self.handleButtonClick)

        QTimer.singleShot(0, self.refreshPosGroupsTable)

        self.closeBtn.clicked.connect(self.close)

    def handleButtonClick(self, row):
        model = self.positionGroupTableView.model()
        self.currentPositionId = model.index(row, 0).data(Qt.ItemDataRole.UserRole)
        positionName = model.index(row, 1).data(Qt.ItemDataRole.DisplayRole)
        existingGroups = WoS.getGroupsForPosition(self.currentPositionId)
        dialog = CustomWorkingPlaceDialog(positionName, existingGroups, True)
        dialog.workPlaces.connect(self.setGroupsForPosition)
        dialog.exec_()

    def setGroupsForPosition(self, groups):
        result = WoS.addGroupsForPosition(self.currentPositionId, groups)
        if result:
            MM.showOnWidget(self, "Успешно добавени групи към позиция", "success")
        else:
            MM.showOnWidget(self, "Грешка при добавяне на групи към позиция", "error")

    def refreshPosGroupsTable(self):
        workerPositions = WoS.getWorkersPositions()
        if workerPositions:
            self.posGroupsTableModel.setRowCount(0)
            count = 1
            for id, position in workerPositions.items():
                self.postions[int(id)] = position
                idCell = QStandardItem(str(count))
                idCell.setData(int(id), Qt.ItemDataRole.UserRole)

                row = [
                    idCell,
                    QStandardItem(position),
                    QStandardItem()
                ]

                self.posGroupsTableModel.appendRow(row)
                count += 1
            self.positionGroupTableView.setItemDelegateForColumn(2, self.buttonDelegate)

