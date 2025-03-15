import sys
import locale

from app.ui.widgets.ui_MainWindow import *
from app.database import createTable
from app.ui.logInPage import LoginPage


locale.setlocale(locale.LC_TIME, 'bg_BG.utf8')

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.settings = QSettings('Knitex-96', 'WorkSalary_v01')

        # self.widthMinWin, self.heightMinWin = 1200, 750
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Knitex-96 Work Salary")
        # self.setAttribute(Qt.WA_TranslucentBackground)
        LoginPage(self)
        createTable()
        # user = UsersFuncs.createUser('test', '000')
        # print(user)




def startUi():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
