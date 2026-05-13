from functools import partial

from PySide6.QtCore import Signal, QTimer, QRegularExpression
from PySide6.QtGui import QStandardItemModel, QStandardItem, QDoubleValidator, QShortcut, QKeySequence, QIntValidator
from PySide6.QtWidgets import QMenu, QDialog, QAbstractScrollArea

from app.ui.customSortingMenuWidget import CustomSortingMenuWidget
from app.ui.widgets.ui_groupOpersCustomWidget import *
from app.services.groupOperServices import GroupOperationsService as GoS
from app.services.modelServices import ModelService as Ms
from app.models.sortingModel import CaseInsensitiveProxyModel, FilterableHeaderView, CustomInsensitiveTreeProxyModel
from app.models.customTreeView import CustomTreeViewWithDrop
from app.models.tableModel import CustomTableWithDrag
from app.ui.customAddingOpersDialog import CustomAddOperationDialog
from app.ui.customOperTimesDialog import CustomTimeChangeOpersDialog as timeChangeDialog
from app.ui.messagesManager import MessageManager as MM
from app.models.customLineEditWidget import CustomLineEdit
from app.ui.customAddOperationDialog import CustomAddOperationDialog as addOperDialog
from app.ui.customAddingOpersDialog import CustomBranchDialog as branchDialog
from app.ui.customYesNoMessage import CustomYesNowDialog
from app.ui.addingCehoveDialog import CustomWorkingPlaceDialog
from app.utils.utils import Utils


class CustomGroupOperWidget(QWidget, Ui_customWidgetGroupOpers):
    logoutSignal = Signal(bool)
    oldModelsSignal = Signal(bool)

    def __init__(self, mainWindow, user, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle('Модели и операции')
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
        self.clients = {}
        self.models = {}
        self.changedOperTimes = {}
        self.workingPlaces = []
        self.removedOperations = []
        self.existingModelOperations = []
        self.changedModelOperations = {}

        self.clientNameLineEdit.setReadOnly(True)
        self.dateLineEdit.setReadOnly(True)
        self.modelInfoWidget.setEnabled(False)
        self.deleteModelBtn.setVisible(False)
        self.editModelCheckBox.setVisible(False)
        self.operTimesWidget.setVisible(False)

        self.operTreeView = CustomTreeViewWithDrop(self)
        self.operViewWidget.layout().addWidget(self.operTreeView)

        self.operationsTableView = CustomTableWithDrag(self)
        self.operationListViewWidget.layout().addWidget(self.operationsTableView)

        self.searchLineEdit = CustomLineEdit(self)
        self.searchHolderWidget.layout().addWidget(self.searchLineEdit)
        self.searchTreeLineEdit = CustomLineEdit(self)
        self.searchTreeHolderWidget.layout().addWidget(self.searchTreeLineEdit)
        self.modelsNameLineEdit = CustomLineEdit(self)
        self.modelsNameWidget.layout().addWidget(self.modelsNameLineEdit)

        intValidator = QIntValidator(0, 9999999)
        self.piecesLineEdit.setValidator(intValidator)

        self.operTreeViewModel = QStandardItemModel()
        self.operTreeViewModel.setHorizontalHeaderLabels(["Операции", "Време"])
        self.proxyOperTreeView = CustomInsensitiveTreeProxyModel(numericColumns=[1], parent=self)
        self.proxyOperTreeView.setSourceModel(self.operTreeViewModel)
        self.proxyOperTreeView.setSearchColumns([0])
        self.operTreeView.setModel(self.proxyOperTreeView)
        # self.operTreeView.header().hide()
        self.operTreeView.setColumnWidth(0, 500)
        self.operTableViewModel = QStandardItemModel()
        self.tableOperDetailsNames = ['№', 'Операция', 'Вр.']

        for i, tableHeaderName in enumerate(self.tableOperDetailsNames):
            self.operTableViewModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.operTableViewModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            # self.operTableViewModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelOperDetailsTable = CaseInsensitiveProxyModel(numericColumns=[0, 2], parent=self)

        self.setProxyModel(self.proxyModelOperDetailsTable, self.operTableViewModel, self.operationsTableView)
        # self.operationsTableView.horizontalHeader().setStretchLastSection(True)
        self.operationsTableView.setColumnWidth(0, 40)
        self.operationsTableView.setColumnWidth(1, 300)
        self.operationsTableView.setColumnWidth(2, 40)

        self.operationsTableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.operationsTableView.customContextMenuRequested.connect(self.showCustomTableMenu)

        self.operTreeView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.operTreeView.customContextMenuRequested.connect(self.showCustomTreeMenu)

        self.copyTreeShortcut = QShortcut(QKeySequence("Ctrl+C"), self.operTreeView)
        self.copyTreeShortcut.activated.connect(self.copyTreeOperations)

        self.pasteTreeShortcut = QShortcut(QKeySequence("Ctrl+V"), self.operTreeView)
        self.pasteTreeShortcut.activated.connect(self.pasteTreeOperations)

        self.checkBoxFiltering = {}
        self.initialCheckBoxes = {}

        self.operTreeView.dropedOpers.connect(self.dropOpers)
        self.operTreeViewModel.dataChanged.connect(self.updateOperList)
        self._handlingTreeChecks = False
        self.operTreeViewModel.itemChanged.connect(self.handleTreeItemChanged)

        QTimer.singleShot(0, self.loadInitialData)

        self.searchLineEdit.textChanged.connect(self.proxyModelOperDetailsTable.setSearchText)
        # self.searchTreeLineEdit.textChanged.connect(self.proxyOperTreeView.setSearchText)
        self.searchTreeLineEdit.textChanged.connect(self.onTreeSearchTextChanged)

        self.addTypeBtn.clicked.connect(partial(self.addNewBranch, "type"))
        self.addGaugeBtn.clicked.connect(partial(self.addNewBranch, "gauge"))
        self.addGroupBtn.clicked.connect(partial(self.addNewBranch, "group"))
        self.addStructBtn.clicked.connect(partial(self.addNewBranch, "struct"))
        self.newModelCheckBox.stateChanged.connect(self.setNewModel)
        self.editModelCheckBox.stateChanged.connect(self.setEditModel)
        self.oldModelsBtn.clicked.connect(self.loadOldModelsPage)
        self.forClientComboBox.currentIndexChanged.connect(self.updateEditNewCheckboxes)

        self.saveOperTimesBtn.clicked.connect(self.changeOperTimes)
        self.refreshOperTimesBtn.clicked.connect(self.refreshOperTimes)
        self.saveBtn.clicked.connect(self.saveModelWithOperations)
        self.deleteModelBtn.clicked.connect(self.deleteSelectedModel)

        # self.modelNameLineEdit.editingFinished.connect(self.setModelInfo)
        self.cehoveBtn.clicked.connect(self.showWorkingPlacesDialog)
        self.modelsNameLineEdit.editingFinished.connect(self.setModelInfo)

        self.closeBtn.clicked.connect(self.close)
        self.logoutBtn.clicked.connect(self.logout)

    # ------- MODEL OPERATIONS ------- #

    def deleteSelectedModel(self):
        modelName = self.modelsNameLineEdit.text()
        if modelName == "":
            MM.showOnWidget(self, "Моля, изберете модел.", "warning")
            return
        modelId = self.models[modelName]
        dialog = CustomYesNowDialog(isNormalIcon=False)
        dialog.setMessage(modelName, "Искате ли да изтриете модел:", 'deleting')
        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            isDeleted = Ms.deleteModel(modelId, True)
            if isDeleted == 1:
                MM.showOnWidget(self, "Моделът е изтрит успешно.", "success")
                self.loadInitialData(refreshOperTable=False, gettingClients=False)
                self.resetModelInfo()
                self.modelsNameLineEdit.clear()
            elif isDeleted == 2:
                MM.showOnWidget(self, "Моделът не може да бъде изтрит, съществува в листове за време.", "warning")
                return
            else:
                MM.showOnWidget(self, "Грешка при изтриването на модел.", "error")
                return

    def setModelInfo(self):
        modelText = self.modelsNameLineEdit.text()
        if modelText == "":
            self.resetModelInfo()
            self.clearAllTreeChecks()
            return
        if modelText != "":
            if modelText in self.models:
                self.editModelCheckBox.setVisible(True)
                self.deleteModelBtn.setVisible(True)
                modelId = self.models[modelText]
                if modelId:
                    modelData = Ms.getModelInfo(modelId, isNewModel=True)
                    if modelData:
                        self.changedModelOperations.clear()
                        self.updateModelInfo(modelData["model"])
                        self.setExistingModelOperations(modelData["operations"])
                        self.workingPlaces = modelData["workingPlaces"]
            else:
                MM.showOnWidget(self, "Моделът не е намерен.", "warning")

    def setExistingModelOperations(self, operations):
        self.existingModelOperations.clear()
        savedByCatalogId = {
            int(op["catalogListId"]): op
            for op in operations
        }

        try:
            self.clearAllTreeChecks()

            def walk(parentItem):
                for row in range(parentItem.rowCount()):
                    nameitem = parentItem.child(row, 0)
                    timeItem = parentItem.child(row, 1)
                    if nameitem is None:
                        continue
                    nodeType = nameitem.data(Qt.ItemDataRole.UserRole + 1)
                    if nodeType == "operation":
                        catalogId = nameitem.data(Qt.ItemDataRole.UserRole + 2)
                        if catalogId in savedByCatalogId:
                            savedRow = savedByCatalogId[catalogId]
                            nameitem.setCheckState(Qt.CheckState.Checked)

                            if timeItem is not None:
                                savedTime = float(savedRow["time"])
                                currentTime = timeItem.data(Qt.ItemDataRole.UserRole)
                                self.existingModelOperations.append({catalogId: savedTime})
                                if currentTime != savedTime:
                                    self.operTreeView.blockSignals(True)
                                    timeItem.setText(f"{savedTime:.2f}")
                                    timeItem.setData(savedTime, Qt.ItemDataRole.UserRole)
                                    self.operTreeView.blockSignals(False)
                            self.expandParentsForItem(nameitem)
                    if nameitem.hasChildren():
                        walk(nameitem)

            for row in range(self.operTreeViewModel.rowCount()):
                rootItem = self.operTreeViewModel.item(row, 0)
                if rootItem is not None:
                    walk(rootItem)
        finally:
            print("Restoring checkboxes...")

    def updateModelInfo(self, modelData):
        self.modelNameLineEdit.setText(modelData["orderNo"])
        self.clientNameLineEdit.setText(modelData["clientName"])
        self.dateLineEdit.setText(modelData["dateCreated"])
        if modelData["actual"]:
            self.actualCheckBox.setCheckState(Qt.CheckState.Checked)
        if modelData["forProduction"]:
            self.forProdCheckBox.setCheckState(Qt.CheckState.Checked)
        self.piecesLineEdit.setText(str(modelData["pieces"]))
        self.forClientComboBox.setCurrentText(modelData["clientName"])
        if modelData["comment"]:
            self.commentLineEdit.setText(modelData["comment"])

    def updateEditNewCheckboxes(self):
        clientText = self.forClientComboBox.currentText()
        if self.modelsNameLineEdit.text() != "":
            modelName = self.modelsNameLineEdit.text().split(' : ')[0]
            clientName = self.modelsNameLineEdit.text().split(' : ')[1]
            if clientText != clientName:
                self.newModelCheckBox.setCheckState(Qt.CheckState.Checked)
            elif clientText == clientName and modelName == self.modelNameLineEdit.text():
                self.editModelCheckBox.setCheckState(Qt.CheckState.Checked)

    def saveModelWithOperations(self):
        if self.modelNameLineEdit.text() == "":
            MM.showOnWidget(self, "Моля въведете има за модел.", "warning")
            self.modelNameLineEdit.setFocus()
            return

        if self.forClientComboBox.currentText() != '':
            if not self.forClientComboBox.currentText() in self.clients:
                MM.showOnWidget(self, "Няма такъв клиент.", "warning")
                return
        else:
            MM.showOnWidget(self, "Моля изберете клиент.", "warning")
            return

        modelPayload = self.buildModelPayload()
        if not modelPayload:
            MM.showOnWidget(self, "Моля изберете поне една операция.", "warning")
            return

        if self.editModelCheckBox.isChecked():
            if self.removedOperations:
                returnedOperations = Ms.checkIfOperationsCanBeDeleted(modelPayload['model'],
                                                                      self.removedOperations, isNewModel=True)
                if returnedOperations:
                    dialog = CustomYesNowDialog(isNormalIcon=False)
                    message = "Следните операции не могат да бъдат изтрити:\n\n"
                    message = message + "\n".join(op for op in returnedOperations)
                    dialog.yesBtn.setText("Затваряне")
                    dialog.setMessage(modelPayload['model']['modelName'], message, 'warning')
                    dialog.exec()
                    return
            if self.changedModelOperations:
                updatedModel = None
                customDialog = timeChangeDialog(self.changedModelOperations, showEffectModel=False)
                result = customDialog.exec()
                if result == QDialog.DialogCode.Rejected or not result:
                    return
                if result == QDialog.DialogCode.Accepted:
                    if customDialog.effectTPCheckBox.isChecked():
                        currentMonth = customDialog.currentMonth
                        if not Ms.effectTimePapers(modelPayload['model']['modelId'],
                                               currentMonth, self.changedModelOperations):
                            MM.showOnWidget(self, "Грешка при промяна на времената за операции", "error")
                            return
                        updatedModel = Ms.updateSelectedNewModel(modelPayload, self.removedOperations)
            if not updatedModel:
                MM.showOnWidget(self, "Грешка при редактиране на модел.", "error")
                return
            else:
                MM.showOnWidget(self, "Моделът е редактиран успешно.", "success")

        if self.newModelCheckBox.isChecked():
            isExists = Ms.checkIfModelExistsForClient(modelPayload['model']['modelName'],
                                                      modelPayload['model']['clientId'])
            if isExists == 1:
                MM.showOnWidget(self, "Модел с такова име за клиент съществува.", "warning")
                return
            elif not isExists:
                MM.showOnWidget(self, "Грешка при запис на модел.", "error")
                return
            else:
                modelId = Ms.saveNewModel(modelPayload)
                if modelId:
                    MM.showOnWidget(self, f"Модел: {modelPayload['model']['modelName']} е създаден успешно.",
                                    "success")
                else:
                    MM.showOnWidget(self, "Неуспешно създаване на модел.", "error")
                    return
        self.loadInitialData(refreshOperTable=False, gettingClients=False)
        self.resetModelInfo()
        self.modelsNameLineEdit.clear()
        self.editModelCheckBox.setVisible(False)
        self.deleteModelBtn.setVisible(False)
        self.workingPlaces = []
        self.changedModelOperations.clear()
        self.existingModelOperations.clear()

    def buildModelPayload(self):
        pieces = 0
        if self.piecesLineEdit.text() != "":
            pieces = int(self.piecesLineEdit.text())
        yarn = None
        if self.yarnLineEdit.text() != "":
            yarn = self.yarnLineEdit.text().strip()
        comment = None
        if self.commentLineEdit.text() != "":
            comment = self.commentLineEdit.text()
        client = self.forClientComboBox.currentText()
        clientId = self.clients[client]
        modelName = self.modelNameLineEdit.text().strip()
        actual = self.actualCheckBox.isChecked()
        forProduction = self.forProdCheckBox.isChecked()
        modelId = None
        if self.editModelCheckBox.isChecked() and self.modelsNameLineEdit.text() != "":
            name = f"{modelName} : {client}"
            modelId = self.models[name]

        operations = self.getCheckedTreeOperations()
        if not operations:
            return None

        modelData = {
            "modelId": modelId,
            "orderNo": modelId,
            "modelName": modelName,
            "clientId": clientId,
            "actual": actual,
            "forProduction": forProduction,
            "pieces": pieces,
            "yarn": yarn,
            "comment": comment,
            "user": self.user
        }

        payload = {
            "model": modelData,
            "operations": operations,
            "workingPlaces": self.workingPlaces,
        }

        return payload

    def getCheckedTreeOperations(self):
        """
        Walk through the whole tree and collect only checked operation rows.

        Returns:
            list[dict]: one dict per checked operation
        """
        checkedOperations = []

        def walk(parentItem):
            # Go through all child rows of the current parent
            for row in range(parentItem.rowCount()):
                nameItem = parentItem.child(row, 0)
                timeItem = parentItem.child(row, 1)

                if nameItem is None:
                    continue

                nodeType = nameItem.data(Qt.ItemDataRole.UserRole + 1)

                # If this is an operation row, check if it is selected
                if nodeType == "operation":
                    if nameItem.checkState() == Qt.CheckState.Checked:
                        checkedOperations.append({
                            # Id from table newOperations.Id
                            "operationId": nameItem.data(Qt.ItemDataRole.UserRole),

                            # Id from operationCatalogLists.Id
                            "operationCatalogListId": nameItem.data(Qt.ItemDataRole.UserRole + 2),

                            # Visible operation name
                            "operationName": nameItem.text(),

                            # Current time shown in the tree
                            "timeForOper": float(timeItem.data(Qt.ItemDataRole.UserRole) or 0),
                        })

                # Continue deeper if this row has children
                if nameItem.hasChildren():
                    walk(nameItem)

        # Start from the root of the model
        for row in range(self.operTreeViewModel.rowCount()):
            rootItem = self.operTreeViewModel.item(row, 0)
            if rootItem is not None:
                walk(rootItem)

        return checkedOperations

    # ------- TREE OPERATIONS ------- #

    def clearAllTreeChecks(self):
        for row in range(self.operTreeViewModel.rowCount()):
            rootItem = self.operTreeViewModel.item(row, 0)
            if rootItem is not None:
                nodeType = rootItem.data(Qt.ItemDataRole.UserRole + 1)
                if nodeType != "type":
                    continue
                rootItem.setCheckState(Qt.CheckState.Unchecked)
        self.operTreeView.collapseAll()

    def expandParentsForItem(self, item):
        """
        Expand all parents of a source-model item in the tree view.
        """
        current = item.parent()

        while current is not None:
            sourceIndex = self.operTreeViewModel.indexFromItem(current)
            proxyIndex = self.proxyOperTreeView.mapFromSource(sourceIndex)

            if proxyIndex.isValid():
                self.operTreeView.expand(proxyIndex)

            current = current.parent()

    def refreshOperTimes(self):
        self.loadInitialData(refreshOperTable=False, gettingModels=False, gettingClients=False)
        if self.operTimesWidget.isVisible():
            self.changedOperTimes.clear()
            self.operTimesWidget.setVisible(False)

    def changeOperTimes(self):
        customDialog = timeChangeDialog(self.changedOperTimes)
        result = customDialog.exec()
        if result == QDialog.DialogCode.Accepted:
            if customDialog.effectTPCheckBox.isChecked() or customDialog.effectModelsCheckBox.isChecked():
                currentMonth = customDialog.currentMonth
                effectModel = customDialog.effectModelsCheckBox.isChecked()
                effectTimePapers = customDialog.effectTPCheckBox.isChecked()
                if not Ms.effectTimePapersAndModelOperations(currentMonth, self.changedOperTimes,
                                                              effectModel, effectTimePapers):
                    MM.showOnWidget(self, "Грешка при промяна на времената за операции", "error")
                    return
            self.operTimesWidget.setVisible(False)
            if GoS.updateTreeOpersTimes(self.changedOperTimes):
                MM.showOnWidget(self, "Времена за операции са променени успешно", "success")
                if self.operTimesWidget.isVisible():
                    self.changedOperTimes.clear()
                    self.operTimesWidget.setVisible(False)
            else:
                MM.showOnWidget(self, "Грешка при промяна на времена за операции", "error")
                self.loadInitialData(refreshOperTable=False, gettingModels=False, gettingClients=False)
                self.changedOperTimes.clear()
                self.operTimesWidget.setVisible(False)

    def onTreeSearchTextChanged(self, text):
        self.proxyOperTreeView.setSearchText(text)

        if text.strip():
            self.operTreeView.expandToDepth(2)  # or expandAll()
        else:
            self.operTreeView.collapseAll()

    def getNodeType(self, item):
        """
        Returns the custom node type stored in UserRole + 1.
        """
        if item is None:
            return None
        return item.data(Qt.ItemDataRole.UserRole + 1)

    def setItemChecked(self, item, checked):
        """
        Safely sets item checked/unchecked only if needed.
        """
        if item is None or not item.isCheckable():
            return

        newState = Qt.CheckState.Checked if checked else Qt.CheckState.Unchecked
        if item.checkState() != newState:
            item.setCheckState(newState)

    def uncheckOtherTypeItems(self, currentTypeItem):
        """
        Make sure only one top-level 'type' item can stay checked.

        When a new type is checked:
        - all other checked type items become unchecked
        - all their children also become unchecked

        Example:
        If "Жилетка" is checked and the user checks "Пуловер",
        then "Жилетка" and everything under it will be unchecked.
        """
        if currentTypeItem is None:
            return

        # Loop through all top-level rows in the tree model.
        # In your tree, top-level items are the nodeType == "type" items.
        for row in range(self.operTreeViewModel.rowCount()):
            typeItem = self.operTreeViewModel.item(row, 0)

            if typeItem is None:
                continue

            # Skip the currently selected type.
            if typeItem is currentTypeItem:
                continue

            # Safety check: apply this only to nodeType "type".
            if self.getNodeType(typeItem) != "type":
                continue

            # If another type is checked, uncheck it and all children under it.
            if typeItem.checkState() == Qt.CheckState.Checked:
                self.setItemChecked(typeItem, False)
                self.setChildrenCheckedRecursive(typeItem, False)

    def setChildrenCheckedRecursive(self, parentItem, checked):
        """
        Recursively checks/unchecks all children in column 0.
        """
        if parentItem is None:
            return

        for row in range(parentItem.rowCount()):
            childItem = parentItem.child(row, 0)
            if childItem is not None:
                self.setRemovedOperations(childItem, checked)
                self.setItemChecked(childItem, checked)
                self.setChildrenCheckedRecursive(childItem, checked)

    def checkParentsUpward(self, item):
        """
        Checks all parents of the given item.

        Special rule:
        If a parent is nodeType 'type', first uncheck all other type items
        so only one type can stay checked at a time.
        """
        parentItem = item.parent()
        while parentItem is not None:
            if self.getNodeType(parentItem) == "type":
                self.uncheckOtherTypeItems(parentItem)

            self.setItemChecked(parentItem, True)
            parentItem = parentItem.parent()

    def hasCheckedDirectChild(self, parentItem):
        """
        Returns True if parentItem has at least one direct checked child.
        """
        if parentItem is None:
            return False

        for row in range(parentItem.rowCount()):
            childItem = parentItem.child(row, 0)
            if childItem is not None and childItem.checkState() == Qt.CheckState.Checked:
                return True
        return False

    def updateParentsAfterUncheck(self, item):
        """
        Walk upward and uncheck parents that no longer have checked direct children.
        """
        parentItem = item.parent()
        while parentItem is not None:
            if self.hasCheckedDirectChild(parentItem):
                self.setItemChecked(parentItem, True)
            else:
                self.setItemChecked(parentItem, False)
            parentItem = parentItem.parent()

    def checkGaugeFlow(self, gaugeItem):
        """
        Flow for selected gauge:
        - check parent type
        - check all groups except 'Плетене'
        - check all operations under those groups
        - do NOT auto-check structs under 'Плетене'
        """
        if gaugeItem is None:
            return

        # Check type parent
        self.checkParentsUpward(gaugeItem)

        # Check all groups except 'Плетене'
        for row in range(gaugeItem.rowCount()):
            groupItem = gaugeItem.child(row, 0)
            if groupItem is None:
                continue

            groupName = groupItem.text().strip()
            groupNodeType = self.getNodeType(groupItem)

            if groupNodeType != "group":
                continue

            if groupName == "Плетене":
                # Important: do NOT auto-check knitting struct/items here
                continue

            self.setItemChecked(groupItem, True)
            self.setChildrenCheckedRecursive(groupItem, True)

    def checkStructFlow(self, structItem):
        """
        Flow for selected struct under group 'Плетене':
        - check all operations under struct
        - check all parents upward
        """
        if structItem is None:
            return

        self.setChildrenCheckedRecursive(structItem, True)
        self.checkParentsUpward(structItem)

    def handleTypeItem(self, item, checked):
        """
        Type behavior:
        - checked   -> uncheck every other type, so only this one stays checked
        - unchecked -> uncheck everything below it
        """
        if checked:
            # Keep only one checked type in the whole tree.
            self.uncheckOtherTypeItems(item)
        else:
            # If the current type is unchecked, clear everything below it too.
            self.setChildrenCheckedRecursive(item, False)

    def handleGaugeItem(self, item, checked):
        """
        Gauge behavior:
        - checked -> type checked + all groups except 'Плетене' + their operations
        - unchecked -> uncheck everything below gauge and update parents
        """
        if checked:
            self.checkGaugeFlow(item)
        else:
            self.setChildrenCheckedRecursive(item, False)
            self.updateParentsAfterUncheck(item)

    def handleGroupItem(self, item, checked):
        """
        Group behavior:
        - for 'Плетене':
            checked   -> only check parents upward, no auto struct selection
            unchecked -> uncheck all structs/operations under it
        - for other groups:
            checked   -> check all operations under group + parents
            unchecked -> uncheck all operations under group
        """
        groupName = item.text().strip()

        if groupName == "Плетене":
            if checked:
                self.checkParentsUpward(item)
            else:
                self.setChildrenCheckedRecursive(item, False)
                self.updateParentsAfterUncheck(item)
        else:
            if checked:
                self.setChildrenCheckedRecursive(item, True)
                self.checkParentsUpward(item)
            else:
                self.setChildrenCheckedRecursive(item, False)
                self.updateParentsAfterUncheck(item)

    def handleStructItem(self, item, checked):
        """
        Struct behavior:
        - checked -> check all struct operations + all parents
        - unchecked -> uncheck struct operations and update parents
        """
        if checked:
            self.checkStructFlow(item)
        else:
            self.setChildrenCheckedRecursive(item, False)
            self.updateParentsAfterUncheck(item)

    def handleOperationItem(self, item, checked):
        """
        Operation behavior:
        - checked -> check all parents
        - unchecked -> update parents based on remaining checked siblings
        """
        self.setRemovedOperations(item, checked)
        if checked:
            self.checkParentsUpward(item)
        else:
            self.updateParentsAfterUncheck(item)

    def setRemovedOperations(self, item, checked):
        if (self.modelsNameLineEdit.text() != "" and
                item.data(Qt.ItemDataRole.UserRole + 1) == "operation"):
            if checked and item.data(Qt.ItemDataRole.UserRole + 2) in self.removedOperations:
                self.removedOperations.remove(item.data(Qt.ItemDataRole.UserRole + 2))
            elif not checked and item.data(Qt.ItemDataRole.UserRole + 2) not in self.removedOperations:
                self.removedOperations.append(item.data(Qt.ItemDataRole.UserRole + 2))

    def handleTreeItemChanged(self, item):
        """
        Main checkbox logic for the operations tree.

        node types:
        - type
        - gauge
        - group
        - struct
        - оperation   (kept exactly as in your current code)
        """
        if item is None:
            return

        # We only care about first column tree items
        if item.column() != 0:
            return

        nodeType = self.getNodeType(item)
        if nodeType is None:
            return

        if self._handlingTreeChecks:
            return

        checked = item.checkState() == Qt.CheckState.Checked

        self._handlingTreeChecks = True
        try:
            if nodeType == "type":
                self.handleTypeItem(item, checked)

            elif nodeType == "gauge":
                self.handleGaugeItem(item, checked)

            elif nodeType == "group":
                self.handleGroupItem(item, checked)

            elif nodeType == "struct":
                self.handleStructItem(item, checked)

            elif nodeType == "operation":
                self.handleOperationItem(item, checked)

        finally:
            self._handlingTreeChecks = False

    def updateOperList(self, topLeft, bottomRight=None, roles=None):
        """
        Handles editing only for the time column.
        Ignores checkbox changes in column 0.

        Also stores changed operation rows in self.changedOperTimes,
        so later they can be saved when a button is clicked.
        """
        if not topLeft.isValid():
            return

        # Only process the "Време" column
        if topLeft.column() != 1:
            return

        self.operTreeViewModel.blockSignals(True)

        try:
            # Item from edited cell (column 1 = time)
            timeItem = self.operTreeViewModel.itemFromIndex(topLeft)
            if timeItem is None:
                return

            # Get the item from the same row but column 0
            # Example use: operation name / operation id / tree node info
            nameIndex = self.operTreeViewModel.index(topLeft.row(), 0, topLeft.parent())
            nameItem = self.operTreeViewModel.itemFromIndex(nameIndex)
            nodeType = topLeft.parent().data(Qt.ItemDataRole.UserRole + 1)
            firstParent = topLeft.parent()
            secondParent = firstParent.parent()
            thirdParent = secondParent.parent()
            firstParentText = firstParent.data(Qt.ItemDataRole.DisplayRole)
            secondParentText = secondParent.data(Qt.ItemDataRole.DisplayRole)
            thirdParentText = thirdParent.data(Qt.ItemDataRole.DisplayRole)
            if nodeType == "struct":
                forthParent = thirdParent.parent()
                forthParentText = forthParent.data(Qt.ItemDataRole.DisplayRole)
            else:
                forthParent = None
            if nameItem is None:
                return

            currentText = timeItem.text()
            originalValue = timeItem.data(Qt.ItemDataRole.UserRole)

            if currentText:
                normalizedText = currentText.replace(",", ".")
            else:
                normalizedText = currentText

            try:
                numText = float(normalizedText)

                # Validate range like QDoubleValidator(0.01, 999, 2)
                if not (0.01 <= numText <= 999):
                    # Restore old value if input is outside allowed range
                    currentText = f"{originalValue:.2f}"
                else:
                    # If value is changed, format and store it
                    if originalValue is None or numText != float(originalValue):
                        currentText = f"{numText:.2f}"

                        # Save the normalized float in UserRole
                        timeItem.setData(float(currentText), Qt.ItemDataRole.UserRole)
                        # Example:
                        # column 0 item may contain operation name and operation id
                        operName = nameItem.text()
                        operId = nameItem.data(Qt.ItemDataRole.UserRole)

                        if forthParent:
                            key = f"{forthParentText} > {thirdParentText} > {secondParentText} > {firstParentText}"
                        else:
                            key = f"{thirdParentText} > {secondParentText} > {firstParentText}"

                        # Store changed operation in dict
                        # This avoids duplicates if user edits same row more than once
                        catalogListId = timeItem.data(Qt.ItemDataRole.UserRole + 1)

                        operToAdd = {
                                    "operId": operId,
                                    "operName": operName,
                                    "oldTime": originalValue,
                                    "newTime": float(currentText),
                        }

                        for existingOper in self.existingModelOperations:
                            if catalogListId in existingOper:
                                if existingOper[catalogListId] != float(currentText):
                                    if key not in self.changedModelOperations.keys():
                                        self.changedModelOperations[key] = {
                                            catalogListId: operToAdd
                                        }
                                    else:
                                        self.changedModelOperations[key][catalogListId] = operToAdd

                        if key not in self.changedOperTimes.keys():
                            self.changedOperTimes[key] = {
                                catalogListId: operToAdd
                                }
                        else:
                            self.changedOperTimes[key][catalogListId] = operToAdd

                # Set formatted text in the cell
                timeItem.setText(currentText)

            except (ValueError, TypeError):
                # Restore old value if input is invalid
                if originalValue is not None:
                    timeItem.setText(f"{float(originalValue):.2f}")

        finally:
            self.operTreeViewModel.blockSignals(False)
            if not self.operTimesWidget.isVisible():
                self.operTimesWidget.setVisible(True)

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
                self.operTreeViewModel.blockSignals(True)
                self.updateOperation(currentNode, operId, mins)
                self.operTreeViewModel.blockSignals(False)
            else:
                self.appendOperationToBranch(currentNode, operId, mins, operCatalogId)

        if savedOpers:
            MM.showOnWidget(self, f"{len(savedOpers.keys())} операции успешно добавени.", "success")
        else:
            MM.showOnWidget(self, f"{len(savedOpers.keys())} операции неуспешно добавени.", "error")

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
        operName = self.operNamesById[operId][0]
        operNameItem = QStandardItem(operName)
        operNameItem.setData(operId, Qt.ItemDataRole.UserRole)
        operNameItem.setData("operation", Qt.ItemDataRole.UserRole + 1)
        operNameItem.setData(operCatalogId, Qt.ItemDataRole.UserRole + 2)
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

    def addNewBranch(self, nodeType):
        if nodeType:
            self.addBranch(nodeType, None)

    # ----Tree Context Menu Setter---- #

    def copyTreeOperations(self):
        copiedOpers = self.operTreeView.copySelectedOperations()
        if copiedOpers:
            MM.showOnWidget(self, "Операциите са копирани.", "info")
        else:
            MM.showOnWidget(self, "Няма избрани операции за копиране.", "warning")

    def pasteTreeOperations(self):
        pastedOpers = self.operTreeView.pasteOperations()
        if not pastedOpers:
            MM.showOnWidget(self, "Няма копирани операции за поставяне.", "warning")

    def showCustomTreeMenu(self, pos):

        item = self.checkItem(pos)
        nodeType = item.data(Qt.ItemDataRole.UserRole + 1)
        if not nodeType:
            return
        operations = []
        if nodeType == "operation":
            operations = self.getSelectedOperations(item.parent())

        editAction, addAction, deleteAction = self.setCustomMenuActions(nodeType)

        copyAction = None
        pasteAction = None

        menu = QMenu(self)
        addAction = menu.addAction(addAction)
        editAction = menu.addAction(editAction)
        deleteAction = menu.addAction(deleteAction)
        if nodeType == "operation":
            copyAction = menu.addAction("Копиране")

        if nodeType in ("group", "struct"):
            clipboard = QApplication.clipboard()
            mimeData = clipboard.mimeData()
            hasTableData = mimeData.hasFormat("application/x-operations-json")

            pasteAction = menu.addAction("Поставяне")
            pasteAction.setEnabled(hasTableData)

        action = menu.exec_(self.operTreeView.viewport().mapToGlobal(pos))
        if action == addAction:
            self.addBranch(nodeType, item)
        elif action == editAction:
            self.editBranch(nodeType, item)
        elif action == deleteAction:
            self.deleteBranch(nodeType, item, operations)
        elif action == copyAction:
            copiedOpers = self.operTreeView.copySelectedOperations()
            if copiedOpers:
                MM.showOnWidget(self, "Операциите са копирани.", "info")
            else:
                MM.showOnWidget(self, "Няма избрани операции за копиране.", "warning")
        elif action == pasteAction:
            pastedOpers = self.operTreeView.pasteOperations(item)
            if not pastedOpers:
                MM.showOnWidget(self, "Няма копирани операции за поставяне.", "warning")

    def addBranch(self, nodeType, item):
        dialog = branchDialog()
        result = None
        if nodeType == "type":
            dialog.dialogTitle.setText("Добавяне вид")
            result = dialog.exec()
        elif nodeType == "gauge":
            dialog.dialogTitle.setText("Добавяне файн")
            result = dialog.exec()
        elif nodeType == "group":
            dialog.dialogTitle.setText("Добавяне група")
            result = dialog.exec()
        elif nodeType == "struct":
            dialog.dialogTitle.setText("Добавяне структура")
            result = dialog.exec()
        elif nodeType == "operation":
            newOper = {}

            def onOperInfo(operInfo):
                newOper['result'] = self.addNewOper(True, operInfo)

            dialog = addOperDialog(isNewOper=True, operations=self.operations)
            dialog.operInfo.connect(onOperInfo)
            dialog.exec()
            if newOper:
                self.dropOpers([newOper['result'], item.parent()])
            else:
                return
        if result == QDialog.Accepted:
            name = dialog.branchNameLineEdit.text()
            newBranch = GoS.addBranch(nodeType, name)
            if newBranch:
                MM.showOnWidget(self, f"Успешно добавен {name}.", "success")
                self.loadInitialData(refreshOperTable=False, gettingModels=False, gettingClients=False)
            else:
                MM.showOnWidget(self, f"Неуспешно добавен {name}.", "error")

    def editBranch(self, nodeType, item):
        dialog = branchDialog()
        if nodeType == "type":
            dialog.dialogTitle.setText("Редактиране вид")
        elif nodeType == "gauge":
            dialog.dialogTitle.setText("Редактиране файн")
        elif nodeType == "group":
            dialog.dialogTitle.setText("Редактиране група")
        elif nodeType == "struct":
            dialog.dialogTitle.setText("Редактиране структура")
        elif nodeType == "operation":
            operId = item.data(Qt.ItemDataRole.UserRole)
            operName = item.text()
            operNum = self.operNamesById[operId][1]
            operGroupId = int(str(operNum)[0])
            operation = {
                "id": operId,
                "name": operName,
                "groupId": operGroupId,
                "number": operNum
            }
            dialog = addOperDialog(isNewOper=True, oper=operation, operations=self.operations)
            dialog.operInfo.connect(self.updateOper)

        branchName = item.text()
        branchId = item.data(Qt.ItemDataRole.UserRole)
        dialog.branchNameLineEdit.setText(branchName)
        dialog.branchNameLineEdit.setFocus()
        dialog.branchNameLineEdit.selectAll()
        result = dialog.exec()

        if result == QDialog.Accepted:
            newBranchName = dialog.branchNameLineEdit.text()
            updatedBranch = GoS.editBranch(nodeType, branchId, newBranchName)
            if updatedBranch:
                MM.showOnWidget(self, f"Успешно редактиран {updatedBranch['name']}.", "success")
                self.loadInitialData(refreshOperTable=False, gettingModels=False, gettingClients=False)
            else:
                MM.showOnWidget(self, f"Неуспешно редактиран {branchName}.", "error")

    def deleteBranch(self, nodeType, item, operations):
        itemId = item.data(Qt.ItemDataRole.UserRole)
        if nodeType == "type":
            nodeName = "Вид облеко"
        elif nodeType == "gauge":
            nodeName = "Файн"
        elif nodeType == "group":
            nodeName = "Група"
        elif nodeType == "struct":
            nodeName = "Структура"
        else:
            nodeName = "Операция"

        acceptDialog = CustomYesNowDialog(isNormalIcon=False)
        message = f"Изтриване на {nodeName}: "

        if not operations:
            acceptDialog.setMessage(name=item.text(), message=message, mode='deleting')
            result = acceptDialog.exec()
            if result == QDialog.Accepted:
                deletedBranch = GoS.deleteBranch(nodeType, itemId, item.text())
                if deletedBranch:
                    MM.showOnWidget(self, f"Успешно изтрит {nodeName}.", "success")
                    self.loadInitialData(refreshOperTable=False, gettingModels=False, gettingClients=False)
                else:
                    MM.showOnWidget(self, f"Неуспешно изтрит {nodeName}.", "error")
        else:
            name = "\n".join(op["name"] for op in operations)
            acceptDialog.setMessage(name=name, message=message, mode='deleting')
            result = acceptDialog.exec()
            if result == QDialog.Accepted:
                deletedOperations = GoS.deleteSelectedOperationsFromTreeView(operations)
                if deletedOperations:
                    MM.showOnWidget(self, f"Успешно изтрити операции:\n{name}", "success")
                    self.loadInitialData(refreshOperTable=False, gettingModels=False, gettingClients=False)
                else:
                    MM.showOnWidget(self, f"Неуспешно изтрити операции.\n{name}", "error")

    def checkItem(self, pos):
        proxyIndex = self.operTreeView.indexAt(pos)
        if not proxyIndex.isValid():
            return None
        sourceIndex = self.proxyOperTreeView.mapToSource(proxyIndex)
        item = self.operTreeViewModel.itemFromIndex(sourceIndex)
        if item is None:
            return None
        return item

    def getSelectedOperations(self, selectedParent):

        # ---- Make so more then one operations can be deleted at the same time
        indexes = self.operTreeView.selectionModel().selectedIndexes()
        seenKeys = set()
        operations = []
        for index in indexes:
            sourceIndex = self.proxyOperTreeView.mapToSource(index)
            item = self.operTreeViewModel.itemFromIndex(sourceIndex)
            if selectedParent != item.parent():
                continue
            else:
                parent = item.parent()
            row = item.row()
            operId = parent.child(row, 0).data(Qt.ItemDataRole.UserRole)
            catalogId = parent.child(row, 0).data(Qt.ItemDataRole.UserRole + 2)
            operName = parent.child(row, 0).text()
            key = (operId, catalogId)
            if key in seenKeys:
                continue
            seenKeys.add(key)
            operations.append({
                "id": operId,
                "catalogId": catalogId,
                "name": operName,
            })
        return operations

    def setCustomMenuActions(self, nodeType):
        if nodeType == "type":
            editAction = "Редактиране вид"
            addAction = "Добавяне вид"
            deleteAction = "Изтриване вид"
        elif nodeType == "gauge":
            editAction = "Редактиране файн"
            addAction = "Добавяне файн"
            deleteAction = "Изтриване файн"
        elif nodeType == "group":
            editAction = "Редактиране група"
            addAction = "Добавяне група"
            deleteAction = "Изтриване група"
        elif nodeType == "struct":
            editAction = "Редактиране структура"
            addAction = "Добавяне структура"
            deleteAction = "Изтриване структура"
        elif nodeType == "operation":
            editAction = "Редактиране операция"
            addAction = "Добавяне операция"
            deleteAction = "Изтриване операция"
        else:
            editAction = None
            addAction = None
            deleteAction = None

        return editAction, addAction, deleteAction

    # ------- TABLE OPERATIONS ------- #

    def setOperations(self, value):
        self.operTableViewModel.setRowCount(0)
        self.operations.clear()
        self.operNamesById.clear()
        for oper in value:
            self.operations[oper["name"]] = [oper["id"], oper["number"]]
            self.operNamesById[oper["id"]] = [oper["name"], oper["number"]]
            operationName = QStandardItem(oper["name"])
            operationNumber = QStandardItem(str(oper["number"]))
            operationTime = QStandardItem(str(oper["time"]))
            operationName.setData(oper["id"], Qt.ItemDataRole.UserRole)
            operationName.setData("catalogOperation", Qt.ItemDataRole.UserRole + 1)
            operationNumber.setData(oper["id"], Qt.ItemDataRole.UserRole)
            operationTime.setData(oper["time"], Qt.ItemDataRole.UserRole)
            self.operTableViewModel.appendRow([operationNumber, operationName, operationTime])
        self.operationsTableView.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

    # ----Table Context Menu Setter---- #

    def showCustomTableMenu(self, pos):
        menu = QMenu(self)
        addAction = menu.addAction("Добавяне")
        editAction = menu.addAction("Редактиране")
        deleteAction = menu.addAction("Изтриване")

        action = menu.exec_(self.operationsTableView.viewport().mapToGlobal(pos))
        if action == addAction:
            self.addOperation()
        elif action == editAction:
            self.editOperation()
        elif action == deleteAction:
            self.deleteOperation()

    def addOperation(self):
        dialog = addOperDialog(isNewOper=True, operations=self.operations)
        dialog.isInputs.connect(self.checkInputs)
        dialog.operInfo.connect(partial(self.addNewOper, False))
        dialog.exec()

    def editOperation(self):
        selectedItems = self.operationsTableView.selectionModel().selectedRows(1)
        selectedRow = self.proxyModelOperDetailsTable.mapToSource(selectedItems[0]).row()
        operId = self.operTableViewModel.item(selectedRow, 2).data(Qt.ItemDataRole.UserRole)
        operNum = self.operTableViewModel.item(selectedRow, 0).data(Qt.ItemDataRole.DisplayRole)
        operTime = self.operTableViewModel.item(selectedRow, 1).data(Qt.ItemDataRole.DisplayRole)
        operGropId = int(operNum[0])
        selectedOper = self.operNamesById[operId][0]
        operation = {
            "id": operId,
            "name": selectedOper,
            "groupId": operGropId,
            "number": int(operNum),
            "time": operTime
        }
        dialog = addOperDialog(isNewOper=True, oper=operation, operations=self.operations)
        dialog.isInputs.connect(self.checkInputs)
        dialog.operInfo.connect(self.updateOper)
        dialog.exec()

    def checkInputs(self, isInputs):
        if not isInputs:
            MM.showOnWidget(self, "Трябва да въведете входни данни за операцията.", "error")
            return

    def addNewOper(self, isFromBranch, oper):
        addedOper = GoS.addOperation(oper)
        if addedOper:
            operName = addedOper.get("name")
            MM.showOnWidget(self, f"Операцията '{operName}' беше добавена успешно.", "success")
            if isFromBranch:
                self.loadInitialData(refreshTable=True, gettingModels=False, gettingClients=False)
                return [{
                    "id": addedOper.get("id"),
                    "name": operName
                }]
            else:
                self.loadInitialData(gettingModels=False, gettingClients=False)
        else:
            MM.showOnWidget(self, "Добавянето на операцията неуспешно.", "error")
            if isFromBranch:
                return []

    def updateOper(self, oper):
        updateOper = GoS.updateOperation(oper)
        if updateOper:
            operName = updateOper.get("name")
            operId = updateOper.get("id")
            self.loadInitialData(gettingModels=False, gettingClients=False)
            MM.showOnWidget(self, f"Операцията {operId}: '{operName}' беше редактирана успешно.", "success")
        else:
            MM.showOnWidget(self, "Редактирането на операцията неуспешно.", "error")

    def deleteOperation(self):
        operations = []
        selectedItems = self.operationsTableView.selectionModel().selectedRows()

        if not selectedItems:
            return

        for item in selectedItems:
            selectedRow = self.proxyModelOperDetailsTable.mapToSource(item).row()
            operId = self.operTableViewModel.item(selectedRow, 1).data(Qt.ItemDataRole.UserRole)
            operName = self.operTableViewModel.item(selectedRow, 1).data(Qt.ItemDataRole.DisplayRole)
            operations.append({
                "id": operId,
                "name": operName
            })
        if not operations:
            return
        acceptDialog = CustomYesNowDialog(isNormalIcon=False)
        message = f"Изтриване на операция: "
        name = "\n".join(op["name"] for op in operations)
        if len(operations) > 1:
            message = f"Изтриване на операции: "
        acceptDialog.setMessage(name=name, message=message, mode='deleting')
        result = acceptDialog.exec()

        if result == QDialog.Accepted:
            operationsInTreeView = GoS.checkExistingOperationsInTreeView(operations)
            if operationsInTreeView:
                warningDialog = CustomYesNowDialog(isNormalIcon=False)
                message = 'Селектираните операции съществуват в видове модели. Потвърждавате ли да изтриете тези операции?'
                name = "\n".join(op for op in operationsInTreeView)
                warningDialog.setMessage(name=name, message=message, mode='warning')
                warningnResult = warningDialog.exec()
                if warningnResult == QDialog.Accepted:
                    deletedOperations = GoS.deleteSelectedOperationsFromTableView(operations)
                    if deletedOperations:
                        MM.showOnWidget(self, f"Успешно изтрити операции:\n{name}", "success")
                        self.loadInitialData(gettingModels=False, gettingClients=False)
                    else:
                        MM.showOnWidget(self, f"Неуспешно изтрити операции.\n{name}", "error")
            else:
                deletedOperations = GoS.deleteSelectedOperationsFromTableView(operations)
                if deletedOperations:
                    MM.showOnWidget(self, f"Успешно изтрити операции:\n{name}", "success")
                    self.loadInitialData(gettingModels=False, gettingClients=False)
                else:
                    MM.showOnWidget(self, f"Неуспешно изтрити операции.\n{name}", "error")

    # ---- UI Setting ---- #

    def loadOldModelsPage(self):
        self.oldModelsSignal.emit(True)

    def showWorkingPlacesDialog(self):
        modelName = self.modelNameLineEdit.text()
        if modelName == "":
            MM.showOnWidget(self, "Моля, въведете име на модела.", "warning")
            return
        dialog = CustomWorkingPlaceDialog(modelName, self.workingPlaces)
        dialog.workPlaces.connect(self.setWorkingPlaces)
        dialog.exec()

    def setWorkingPlaces(self, workingPlaces):
        self.workingPlaces = workingPlaces

    def setNewModel(self, state):
        if state == 2:
            if self.editModelCheckBox.isChecked():
                self.editModelCheckBox.blockSignals(True)
                self.editModelCheckBox.setCheckState(Qt.CheckState.Unchecked)
                self.editModelCheckBox.blockSignals(False)
            self.modelInfoWidget.setEnabled(True)
            self.actualCheckBox.setCheckState(Qt.CheckState.Checked)
            self.modelNameLineEdit.setReadOnly(False)
        else:
            self.modelInfoWidget.setEnabled(False)
            self.actualCheckBox.setCheckState(Qt.CheckState.Unchecked)
            # self.resetModelInfo()
            # self.clearAllTreeChecks()

    def setEditModel(self, state):
        if state == 2:
            if self.newModelCheckBox.isChecked():
                self.newModelCheckBox.blockSignals(True)
                self.newModelCheckBox.setCheckState(Qt.CheckState.Unchecked)
                self.newModelCheckBox.blockSignals(False)
            self.modelInfoWidget.setEnabled(True)
            self.modelNameLineEdit.setReadOnly(True)
            if self.modelsNameLineEdit.text() == "":
                self.actualCheckBox.setCheckState(Qt.CheckState.Unchecked)
            # self.resetModelInfo(isEdit=True)
        else:
            self.modelInfoWidget.setEnabled(False)
            # self.resetModelInfo()
            # self.clearAllTreeChecks()

    def resetModelInfo(self, isEdit=False):
        self.modelNameLineEdit.clear()
        self.piecesLineEdit.clear()
        self.yarnLineEdit.clear()
        self.commentLineEdit.clear()
        self.actualCheckBox.setCheckState(Qt.CheckState.Unchecked)
        self.forProdCheckBox.setCheckState(Qt.CheckState.Unchecked)
        self.newModelCheckBox.blockSignals(True)
        self.newModelCheckBox.setCheckState(Qt.CheckState.Unchecked)
        self.newModelCheckBox.blockSignals(False)
        if not isEdit:
            self.editModelCheckBox.blockSignals(True)
            self.editModelCheckBox.setCheckState(Qt.CheckState.Unchecked)
            self.editModelCheckBox.blockSignals(False)
        self.clientNameLineEdit.clear()
        self.dateLineEdit.clear()
        self.forClientComboBox.setCurrentIndex(-1)
        self.modelInfoWidget.setEnabled(False)
        self.deleteModelBtn.setVisible(False)
        self.operTimesWidget.setVisible(False)
        self.newModelCheckBox.setCheckState(Qt.CheckState.Unchecked)
        self.editModelCheckBox.setCheckState(Qt.CheckState.Unchecked)
        self.editModelCheckBox.setVisible(False)

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

    def loadInitialData(self, refreshOperTable=True, refreshTable=False, gettingModels=True, gettingClients=True):
        data = GoS.getInitialData()
        if data:
            if not refreshTable:
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
                        if refreshOperTable:
                            self.setOperations(value)
                    elif key == "operCatalog":
                        self.operCatalog = value

                self.setTreeView()
                self.refreshTreeView()
            else:
                for key, value in data.items():
                    if key == "operations":
                        self.setOperations(value)

        if gettingModels:
            self.getModels()

        if gettingClients:
            self.getClients()

    def getClients(self):
        clients = Ms.getClients()
        if clients:
            self.forClientComboBox.clear()
            self.forClientComboBox.setEditable(True)
            for idClient, client in clients.items():
                self.clients[client] = int(idClient)
                self.forClientComboBox.addItem(client)
            self.forClientComboBox.setCurrentIndex(-1)
            Utils.setupCompleter(self.clients.keys(), self.forClientComboBox)

    def getModels(self):
        models = Ms.getNewModelsAndClients()
        if models:
            modelsList = []
            for model in models:
                name = f'{model["orderNo"]} : {model["client"]}'
                modelsList.append(name)
                self.models[name] = model["id"]
            Utils.setupCompleter(modelsList, self.modelsNameLineEdit)

    def setModelTypes(self, value):
        self.typeComboBox.clear()
        self.modelTypes.clear()
        for item in value:
            self.modelTypes[item["name"]] = item["id"]
            self.typeComboBox.addItem(item["name"])

    def setGauges(self, value):
        self.gaugeComboBox.clear()
        self.gauges.clear()
        for item in value:
            self.gauges[item["name"]] = item["id"]
            self.gaugeComboBox.addItem(item["name"])

    def setGroups(self, value):
        self.groupComboBox.clear()
        self.groupsOper.clear()
        for item in value:
            self.groupsOper[item["name"]] = item["id"]
            self.groupComboBox.addItem(item["name"])

    def setStruct(self, value):
        self.structComboBox.clear()
        self.struct.clear()
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
