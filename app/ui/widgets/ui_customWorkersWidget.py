# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customWorkersWidgetNAzbsJ.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_customWorkersEditWidget(object):
    def setupUi(self, customWorkersEditWidget):
        if not customWorkersEditWidget.objectName():
            customWorkersEditWidget.setObjectName(u"customWorkersEditWidget")
        customWorkersEditWidget.resize(800, 580)
        customWorkersEditWidget.setMinimumSize(QSize(800, 580))
        customWorkersEditWidget.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 600 9pt \"Segoe UI\";\n"
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
"	font-size: 9pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #aeaeae;\n"
"}\n"
"\n"
"QMenu {\n"
"	border: 1px solid #aeaeae;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"	padding: 5px;\n"
"	font: 8pt;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"	background-color: #aeaeae;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"#addNewTimePaperBtn {\n"
"	font-size: 9pt;\n"
"}\n"
"\n"
"QDateEdit::up-button, QDateEdit::down-button{\n"
"	width: 0px;\n"
"}\n"
"\n"
"\n"
"QLineEdit, QDateEdit{\n"
"	border: none;\n"
"	font-size: 9pt;\n"
"	border-bottom: 1px solid #7c9399;\n"
"}\n"
"\n"
"#se"
                        "archLineEdit {\n"
"	font-size: 8pt;\n"
"}\n"
"\n"
"#calStartBtn, #calLeavingBtn {\n"
"	background-color: #dfdfdf;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"#optionsHolder, #optionsHolder_2 {\n"
"	border-bottom: 2px dashed #7c9399;\n"
"}\n"
"\n"
"#pageTitle {\n"
"	font: 700 11pt \"Segoe UI\";\n"
"}\n"
"\n"
"#calendarBtn {\n"
"	background-color: #dfdfdf;\n"
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
"	font-size: 10pt;\n"
"}\n"
"\n"
"#workerPlaceLineEdit, #workerPositionLineEdit {\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"#widget_3 * {\n"
"	font-size: 8pt;\n"
"	font-weight: 500;\n"
"}")
        self.verticalLayout = QVBoxLayout(customWorkersEditWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(customWorkersEditWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.headerHolder = QWidget(self.widget)
        self.headerHolder.setObjectName(u"headerHolder")
        self.horizontalLayout = QHBoxLayout(self.headerHolder)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 3)
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
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 5, 0)
        self.logoutBtn = QPushButton(self.userHolder)
        self.logoutBtn.setObjectName(u"logoutBtn")
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Log-Out--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBtn.setIcon(icon)
        self.logoutBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.logoutBtn)

        self.userIcon = QPushButton(self.userHolder)
        self.userIcon.setObjectName(u"userIcon")
        self.userIcon.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/User--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userIcon.setIcon(icon1)
        self.userIcon.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.userIcon)

        self.usernameLabel = QLabel(self.userHolder)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.horizontalLayout_3.addWidget(self.usernameLabel)


        self.horizontalLayout.addWidget(self.userHolder, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.headerHolder)

        self.workerInfoHolder = QWidget(self.widget)
        self.workerInfoHolder.setObjectName(u"workerInfoHolder")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workerInfoHolder.sizePolicy().hasHeightForWidth())
        self.workerInfoHolder.setSizePolicy(sizePolicy)
        self.workerInfoHolder.setMinimumSize(QSize(300, 0))
        self.verticalLayout_2 = QVBoxLayout(self.workerInfoHolder)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.workerInfoHolder)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.addNewWorkerBtn = QPushButton(self.widget_2)
        self.addNewWorkerBtn.setObjectName(u"addNewWorkerBtn")

        self.horizontalLayout_4.addWidget(self.addNewWorkerBtn)


        self.verticalLayout_2.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget_3 = QWidget(self.workerInfoHolder)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.allCheckBox = QCheckBox(self.widget_3)
        self.allCheckBox.setObjectName(u"allCheckBox")

        self.verticalLayout_3.addWidget(self.allCheckBox)

        self.workerEGNCheckBox = QCheckBox(self.widget_3)
        self.workerEGNCheckBox.setObjectName(u"workerEGNCheckBox")

        self.verticalLayout_3.addWidget(self.workerEGNCheckBox)

        self.adressCheckBox = QCheckBox(self.widget_3)
        self.adressCheckBox.setObjectName(u"adressCheckBox")

        self.verticalLayout_3.addWidget(self.adressCheckBox)

        self.expCheckBox = QCheckBox(self.widget_3)
        self.expCheckBox.setObjectName(u"expCheckBox")

        self.verticalLayout_3.addWidget(self.expCheckBox)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.workerInfoHolder)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setSpacing(8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.searchLineEdit = QLineEdit(self.widget_5)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setMinimumSize(QSize(250, 0))
        self.searchLineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_6.addWidget(self.searchLineEdit)


        self.verticalLayout_2.addWidget(self.widget_5, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.workerInfoHolder, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.optionsHolder = QWidget(customWorkersEditWidget)
        self.optionsHolder.setObjectName(u"optionsHolder")
        self.verticalLayout_5 = QVBoxLayout(self.optionsHolder)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)

        self.verticalLayout.addWidget(self.optionsHolder)

        self.scrollArea = QScrollArea(customWorkersEditWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 788, 380))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.workersHolder = QWidget(self.scrollAreaWidgetContents)
        self.workersHolder.setObjectName(u"workersHolder")
        self.workersHolder.setStyleSheet(u"* {\n"
"	padding: 0px;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.workersHolder)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 0)
        self.workersTableView = QTableView(self.workersHolder)
        self.workersTableView.setObjectName(u"workersTableView")
        self.workersTableView.setFocusPolicy(Qt.NoFocus)
        self.workersTableView.setStyleSheet(u"QHeaderView:section{\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	background-color: #dfdfdf;\n"
"	padding: 3px;\n"
"}\n"
"QVerticalView:section{\n"
"	min-height: 20px;\n"
"}\n"
"QAbstractItemView{\n"
"	alternate-background-color: #d3d3d3;\n"
"	font: 8pt \"Segoe UI\";\n"
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
        self.workersTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.workersTableView.setTabKeyNavigation(False)
        self.workersTableView.setAlternatingRowColors(True)
        self.workersTableView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.workersTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.workersTableView.setShowGrid(True)
        self.workersTableView.setCornerButtonEnabled(False)
        self.workersTableView.verticalHeader().setVisible(False)
        self.workersTableView.verticalHeader().setMinimumSectionSize(20)
        self.workersTableView.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout_5.addWidget(self.workersTableView)


        self.verticalLayout_12.addWidget(self.workersHolder)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(customWorkersEditWidget)

        QMetaObject.connectSlotsByName(customWorkersEditWidget)
    # setupUi

    def retranslateUi(self, customWorkersEditWidget):
        customWorkersEditWidget.setWindowTitle(QCoreApplication.translate("customWorkersEditWidget", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u041f\u0415\u0420\u0421\u041e\u041d\u0410\u041b", None))
        self.logoutBtn.setText("")
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customWorkersEditWidget", u"admin", None))
        self.addNewWorkerBtn.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u041d\u043e\u0432 \u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a", None))
        self.allCheckBox.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0412\u0441\u0438\u0447\u043a\u0438", None))
        self.workerEGNCheckBox.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0415\u0413\u041d/\u041f\u0440\u0435\u0437\u0438\u043c\u0435", None))
        self.adressCheckBox.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.expCheckBox.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0422\u0440\u0443\u0434\u043e\u0432 \u0421\u0442\u0430\u0436", None))
        self.label.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0422\u044a\u0440\u0441\u0435\u043d\u0435:", None))
    # retranslateUi

