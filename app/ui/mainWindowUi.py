import sys
import locale

from app.logger import logger
from PySide6.QtWidgets import QMdiSubWindow

from app.ui.widgets.ui_MainWindow import *
from app.database import createTable
from app.ui.logInPage import LoginPage
from app.ui.mainMenuPage import MainMenuPage
from app.ui.workersPage import WorkersPageCustomWidget
from app.ui.customWidgetForDefaultOper import DefaultOperToModelTypeCustomWidget
from app.ui.messagesManager import MessageManager



locale.setlocale(locale.LC_TIME, 'bg_BG.utf8')

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.settings = QSettings('Knitex-96', 'WorkSalary_v01')

        # self.widthMinWin, self.heightMinWin = 1200, 750
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Knitex-96 Work Salary")
        MessageManager.initialize(self)
        self.newWidget = None
        # self.setAttribute(Qt.WA_TranslucentBackground)
        LoginPage(self)
        MainMenuPage(self)
        createTable()
        logger.info('Application started')
        windows = ['clients', 'operations']
        self.ui.pageBtn.clicked.connect(lambda: self.changePage(windows))
        self.ui.setDefaultOperBtn.clicked.connect(lambda: self.setDefaultOper())

        # user = UsersFuncs.createUser('test', '000')
        # print(user)

    def changePage(self, windows):
        for window in windows:
            subWindow = QMdiSubWindow()
            newWindow = WorkersPageCustomWidget(self, window)
            subWindow.setWidget(newWindow)
            self.ui.mainWindowsArea.addSubWindow(subWindow)
            subWindow.show()

    def setDefaultOper(self):
        self.newWidget = DefaultOperToModelTypeCustomWidget(self)
        self.newWidget.show()




def startUi():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
