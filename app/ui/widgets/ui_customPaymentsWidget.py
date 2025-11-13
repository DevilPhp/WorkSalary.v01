# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customPaymentsWidgetBXgSfu.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_customPaymentsWidget(object):
    def setupUi(self, customPaymentsWidget):
        if not customPaymentsWidget.objectName():
            customPaymentsWidget.setObjectName(u"customPaymentsWidget")
        customPaymentsWidget.resize(1092, 580)
        customPaymentsWidget.setMinimumSize(QSize(800, 580))
        customPaymentsWidget.setStyleSheet(u"*{\n"
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
"#statusBar {\n"
"	border: 1px solid #7c9399;\n"
"}\n"
"#statusBar *{\n"
"	font-size: 8pt;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"#avrEuroLabel, #avrLevaLabel, #totalLevaLabel, #totalSelectedRows, #totalEuroLabel, #totalViewRows {\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"#modelHolder QLabel, #newModelIn"
                        "foHolder *{\n"
"	font-size: 9pt;\n"
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
"#fromCalendarBtn, #toCalendarBtn {\n"
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
"#refreshShiftsBtn {\n"
"	padding: 0px;\n"
"	background-color: #dfdfdf;\n"
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
"#widget_3 QCheckBox {\n"
"	font-size: 8pt;\n"
"	padding: 0px;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #dfdfdf;\n"
"	border-bottom: 2px solid #7c9399;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	image: url(':/icons/app/assets/icons/Alt-Arrow-Down--Streamline-"
                        "Solar-Broken.svg');\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	color: #2b2b2c;\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border-radius: 0px;\n"
"	alternate-background-color: #2c313c;\n"
"}\n"
"QComboBox::item:selected{\n"
"	color: #2b2b2c;\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border-radius: 0px;\n"
"}\n"
"QComboBox::item{\n"
"	color: #324b4c;\n"
"	font: 600 9pt \"Segoe UI\";\n"
"	height: 10px;  \n"
"	border: 4px solid transparent;\n"
"	padding: 0px 4px 0px 4px;\n"
"}")
        self.verticalLayout = QVBoxLayout(customPaymentsWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(customPaymentsWidget)
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
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 5, 0)
        self.logoutBtn = QPushButton(self.userHolder)
        self.logoutBtn.setObjectName(u"logoutBtn")
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Log-Out--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBtn.setIcon(icon)
        self.logoutBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.logoutBtn, 0, Qt.AlignRight)

        self.userIcon = QPushButton(self.userHolder)
        self.userIcon.setObjectName(u"userIcon")
        self.userIcon.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/User--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userIcon.setIcon(icon1)
        self.userIcon.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.userIcon, 0, Qt.AlignRight)

        self.usernameLabel = QLabel(self.userHolder)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.horizontalLayout_3.addWidget(self.usernameLabel)


        self.horizontalLayout.addWidget(self.userHolder, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.headerHolder)

        self.operationsHolder = QWidget(self.widget)
        self.operationsHolder.setObjectName(u"operationsHolder")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operationsHolder.sizePolicy().hasHeightForWidth())
        self.operationsHolder.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.operationsHolder)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.operationsHolder)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_5)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_12)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 10, 0)
        self.label_25 = QLabel(self.widget_6)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_5.addWidget(self.label_25)


        self.horizontalLayout_7.addWidget(self.widget_6, 0, Qt.AlignLeft)

        self.widget_7 = QWidget(self.widget_12)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_7)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.fromDateEdit = QDateEdit(self.widget_13)
        self.fromDateEdit.setObjectName(u"fromDateEdit")
        self.fromDateEdit.setMaximumSize(QSize(70, 16777215))
        self.fromDateEdit.setFocusPolicy(Qt.WheelFocus)
        self.fromDateEdit.setFrame(False)
        self.fromDateEdit.setAlignment(Qt.AlignCenter)
        self.fromDateEdit.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.fromDateEdit.setMinimumDateTime(QDateTime(QDate(1990, 8, 26), QTime(0, 0, 0)))

        self.horizontalLayout_9.addWidget(self.fromDateEdit)

        self.fromCalendarBtn = QPushButton(self.widget_13)
        self.fromCalendarBtn.setObjectName(u"fromCalendarBtn")
        self.fromCalendarBtn.setFocusPolicy(Qt.NoFocus)
        self.fromCalendarBtn.setStyleSheet(u"*{\n"
"	padding: 0px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/app/assets/icons/Calendar--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fromCalendarBtn.setIcon(icon2)
        self.fromCalendarBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_9.addWidget(self.fromCalendarBtn)


        self.horizontalLayout_6.addWidget(self.widget_13)

        self.label = QLabel(self.widget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label)

        self.widget_20 = QWidget(self.widget_7)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.toDateEdit = QDateEdit(self.widget_20)
        self.toDateEdit.setObjectName(u"toDateEdit")
        self.toDateEdit.setMaximumSize(QSize(70, 16777215))
        self.toDateEdit.setFocusPolicy(Qt.WheelFocus)
        self.toDateEdit.setFrame(False)
        self.toDateEdit.setAlignment(Qt.AlignCenter)
        self.toDateEdit.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.toDateEdit.setMinimumDateTime(QDateTime(QDate(1990, 8, 28), QTime(0, 0, 0)))

        self.horizontalLayout_11.addWidget(self.toDateEdit)

        self.toCalendarBtn = QPushButton(self.widget_20)
        self.toCalendarBtn.setObjectName(u"toCalendarBtn")
        self.toCalendarBtn.setFocusPolicy(Qt.NoFocus)
        self.toCalendarBtn.setStyleSheet(u"*{\n"
"	padding: 0px;\n"
"}")
        self.toCalendarBtn.setIcon(icon2)
        self.toCalendarBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_11.addWidget(self.toCalendarBtn)


        self.horizontalLayout_6.addWidget(self.widget_20)


        self.horizontalLayout_7.addWidget(self.widget_7, 0, Qt.AlignLeft)


        self.horizontalLayout_8.addWidget(self.widget_12, 0, Qt.AlignLeft)

        self.searchBtn = QPushButton(self.widget_5)
        self.searchBtn.setObjectName(u"searchBtn")

        self.horizontalLayout_8.addWidget(self.searchBtn)

        self.exportToExcelBtn = QPushButton(self.widget_5)
        self.exportToExcelBtn.setObjectName(u"exportToExcelBtn")

        self.horizontalLayout_8.addWidget(self.exportToExcelBtn)

        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(2)
        self.selectAllCheckBox = QCheckBox(self.widget_3)
        self.selectAllCheckBox.setObjectName(u"selectAllCheckBox")

        self.gridLayout.addWidget(self.selectAllCheckBox, 0, 0, 1, 1)

        self.overtimeCheckBox = QCheckBox(self.widget_3)
        self.overtimeCheckBox.setObjectName(u"overtimeCheckBox")

        self.gridLayout.addWidget(self.overtimeCheckBox, 1, 0, 1, 1)

        self.hourlyCheckBox = QCheckBox(self.widget_3)
        self.hourlyCheckBox.setObjectName(u"hourlyCheckBox")

        self.gridLayout.addWidget(self.hourlyCheckBox, 2, 0, 1, 1)

        self.holidaysCheckBox = QCheckBox(self.widget_3)
        self.holidaysCheckBox.setObjectName(u"holidaysCheckBox")

        self.gridLayout.addWidget(self.holidaysCheckBox, 2, 1, 1, 1)

        self.weekendDaysCheckBox = QCheckBox(self.widget_3)
        self.weekendDaysCheckBox.setObjectName(u"weekendDaysCheckBox")

        self.gridLayout.addWidget(self.weekendDaysCheckBox, 1, 1, 1, 1)

        self.nightTimeCheckBox = QCheckBox(self.widget_3)
        self.nightTimeCheckBox.setObjectName(u"nightTimeCheckBox")

        self.gridLayout.addWidget(self.nightTimeCheckBox, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.horizontalLayout_8.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.widget_5, 0, Qt.AlignLeft)

        self.optionsHolder_2 = QFrame(self.operationsHolder)
        self.optionsHolder_2.setObjectName(u"optionsHolder_2")
        self.optionsHolder_2.setFrameShape(QFrame.StyledPanel)
        self.optionsHolder_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.optionsHolder_2)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 10)

        self.verticalLayout_2.addWidget(self.optionsHolder_2)


        self.verticalLayout_4.addWidget(self.operationsHolder, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(customPaymentsWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1080, 420))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.paymentsTableHolder = QWidget(self.scrollAreaWidgetContents)
        self.paymentsTableHolder.setObjectName(u"paymentsTableHolder")
        self.verticalLayout_11 = QVBoxLayout(self.paymentsTableHolder)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 0)

        self.verticalLayout_12.addWidget(self.paymentsTableHolder)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.statusBar = QWidget(customPaymentsWidget)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMinimumSize(QSize(0, 25))
        self.horizontalLayout_18 = QHBoxLayout(self.statusBar)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(5, 0, 5, 5)
        self.widget_2 = QWidget(self.statusBar)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(10, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_2)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_25.setSpacing(5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.widget_17)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_25.addWidget(self.label_42)

        self.totalViewRows = QLabel(self.widget_17)
        self.totalViewRows.setObjectName(u"totalViewRows")

        self.horizontalLayout_25.addWidget(self.totalViewRows)


        self.horizontalLayout_21.addWidget(self.widget_17, 0, Qt.AlignLeft)


        self.horizontalLayout_18.addWidget(self.widget_2, 0, Qt.AlignBottom)

        self.widget_8 = QWidget(self.statusBar)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_18.addWidget(self.widget_8, 0, Qt.AlignHCenter)

        self.widget_9 = QWidget(self.statusBar)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_9)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_24.setSpacing(3)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.widget_16)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_24.addWidget(self.label_36)

        self.totalSelectedRows = QLabel(self.widget_16)
        self.totalSelectedRows.setObjectName(u"totalSelectedRows")

        self.horizontalLayout_24.addWidget(self.totalSelectedRows)


        self.horizontalLayout_4.addWidget(self.widget_16)

        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_22.setSpacing(3)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.widget_10)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_22.addWidget(self.label_38)

        self.totalLevaLabel = QLabel(self.widget_10)
        self.totalLevaLabel.setObjectName(u"totalLevaLabel")

        self.horizontalLayout_22.addWidget(self.totalLevaLabel)


        self.horizontalLayout_4.addWidget(self.widget_10)

        self.widget_15 = QWidget(self.widget_9)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_23 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_23.setSpacing(3)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.widget_15)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_23.addWidget(self.label_37)

        self.totalEuroLabel = QLabel(self.widget_15)
        self.totalEuroLabel.setObjectName(u"totalEuroLabel")

        self.horizontalLayout_23.addWidget(self.totalEuroLabel)


        self.horizontalLayout_4.addWidget(self.widget_15)

        self.widget_18 = QWidget(self.widget_9)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_26 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_26.setSpacing(3)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.widget_18)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_26.addWidget(self.label_39)

        self.avrLevaLabel = QLabel(self.widget_18)
        self.avrLevaLabel.setObjectName(u"avrLevaLabel")

        self.horizontalLayout_26.addWidget(self.avrLevaLabel)


        self.horizontalLayout_4.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.widget_9)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_27 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_27.setSpacing(3)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.widget_19)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_27.addWidget(self.label_40)

        self.avrEuroLabel = QLabel(self.widget_19)
        self.avrEuroLabel.setObjectName(u"avrEuroLabel")

        self.horizontalLayout_27.addWidget(self.avrEuroLabel)


        self.horizontalLayout_4.addWidget(self.widget_19)


        self.horizontalLayout_18.addWidget(self.widget_9, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.statusBar)


        self.retranslateUi(customPaymentsWidget)

        QMetaObject.connectSlotsByName(customPaymentsWidget)
    # setupUi

    def retranslateUi(self, customPaymentsWidget):
        customPaymentsWidget.setWindowTitle(QCoreApplication.translate("customPaymentsWidget", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("customPaymentsWidget", u"\u041d\u0410\u0427\u0418\u0421\u041b\u0415\u041d\u0418\u042f", None))
        self.logoutBtn.setText("")
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customPaymentsWidget", u"admin", None))
        self.label_25.setText(QCoreApplication.translate("customPaymentsWidget", u"\u041e\u0442/\u0414\u043e \u0414\u0430\u0442\u0430: ", None))
        self.fromDateEdit.setDisplayFormat(QCoreApplication.translate("customPaymentsWidget", u"dd.MM.yy '\u0433.'", None))
        self.fromCalendarBtn.setText("")
        self.label.setText(QCoreApplication.translate("customPaymentsWidget", u"  /  ", None))
        self.toDateEdit.setDisplayFormat(QCoreApplication.translate("customPaymentsWidget", u"dd.MM.yy '\u0433.'", None))
        self.toCalendarBtn.setText("")
        self.searchBtn.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0422\u044a\u0440\u0441\u0435\u043d\u0435", None))
        self.exportToExcelBtn.setText(QCoreApplication.translate("customPaymentsWidget", u"Excel", None))
        self.selectAllCheckBox.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0412\u0441\u0438\u0447\u043a\u0438", None))
        self.overtimeCheckBox.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0418\u0437\u0432\u044a\u043d\u0440\u0435\u0434\u0435\u043d", None))
        self.hourlyCheckBox.setText(QCoreApplication.translate("customPaymentsWidget", u"\u041f\u043e\u0447\u0430\u0441\u043e\u0432\u043e", None))
        self.holidaysCheckBox.setText(QCoreApplication.translate("customPaymentsWidget", u"\u041f\u0440\u0430\u0437\u043d\u0438\u0447\u043d\u0438 \u0434\u043d\u0438", None))
        self.weekendDaysCheckBox.setText(QCoreApplication.translate("customPaymentsWidget", u"\u041f\u043e\u0447\u0438\u0432\u043d\u0438 \u0434\u043d\u0438", None))
        self.nightTimeCheckBox.setText(QCoreApplication.translate("customPaymentsWidget", u"\u041d\u043e\u0449\u0435\u043d", None))
        self.label_42.setText(QCoreApplication.translate("customPaymentsWidget", u"\u041e\u0431\u0449\u043e \u0440\u0435\u0434\u043e\u0432\u0435:", None))
        self.totalViewRows.setText(QCoreApplication.translate("customPaymentsWidget", u"0", None))
        self.label_36.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0420\u0435\u0434\u043e\u0432\u0435:", None))
        self.totalSelectedRows.setText(QCoreApplication.translate("customPaymentsWidget", u"0", None))
        self.label_38.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0422\u043e\u0442\u0430\u043b \u041b\u0432", None))
        self.totalLevaLabel.setText(QCoreApplication.translate("customPaymentsWidget", u"0.0", None))
        self.label_37.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0422\u043e\u0442\u0430\u043b \u20ac", None))
        self.totalEuroLabel.setText(QCoreApplication.translate("customPaymentsWidget", u"0.0", None))
        self.label_39.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0421\u0440. \u043b\u0432.:", None))
        self.avrLevaLabel.setText(QCoreApplication.translate("customPaymentsWidget", u"0.0", None))
        self.label_40.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0421\u0440. \u20ac:", None))
        self.avrEuroLabel.setText(QCoreApplication.translate("customPaymentsWidget", u"0.0", None))
    # retranslateUi

