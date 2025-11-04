import sys
import locale
import json
from PySide6.QtCore import QMimeData
from PySide6.QtGui import QClipboard

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
from app.ui.customPaymentsDetailsWidget import CustomPaymentsDetailsWidget
from app.ui.customWorkersWidget import CustomWorkersWidget
from app.ui.messagesManager import MessageManager
from app.ui.customHolidayWidget import CustomHolidaysWidget
from app.ui.customPayPerMinWidget import CustomPayPerMinWidget
from app.ui.customParametersWidget import CustomParametersWidget

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
        self.workersPage = None
        self.holidaysPage = None
        self.payPerMinPage = None
        self.parametersPage = None
        self.workerPaymentsDetails = {}
        self.openedWindows = []
        self.clipboardData = QApplication.clipboard()

        self.user = None
        LoginPage(self)

        MainMenuPage(self)
        createTable()
        logger.info('Application started')
        # windows = ['clients', 'operations']

        # self.ui.pageBtn.clicked.connect(lambda: self.changePage(windows))
        self.ui.setDefaultOperBtn.clicked.connect(self.setDefaultOperPage)
        self.ui.setModelsOperBtn.clicked.connect(self.setModelOperPage)
        self.ui.timePapersBtn.clicked.connect(self.setTimePapersPage)
        self.ui.workingShiftsPageBtn.clicked.connect(self.setWorkingShiftsPage)
        self.ui.paymentsPageBtn.clicked.connect(self.setPaymentsPage)
        self.ui.workersPageBtn.clicked.connect(self.setWorkersPage)
        self.ui.holidaysPageBtn.clicked.connect(self.setHolidaysPage)
        self.ui.payPerMinBtn.clicked.connect(self.setPayPerMinPage)
        self.ui.parametersBtn.clicked.connect(self.setParametersPage)

        self.ui.logoutBtn.clicked.connect(lambda: self.logout(True))

    def closeEvent(self, event):
        QApplication.quit()

    def resetParametersPage(self):
        self.parametersPage = None

    def resetWorkersPage(self):
        self.workersPage = None

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

    def resetHolidaysPage(self):
        self.holidaysPage = None

    def resetPayPerMinPage(self):
        self.payPerMinPage = None

    def removeWorkerPaymentsDetails(self, workerId):
        if workerId in self.workerPaymentsDetails:
            del self.workerPaymentsDetails[workerId]

    def closeAllPaymentsDetails(self):
        for workerId, window in self.workerPaymentsDetails.items():
            window.close()

    def changePage(self, windows):
        for window in windows:
            subWindow = QMdiSubWindow()
            newWindow = WorkersPageCustomWidget(self, window)
            subWindow.setWidget(newWindow)
            self.ui.mainWindowsArea.addSubWindow(subWindow)
            subWindow.show()

    def setParametersPage(self):
        # self.parametersPage = None
        # print(self.parametersPage)
        if self.parametersPage is None:
            # print(self.user)
            self.parametersPage = CustomParametersWidget(self, self.user)
            self.parametersPage.show()
            self.parametersPage.destroyed.connect(self.resetParametersPage)
            self.parametersPage.logoutSignal.connect(self.logout)
        else:
            self.parametersPage.activateWindow()

    def setPayPerMinPage(self):
        if self.payPerMinPage is None:
            self.payPerMinPage = CustomPayPerMinWidget(self, self.user)
            self.payPerMinPage.show()
            self.payPerMinPage.destroyed.connect(self.resetPayPerMinPage)
            self.payPerMinPage.logoutSignal.connect(self.logout)
        else:
            self.payPerMinPage.activateWindow()

    def setHolidaysPage(self):
        if self.holidaysPage is None:
            self.holidaysPage = CustomHolidaysWidget(self, self.user)
            self.holidaysPage.show()
            self.holidaysPage.destroyed.connect(self.resetHolidaysPage)
            self.holidaysPage.logoutSignal.connect(self.logout)
        else:
            self.holidaysPage.activateWindow()

    def setWorkersPage(self):
        if self.workersPage is None:
            self.workersPage = CustomWorkersWidget(self, self.user)
            self.workersPage.show()
            self.workersPage.destroyed.connect(self.resetWorkersPage)
            self.workersPage.logoutSignal.connect(self.logout)
        else:
            self.workersPage.activateWindow()

    def setPaymentsDetailsPage(self, workerId, start, end, totalLeva, totalEuro):
        if workerId not in self.workerPaymentsDetails:
            self.workerPaymentsDetails[workerId] = CustomPaymentsDetailsWidget(self, workerId, start, end,
                                                                               totalLeva, totalEuro, self.user)
            self.workerPaymentsDetails[workerId].show()
            self.workerPaymentsDetails[workerId].destroyed.connect(lambda: self.removeWorkerPaymentsDetails(workerId))
            self.workerPaymentsDetails[workerId].logoutSignal.connect(self.logout)
        else:
            self.workerPaymentsDetails[workerId].activateWindow()

    def setPaymentsPage(self):
        if self.paymentsPage is None:
            self.paymentsPage = CustomPaymentsWidget(self, self.user)
            self.paymentsPage.show()
            self.paymentsPage.destroyed.connect(self.resetPaymentsPage)
            self.paymentsPage.logoutSignal.connect(self.logout)
        else:
            self.paymentsPage.activateWindow()

    def setWorkingShiftsPage(self, initialData=None):
        if self.workingShiftsPage is None:
            self.workingShiftsPage = CustomShiftsEditWidget(self, self.user)
            if initialData:
                self.workingShiftsPage.workingShiftsNameLineEdit.setText(initialData[0])
                self.workingShiftsPage.shiftStart.setTime(initialData[1])
                self.workingShiftsPage.shiftEnd.setTime(initialData[2])
            self.workingShiftsPage.show()
            self.workingShiftsPage.destroyed.connect(self.resetWorkingShiftsPage)
            self.workingShiftsPage.logoutSignal.connect(self.logout)
        else:
            self.workingShiftsPage.activateWindow()

    def setTimePapersPage(self):
        if self.timePapersPage is None:
            self.timePapersPage = CustomTimePapersWidget(self, self.user)
            self.timePapersPage.show()
            self.timePapersPage.destroyed.connect(self.resetTimePapersPage)
            self.timePapersPage.logoutSignal.connect(self.logout)
        else:
            self.timePapersPage.activateWindow()

    def setDefaultOperPage(self):
        if self.defaultModelOperPage is None:
            self.defaultModelOperPage = DefaultOperToModelTypeCustomWidget(self, self.user)
            self.defaultModelOperPage.show()
            self.defaultModelOperPage.destroyed.connect(self.resetDefaultOperPage)
            self.defaultModelOperPage.logoutSignal.connect(self.logout)
        else:
            self.defaultModelOperPage.activateWindow()

    def setModelOperPage(self, isCallingFromOtherWindow=False):
        if self.modelOperPage is None:
            self.modelOperPage = CustomWidgetForModelOper(self, self.user)
            self.modelOperPage.show()
            self.modelOperPage.destroyed.connect(self.resetModelOperPage)
            self.modelOperPage.logoutSignal.connect(self.logout)
            if isCallingFromOtherWindow:
                self.modelOperPage.setWindowsForTimePapersCall()
        else:
            self.modelOperPage.activateWindow()

    def logout(self, signal):
        if signal:
            pages = [
                self.defaultModelOperPage,
                self.modelOperPage,
                self.timePapersPage,
                self.workingShiftsPage,
                self.paymentsPage,
                self.workersPage,
                self.holidaysPage,
                self.payPerMinPage,
                self.parametersPage,
            ]

            pages.extend(self.workerPaymentsDetails.values())

            for page in pages:
                if page is not None:
                    page.close()

            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.userNameField.setText(self.ui.usernameLabel.text())
            self.ui.userPassField.clear()
            self.ui.userNameField.selectAll()
            self.ui.userNameField.setFocus()
            self.user = None
            self.activateWindow()
            MessageManager.showOnWidget(self, f'Изход на {self.ui.usernameLabel.text()}', 'info')
            # MessageManager.info(f'Изход на {self.ui.usernameLabel.text()}', 3000)


def startUi():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
