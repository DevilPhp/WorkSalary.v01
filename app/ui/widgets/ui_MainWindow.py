# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowYOVPAV.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMdiArea,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1220, 933)
        MainWindow.setMinimumSize(QSize(756, 670))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 700 12pt \"Segoe UI\";\n"
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
"#userLogoLabel, #userPassVisBtn {\n"
"	background-color: #dfdfdf;\n"
"	border: none;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	background-color: #c9c9c9;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #aeaeae;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setPixmap(QPixmap(u":/logo/app/assets/logo/KnitexLogo3.png"))

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.logInHolder = QWidget(self.widget)
        self.logInHolder.setObjectName(u"logInHolder")
        self.logInHolder.setMinimumSize(QSize(0, 300))
        self.verticalLayout_3 = QVBoxLayout(self.logInHolder)
        self.verticalLayout_3.setSpacing(35)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.userLogoLabel = QPushButton(self.logInHolder)
        self.userLogoLabel.setObjectName(u"userLogoLabel")
        self.userLogoLabel.setFocusPolicy(Qt.NoFocus)
        self.userLogoLabel.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/User--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userLogoLabel.setIcon(icon)
        self.userLogoLabel.setIconSize(QSize(80, 80))

        self.verticalLayout_3.addWidget(self.userLogoLabel)

        self.widget_3 = QWidget(self.logInHolder)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(20)
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.userNameField = QLineEdit(self.widget_3)
        self.userNameField.setObjectName(u"userNameField")
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/Eye-Off--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/app/assets/icons/Eye--Streamline-Feather.svg", QSize(), QIcon.Selected, QIcon.On)
        self.userPassVisBtn.setIcon(icon1)
        self.userPassVisBtn.setIconSize(QSize(22, 22))

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
        self.loginBtn.setFocusPolicy(Qt.NoFocus)
        self.loginBtn.setLayoutDirection(Qt.RightToLeft)
        icon2 = QIcon()
        icon2.addFile(u":/icons/app/assets/icons/Log-In--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.loginBtn.setIcon(icon2)
        self.loginBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.loginBtn)


        self.verticalLayout_3.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.logInHolder, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.infoLabel = QLabel(self.widget_4)
        self.infoLabel.setObjectName(u"infoLabel")

        self.horizontalLayout_3.addWidget(self.infoLabel)


        self.verticalLayout.addWidget(self.widget_4, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget.addWidget(self.loginPage)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.horizontalLayout_2 = QHBoxLayout(self.mainPage)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_6 = QWidget(self.mainPage)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"QPushButton {\n"
"	padding: 8px;\n"
"	font-size: 10pt;\n"
"	font-weight: 500pt;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_9 = QPushButton(self.widget_6)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_7.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.widget_6)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_7.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.widget_6)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_7.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.widget_6)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_7.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.widget_6)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_7.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.widget_6)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_7.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.widget_6)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_7.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.widget_6)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_7.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.widget_6)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_7.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.widget_6)

        self.mdiArea = QMdiArea(self.mainPage)
        self.mdiArea.setObjectName(u"mdiArea")
        self.subwindow = QWidget()
        self.subwindow.setObjectName(u"subwindow")
        self.verticalLayout_8 = QVBoxLayout(self.subwindow)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_7 = QWidget(self.subwindow)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_9 = QVBoxLayout(self.widget_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_9.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.tableWidget = QTableWidget(self.widget_7)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 6):
            self.tableWidget.setRowCount(6)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(4, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(5, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(5, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(5, 2, __qtablewidgetitem26)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_9.addWidget(self.tableWidget)

        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_9.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.widget_7)

        self.mdiArea.addSubWindow(self.subwindow)

        self.horizontalLayout_2.addWidget(self.mdiArea)

        self.stackedWidget.addWidget(self.mainPage)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.userLogoLabel.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0442\u0440\u0435\u0431\u0438\u0442\u0435\u043b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u0430", None))
        self.userPassVisBtn.setText("")
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u" \u0412\u0425\u041e\u0414", None))
        self.infoLabel.setText(QCoreApplication.translate("MainWindow", u"Dev v0.1.010", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u0446\u0438", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.subwindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Subwindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"test", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"6", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem9 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"434", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"553", None));
        ___qtablewidgetitem12 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem13 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"42", None));
        ___qtablewidgetitem14 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"423", None));
        ___qtablewidgetitem15 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"33", None));
        ___qtablewidgetitem16 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"23", None));
        ___qtablewidgetitem17 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"234", None));
        ___qtablewidgetitem18 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"44", None));
        ___qtablewidgetitem19 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"34", None));
        ___qtablewidgetitem20 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"132", None));
        ___qtablewidgetitem21 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"55", None));
        ___qtablewidgetitem22 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"34", None));
        ___qtablewidgetitem23 = self.tableWidget.item(4, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"234", None));
        ___qtablewidgetitem24 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"66", None));
        ___qtablewidgetitem25 = self.tableWidget.item(5, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"77", None));
        ___qtablewidgetitem26 = self.tableWidget.item(5, 2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"4312", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

