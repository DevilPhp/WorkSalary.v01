from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QLineEdit, QGraphicsDropShadowEffect
from config import SECRET_LOGIN
from app.ui.messagesManager import MessageManager


class LoginPage:
    SECRET_LOGIN = SECRET_LOGIN

    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

        self.setShadowEffect(self.mainWindow.ui.userNameField)
        self.setShadowEffect(self.mainWindow.ui.userPassField)
        self.setShadowEffect(self.mainWindow.ui.loginBtn)

        self.mainWindow.ui.userPassVisBtn.clicked.connect(lambda: self.togglePasswordVisibility())
        self.mainWindow.ui.loginBtn.clicked.connect(lambda: self.mainWindow.ui.stackedWidget.setCurrentIndex(1))
        # MessageManager.info('DefaultOperToModelTypeCustomWidget initialized', timeout=3000)
        # MessageManager.error('DefaultOperToModelTypeCustomWidget initialized', timeout=2000)
        # print(self.mainWindow)
        # self.mainWindow.ui.userPassField.setVisible(False)

    def togglePasswordVisibility(self):
        passwordField = self.mainWindow.ui.userPassField
        if passwordField.echoMode() == QLineEdit.EchoMode.Normal:
            passwordField.setEchoMode(QLineEdit.EchoMode.Password)
            self.mainWindow.ui.userPassVisBtn.setIcon(QIcon(":/icons/app/assets/icons/Eye-Off--Streamline-Feather.svg"))
        else:
            passwordField.setEchoMode(QLineEdit.EchoMode.Normal)
            self.mainWindow.ui.userPassVisBtn.setIcon(QIcon(":/icons/app/assets/icons/Eye--Streamline-Feather.svg"))

    def setShadowEffect(self, widget):
        shadow = QGraphicsDropShadowEffect(widget)
        shadow.setBlurRadius(15)
        shadow.setXOffset(2)
        shadow.setYOffset(2)
        shadow.setColor(QColor("#7f7f7f"))
        widget.setGraphicsEffect(shadow)

