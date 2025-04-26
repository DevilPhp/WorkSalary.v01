# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customShiftsEditWidgetyPVmlQ.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QTimeEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_customTimePapersWidget(object):
    def setupUi(self, customTimePapersWidget):
        if not customTimePapersWidget.objectName():
            customTimePapersWidget.setObjectName(u"customTimePapersWidget")
        customTimePapersWidget.resize(967, 800)
        customTimePapersWidget.setMinimumSize(QSize(900, 800))
        customTimePapersWidget.setStyleSheet(u"*{\n"
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
"#statusBar {\n"
"	border: 1px solid #7c9399;\n"
"}\n"
"#statusBar *{\n"
"	font-size: 9pt;\n"
"}\n"
"\n"
"#avrTimePerPiece, #totalSelectedPieces, #totalSelectedTime, #totalSelectedRows, #totalViewRows, #totalProducedPieces {\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"#modelHolder QLabel, #newModelInfo"
                        "Holder * , #widget_11 *{\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"#optionsHolder, #optionsHolder_2 {\n"
"	border-bottom: 2px dashed #7c9399;\n"
"}\n"
"\n"
"#pageTitle {\n"
"	font: 700 13pt \"Segoe UI\";\n"
"}\n"
"\n"
"#userIcon, #calendarBtn {\n"
"	background-color: #dfdfdf;\n"
"}\n"
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
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #dfdfdf;\n"
"	border-bottom: 2px solid #7c9399;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	image: url(':/icons/app/assets/icons/Alt-Arrow-Down--Streamline-Solar-Broken.svg');\n"
"	width: 18px;\n"
"	height: 18px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	color: #2b2b2c;\n"
"	font: 720 10.5pt \"Segoe UI\";\n"
"	border-radius: 0px;\n"
"	alternate-background-color: #2c313c;\n"
"}\n"
"QComboBox::item:selected{\n"
"	color: #2b2b2c;\n"
"	font: 900 10.5pt \"Segoe UI\";\n"
"	border-radius: 0px;\n"
""
                        "}\n"
"QComboBox::item{\n"
"	color: #324b4c;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	height: 11px;  \n"
"	border: 4px solid transparent;\n"
"	padding: 0px 8px 0px 8px;\n"
"}")
        self.verticalLayout = QVBoxLayout(customTimePapersWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(customTimePapersWidget)
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
        self.userIcon = QPushButton(self.userHolder)
        self.userIcon.setObjectName(u"userIcon")
        self.userIcon.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/User--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userIcon.setIcon(icon)
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

        self.shiftNameLineEdit = QComboBox(self.widget_6)
        self.shiftNameLineEdit.setObjectName(u"shiftNameLineEdit")
        self.shiftNameLineEdit.setEditable(True)
        self.shiftNameLineEdit.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.shiftNameLineEdit.setIconSize(QSize(12, 12))

        self.newModelLayout.addWidget(self.shiftNameLineEdit, 0, 1, 1, 1)

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


        self.verticalLayout_3.addLayout(self.newModelLayout)

        self.acceptWorkingShifts = QPushButton(self.widget_6)
        self.acceptWorkingShifts.setObjectName(u"acceptWorkingShifts")
        self.acceptWorkingShifts.setFocusPolicy(Qt.NoFocus)
        self.acceptWorkingShifts.setStyleSheet(u"*{\n"
"	padding: 0px;\n"
"	background-color: #dfdfdf;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/Check-Square--Streamline-Solar-Broken-#008b69.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.acceptWorkingShifts.setIcon(icon1)
        self.acceptWorkingShifts.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.acceptWorkingShifts)


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

        self.scrollArea = QScrollArea(customTimePapersWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 955, 526))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.workingShiftsTable = QWidget(self.scrollAreaWidgetContents)
        self.workingShiftsTable.setObjectName(u"workingShiftsTable")
        self.verticalLayout_11 = QVBoxLayout(self.workingShiftsTable)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 0)

        self.verticalLayout_12.addWidget(self.workingShiftsTable)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.statusBar = QWidget(customTimePapersWidget)
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
        self.widget_19 = QWidget(self.widget_8)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_27.setSpacing(5)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.widget_19)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_27.addWidget(self.label_43)

        self.totalProducedPieces = QLabel(self.widget_19)
        self.totalProducedPieces.setObjectName(u"totalProducedPieces")

        self.horizontalLayout_27.addWidget(self.totalProducedPieces)


        self.horizontalLayout_19.addWidget(self.widget_19)


        self.horizontalLayout_18.addWidget(self.widget_8, 0, Qt.AlignHCenter)

        self.widget_9 = QWidget(self.statusBar)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_20 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
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


        self.horizontalLayout_20.addWidget(self.widget_16)

        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.widget_10)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_22.addWidget(self.label_38)

        self.totalSelectedPieces = QLabel(self.widget_10)
        self.totalSelectedPieces.setObjectName(u"totalSelectedPieces")

        self.horizontalLayout_22.addWidget(self.totalSelectedPieces)


        self.horizontalLayout_20.addWidget(self.widget_10)

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

        self.totalSelectedTime = QLabel(self.widget_15)
        self.totalSelectedTime.setObjectName(u"totalSelectedTime")

        self.horizontalLayout_23.addWidget(self.totalSelectedTime)


        self.horizontalLayout_20.addWidget(self.widget_15)

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

        self.avrTimePerPiece = QLabel(self.widget_18)
        self.avrTimePerPiece.setObjectName(u"avrTimePerPiece")

        self.horizontalLayout_26.addWidget(self.avrTimePerPiece)


        self.horizontalLayout_20.addWidget(self.widget_18)


        self.horizontalLayout_18.addWidget(self.widget_9, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.statusBar)


        self.retranslateUi(customTimePapersWidget)

        QMetaObject.connectSlotsByName(customTimePapersWidget)
    # setupUi

    def retranslateUi(self, customTimePapersWidget):
        customTimePapersWidget.setWindowTitle(QCoreApplication.translate("customTimePapersWidget", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0420\u0410\u0411\u041e\u0422\u041d\u0418 \u0421\u041c\u0415\u041d\u0418", None))
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customTimePapersWidget", u"admin", None))
        self.label_21.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041e\u0431\u0449\u043e:", None))
        self.label_15.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0447.", None))
        self.label_10.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041a\u0440\u0430\u0439:", None))
        self.label_14.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0447.", None))
        self.label_5.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0421\u043c\u044f\u043d\u0430:", None))
        self.shiftTotalMins.setText(QCoreApplication.translate("customTimePapersWidget", u"480", None))
        self.label_27.setText(QCoreApplication.translate("customTimePapersWidget", u"\u043c\u0438\u043d.", None))
        self.label_7.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.shiftNameLineEdit.setPlaceholderText(QCoreApplication.translate("customTimePapersWidget", u"\u0420\u0435\u0434\u043e\u0432\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041f\u043e\u043a\u0438\u0447\u043a\u0430:", None))
        self.shiftBreakLineEdit.setPlaceholderText(QCoreApplication.translate("customTimePapersWidget", u"60", None))
        self.label_2.setText(QCoreApplication.translate("customTimePapersWidget", u"\u043c\u0438\u043d.", None))
        self.acceptWorkingShifts.setText("")
        self.label_42.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041e\u0431\u0449\u043e \u0440\u0435\u0434\u043e\u0432\u0435:", None))
        self.totalViewRows.setText(QCoreApplication.translate("customTimePapersWidget", u"0", None))
        self.label_43.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0417\u0430\u0432\u044a\u0440\u0448\u0435\u043d\u0438 \u0431\u0440 \u0437\u0430 \u0434\u0435\u043d\u044f:", None))
        self.totalProducedPieces.setText(QCoreApplication.translate("customTimePapersWidget", u"0", None))
        self.label_36.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0420\u0435\u0434\u043e\u0432\u0435:", None))
        self.totalSelectedRows.setText(QCoreApplication.translate("customTimePapersWidget", u"0", None))
        self.label_38.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0411\u0440\u043e\u0439\u043a\u0438:", None))
        self.totalSelectedPieces.setText(QCoreApplication.translate("customTimePapersWidget", u"0", None))
        self.label_37.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0412\u0440\u0435\u043c\u0435:", None))
        self.totalSelectedTime.setText(QCoreApplication.translate("customTimePapersWidget", u"0.0", None))
        self.label_39.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0421\u0440. \u0412\u0440\u0435\u043c\u0435 \u0437\u0430 \u0431\u0440.:", None))
        self.avrTimePerPiece.setText(QCoreApplication.translate("customTimePapersWidget", u"0.0", None))
    # retranslateUi

