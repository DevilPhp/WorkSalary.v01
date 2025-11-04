# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customParametersWidgetQHLpCE.ui'
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

class Ui_customParametersWidget(object):
    def setupUi(self, customParametersWidget):
        if not customParametersWidget.objectName():
            customParametersWidget.setObjectName(u"customParametersWidget")
        customParametersWidget.resize(900, 800)
        customParametersWidget.setMinimumSize(QSize(900, 800))
        customParametersWidget.setStyleSheet(u"*{\n"
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
"	font-size: 10pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #aeaeae;\n"
"}\n"
"\n"
"QDateEdit::up-button, QDateEdit::down-button{\n"
"	width: 0px;\n"
"}\n"
"\n"
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
"yearsBtnsHolder QPushButton:clicked {\n"
"	background-color: black;\n"
"}\n"
""
                        "\n"
"#optionsHolder, #optionsHolder_2 {\n"
"	border-bottom: 2px dashed #7c9399;\n"
"}\n"
"\n"
"#pageTitle {\n"
"	font: 700 13pt \"Segoe UI\";\n"
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
"\n"
"#usernameLabel {\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"#workerPlaceLineEdit, #workerPositionLineEdit {\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"#widget_3 * {\n"
"	font-size: 11pt;\n"
"}")
        self.verticalLayout = QVBoxLayout(customParametersWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(customParametersWidget)
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

        self.parametersInfoHolder = QWidget(self.widget)
        self.parametersInfoHolder.setObjectName(u"parametersInfoHolder")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parametersInfoHolder.sizePolicy().hasHeightForWidth())
        self.parametersInfoHolder.setSizePolicy(sizePolicy)
        self.parametersInfoHolder.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_5 = QHBoxLayout(self.parametersInfoHolder)
        self.horizontalLayout_5.setSpacing(35)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 5)
        self.parametersHolder = QWidget(self.parametersInfoHolder)
        self.parametersHolder.setObjectName(u"parametersHolder")
        self.parametersHolder.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.parametersHolder)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.parametersHolder)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.clientsBtn = QPushButton(self.widget_7)
        self.clientsBtn.setObjectName(u"clientsBtn")

        self.horizontalLayout_4.addWidget(self.clientsBtn)

        self.cehoveBtn = QPushButton(self.widget_7)
        self.cehoveBtn.setObjectName(u"cehoveBtn")

        self.horizontalLayout_4.addWidget(self.cehoveBtn)

        self.machinesBtn = QPushButton(self.widget_7)
        self.machinesBtn.setObjectName(u"machinesBtn")

        self.horizontalLayout_4.addWidget(self.machinesBtn)

        self.workingPosBtn = QPushButton(self.widget_7)
        self.workingPosBtn.setObjectName(u"workingPosBtn")

        self.horizontalLayout_4.addWidget(self.workingPosBtn)

        self.operTypesBtn = QPushButton(self.widget_7)
        self.operTypesBtn.setObjectName(u"operTypesBtn")

        self.horizontalLayout_4.addWidget(self.operTypesBtn)

        self.yarnsBtn = QPushButton(self.widget_7)
        self.yarnsBtn.setObjectName(u"yarnsBtn")

        self.horizontalLayout_4.addWidget(self.yarnsBtn)

        self.usersBtn = QPushButton(self.widget_7)
        self.usersBtn.setObjectName(u"usersBtn")

        self.horizontalLayout_4.addWidget(self.usersBtn)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.addNewEntryBtn = QPushButton(self.parametersHolder)
        self.addNewEntryBtn.setObjectName(u"addNewEntryBtn")

        self.verticalLayout_2.addWidget(self.addNewEntryBtn, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.parametersHolder, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.parametersInfoHolder, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(customParametersWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 888, 673))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.parametersTableHolder = QWidget(self.scrollAreaWidgetContents)
        self.parametersTableHolder.setObjectName(u"parametersTableHolder")
        self.verticalLayout_11 = QVBoxLayout(self.parametersTableHolder)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 0)
        self.parametersTableView = QTableView(self.parametersTableHolder)
        self.parametersTableView.setObjectName(u"parametersTableView")
        self.parametersTableView.setStyleSheet(u"QHeaderView:section{\n"
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
        self.parametersTableView.setAlternatingRowColors(True)
        self.parametersTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.parametersTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.parametersTableView.setCornerButtonEnabled(False)
        self.parametersTableView.verticalHeader().setVisible(False)

        self.verticalLayout_11.addWidget(self.parametersTableView)


        self.verticalLayout_12.addWidget(self.parametersTableHolder)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(customParametersWidget)

        QMetaObject.connectSlotsByName(customParametersWidget)
    # setupUi

    def retranslateUi(self, customParametersWidget):
        customParametersWidget.setWindowTitle(QCoreApplication.translate("customParametersWidget", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("customParametersWidget", u"\u041d\u041e\u041c\u0415\u041d\u041a\u041b\u0410\u0422\u0423\u0420\u0418", None))
        self.logoutBtn.setText("")
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customParametersWidget", u"admin", None))
        self.clientsBtn.setText(QCoreApplication.translate("customParametersWidget", u"\u041a\u043b\u0438\u0435\u043d\u0442\u0438", None))
        self.cehoveBtn.setText(QCoreApplication.translate("customParametersWidget", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438 \u043c\u0435\u0441\u0442\u0430", None))
        self.machinesBtn.setText(QCoreApplication.translate("customParametersWidget", u"\u041c\u0430\u0448\u0438\u043d\u0438", None))
        self.workingPosBtn.setText(QCoreApplication.translate("customParametersWidget", u"\u0414\u043b\u044a\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.operTypesBtn.setText(QCoreApplication.translate("customParametersWidget", u"\u0412\u0438\u0434\u043e\u0432\u0435 \u0414\u043b\u044a\u0436\u043d\u043e\u0441\u0442", None))
        self.yarnsBtn.setText(QCoreApplication.translate("customParametersWidget", u"\u041f\u0440\u0435\u0436\u0434\u0438", None))
        self.usersBtn.setText(QCoreApplication.translate("customParametersWidget", u"\u041f\u043e\u0442\u0440\u0435\u0431\u0438\u0442\u0435\u043b\u0438", None))
        self.addNewEntryBtn.setText(QCoreApplication.translate("customParametersWidget", u"\u0414\u043e\u0431\u0430\u0432\u044f\u043d\u0435", None))
    # retranslateUi

