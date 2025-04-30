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
from app.ui.customModelsOperWidget import CustomWidgetForModelOper
from app.ui.customTimePapersWidget import CustomTimePapersWidget
from app.ui.customWorkingShiftsWidget import CustomShiftsEditWidget
from app.ui.customPaymentsWidget import CustomPaymentsWidget
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
        self.defaultModelOperPage = None
        self.modelOperPage = None
        self.timePapersPage = None
        self.workingShiftsPage = None
        self.paymentsPage = None
        # self.setAttribute(Qt.WA_TranslucentBackground)
        LoginPage(self)
        MainMenuPage(self)
        createTable()
        logger.info('Application started')
        windows = ['clients', 'operations']
        self.ui.pageBtn.clicked.connect(lambda: self.changePage(windows))
        self.ui.setDefaultOperBtn.clicked.connect(self.setDefaultOperPage)
        self.ui.setModelsOperBtn.clicked.connect(self.setModelOperPage)
        self.ui.timePapersBtn.clicked.connect(self.setTimePapersPage)
        self.ui.workingShiftsPageBtn.clicked.connect(self.setWorkingShiftsPage)
        self.ui.paymentsPageBtn.clicked.connect(self.setPaymentsPage)
        # MessageManager.success('DefaultOperToModelTypeCustomWidget initialized', timeout=3000)

        # user = UsersFuncs.createUser('test', '000')
        # print(user)

    def resetPaymentsPage(self):
        self.paymentsPage = None

    def resetWorkingShiftsPage(self):
        self.workingShiftsPage = None

    def resetDefaultOperPage(self):
        self.defaultModelOperPage = None

    def resetModelOperPage(self):
        self.modelOperPage = None

    def resetTimePapersPage(self):
        self.timePapersPage = None

    def changePage(self, windows):
        for window in windows:
            subWindow = QMdiSubWindow()
            newWindow = WorkersPageCustomWidget(self, window)
            subWindow.setWidget(newWindow)
            self.ui.mainWindowsArea.addSubWindow(subWindow)
            subWindow.show()

    def setPaymentsPage(self):
        if self.paymentsPage is None:
            self.paymentsPage = CustomPaymentsWidget(self)
            self.paymentsPage.show()
            self.paymentsPage.destroyed.connect(self.resetPaymentsPage)
        else:
            self.paymentsPage.activateWindow()

    def setWorkingShiftsPage(self, initialData=None):
        if self.workingShiftsPage is None:
            self.workingShiftsPage = CustomShiftsEditWidget(self)
            if initialData:
                self.workingShiftsPage.workingShiftsNameLineEdit.setText(initialData[0])
                self.workingShiftsPage.shiftStart.setTime(initialData[1])
                self.workingShiftsPage.shiftEnd.setTime(initialData[2])
            self.workingShiftsPage.show()
            self.workingShiftsPage.destroyed.connect(self.resetWorkingShiftsPage)
        else:
            self.workingShiftsPage.activateWindow()

    def setTimePapersPage(self):
        if self.timePapersPage is None:
            self.timePapersPage = CustomTimePapersWidget(self)
            self.timePapersPage.show()
            self.timePapersPage.destroyed.connect(self.resetTimePapersPage)
        else:
            self.timePapersPage.activateWindow()

    def setDefaultOperPage(self):
        if self.defaultModelOperPage is None:
            self.defaultModelOperPage = DefaultOperToModelTypeCustomWidget(self)
            self.defaultModelOperPage.show()
            self.defaultModelOperPage.destroyed.connect(self.resetDefaultOperPage)
        else:
            self.defaultModelOperPage.activateWindow()

    def setModelOperPage(self):
        if self.modelOperPage is None:
            self.modelOperPage = CustomWidgetForModelOper(self)
            self.modelOperPage.show()
            self.modelOperPage.destroyed.connect(self.resetModelOperPage)
        else:
            self.modelOperPage.activateWindow()




def startUi():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
