# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customPaymentsDetailsWidgetDlvKoo.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_customPaymentsDetailsWidget(object):
    def setupUi(self, customPaymentsDetailsWidget):
        if not customPaymentsDetailsWidget.objectName():
            customPaymentsDetailsWidget.setObjectName(u"customPaymentsDetailsWidget")
        customPaymentsDetailsWidget.resize(800, 580)
        customPaymentsDetailsWidget.setMinimumSize(QSize(800, 580))
        customPaymentsDetailsWidget.setStyleSheet(u"*{\n"
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
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	font-size: 9pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #aeaeae;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: none;\n"
"	border-bottom: 1px solid #7c9399;\n"
"	max-width: 35px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font-size:8pt;\n"
"}\n"
"\n"
"#widget_6 QCheckBox {\n"
"	font-size: 8pt;\n"
"	padding: 0px;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"#workerNameLabel, #workerLastNameLabel, #workerNumberLabel, #paymentWidget QLabel {\n"
"	font-weight: 900;\n"
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
""
                        "#avrLevaLabel, #totalLevaLabel, #totalEuroLabel, #totalSelectedRows, #totalViewRows, #avrEuroLabel {\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"#modelHolder QLabel, #newModelInfoHolder *{\n"
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
"#userIcon, #fromCalendarBtn, #toCalendarBtn, #logoutBtn {\n"
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
"}")
        self.verticalLayout = QVBoxLayout(customPaymentsDetailsWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(customPaymentsDetailsWidget)
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
        self.workerInfoHolder.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.workerInfoHolder)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.widget_7 = QWidget(self.workerInfoHolder)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.excelBtn = QPushButton(self.widget_7)
        self.excelBtn.setObjectName(u"excelBtn")

        self.horizontalLayout_5.addWidget(self.excelBtn)

        self.includeSubrowCheckBox = QCheckBox(self.widget_7)
        self.includeSubrowCheckBox.setObjectName(u"includeSubrowCheckBox")
        self.includeSubrowCheckBox.setChecked(True)

        self.horizontalLayout_5.addWidget(self.includeSubrowCheckBox)


        self.verticalLayout_3.addWidget(self.widget_7, 0, Qt.AlignLeft)

        self.workerHolder = QWidget(self.workerInfoHolder)
        self.workerHolder.setObjectName(u"workerHolder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.workerHolder.sizePolicy().hasHeightForWidth())
        self.workerHolder.setSizePolicy(sizePolicy1)
        self.workerHolder.setMinimumSize(QSize(280, 85))
        self.horizontalLayout_9 = QHBoxLayout(self.workerHolder)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 5)
        self.workerInfoLayout = QGridLayout()
        self.workerInfoLayout.setObjectName(u"workerInfoLayout")
        self.workerInfoLayout.setHorizontalSpacing(5)
        self.workerInfoLayout.setVerticalSpacing(3)
        self.label_4 = QLabel(self.workerHolder)
        self.label_4.setObjectName(u"label_4")

        self.workerInfoLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.label = QLabel(self.workerHolder)
        self.label.setObjectName(u"label")

        self.workerInfoLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_8 = QLabel(self.workerHolder)
        self.label_8.setObjectName(u"label_8")

        self.workerInfoLayout.addWidget(self.label_8, 1, 2, 1, 1)

        self.workerNameLabel = QLabel(self.workerHolder)
        self.workerNameLabel.setObjectName(u"workerNameLabel")
        self.workerNameLabel.setMinimumSize(QSize(50, 0))

        self.workerInfoLayout.addWidget(self.workerNameLabel, 0, 1, 1, 1)

        self.workerPositionLabel = QLabel(self.workerHolder)
        self.workerPositionLabel.setObjectName(u"workerPositionLabel")
        self.workerPositionLabel.setMinimumSize(QSize(160, 0))

        self.workerInfoLayout.addWidget(self.workerPositionLabel, 1, 3, 1, 1, Qt.AlignLeft)

        self.paymentWidget = QWidget(self.workerHolder)
        self.paymentWidget.setObjectName(u"paymentWidget")
        self.horizontalLayout_13 = QHBoxLayout(self.paymentWidget)
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.paymentLevaLabel = QLabel(self.paymentWidget)
        self.paymentLevaLabel.setObjectName(u"paymentLevaLabel")

        self.horizontalLayout_13.addWidget(self.paymentLevaLabel)

        self.label_2 = QLabel(self.paymentWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_13.addWidget(self.label_2)

        self.paymentEuroLabel = QLabel(self.paymentWidget)
        self.paymentEuroLabel.setObjectName(u"paymentEuroLabel")

        self.horizontalLayout_13.addWidget(self.paymentEuroLabel)


        self.workerInfoLayout.addWidget(self.paymentWidget, 2, 3, 1, 1, Qt.AlignLeft)

        self.label_6 = QLabel(self.workerHolder)
        self.label_6.setObjectName(u"label_6")

        self.workerInfoLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_5 = QLabel(self.workerHolder)
        self.label_5.setObjectName(u"label_5")

        self.workerInfoLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_3 = QLabel(self.workerHolder)
        self.label_3.setObjectName(u"label_3")

        self.workerInfoLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.workerNumberLabel = QLabel(self.workerHolder)
        self.workerNumberLabel.setObjectName(u"workerNumberLabel")

        self.workerInfoLayout.addWidget(self.workerNumberLabel, 2, 1, 1, 1)

        self.workerLastNameLabel = QLabel(self.workerHolder)
        self.workerLastNameLabel.setObjectName(u"workerLastNameLabel")

        self.workerInfoLayout.addWidget(self.workerLastNameLabel, 1, 1, 1, 1)

        self.workerPlaceLabel = QLabel(self.workerHolder)
        self.workerPlaceLabel.setObjectName(u"workerPlaceLabel")
        self.workerPlaceLabel.setMinimumSize(QSize(160, 0))

        self.workerInfoLayout.addWidget(self.workerPlaceLabel, 0, 3, 1, 1)


        self.horizontalLayout_9.addLayout(self.workerInfoLayout)

        self.widget_6 = QWidget(self.workerHolder)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.selectAllCheckBox = QCheckBox(self.widget_6)
        self.selectAllCheckBox.setObjectName(u"selectAllCheckBox")

        self.gridLayout_3.addWidget(self.selectAllCheckBox, 1, 0, 1, 1)

        self.hourlyCheckBox = QCheckBox(self.widget_6)
        self.hourlyCheckBox.setObjectName(u"hourlyCheckBox")

        self.gridLayout_3.addWidget(self.hourlyCheckBox, 3, 0, 1, 1)

        self.overtimeCheckBox = QCheckBox(self.widget_6)
        self.overtimeCheckBox.setObjectName(u"overtimeCheckBox")

        self.gridLayout_3.addWidget(self.overtimeCheckBox, 2, 0, 1, 1)

        self.nightTimeCheckBox = QCheckBox(self.widget_6)
        self.nightTimeCheckBox.setObjectName(u"nightTimeCheckBox")

        self.gridLayout_3.addWidget(self.nightTimeCheckBox, 1, 1, 1, 1)

        self.weekendHolidaysCheckBox = QCheckBox(self.widget_6)
        self.weekendHolidaysCheckBox.setObjectName(u"weekendHolidaysCheckBox")

        self.gridLayout_3.addWidget(self.weekendHolidaysCheckBox, 2, 1, 1, 1)


        self.horizontalLayout_11.addLayout(self.gridLayout_3)


        self.horizontalLayout_9.addWidget(self.widget_6)


        self.verticalLayout_3.addWidget(self.workerHolder)


        self.verticalLayout_4.addWidget(self.workerInfoHolder, 0, Qt.AlignLeft|Qt.AlignTop)

        self.operationsHolder = QWidget(self.widget)
        self.operationsHolder.setObjectName(u"operationsHolder")
        sizePolicy.setHeightForWidth(self.operationsHolder.sizePolicy().hasHeightForWidth())
        self.operationsHolder.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.operationsHolder)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.optionsHolder = QFrame(self.operationsHolder)
        self.optionsHolder.setObjectName(u"optionsHolder")
        self.optionsHolder.setFrameShape(QFrame.StyledPanel)
        self.optionsHolder.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.optionsHolder)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 10)

        self.verticalLayout_2.addWidget(self.optionsHolder, 0, Qt.AlignTop)

        self.widget_5 = QWidget(self.operationsHolder)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setSpacing(25)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.widget_5)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_17.setSpacing(7)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_20 = QWidget(self.widget_14)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 2, 0)
        self.label_27 = QLabel(self.widget_20)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_14.addWidget(self.label_27)


        self.horizontalLayout_17.addWidget(self.widget_20, 0, Qt.AlignLeft)

        self.widget_21 = QWidget(self.widget_14)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_15.setSpacing(1)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.fromDateLineEdit = QLabel(self.widget_21)
        self.fromDateLineEdit.setObjectName(u"fromDateLineEdit")

        self.horizontalLayout_15.addWidget(self.fromDateLineEdit)

        self.label_10 = QLabel(self.widget_21)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_15.addWidget(self.label_10)

        self.toDateLineEdit = QLabel(self.widget_21)
        self.toDateLineEdit.setObjectName(u"toDateLineEdit")

        self.horizontalLayout_15.addWidget(self.toDateLineEdit)


        self.horizontalLayout_17.addWidget(self.widget_21, 0, Qt.AlignLeft)


        self.horizontalLayout_8.addWidget(self.widget_14, 0, Qt.AlignLeft)

        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.euroPerMinNightLabel = QLabel(self.widget_3)
        self.euroPerMinNightLabel.setObjectName(u"euroPerMinNightLabel")

        self.gridLayout_2.addWidget(self.euroPerMinNightLabel, 1, 3, 1, 1)

        self.euroPerMinDayLabel = QLabel(self.widget_3)
        self.euroPerMinDayLabel.setObjectName(u"euroPerMinDayLabel")

        self.gridLayout_2.addWidget(self.euroPerMinDayLabel, 1, 1, 1, 1)

        self.levaPerMinDayLabel = QLabel(self.widget_3)
        self.levaPerMinDayLabel.setObjectName(u"levaPerMinDayLabel")
        self.levaPerMinDayLabel.setMinimumSize(QSize(60, 0))

        self.gridLayout_2.addWidget(self.levaPerMinDayLabel, 0, 1, 1, 1)

        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.levaPerMinNightLabel = QLabel(self.widget_3)
        self.levaPerMinNightLabel.setObjectName(u"levaPerMinNightLabel")
        self.levaPerMinNightLabel.setMinimumSize(QSize(60, 0))

        self.gridLayout_2.addWidget(self.levaPerMinNightLabel, 0, 3, 1, 1)

        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(90, 0))

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_35 = QLabel(self.widget_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(90, 0))

        self.gridLayout_2.addWidget(self.label_35, 0, 2, 1, 1)

        self.label_40 = QLabel(self.widget_3)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_2.addWidget(self.label_40, 1, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout)


        self.horizontalLayout_8.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.widget_5, 0, Qt.AlignLeft)

        self.modelAndOperationHolder = QWidget(self.operationsHolder)
        self.modelAndOperationHolder.setObjectName(u"modelAndOperationHolder")
        self.verticalLayout_13 = QVBoxLayout(self.modelAndOperationHolder)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.optionsHolder_2 = QFrame(self.modelAndOperationHolder)
        self.optionsHolder_2.setObjectName(u"optionsHolder_2")
        self.optionsHolder_2.setFrameShape(QFrame.StyledPanel)
        self.optionsHolder_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.optionsHolder_2)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 10)

        self.verticalLayout_13.addWidget(self.optionsHolder_2, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.modelAndOperationHolder)


        self.verticalLayout_4.addWidget(self.operationsHolder, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.widget)

        self.scrollArea = QScrollArea(customPaymentsDetailsWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 788, 283))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.paymentsDetailsTableHolder = QWidget(self.scrollAreaWidgetContents)
        self.paymentsDetailsTableHolder.setObjectName(u"paymentsDetailsTableHolder")
        self.verticalLayout_11 = QVBoxLayout(self.paymentsDetailsTableHolder)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 0)

        self.verticalLayout_12.addWidget(self.paymentsDetailsTableHolder)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.statusBar = QWidget(customPaymentsDetailsWidget)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_18 = QHBoxLayout(self.statusBar)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.widget_2 = QWidget(self.statusBar)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_21.setSpacing(20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(20, 0, 0, 0)
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


        self.horizontalLayout_18.addWidget(self.widget_2)

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
        self.horizontalLayout_12 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_9)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_24.setSpacing(5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.widget_16)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_24.addWidget(self.label_36)

        self.totalSelectedRows = QLabel(self.widget_16)
        self.totalSelectedRows.setObjectName(u"totalSelectedRows")

        self.horizontalLayout_24.addWidget(self.totalSelectedRows)


        self.horizontalLayout_12.addWidget(self.widget_16, 0, Qt.AlignLeft)

        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.widget_10)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_22.addWidget(self.label_38)

        self.totalLevaLabel = QLabel(self.widget_10)
        self.totalLevaLabel.setObjectName(u"totalLevaLabel")

        self.horizontalLayout_22.addWidget(self.totalLevaLabel)


        self.horizontalLayout_12.addWidget(self.widget_10, 0, Qt.AlignLeft)

        self.widget_15 = QWidget(self.widget_9)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_23 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.widget_15)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_23.addWidget(self.label_37)

        self.totalEuroLabel = QLabel(self.widget_15)
        self.totalEuroLabel.setObjectName(u"totalEuroLabel")

        self.horizontalLayout_23.addWidget(self.totalEuroLabel)


        self.horizontalLayout_12.addWidget(self.widget_15, 0, Qt.AlignLeft)

        self.widget_18 = QWidget(self.widget_9)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_26 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.widget_18)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_26.addWidget(self.label_39)

        self.avrLevaLabel = QLabel(self.widget_18)
        self.avrLevaLabel.setObjectName(u"avrLevaLabel")

        self.horizontalLayout_26.addWidget(self.avrLevaLabel)


        self.horizontalLayout_12.addWidget(self.widget_18, 0, Qt.AlignLeft)

        self.widget_19 = QWidget(self.widget_9)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_28.setSpacing(5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.widget_19)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_28.addWidget(self.label_43)

        self.avrEuroLabel = QLabel(self.widget_19)
        self.avrEuroLabel.setObjectName(u"avrEuroLabel")

        self.horizontalLayout_28.addWidget(self.avrEuroLabel)


        self.horizontalLayout_12.addWidget(self.widget_19)


        self.horizontalLayout_18.addWidget(self.widget_9, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.statusBar)


        self.retranslateUi(customPaymentsDetailsWidget)

        QMetaObject.connectSlotsByName(customPaymentsDetailsWidget)
    # setupUi

    def retranslateUi(self, customPaymentsDetailsWidget):
        customPaymentsDetailsWidget.setWindowTitle(QCoreApplication.translate("customPaymentsDetailsWidget", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0414\u0415\u0422\u0410\u0419\u041b\u0418", None))
        self.logoutBtn.setText("")
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"admin", None))
        self.excelBtn.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"Excel", None))
        self.includeSubrowCheckBox.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0421 \u043f\u043e\u0434\u0440\u0435\u0434\u043e\u0432\u0435 \u0437\u0430 \u0434\u0435\u043d.", None))
        self.label_4.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0417\u0430\u043f\u043b\u0430\u0442\u0430:", None))
        self.label.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0418\u043c\u0435:", None))
        self.label_8.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0414\u043b\u044a\u0436\u043d.", None))
        self.workerNameLabel.setText("")
        self.workerPositionLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041d\u0435 \u0435 \u043f\u043e\u0441\u043e\u0447\u0435\u043d\u043e", None))
        self.paymentLevaLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0.0 \u043b\u0432", None))
        self.label_2.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"/", None))
        self.paymentEuroLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0.0 \u20ac", None))
        self.label_6.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0426\u0435\u0445:", None))
        self.label_5.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041d\u043e\u043c\u0435\u0440:", None))
        self.label_3.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.workerNumberLabel.setText("")
        self.workerLastNameLabel.setText("")
        self.workerPlaceLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041d\u0435 \u0435 \u043f\u043e\u0441\u043e\u0447\u0435\u043d\u043e", None))
        self.selectAllCheckBox.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0412\u0441\u0438\u0447\u043a\u0438", None))
        self.hourlyCheckBox.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041f\u043e\u0447\u0430\u0441\u043e\u0432\u043e", None))
        self.overtimeCheckBox.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0418\u0437\u0432\u044a\u043d\u0440\u0435\u0434\u0435\u043d", None))
        self.nightTimeCheckBox.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041d\u043e\u0449\u0435\u043d", None))
        self.weekendHolidaysCheckBox.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041f\u043e\u0447\u0438\u0432\u043d\u0438/\u041f\u0430\u0440\u0437\u043d\u0438\u0447\u043d\u0438 \u0434\u043d\u0438", None))
        self.label_27.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041e\u0442/\u0414\u043e \u0414\u0430\u0442\u0430: ", None))
        self.fromDateLineEdit.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"1.1.25", None))
        self.label_10.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"/", None))
        self.toDateLineEdit.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"1.1.25", None))
        self.euroPerMinNightLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.euroPerMinDayLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.levaPerMinDayLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0.1081", None))
        self.label_9.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u20ac/\u043c\u0438\u043d. \u0414\u0435\u043d", None))
        self.levaPerMinNightLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0.1081", None))
        self.label_7.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u043b\u0432/\u043c\u0438\u043d. \u0414\u0435\u043d", None))
        self.label_35.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u043b\u0432/\u043c\u0438\u043d. \u041d\u043e\u0449", None))
        self.label_40.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u20ac/\u043c\u0438\u043d. \u041d\u043e\u0449", None))
        self.label_42.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041e\u0431\u0449\u043e \u0440\u0435\u0434\u043e\u0432\u0435:", None))
        self.totalViewRows.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_36.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0420\u0435\u0434\u043e\u0432\u0435:", None))
        self.totalSelectedRows.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_38.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041b\u0432.:", None))
        self.totalLevaLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_37.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u20ac:", None))
        self.totalEuroLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0.0", None))
        self.label_39.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0421\u0440. \u043b\u0432.:", None))
        self.avrLevaLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0.0", None))
        self.label_43.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0421\u0440. \u20ac:", None))
        self.avrEuroLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0.0", None))
    # retranslateUi

