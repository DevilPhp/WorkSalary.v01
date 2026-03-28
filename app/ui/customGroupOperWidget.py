from PySide6.QtCore import Signal, QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem, QDoubleValidator
from PySide6.QtWidgets import QMenu, QDialog

from app.ui.widgets.ui_groupOpersCustomWidget import *
from app.services.groupOperServices import GroupOperationsService as GoS
from app.models.sortingModel import CaseInsensitiveProxyModel
from app.models.customTreeView import CustomTreeViewWithDrop, CustomListViewWithDrag


class CustomGroupOperWidget(QWidget, Ui_customWidgetGroupOpers):
    logoutSignal = Signal(bool)

    def __init__(self, mainWindow, user, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.mainWindow = mainWindow
        self.user = user
        self.usernameLabel.setText(user)
        self.operations = {}
        self.modelTypes = {}
        self.gauges = {}
        self.groupsOper = {}
        self.struct = {}

        self.operTreeView = CustomTreeViewWithDrop(self)
        self.operViewWidget.layout().addWidget(self.operTreeView)

        self.operationsListView = CustomListViewWithDrag(self)
        self.operationListViewWidget.layout().addWidget(self.operationsListView)

        self.operTreeViewModel = QStandardItemModel()
        # self.proxyOperTreeView = CaseInsensitiveProxyModel(parent=self)
        # self.proxyOperTreeView.setSourceModel(self.operTreeViewModel)
        self.operTreeView.setModel(self.operTreeViewModel)
        self.operTreeView.header().hide()

        self.operListViewModel = QStandardItemModel()
        self.operationsListView.setModel(self.operListViewModel)

        QTimer.singleShot(0, self.loadInitialData)

        self.closeBtn.clicked.connect(self.close)
        self.logoutBtn.clicked.connect(self.logout)

    def loadInitialData(self):
        data = GoS.getInitialData()
        # print(data)
        if data:
            for key, value in data.items():
                if key == "modelTypes":
                    self.setModelTypes(value)
                elif key == "guages":
                    self.setGauges(value)
                elif key == "groups":
                    self.setGroups(value)
                elif key == "structures":
                    self.setStruct(value)
                elif key == "operations":
                    self.setOperations(value)

        self.setTreeView()

    def setOperations(self, value):
        self.operListViewModel.setRowCount(0)
        for oper in value:
            self.operations[oper["name"]] = oper["id"]
            operation = QStandardItem(oper["name"])
            operation.setData(oper["id"], Qt.ItemDataRole.UserRole)
            self.operListViewModel.appendRow(operation)

    def setModelTypes(self, value):
        for item in value:
            self.modelTypes[item["name"]] = item["id"]
            self.typeComboBox.addItem(item["name"])

    def setGauges(self, value):
        for item in value:
            self.gauges[item["name"]] = item["id"]
            self.gaugeComboBox.addItem(item["name"])

    def setGroups(self, value):
        for item in value:
            self.groupsOper[item["name"]] = item["id"]
            self.groupComboBox.addItem(item["name"])

    def setStruct(self, value):
        for item in value:
            self.struct[item["name"]] = item["id"]
            self.structComboBox.addItem(item["name"])

    def setTreeView(self):
        self.operTreeViewModel.setRowCount(0)
        for modelType, value in self.modelTypes.items():
            item = QStandardItem(modelType)
            item.setCheckable(True)
            item.setData(value, Qt.ItemDataRole.UserRole)
            item.setData("type", Qt.ItemDataRole.UserRole + 1)
            self.operTreeViewModel.appendRow(item)

            for gauge, gaugeId in self.gauges.items():
                gaugeItem = QStandardItem(gauge)
                gaugeItem.setCheckable(True)
                gaugeItem.setData(gaugeId, Qt.ItemDataRole.UserRole)
                gaugeItem.setData("gauge", Qt.ItemDataRole.UserRole + 1)
                item.appendRow(gaugeItem)

                for group, groupId in self.groupsOper.items():
                    groupItem = QStandardItem(group)
                    groupItem.setCheckable(True)
                    groupItem.setData(groupId, Qt.ItemDataRole.UserRole)
                    groupItem.setData("group", Qt.ItemDataRole.UserRole + 1)
                    gaugeItem.appendRow(groupItem)

                    if group == 'Плетене':
                        for struct, structId in self.struct.items():
                            structItem = QStandardItem(struct)
                            structItem.setCheckable(True)
                            structItem.setData(structId, Qt.ItemDataRole.UserRole)
                            structItem.setData("struct", Qt.ItemDataRole.UserRole + 1)
                            groupItem.appendRow(structItem)

    def logout(self):
        self.logoutSignal.emit(True)
