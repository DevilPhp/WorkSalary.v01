# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customClientsWidgetWOhThX.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import resources_rc

class Ui_customClientsWidget(object):
    def setupUi(self, customClientsWidget):
        if not customClientsWidget.objectName():
            customClientsWidget.setObjectName(u"customClientsWidget")
        customClientsWidget.resize(900, 800)
        customClientsWidget.setMinimumSize(QSize(900, 800))
        customClientsWidget.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 600 12pt \"Segoe UI\";\n"
"	color: #324b4c;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"        width: 20px;\n"
"        background: none;\n"
"    }\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"        background: #dfdfdf;\n"
"    }\n"
"\n"
"QPushButton {\n"
"	background-color: #c9c9c9;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-size: 12pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #aeaeae;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"QStandartItem{\n"
"	\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"QLineEdit, QDateEdit{\n"
"	border: none;\n"
"	font-size: 11pt;\n"
"	border-bottom: 1px solid #7c9399;\n"
"}\n"
"\n"
"QMenu {\n"
"	border: 1px solid #aeaeae;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"	background-color: #aeaeae;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"#pageTitle {\n"
"	font: 700 13"
                        "pt \"Segoe UI\";\n"
"}\n"
"\n"
"#userIcon, #logoutBtn{\n"
"	background-color: #dfdfdf;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"#logoutBtn:hover{\n"
"	icon: url(:/icons/app/assets/icons/Log-Out--Streamline-Feather_#192626.svg);\n"
"}\n"
"\n"
"#usernameLabel {\n"
"	font-size: 11pt;\n"
"}")
        self.verticalLayout = QVBoxLayout(customClientsWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(customClientsWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.headerHolder = QWidget(self.widget)
        self.headerHolder.setObjectName(u"headerHolder")
        self.horizontalLayout = QHBoxLayout(self.headerHolder)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.headerHolder)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.widget_4, 0, Qt.AlignLeft)

        self.pageTitle = QLabel(self.headerHolder)
        self.pageTitle.setObjectName(u"pageTitle")

        self.horizontalLayout.addWidget(self.pageTitle, 0, Qt.AlignHCenter)

        self.userHolder = QWidget(self.headerHolder)
        self.userHolder.setObjectName(u"userHolder")
        self.horizontalLayout_3 = QHBoxLayout(self.userHolder)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 5, 0)
        self.logoutBtn = QPushButton(self.userHolder)
        self.logoutBtn.setObjectName(u"logoutBtn")
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Log-Out--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBtn.setIcon(icon)
        self.logoutBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.logoutBtn)

        self.userIcon = QPushButton(self.userHolder)
        self.userIcon.setObjectName(u"userIcon")
        self.userIcon.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/User--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userIcon.setIcon(icon1)
        self.userIcon.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.userIcon)

        self.usernameLabel = QLabel(self.userHolder)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.horizontalLayout_3.addWidget(self.usernameLabel)


        self.horizontalLayout.addWidget(self.userHolder, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.headerHolder)

        self.addNewClientBtn = QPushButton(self.widget)
        self.addNewClientBtn.setObjectName(u"addNewClientBtn")

        self.verticalLayout_4.addWidget(self.addNewClientBtn, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(customClientsWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 888, 712))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.clientsTableHolder = QWidget(self.scrollAreaWidgetContents)
        self.clientsTableHolder.setObjectName(u"clientsTableHolder")
        self.verticalLayout_11 = QVBoxLayout(self.clientsTableHolder)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 0)
        self.clientsTableView = QTableView(self.clientsTableHolder)
        self.clientsTableView.setObjectName(u"clientsTableView")
        self.clientsTableView.setStyleSheet(u"QHeaderView:section{\n"
"	font: 700 10.5pt \"Segoe UI\";\n"
"	background-color: #dfdfdf;\n"
"	padding: 5px;\n"
"}\n"
"QVerticalView:section{\n"
"	min-height: 30;\n"
"}\n"
"QAbstractItemView{\n"
"	alternate-background-color: #d3d3d3;\n"
"	font: 10.5pt \"Segoe UI\";\n"
"	selection-background-color: rgba(198, 228, 254, 45);\n"
"	selection-color: #324b4c;\n"
"	focus: none;\n"
"}\n"
"QAbstractItemView:item{\n"
"	selection-background-color: rgba(198, 228, 254, 45);\n"
"	selection-color: #324b4c;\n"
"	focus: none;\n"
"}\n"
"QAbstractItemView::item:selected{\n"
"	background-color: rgba(198, 228, 254, 45);\n"
"}")
        self.clientsTableView.setAlternatingRowColors(True)
        self.clientsTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.clientsTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.clientsTableView.setShowGrid(False)
        self.clientsTableView.setCornerButtonEnabled(False)
        self.clientsTableView.verticalHeader().setVisible(False)

        self.verticalLayout_11.addWidget(self.clientsTableView)


        self.verticalLayout_12.addWidget(self.clientsTableHolder)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(customClientsWidget)

        QMetaObject.connectSlotsByName(customClientsWidget)
    # setupUi

    def retranslateUi(self, customClientsWidget):
        customClientsWidget.setWindowTitle(QCoreApplication.translate("customClientsWidget", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("customClientsWidget", u"\u041a\u041b\u0418\u0415\u041d\u0422\u0418", None))
        self.logoutBtn.setText("")
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customClientsWidget", u"admin", None))
        self.addNewClientBtn.setText(QCoreApplication.translate("customClientsWidget", u"\u0414\u043e\u0431\u0430\u0432\u044f\u043d\u0435", None))
    # retranslateUi

