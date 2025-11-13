# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowlTdYyq.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMdiArea, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1037, 684)
        MainWindow.setMinimumSize(QSize(756, 670))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 600 9pt \"Segoe UI\";\n"
"	color: #324b4c;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: #c9c9c9;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 0px 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #c9c9c9;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #aeaeae;\n"
"}\n"
"\n"
"#logoIcon, #logoIcon_2 {\n"
"	background-color: #dfdfdf;\n"
"	padding: 0px;\n"
"	border: none;\n"
"}\n"
"\n"
"#userLogoLabel, #userPassVisBtn {\n"
"	background-color: #dfdfdf;\n"
"	border: none;\n"
"}\n"
"\n"
"#mainMenuWidget QLabel {\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	max-height: 20px;\n"
"	padding: 3px;\n"
"}\n"
"\n"
"#mainMenuWidget QPushButton {\n"
"	padding: 5px;\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"#label, #label_8 {\n"
"	padding-top: 30px;\n"
"}\n"
"\n"
"#userIcon, #logoutBtn{\n"
"	background-color: #dfdfdf;\n"
"}\n"
"\n"
"#logoutBtn:hover{\n"
"	icon: url(:/icons/app/assets/icons/Log-Out--Streamline-Fea"
                        "ther_#192626.svg);\n"
"}\n"
"\n"
"#usernameLabel {\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.verticalLayout_5 = QVBoxLayout(self.loginPage)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.loginPage)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 160))
        self.widget_2.setMaximumSize(QSize(16777215, 160))
        self.verticalLayout_11 = QVBoxLayout(self.widget_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.logoIcon = QPushButton(self.widget_2)
        self.logoIcon.setObjectName(u"logoIcon")
        self.logoIcon.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/logo/app/assets/logo/KnitexLogo3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logoIcon.setIcon(icon)
        self.logoIcon.setIconSize(QSize(320, 280))

        self.verticalLayout_11.addWidget(self.logoIcon)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.logInHolder = QWidget(self.widget)
        self.logInHolder.setObjectName(u"logInHolder")
        self.logInHolder.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.logInHolder)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.userLogoLabel = QPushButton(self.logInHolder)
        self.userLogoLabel.setObjectName(u"userLogoLabel")
        self.userLogoLabel.setFocusPolicy(Qt.NoFocus)
        self.userLogoLabel.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/User--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userLogoLabel.setIcon(icon1)
        self.userLogoLabel.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.userLogoLabel)

        self.widget_3 = QWidget(self.logInHolder)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 15)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(20)
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.userNameField = QLineEdit(self.widget_3)
        self.userNameField.setObjectName(u"userNameField")
        self.userNameField.setFont(font)
        self.userNameField.setFocusPolicy(Qt.StrongFocus)
        self.userNameField.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.userNameField, 0, 1, 1, 1)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.userPassField = QLineEdit(self.widget_3)
        self.userPassField.setObjectName(u"userPassField")
        self.userPassField.setFocusPolicy(Qt.StrongFocus)
        self.userPassField.setEchoMode(QLineEdit.Password)
        self.userPassField.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.userPassField, 1, 1, 1, 1)

        self.userPassVisBtn = QPushButton(self.widget_3)
        self.userPassVisBtn.setObjectName(u"userPassVisBtn")
        self.userPassVisBtn.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/icons/app/assets/icons/Eye-Off--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/app/assets/icons/Eye--Streamline-Feather.svg", QSize(), QIcon.Selected, QIcon.On)
        self.userPassVisBtn.setIcon(icon2)
        self.userPassVisBtn.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.userPassVisBtn, 1, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.logInHolder)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.loginBtn = QPushButton(self.widget_5)
        self.loginBtn.setObjectName(u"loginBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginBtn.sizePolicy().hasHeightForWidth())
        self.loginBtn.setSizePolicy(sizePolicy)
        self.loginBtn.setMaximumSize(QSize(16777215, 26))
        self.loginBtn.setFont(font)
        self.loginBtn.setFocusPolicy(Qt.NoFocus)
        self.loginBtn.setLayoutDirection(Qt.RightToLeft)
        icon3 = QIcon()
        icon3.addFile(u":/icons/app/assets/icons/Log-In--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.loginBtn.setIcon(icon3)
        self.loginBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_6.addWidget(self.loginBtn)


        self.verticalLayout_3.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.logInHolder, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.footerWidget = QWidget(self.widget)
        self.footerWidget.setObjectName(u"footerWidget")
        self.footerWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.footerWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 5)
        self.footerLabel = QLabel(self.footerWidget)
        self.footerLabel.setObjectName(u"footerLabel")
        self.footerLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.footerLabel)


        self.verticalLayout.addWidget(self.footerWidget, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget.addWidget(self.loginPage)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.horizontalLayout_2 = QHBoxLayout(self.mainPage)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.mainPage)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_9 = QVBoxLayout(self.widget_8)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_10)
        self.widget_13.setObjectName(u"widget_13")

        self.horizontalLayout_6.addWidget(self.widget_13)

        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 160))
        self.widget_12.setMaximumSize(QSize(16777215, 160))
        self.verticalLayout_12 = QVBoxLayout(self.widget_12)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.logoIcon_2 = QPushButton(self.widget_12)
        self.logoIcon_2.setObjectName(u"logoIcon_2")
        self.logoIcon_2.setFocusPolicy(Qt.NoFocus)
        self.logoIcon_2.setIcon(icon)
        self.logoIcon_2.setIconSize(QSize(320, 280))

        self.verticalLayout_12.addWidget(self.logoIcon_2)


        self.horizontalLayout_6.addWidget(self.widget_12, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget_9 = QWidget(self.widget_10)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 5, 0)
        self.logoutBtn = QPushButton(self.widget_9)
        self.logoutBtn.setObjectName(u"logoutBtn")
        self.logoutBtn.setFocusPolicy(Qt.NoFocus)
        icon4 = QIcon()
        icon4.addFile(u":/icons/app/assets/icons/Log-Out--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBtn.setIcon(icon4)
        self.logoutBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_8.addWidget(self.logoutBtn)

        self.userIcon = QPushButton(self.widget_9)
        self.userIcon.setObjectName(u"userIcon")
        self.userIcon.setFocusPolicy(Qt.NoFocus)
        self.userIcon.setIcon(icon1)
        self.userIcon.setIconSize(QSize(18, 18))

        self.horizontalLayout_8.addWidget(self.userIcon)

        self.usernameLabel = QLabel(self.widget_9)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.horizontalLayout_8.addWidget(self.usernameLabel)


        self.horizontalLayout_6.addWidget(self.widget_9, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.widget_10, 0, Qt.AlignTop)

        self.mainMenuWidget = QWidget(self.widget_8)
        self.mainMenuWidget.setObjectName(u"mainMenuWidget")
        self.mainMenuWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_10 = QVBoxLayout(self.mainMenuWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.mainMenuLayout = QGridLayout()
        self.mainMenuLayout.setObjectName(u"mainMenuLayout")
        self.mainMenuLayout.setHorizontalSpacing(30)
        self.mainMenuLayout.setVerticalSpacing(15)
        self.label_7 = QLabel(self.mainMenuWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.mainMenuLayout.addWidget(self.label_7, 0, 3, 1, 1)

        self.label_6 = QLabel(self.mainMenuWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.mainMenuLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_3 = QLabel(self.mainMenuWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.mainMenuLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_2 = QLabel(self.mainMenuWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.mainMenuLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.payPerMinBtn = QPushButton(self.mainMenuWidget)
        self.payPerMinBtn.setObjectName(u"payPerMinBtn")

        self.mainMenuLayout.addWidget(self.payPerMinBtn, 1, 3, 1, 1)

        self.setDefaultOperBtn = QPushButton(self.mainMenuWidget)
        self.setDefaultOperBtn.setObjectName(u"setDefaultOperBtn")
        self.setDefaultOperBtn.setFocusPolicy(Qt.NoFocus)

        self.mainMenuLayout.addWidget(self.setDefaultOperBtn, 2, 2, 1, 1)

        self.setModelsOperBtn = QPushButton(self.mainMenuWidget)
        self.setModelsOperBtn.setObjectName(u"setModelsOperBtn")
        self.setModelsOperBtn.setFocusPolicy(Qt.NoFocus)

        self.mainMenuLayout.addWidget(self.setModelsOperBtn, 1, 2, 1, 1)

        self.paymentsPageBtn = QPushButton(self.mainMenuWidget)
        self.paymentsPageBtn.setObjectName(u"paymentsPageBtn")

        self.mainMenuLayout.addWidget(self.paymentsPageBtn, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.mainMenuWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.mainMenuLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.timePapersBtn = QPushButton(self.mainMenuWidget)
        self.timePapersBtn.setObjectName(u"timePapersBtn")

        self.mainMenuLayout.addWidget(self.timePapersBtn, 1, 0, 1, 1)

        self.workersPageBtn = QPushButton(self.mainMenuWidget)
        self.workersPageBtn.setObjectName(u"workersPageBtn")

        self.mainMenuLayout.addWidget(self.workersPageBtn, 1, 1, 1, 1)

        self.workingShiftsPageBtn = QPushButton(self.mainMenuWidget)
        self.workingShiftsPageBtn.setObjectName(u"workingShiftsPageBtn")

        self.mainMenuLayout.addWidget(self.workingShiftsPageBtn, 3, 1, 1, 1)

        self.holidaysPageBtn = QPushButton(self.mainMenuWidget)
        self.holidaysPageBtn.setObjectName(u"holidaysPageBtn")

        self.mainMenuLayout.addWidget(self.holidaysPageBtn, 2, 3, 1, 1)

        self.parametersBtn = QPushButton(self.mainMenuWidget)
        self.parametersBtn.setObjectName(u"parametersBtn")

        self.mainMenuLayout.addWidget(self.parametersBtn, 3, 3, 1, 1)


        self.verticalLayout_10.addLayout(self.mainMenuLayout)


        self.verticalLayout_9.addWidget(self.mainMenuWidget, 0, Qt.AlignHCenter)

        self.footerWidget_2 = QWidget(self.widget_8)
        self.footerWidget_2.setObjectName(u"footerWidget_2")
        self.horizontalLayout_7 = QHBoxLayout(self.footerWidget_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 5)
        self.footerLabel_2 = QLabel(self.footerWidget_2)
        self.footerLabel_2.setObjectName(u"footerLabel_2")

        self.horizontalLayout_7.addWidget(self.footerLabel_2)


        self.verticalLayout_9.addWidget(self.footerWidget_2, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.widget_8)

        self.stackedWidget.addWidget(self.mainPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.horizontalLayout_4 = QHBoxLayout(self.settingsPage)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.settingsPage)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"QPushButton {\n"
"	padding: 8px;\n"
"	font-size: 10pt;\n"
"	font-weight: 500pt;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_8 = QVBoxLayout(self.widget_7)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pageBtn = QPushButton(self.widget_7)
        self.pageBtn.setObjectName(u"pageBtn")

        self.verticalLayout_8.addWidget(self.pageBtn)


        self.verticalLayout_7.addWidget(self.widget_7, 0, Qt.AlignTop)


        self.horizontalLayout_4.addWidget(self.widget_6)

        self.mainWindowsArea = QMdiArea(self.settingsPage)
        self.mainWindowsArea.setObjectName(u"mainWindowsArea")

        self.horizontalLayout_4.addWidget(self.mainWindowsArea)

        self.stackedWidget.addWidget(self.settingsPage)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoIcon.setText("")
        self.userLogoLabel.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0442\u0440\u0435\u0431\u0438\u0442\u0435\u043b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u0430", None))
        self.userPassVisBtn.setText("")
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u" \u0412\u0425\u041e\u0414", None))
        self.footerLabel.setText(QCoreApplication.translate("MainWindow", u"Author: Filip Chaushev   Dev v0.1.030", None))
        self.logoIcon_2.setText("")
        self.logoutBtn.setText("")
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"admin", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u0438", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0441\u0442\u043e\u0432\u0435 \u0437\u0430 \u0432\u0440\u0435\u043c\u0435", None))
        self.payPerMinBtn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043b\u0430\u0449\u0430\u043d\u0435 \u0437\u0430 \u041c\u0438\u043d", None))
        self.setDefaultOperBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0439 \u043f\u043e \u043f\u043e\u0434\u0440\u0430\u0437\u0431\u0438\u0440\u0430\u043d\u0435", None))
        self.setModelsOperBtn.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u0438 \u0438 \u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.paymentsPageBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.timePapersBtn.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0441\u0442\u043e\u0432\u0435 \u0437\u0430 \u0432\u0440\u0435\u043c\u0435", None))
        self.workersPageBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None))
        self.workingShiftsPageBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438 \u0421\u043c\u0435\u043d\u0438", None))
        self.holidaysPageBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0437\u043d\u0438\u0447\u043d\u0438 \u0414\u043d\u0438", None))
        self.parametersBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0438", None))
        self.footerLabel_2.setText(QCoreApplication.translate("MainWindow", u"Author: Filip Chaushev   Dev v0.1.030", None))
        self.pageBtn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

