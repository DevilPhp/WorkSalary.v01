from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QLineEdit, QGraphicsDropShadowEffect
from config import SECRET_LOGIN
from app.ui.messagesManager import MessageManager
from app.services.userServices import UserServices as Us


class LoginPage:
    SECRET_LOGIN = SECRET_LOGIN

    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

        self.setShadowEffect(self.mainWindow.ui.userNameField)
        self.setShadowEffect(self.mainWindow.ui.userPassField)
        self.setShadowEffect(self.mainWindow.ui.loginBtn)

        self.mainWindow.ui.userPassVisBtn.clicked.connect(lambda: self.togglePasswordVisibility())
        self.mainWindow.ui.loginBtn.clicked.connect(self.login)
        self.mainWindow.ui.userPassField.returnPressed.connect(lambda: self.mainWindow.ui.loginBtn.click())
        self.mainWindow.ui.userNameField.returnPressed.connect(self.setUserName)
        # MessageManager.info('DefaultOperToModelTypeCustomWidget initialized', timeout=3000)
        # MessageManager.error('DefaultOperToModelTypeCustomWidget initialized', timeout=2000)
        # print(self.mainWindow)
        # self.mainWindow.ui.userPassField.setVisible(False)
        self.login('new', '000')

    def setUserName(self):
        self.mainWindow.ui.userPassField.selectAll()
        self.mainWindow.ui.userPassField.setFocus()

    def login(self, name=None, passwordNew=None):
        userName = self.mainWindow.ui.userNameField.text()
        password = self.mainWindow.ui.userPassField.text()
        if name and passwordNew:
            userName = name
            password = passwordNew

        if userName == 'admin' and password == self.SECRET_LOGIN:
            self.mainWindow.ui.stackedWidget.setCurrentIndex(1)
            self.mainWindow.ui.usernameLabel.setText(userName)
            self.mainWindow.user = userName
            MessageManager.showOnWidget(self.mainWindow, 'Успешен вход на Админ', 'success')

        elif userName == '':
            MessageManager.showOnWidget(self.mainWindow, 'Моля попълнете потребител', 'error')
            self.mainWindow.ui.userNameField.setFocus()

        elif password == '':
            MessageManager.showOnWidget(self.mainWindow, 'Моля попълнете парола', 'error')
            self.mainWindow.ui.userPassField.setFocus()

        else:
            if Us.loginUser(userName, password):
                self.mainWindow.ui.stackedWidget.setCurrentIndex(1)
                MessageManager.showOnWidget(self.mainWindow, f'Успешен вход на {userName}.', 'success')
                self.mainWindow.ui.usernameLabel.setText(userName)
                self.mainWindow.user = userName
            else:
                MessageManager.showOnWidget(self.mainWindow, 'Невалиден потребител или парола.', 'error')
                if self.mainWindow.ui.userPassField.text() != '':
                    self.mainWindow.ui.userPassField.setFocus()
                    self.mainWindow.ui.userPassField.selectAll()
                elif self.mainWindow.ui.userNameField.text() != '':
                    self.mainWindow.ui.userNameField.setFocus()
                    self.mainWindow.ui.userNameField.selectAll()

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

