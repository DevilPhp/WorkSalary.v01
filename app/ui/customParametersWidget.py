from app.ui.widgets.ui_customParametersWidget import *
from app.models.tableModel import TableModel
from app.services.tableServices import fetchDataFromDbWithRelations
from app.models.sortingModel import CaseInsensitiveProxyModel


class CustomParametersWidget(QWidget, Ui_customParametersWidget):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle('Номенклатури')
        self.mainWindow = mainWindow
        self.proxyModel = None

        self.selectedTable = None

        # self.loadTable('cehove')

        self.cehoveBtn.clicked.connect(lambda: self.btnClicked('cehove', self.cehoveBtn))
        self.machinesBtn.clicked.connect(lambda: self.btnClicked('machines', self.machinesBtn))
        self.workingPosBtn.clicked.connect(lambda: self.btnClicked('workerPositions', self.workingPosBtn))
        self.yarnsBtn.clicked.connect(lambda: self.btnClicked('yarns', self.yarnsBtn))
        self.usersBtn.clicked.connect(lambda: self.btnClicked('users', self.usersBtn))

        self.cehoveBtn.click()

    def btnClicked(self, tableName, btn):
        self.loadTable(tableName)
        self.selectedTable = tableName

        for btns in self.widget_7.findChildren(QPushButton):
            btns.setStyleSheet("")

        btn.setStyleSheet("background-color: #92b1a8;")

        print(self.selectedTable)

    def loadTable(self, tableName):
        self.proxyModel = None
        # print('Fetching data from database...')
        # tableName = 'workerPositions'
        data = fetchDataFromDbWithRelations(tableName)
        # print(data.dtypes)
        model = TableModel(data)
        self.parametersTableView.setModel(model)
        self.proxyModel = CaseInsensitiveProxyModel(numericColumns=[0], parent=self)
        self.setProxyModel(self.proxyModel, model, self.parametersTableView)
        self.proxyModel.dataChanged.connect(self.tableDataChanged)
        # self.parametersTableView.resizeColumnsToContents()
        self.parametersTableView.sortByColumn(0, Qt.SortOrder.DescendingOrder)
        self.parametersTableView.horizontalHeader().setStretchLastSection(True)
        self.parametersTableView.horizontalHeader().setMinimumWidth(80)
        self.parametersTableView.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)

    def setProxyModel(self, proxyModel, model, table):
        proxyModel.setSourceModel(model)
        table.setModel(proxyModel)
        table.setSortingEnabled(True)

    def tableDataChanged(self):
        print(self.selectedTable)
        if self.selectedTable == 'cehove':
            self.updateCehoveTable()

    def updateCehoveTable(self):
        selectedRows = self.parametersTableView.selectionModel().selectedRows()
        print(selectedRows)
