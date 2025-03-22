from numpy import float64

from app.ui.widgets.ui_workersPageCustomWidget import *
from app.models.tableModel import TableModel
from app.services.tableServices import fetchDataFromDbWithRelations
from app.models.sortingModel import CaseInsensitiveProxyModel
from app.models.customSelectionModel import SingleMultiSelectionModel

class WorkersPageCustomWidget(QWidget, Ui_workersPageWidget):
    def __init__(self, mainWindow, tableName, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.tableName = tableName
        self.proxyModelWorkers = None
        title = self.mainWindow.ui.pageBtn.text()
        self.setWindowTitle(title)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.loadData()

        selectionModel = SingleMultiSelectionModel(self.tableView.model())
        self.tableView.setSelectionModel(selectionModel)


    def loadData(self):
        print('Fetching data from database...')
        # tableName = 'workerPositions'
        data = fetchDataFromDbWithRelations(self.tableName)
        # print(data.dtypes)
        model = TableModel(data)
        self.tableView.setModel(model)
        self.proxyModelWorkers = CaseInsensitiveProxyModel(numericColumns=[0],
                                                           parent=self)
        self.setProxyModel(self.proxyModelWorkers, model, self.tableView)
        self.tableView.resizeColumnsToContents()
        self.tableView.sortByColumn(0, Qt.SortOrder.AscendingOrder)

    def setProxyModel(self, proxyModel, model, table):
        proxyModel.setSourceModel(model)
        table.setModel(proxyModel)
        table.setSortingEnabled(True)
