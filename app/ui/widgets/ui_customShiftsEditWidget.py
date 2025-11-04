# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customShiftsEditWidgetCkXPGK.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QTimeEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_customWorkingShiftsWidget(object):
    def setupUi(self, customWorkingShiftsWidget):
        if not customWorkingShiftsWidget.objectName():
            customWorkingShiftsWidget.setObjectName(u"customWorkingShiftsWidget")
        customWorkingShiftsWidget.resize(900, 800)
        customWorkingShiftsWidget.setMinimumSize(QSize(900, 800))
        customWorkingShiftsWidget.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 600 11pt \"Segoe UI\";\n"
"	color: #324b4c;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	width: 20px;\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"	background: #dfdfdf;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #c9c9c9;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #aeaeae;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: none;\n"
"	font-size: 10pt;\n"
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
"#modelHolder QLabel, #newModelInfoHolder * , #widget_11 *{\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"#optionsHolder, #optionsHolder_2 {\n"
"	border-bottom: 2px dashed #7c9399;\n"
"}\n"
"\n"
"#pageTitle"
                        " {\n"
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
"	font-size: 10pt;\n"
"}")
        self.verticalLayout = QVBoxLayout(customWorkingShiftsWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(customWorkingShiftsWidget)
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

        self.workerInfoHolder = QWidget(self.widget)
        self.workerInfoHolder.setObjectName(u"workerInfoHolder")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workerInfoHolder.sizePolicy().hasHeightForWidth())
        self.workerInfoHolder.setSizePolicy(sizePolicy)
        self.workerInfoHolder.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_5 = QHBoxLayout(self.workerInfoHolder)
        self.horizontalLayout_5.setSpacing(35)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 5)
        self.workerShiftsHolder = QWidget(self.workerInfoHolder)
        self.workerShiftsHolder.setObjectName(u"workerShiftsHolder")
        self.verticalLayout_6 = QVBoxLayout(self.workerShiftsHolder)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.workerShiftsHolder)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_10 = QVBoxLayout(self.widget_11)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 5)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout_10.addLayout(self.gridLayout)


        self.verticalLayout_6.addWidget(self.widget_11)

        self.newModelInfoHolder = QWidget(self.workerShiftsHolder)
        self.newModelInfoHolder.setObjectName(u"newModelInfoHolder")
        self.newModelInfoHolder.setMinimumSize(QSize(0, 0))
        self.verticalLayout_8 = QVBoxLayout(self.newModelInfoHolder)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.newModelInfoHolder)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.newModelLayout = QGridLayout()
        self.newModelLayout.setSpacing(10)
        self.newModelLayout.setObjectName(u"newModelLayout")
        self.label_21 = QLabel(self.widget_6)
        self.label_21.setObjectName(u"label_21")

        self.newModelLayout.addWidget(self.label_21, 0, 6, 1, 1)

        self.shiftEndWidget = QWidget(self.widget_6)
        self.shiftEndWidget.setObjectName(u"shiftEndWidget")
        self.horizontalLayout_9 = QHBoxLayout(self.shiftEndWidget)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.shiftEnd = QTimeEdit(self.shiftEndWidget)
        self.shiftEnd.setObjectName(u"shiftEnd")
        self.shiftEnd.setTime(QTime(17, 0, 0))

        self.horizontalLayout_9.addWidget(self.shiftEnd)

        self.label_15 = QLabel(self.shiftEndWidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_9.addWidget(self.label_15)


        self.newModelLayout.addWidget(self.shiftEndWidget, 0, 5, 1, 1)

        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")

        self.newModelLayout.addWidget(self.label_10, 0, 4, 1, 1)

        self.hourlyStartWidget = QWidget(self.widget_6)
        self.hourlyStartWidget.setObjectName(u"hourlyStartWidget")
        self.horizontalLayout_10 = QHBoxLayout(self.hourlyStartWidget)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.newModelLayout.addWidget(self.hourlyStartWidget, 5, 3, 1, 1)

        self.shiftStartWidget = QWidget(self.widget_6)
        self.shiftStartWidget.setObjectName(u"shiftStartWidget")
        self.horizontalLayout_8 = QHBoxLayout(self.shiftStartWidget)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.shiftStart = QTimeEdit(self.shiftStartWidget)
        self.shiftStart.setObjectName(u"shiftStart")
        self.shiftStart.setCalendarPopup(False)
        self.shiftStart.setTime(QTime(8, 0, 0))

        self.horizontalLayout_8.addWidget(self.shiftStart)

        self.label_14 = QLabel(self.shiftStartWidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_8.addWidget(self.label_14)


        self.newModelLayout.addWidget(self.shiftStartWidget, 0, 3, 1, 1)

        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")

        self.newModelLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.shiftTotalMins = QLabel(self.widget_6)
        self.shiftTotalMins.setObjectName(u"shiftTotalMins")

        self.newModelLayout.addWidget(self.shiftTotalMins, 0, 7, 1, 1)

        self.label_27 = QLabel(self.widget_6)
        self.label_27.setObjectName(u"label_27")

        self.newModelLayout.addWidget(self.label_27, 0, 8, 1, 1)

        self.label_7 = QLabel(self.widget_6)
        self.label_7.setObjectName(u"label_7")

        self.newModelLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.label = QLabel(self.widget_6)
        self.label.setObjectName(u"label")

        self.newModelLayout.addWidget(self.label, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.widget_6)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.shiftBreakLineEdit = QLineEdit(self.widget_3)
        self.shiftBreakLineEdit.setObjectName(u"shiftBreakLineEdit")
        self.shiftBreakLineEdit.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_6.addWidget(self.shiftBreakLineEdit, 0, Qt.AlignLeft)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)


        self.newModelLayout.addWidget(self.widget_3, 1, 1, 1, 1, Qt.AlignLeft)

        self.workingShiftsNameLineEdit = QLineEdit(self.widget_6)
        self.workingShiftsNameLineEdit.setObjectName(u"workingShiftsNameLineEdit")

        self.newModelLayout.addWidget(self.workingShiftsNameLineEdit, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.newModelLayout)

        self.acceptWorkingShiftsBtn = QPushButton(self.widget_6)
        self.acceptWorkingShiftsBtn.setObjectName(u"acceptWorkingShiftsBtn")
        self.acceptWorkingShiftsBtn.setFocusPolicy(Qt.NoFocus)
        self.acceptWorkingShiftsBtn.setStyleSheet(u"*{\n"
"	padding: 0px;\n"
"	background-color: #dfdfdf;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/app/assets/icons/Check-Square--Streamline-Solar-Broken-#008b69.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.acceptWorkingShiftsBtn.setIcon(icon2)
        self.acceptWorkingShiftsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.acceptWorkingShiftsBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_8.addWidget(self.widget_6)


        self.verticalLayout_6.addWidget(self.newModelInfoHolder)


        self.horizontalLayout_5.addWidget(self.workerShiftsHolder, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.workerInfoHolder, 0, Qt.AlignLeft)

        self.operationsHolder = QWidget(self.widget)
        self.operationsHolder.setObjectName(u"operationsHolder")
        sizePolicy.setHeightForWidth(self.operationsHolder.sizePolicy().hasHeightForWidth())
        self.operationsHolder.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.operationsHolder)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.optionsHolder = QFrame(self.operationsHolder)
        self.optionsHolder.setObjectName(u"optionsHolder")
        self.optionsHolder.setFrameShape(QFrame.StyledPanel)
        self.optionsHolder.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.optionsHolder)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 10)

        self.verticalLayout_2.addWidget(self.optionsHolder)


        self.verticalLayout_4.addWidget(self.operationsHolder)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(customWorkingShiftsWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 888, 576))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.workingShiftsTable = QWidget(self.scrollAreaWidgetContents)
        self.workingShiftsTable.setObjectName(u"workingShiftsTable")
        self.workingShiftsTable.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.workingShiftsTable)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 0)

        self.verticalLayout_12.addWidget(self.workingShiftsTable)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(customWorkingShiftsWidget)

        QMetaObject.connectSlotsByName(customWorkingShiftsWidget)
    # setupUi

    def retranslateUi(self, customWorkingShiftsWidget):
        customWorkingShiftsWidget.setWindowTitle(QCoreApplication.translate("customWorkingShiftsWidget", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("customWorkingShiftsWidget", u"\u0420\u0410\u0411\u041e\u0422\u041d\u0418 \u0421\u041c\u0415\u041d\u0418", None))
        self.logoutBtn.setText("")
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customWorkingShiftsWidget", u"admin", None))
        self.label_21.setText(QCoreApplication.translate("customWorkingShiftsWidget", u"\u041e\u0431\u0449\u043e:", None))
        self.label_15.setText(QCoreApplication.translate("customWorkingShiftsWidget", u"\u0447.", None))
        self.label_10.setText(QCoreApplication.translate("customWorkingShiftsWidget", u"\u041a\u0440\u0430\u0439:", None))
        self.label_14.setText(QCoreApplication.translate("customWorkingShiftsWidget", u"\u0447.", None))
        self.label_5.setText(QCoreApplication.translate("customWorkingShiftsWidget", u"\u0421\u043c\u044f\u043d\u0430:", None))
        self.shiftTotalMins.setText(QCoreApplication.translate("customWorkingShiftsWidget", u"480", None))
        self.label_27.setText(QCoreApplication.translate("customWorkingShiftsWidget", u"\u043c\u0438\u043d.", None))
        self.label_7.setText(QCoreApplication.translate("customWorkingShiftsWidget", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.label.setText(QCoreApplication.translate("customWorkingShiftsWidget", u"\u041f\u043e\u043a\u0438\u0432\u043a\u0430:", None))
        self.shiftBreakLineEdit.setPlaceholderText(QCoreApplication.translate("customWorkingShiftsWidget", u"60", None))
        self.label_2.setText(QCoreApplication.translate("customWorkingShiftsWidget", u"\u043c\u0438\u043d.", None))
        self.acceptWorkingShiftsBtn.setText("")
    # retranslateUi

