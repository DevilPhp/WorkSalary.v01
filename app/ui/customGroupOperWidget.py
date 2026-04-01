from functools import partial

from PySide6.QtCore import Signal, QTimer, QRegularExpression
from PySide6.QtGui import QStandardItemModel, QStandardItem, QDoubleValidator
from PySide6.QtWidgets import QMenu, QDialog, QAbstractScrollArea

from app.ui.customSortingMenuWidget import CustomSortingMenuWidget
from app.ui.widgets.ui_groupOpersCustomWidget import *
from app.services.groupOperServices import GroupOperationsService as GoS
from app.models.sortingModel import CaseInsensitiveProxyModel, FilterableHeaderView, CustomInsensitiveTreeProxyModel
from app.models.customTreeView import CustomTreeViewWithDrop
from app.models.tableModel import CustomTableWithDrag
from app.ui.customAddingOpersDialog import CustomAddOperationDialog
from app.ui.messagesManager import MessageManager as MM
from app.models.customLineEditWidget import CustomLineEdit


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
        self.operNamesById = {}
        self.modelTypes = {}
        self.gauges = {}
        self.groupsOper = {}
        self.struct = {}
        self.operCatalog = {}

        self.operTreeView = CustomTreeViewWithDrop(self)
        self.operViewWidget.layout().addWidget(self.operTreeView)

        self.operationsTableView = CustomTableWithDrag(self)
        self.operationListViewWidget.layout().addWidget(self.operationsTableView)

        self.searchLineEdit = CustomLineEdit(self)
        self.searchHolderWidget.layout().addWidget(self.searchLineEdit)
        self.searchTreeLineEdit = CustomLineEdit(self)
        self.searchTreeHolderWidget.layout().addWidget(self.searchTreeLineEdit)

        self.operTreeViewModel = QStandardItemModel()
        self.operTreeViewModel.setHorizontalHeaderLabels(["Операции", "Време"])
        self.proxyOperTreeView = CustomInsensitiveTreeProxyModel(numericColumns=[1], parent=self)
        self.proxyOperTreeView.setSourceModel(self.operTreeViewModel)
        self.proxyOperTreeView.setSearchColumns([0])
        self.operTreeView.setModel(self.proxyOperTreeView)
        # self.operTreeView.header().hide()
        self.operTreeView.setColumnWidth(0, 450)
        self.operTreeViewModel.dataChanged.connect(self.updateOperList)

        self.operTableViewModel = QStandardItemModel()

        self.tableOperDetailsNames = ['№', 'Операция']

        for i, tableHeaderName in enumerate(self.tableOperDetailsNames):
            self.operTableViewModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.operTableViewModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            # self.operTableViewModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelOperDetailsTable = CaseInsensitiveProxyModel(numericColumns=[0], parent=self)

        self.setProxyModel(self.proxyModelOperDetailsTable, self.operTableViewModel, self.operationsTableView)
        self.operationsTableView.horizontalHeader().setStretchLastSection(True)
        self.operationsTableView.setColumnWidth(0, 40)

        self.checkBoxFiltering = {}
        self.initialCheckBoxes = {}

        self.operTreeView.dropedOpers.connect(self.dropOpers)

        QTimer.singleShot(0, self.loadInitialData)

        self.searchLineEdit.textChanged.connect(self.proxyModelOperDetailsTable.setSearchText)
        self.searchTreeLineEdit.textChanged.connect(self.proxyOperTreeView.setSearchText)
        self.searchTreeLineEdit.textChanged.connect(self.onTreeSearchTextChanged)
        self.closeBtn.clicked.connect(self.close)
        self.logoutBtn.clicked.connect(self.logout)

    def onTreeSearchTextChanged(self, text):
        self.proxyOperTreeView.setSearchText(text)

        if text.strip():
            self.operTreeView.expandToDepth(2)  # or expandAll()
        else:
            self.operTreeView.collapseAll()

    def setProxyModel(self, proxyModel, model, table):
        proxyModel.setSourceModel(model)
        filterableHeaderView = FilterableHeaderView(Qt.Orientation.Horizontal, table)
        table.setHorizontalHeader(filterableHeaderView)
        filterableHeaderView.filterRequested.connect(partial(self.updateFilter, proxyModel, filterableHeaderView))
        table.setModel(proxyModel)

    def updateFilter(self, proxyModel, header, column):
        if column < 3:
            # Create dictionaries to store column values and checked states if they don't exist
            if not hasattr(self, 'columnValues'):
                self.columnValues = {}
            if not hasattr(self, 'checkedStates'):
                self.checkedStates = {}
            if column not in self.checkBoxFiltering:
                self.checkBoxFiltering[column] = []

            items = []
            self.columnValues[column] = []

            for row in range(proxyModel.rowCount()):
                index = proxyModel.index(row, column)
                value = proxyModel.data(index, Qt.ItemDataRole.DisplayRole)
                if value not in self.columnValues[column]:
                    self.columnValues[column].append(value)
                    if value not in self.initialCheckBoxes:
                        self.initialCheckBoxes[value] = column

            for value in self.columnValues[column]:
                items.append(value)

            if items:
                menu = CustomSortingMenuWidget(header)
                for item in items:
                    checked = item in self.checkBoxFiltering[column]
                    menu.addItem(item, checked)
                menu.setMenuSize(len(items))
                menu.move(self.cursor().pos())
                menu.checkedCheckbox.connect(partial(self.applyFilter, proxyModel))

    def applyFilter(self, proxyModel, item):
        col = self.initialCheckBoxes[item.text()]
        if item.isChecked() and item.text() not in self.checkBoxFiltering[col]:
            self.checkBoxFiltering[col].append(item.text())
        elif not item.isChecked() and item.text() in self.checkBoxFiltering[col]:
            self.checkBoxFiltering[col].remove(item.text())

        if not self.checkBoxFiltering[col]:
            if col in proxyModel.columnFilters:
                del proxyModel.columnFilters[col]
        else:
            proxyModel.setFilterForColumn(col, self.checkBoxFiltering)
        proxyModel.invalidateFilter()

    def updateOperList(self, data):
        self.operTreeViewModel.blockSignals(True)
        selectedItem = self.operTreeViewModel.itemFromIndex(data)
        currentText = selectedItem.text()
        originalValue = selectedItem.data(Qt.ItemDataRole.UserRole)
        try:
            numText = float(currentText)
            if not (0.01 <= numText <= 999):
                currentText = f"{originalValue:.2f}"
            else:
                if currentText != str(originalValue):
                    currentText = f"{numText:.2f}"
                    selectedItem.setData(float(currentText), Qt.ItemDataRole.UserRole)
            selectedItem.setText(currentText)
        except (ValueError, TypeError):
            selectedItem.setText(str(originalValue))
        self.operTreeViewModel.blockSignals(False)

    def dropOpers(self, items):
        firstParent = items[1].parent()
        secondParent = firstParent.parent()
        if firstParent.text() == "Плетене":
            thirdParent = secondParent.parent()
        else:
            thirdParent = None
        dialog = CustomAddOperationDialog(items[0], items[1], firstParent, secondParent, thirdParent)
        dialog.emitedData.connect(self.addOperations)
        dialog.exec_()

    def addOperations(self, data):
        """
            Called after the custom dialog returns operation times.
            Adds operations under the selected branch and then saves them to DB.
        """
        currentNode = data.get("currentNode", None)
        operList = data.get("operList", [])

        if not currentNode or not operList:
            return

        savedOpers = self.saveOperationsToDB(data)
        for oper in operList:
            operId = oper["id"]
            mins = oper["mins"]
            operCatalogId = savedOpers[str(operId)]
            existingOper = self.checkCurrentNodeOpers(currentNode, operId)
            if existingOper:
                self.updateOperation(currentNode, operId, mins)
            else:
                self.appendOperationToBranch(currentNode, operId, mins, operCatalogId)
        if savedOpers:
            MM.showOnWidget(self, f"{len(savedOpers.keys())} операции успешно добавени.", "success")
        else:
            MM.showOnWidget(self, f"{len(savedOpers.keys())} операции неуспешно добавени.", "error")

    def saveOperationsToDB(self, data):
        row = self.setRowsForDb(data)
        return GoS.saveOperationsToDB(row)

    def setRowsForDb(self, data):
        row = {
            "parentList": {
                "ModelTypeId": data["parentList"][0]["id"],
                "GaugeId": data["parentList"][1]["id"],
                "GroupId": data["parentList"][2]["id"],
                "StructureId": data["parentList"][3]["id"] if len(data["parentList"]) > 3 else None,
                "UserCreated": self.user
            },
            "operList": data.get("operList", [])
        }
        return row

    def checkCurrentNodeOpers(self, currentNode, operId):
        for row in range(currentNode.rowCount()):
            item = currentNode.child(row, 0)
            if item.data(Qt.ItemDataRole.UserRole) == operId:
                return True
        return False

    def findBranchItem(self, parentList):
        """
            Finds the exact tree item where operations should be attached.

            parentList comes from the dialog and contains the hierarchy:
            type -> gauge -> group -> optional struct
        """

        if not parentList:
            return None

        firstParent = None
        secondParent = None
        thirdParent = None
        currentParent = None
        model = self.operTreeViewModel
        for level in parentList:
            levelId = level["id"]
            levelType = level["nodeType"]
            if levelType == "type":
                for row in range(model.rowCount()):
                    item = model.item(row, 0)
                    if item.data(Qt.ItemDataRole.UserRole) == levelId:
                        firstParent = item
                        break
            if levelType == "gauge":
                for row in range(firstParent.rowCount()):
                    item = firstParent.child(row, 0)
                    if item.data(Qt.ItemDataRole.UserRole) == levelId:
                        secondParent = item
                        break
            if levelType == "group":
                for row in range(secondParent.rowCount()):
                    item = secondParent.child(row, 0)
                    if item.data(Qt.ItemDataRole.UserRole) == levelId:
                        thirdParent = item
                        currentParent = item
                        break
            if levelType == "struct":
                for row in range(thirdParent.rowCount()):
                    item = thirdParent.child(row, 0)
                    if item.data(Qt.ItemDataRole.UserRole) == levelId:
                        currentParent = item
                        break
        return currentParent

    def appendOperationToBranch(self, branchItem, operId, mins, operCatalogId):
        operName = self.operNamesById[operId]
        operNameItem = QStandardItem(operName)
        operNameItem.setData(operId, Qt.ItemDataRole.UserRole)
        operNameItem.setData("оperation", Qt.ItemDataRole.UserRole + 1)
        operNameItem.setEditable(False)
        operNameItem.setCheckable(True)
        operMins = QStandardItem(f'{mins:.2f}')
        operMins.setData(mins, Qt.ItemDataRole.UserRole)
        operMins.setData(operCatalogId, Qt.ItemDataRole.UserRole + 1)

        branchItem.appendRow([operNameItem, operMins])

    def updateOperation(self, branchItem, operId, mins):
        for row in range(branchItem.rowCount()):
            item = branchItem.child(row, 0)
            if item.data(Qt.ItemDataRole.UserRole) == operId:
                branchItem.child(row, 1).setText(f'{mins:.2f}')
                branchItem.child(row, 1).setData(mins, Qt.ItemDataRole.UserRole)
                break

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
                elif key == "operCatalog":
                    self.operCatalog = value

        self.setTreeView()
        self.refreshTreeView()

    def setOperations(self, value):
        self.operTableViewModel.setRowCount(0)
        for oper in value:
            self.operations[oper["name"]] = oper["id"]
            self.operNamesById[oper["id"]] = oper["name"]
            operationName = QStandardItem(oper["name"])
            operationNumber = QStandardItem(str(oper["number"]))
            operationName.setData(oper["id"], Qt.ItemDataRole.UserRole)
            operationName.setData("catalogOperation", Qt.ItemDataRole.UserRole + 1)
            operationNumber.setData(oper["id"], Qt.ItemDataRole.UserRole)
            self.operTableViewModel.appendRow([operationNumber, operationName])
        self.operationsTableView.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

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
            item.setEditable(False)
            self.operTreeViewModel.appendRow(item)

            for gauge, gaugeId in self.gauges.items():
                gaugeItem = QStandardItem(gauge)
                gaugeItem.setCheckable(True)
                gaugeItem.setData(gaugeId, Qt.ItemDataRole.UserRole)
                gaugeItem.setData("gauge", Qt.ItemDataRole.UserRole + 1)
                gaugeItem.setEditable(False)
                item.appendRow(gaugeItem)

                for group, groupId in self.groupsOper.items():
                    groupItem = QStandardItem(group)
                    groupItem.setCheckable(True)
                    groupItem.setData(groupId, Qt.ItemDataRole.UserRole)
                    groupItem.setData("group", Qt.ItemDataRole.UserRole + 1)
                    groupItem.setEditable(False)
                    gaugeItem.appendRow(groupItem)

                    if group == 'Плетене':
                        for struct, structId in self.struct.items():
                            structItem = QStandardItem(struct)
                            structItem.setCheckable(True)
                            structItem.setData(structId, Qt.ItemDataRole.UserRole)
                            structItem.setData("struct", Qt.ItemDataRole.UserRole + 1)
                            structItem.setEditable(False)
                            groupItem.appendRow(structItem)

    def refreshTreeView(self):
        for row in self.operCatalog:
            parentList = row["parentList"]
            if parentList:
                branchItem = self.findBranchItem(parentList)
                if branchItem:
                    for oper in row["operList"]:
                        self.appendOperationToBranch(branchItem, oper["id"], oper["mins"], oper["operCatalogListId"])

    def logout(self):
        self.logoutSignal.emit(True)
