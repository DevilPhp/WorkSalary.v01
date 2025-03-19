from numpy import float64

from app.ui.widgets.ui_workersPageCustomWidget import *
from app.models.tableModel import TableModel
from app.services.tableServices import fetchDataFromDbWithRelations
from app.models.sortingModel import CaseInsensitiveProxyModel

class WorkersPageCustomWidget(QWidget, Ui_workersPageWidget):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        title = self.mainWindow.ui.pageBtn.text()
        self.setWindowTitle(title)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.leadData()


    def leadData(self):
        print('Fetching data from database...')
        tableName = 'workerPositions'
        data = fetchDataFromDbWithRelations(tableName)
        print(data.dtypes)
        model = TableModel(data)
        self.tableView.setModel(model)
        self.proxymodelWorkers = CaseInsensitiveProxyModel(numericColumns=[0],
                                                           parent=self)
        self.setProxyModel(self.proxymodelWorkers, model, self.tableView)
        self.tableView.resizeColumnsToContents()
        # self.tableView.setSortingEnabled(True)
        # self.tableView.horizontalHeader().setFont(QFont().setPointSize(13))
        # self.tableView.verticalHeader().setItemDelegate(EmptyDelegate(self.tableView))

    def setProxyModel(self, proxyModel, model, table):
        proxyModel.setSourceModel(model)
        table.setModel(proxyModel)
        table.setSortingEnabled(True)


class EmptyDelegate(QAbstractItemView):
    def paint(self, painter, option, index):
        pass
