from PySide6.QtCore import Signal, QRect, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem

from app.ui.addingCehoveDialog import CustomWorkingPlaceDialog
from app.ui.messagesManager import MessageManager as MM
from app.ui.widgets.ui_customProductionWidget import *
from app.models.tableModel import CustomTableViewWithMultiSelection, ButtonDelegation
from app.models.sortingModel import CaseInsensitiveProxyModel
from app.models.customLineEditWidget import CustomLineEdit
from app.services.modelServices import ModelService as Ms
from app.utils.utils import Utils


class CustomProductionWidget(QWidget, Ui_customProductionWidget):
    logoutSignal = Signal(bool)

    def __init__(self, mainWindow, user, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle('Производство')
        self.usernameLabel.setText(user)
        self.user = user

        self.clientsName = {}
        self.clientModels = None
        self.currentId = None

        self.searchLineEdit = CustomLineEdit()
        self.searchWidget.layout().addWidget(self.searchLineEdit)

        self.productionTableView = CustomTableViewWithMultiSelection(singleSelection=True)
        self.productionTableHolder.layout().addWidget(self.productionTableView)

        self.productionModel = QStandardItemModel()
        self.productionTableHeaderNames = ['ID', 'ПоръчкаNo', 'Активен', 'В Произв.', 'Цехове', 'Файн',
                                           'Статус', 'Бройки', 'Създаден', 'Крайна Дата', 'Коментар']
        for i, header in enumerate(self.productionTableHeaderNames):
            self.productionModel.setHorizontalHeaderItem(i, QStandardItem(header))
            self.productionModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.productionModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.proxyModelProduction = CaseInsensitiveProxyModel(numericColumns=[0, 5, 7], dateColumns=[8, 9], parent=self)
        self.proxyModelProduction.setSourceModel(self.productionModel)
        self.productionTableView.setModel(self.proxyModelProduction)
        self.productionTableView.setSortingEnabled(True)
        self.proxyModelProduction.sort(0, Qt.SortOrder.DescendingOrder)
        self.productionTableView.horizontalHeader().setStretchLastSection(True)
        self.productionTableView.horizontalHeader().setMinimumWidth(80)
        self.productionTableView.setColumnWidth(0, 50)

        self.setUpClientsComboBox()

        self.buttonDelegate = ButtonDelegation("Цехове", self.productionTableView)
        self.buttonDelegate.clickedRow.connect(self.handleButtonClick)

        self.clientsComboBox.currentIndexChanged.connect(self.refreshProductionTable)
        self.oldModelsCheckBox.stateChanged.connect(self.refreshProductionTable)
        # self.yearComboBox.currentIndexChanged.connect(self.refreshProductionTable)
        self.productionModel.itemChanged.connect(self.updateProductionModel)

        self.searchLineEdit.textChanged.connect(self.proxyModelProduction.setSearchText)

        self.posGroupsBtn.clicked.connect(self.openPosGroups)

        self.closeBtn.clicked.connect(self.closeWindows)
        self.logoutBtn.clicked.connect(self.logout)

    def openPosGroups(self):
        self.mainWindow.setPositionGroupsPage()

    def handleButtonClick(self, row):
        model = self.productionTableView.model()
        self.currentId = model.index(row, 0).data(Qt.ItemDataRole.UserRole)
        modelName = model.index(row, 1).data(Qt.ItemDataRole.DisplayRole)
        if self.oldModelsCheckBox.isChecked():
            existingWorkPlaces = Ms.getExistingWorkingPlaces(self.currentId)
        else:
            existingWorkPlaces = Ms.getNewExistingWorkingPlaces(self.currentId)
        dialog = CustomWorkingPlaceDialog(modelName, existingWorkPlaces)
        dialog.workPlaces.connect(self.setWorkingPlaces)
        dialog.exec_()

    def setWorkingPlaces(self, workingPlaces):
        if Ms.addWorkingPlace(self.currentId, workingPlaces, self.oldModelsCheckBox.isChecked()):
            MM.showOnWidget(self, 'Успешно добавени работни места', 'success')
        else:
            MM.showOnWidget(self, 'Грешка при добавяне на работни места', 'error')

    def updateProductionModel(self, item):
        if item.column() == 2:
            if item.checkState() == Qt.CheckState.Checked:
                Ms.updateActualStatus(item.data(Qt.ItemDataRole.UserRole), True)
                item.setData('Активнен', Qt.ItemDataRole.DisplayRole)
            else:
                Ms.updateActualStatus(item.data(Qt.ItemDataRole.UserRole), False)
                item.setData('Неактивнен', Qt.ItemDataRole.DisplayRole)
        elif item.column() == 3:
            if item.checkState() == Qt.CheckState.Checked:
                Ms.setModelProductionStatus(item.data(Qt.ItemDataRole.UserRole), True)
                item.setData('В произв.', Qt.ItemDataRole.DisplayRole)
            else:
                Ms.setModelProductionStatus(item.data(Qt.ItemDataRole.UserRole), False)
                item.setData('Не в произ.', Qt.ItemDataRole.DisplayRole)

    def refreshProductionTable(self):
        if self.clientsComboBox.currentText() != '':
            # year = int(self.yearComboBox.currentText())
            clientId = self.clientsName[self.clientsComboBox.currentText()]
            if self.oldModelsCheckBox.isChecked():
                self.clientModels = Ms.getProductionForClient(clientId)
            else:
                self.clientModels = Ms.getNewProductionForClient(clientId)
        # print(self.clientModels)

        self.productionModel.setRowCount(0)
        count = 1
        # row = []
        if self.clientModels:
            for model, value in self.clientModels.items():
                idCell = QStandardItem(str(count))
                idCell.setData(value[0], Qt.ItemDataRole.UserRole)

                activeCell = QStandardItem()
                activeCell.setCheckable(True)
                inProductionCell = QStandardItem()
                inProductionCell.setCheckable(True)

                if value[1]:
                    activeCell.setCheckState(Qt.CheckState.Checked)
                    activeCell.setData('Активнен', Qt.ItemDataRole.DisplayRole)
                    activeCell.setData(value[0], Qt.ItemDataRole.UserRole)
                else:
                    activeCell.setCheckState(Qt.CheckState.Unchecked)
                    activeCell.setData('Неактивнен', Qt.ItemDataRole.DisplayRole)
                    activeCell.setData(value[0], Qt.ItemDataRole.UserRole)

                if value[2]:
                    inProductionCell.setCheckState(Qt.CheckState.Checked)
                    inProductionCell.setData('В произ.', Qt.ItemDataRole.DisplayRole)
                    inProductionCell.setData(value[0], Qt.ItemDataRole.UserRole)
                else:
                    inProductionCell.setCheckState(Qt.CheckState.Unchecked)
                    inProductionCell.setData('Не в произ.', Qt.ItemDataRole.DisplayRole)
                    inProductionCell.setData(value[0], Qt.ItemDataRole.UserRole)

                row = [
                    idCell,
                    QStandardItem(model),
                    activeCell,
                    inProductionCell,
                    QStandardItem(),
                    QStandardItem(str(value[3])),
                    QStandardItem(str(value[4])),
                    QStandardItem(str(value[5])),
                    QStandardItem(value[6]),
                    QStandardItem(value[7]),
                    QStandardItem(value[8])
                ]

                self.productionModel.appendRow(row)
                count += 1
            self.productionTableView.setItemDelegateForColumn(4, self.buttonDelegate)

    def setUpClientsComboBox(self):
        self.clientsComboBox.clear()
        clients = Ms.getClients()
        for clientId, client in clients.items():
            self.clientsName[client] = int(clientId)

        Utils.setupCompleter(self.clientsName.keys(), self.clientsComboBox)

        sortedClients = sorted(self.clientsName.keys(), key=lambda x: x.lower())
        for client in sortedClients:
            self.clientsComboBox.addItem(client)

        self.clientsComboBox.setCurrentIndex(-1)

    def closeWindows(self):
        if self.mainWindow.posGroupsPage:
            self.mainWindow.posGroupsPage.close()
        self.close()

    def logout(self):
        self.logoutSignal.emit(True)

