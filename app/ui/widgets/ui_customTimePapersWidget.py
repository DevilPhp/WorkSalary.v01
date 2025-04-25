# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customTimePapersWidgetUnvvDQ.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateEdit, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QTimeEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_customTimePapersWidget(object):
    def setupUi(self, customTimePapersWidget):
        if not customTimePapersWidget.objectName():
            customTimePapersWidget.setObjectName(u"customTimePapersWidget")
        customTimePapersWidget.resize(1116, 915)
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
"#modelHolder QLabel, #newModelInfoHolder * , #widget_11 *{\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"#optionsHolder, #optionsHolder_2 {\n"
"	border-bottom: 2px dashed #7c9399;\n"
"}\n"
"\n"
"#page"
                        "Title {\n"
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
"}\n"
"QComboBox::item{\n"
"	color: #324b4c;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	height: 11px;  \n"
"	border: 4px solid transparent;\n"
"	padding: 0px 8px"
                        " 0px 8px;\n"
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
        self.workerHolder = QWidget(self.workerInfoHolder)
        self.workerHolder.setObjectName(u"workerHolder")
        self.workerHolder.setMinimumSize(QSize(320, 0))
        self.verticalLayout_5 = QVBoxLayout(self.workerHolder)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.workerHolder)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"* {\n"
"	font-size: 11pt;\n"
"}")

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_7 = QWidget(self.workerHolder)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_7 = QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.modeLayout = QFormLayout()
        self.modeLayout.setObjectName(u"modeLayout")
        self.modeLayout.setHorizontalSpacing(10)
        self.modeLayout.setVerticalSpacing(10)
        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName(u"label_2")

        self.modeLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.workerNameLineEdit = QLineEdit(self.widget_7)
        self.workerNameLineEdit.setObjectName(u"workerNameLineEdit")

        self.modeLayout.setWidget(0, QFormLayout.FieldRole, self.workerNameLineEdit)

        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")

        self.modeLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.workerLastNameLineEdit = QLineEdit(self.widget_7)
        self.workerLastNameLineEdit.setObjectName(u"workerLastNameLineEdit")
        self.workerLastNameLineEdit.setFocusPolicy(Qt.NoFocus)
        self.workerLastNameLineEdit.setReadOnly(True)

        self.modeLayout.setWidget(1, QFormLayout.FieldRole, self.workerLastNameLineEdit)

        self.label_13 = QLabel(self.widget_7)
        self.label_13.setObjectName(u"label_13")

        self.modeLayout.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.workerNumberLineEdit = QLineEdit(self.widget_7)
        self.workerNumberLineEdit.setObjectName(u"workerNumberLineEdit")
        self.workerNumberLineEdit.setFocusPolicy(Qt.NoFocus)
        self.workerNumberLineEdit.setReadOnly(True)

        self.modeLayout.setWidget(2, QFormLayout.FieldRole, self.workerNumberLineEdit)


        self.verticalLayout_7.addLayout(self.modeLayout)


        self.verticalLayout_5.addWidget(self.widget_7)


        self.horizontalLayout_5.addWidget(self.workerHolder, 0, Qt.AlignLeft|Qt.AlignTop)

        self.workerShiftsHolder = QWidget(self.workerInfoHolder)
        self.workerShiftsHolder.setObjectName(u"workerShiftsHolder")
        self.verticalLayout_6 = QVBoxLayout(self.workerShiftsHolder)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.workerShiftsHolder)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_9 = QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_12)


        self.verticalLayout_6.addWidget(self.widget_3)

        self.widget_11 = QWidget(self.workerShiftsHolder)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_10 = QVBoxLayout(self.widget_11)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 5)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_12.setSpacing(15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.widget_12)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_12.addWidget(self.label_22)

        self.workerPositionLineEdit = QLabel(self.widget_12)
        self.workerPositionLineEdit.setObjectName(u"workerPositionLineEdit")

        self.horizontalLayout_12.addWidget(self.workerPositionLineEdit)


        self.gridLayout.addWidget(self.widget_12, 0, 0, 1, 1, Qt.AlignLeft)

        self.widget_13 = QWidget(self.widget_11)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.widget_13)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_13.addWidget(self.label_26)

        self.workerPlaceLineEdit = QLabel(self.widget_13)
        self.workerPlaceLineEdit.setObjectName(u"workerPlaceLineEdit")

        self.horizontalLayout_13.addWidget(self.workerPlaceLineEdit)


        self.gridLayout.addWidget(self.widget_13, 0, 1, 1, 1, Qt.AlignLeft)


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
        self.horizontalLayout_17 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.newModelLayout = QGridLayout()
        self.newModelLayout.setSpacing(10)
        self.newModelLayout.setObjectName(u"newModelLayout")
        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")

        self.newModelLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.overtimeStartWidget = QWidget(self.widget_6)
        self.overtimeStartWidget.setObjectName(u"overtimeStartWidget")
        self.horizontalLayout_6 = QHBoxLayout(self.overtimeStartWidget)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.overtimeStart = QTimeEdit(self.overtimeStartWidget)
        self.overtimeStart.setObjectName(u"overtimeStart")

        self.horizontalLayout_6.addWidget(self.overtimeStart)

        self.label_19 = QLabel(self.overtimeStartWidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_6.addWidget(self.label_19)


        self.newModelLayout.addWidget(self.overtimeStartWidget, 2, 3, 1, 1)

        self.label_27 = QLabel(self.widget_6)
        self.label_27.setObjectName(u"label_27")

        self.newModelLayout.addWidget(self.label_27, 0, 8, 1, 1)

        self.shiftTotalMins = QLabel(self.widget_6)
        self.shiftTotalMins.setObjectName(u"shiftTotalMins")

        self.newModelLayout.addWidget(self.shiftTotalMins, 0, 7, 1, 1)

        self.label_18 = QLabel(self.widget_6)
        self.label_18.setObjectName(u"label_18")

        self.newModelLayout.addWidget(self.label_18, 2, 4, 1, 1)

        self.hourlyStartWidget = QWidget(self.widget_6)
        self.hourlyStartWidget.setObjectName(u"hourlyStartWidget")
        self.horizontalLayout_10 = QHBoxLayout(self.hourlyStartWidget)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.hourlyStart = QTimeEdit(self.hourlyStartWidget)
        self.hourlyStart.setObjectName(u"hourlyStart")

        self.horizontalLayout_10.addWidget(self.hourlyStart)

        self.label_16 = QLabel(self.hourlyStartWidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_10.addWidget(self.label_16)


        self.newModelLayout.addWidget(self.hourlyStartWidget, 1, 3, 1, 1)

        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")

        self.newModelLayout.addWidget(self.label_3, 2, 2, 1, 1)

        self.label_23 = QLabel(self.widget_6)
        self.label_23.setObjectName(u"label_23")

        self.newModelLayout.addWidget(self.label_23, 1, 6, 1, 1)

        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")

        self.newModelLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.isOvertimeWorking = QCheckBox(self.widget_6)
        self.isOvertimeWorking.setObjectName(u"isOvertimeWorking")
        self.isOvertimeWorking.setFocusPolicy(Qt.NoFocus)

        self.newModelLayout.addWidget(self.isOvertimeWorking, 2, 1, 1, 1)

        self.overtimeEndWidget = QWidget(self.widget_6)
        self.overtimeEndWidget.setObjectName(u"overtimeEndWidget")
        self.horizontalLayout_7 = QHBoxLayout(self.overtimeEndWidget)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.overtimeEnd = QTimeEdit(self.overtimeEndWidget)
        self.overtimeEnd.setObjectName(u"overtimeEnd")
        self.overtimeEnd.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_7.addWidget(self.overtimeEnd)

        self.label_20 = QLabel(self.overtimeEndWidget)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_7.addWidget(self.label_20)


        self.newModelLayout.addWidget(self.overtimeEndWidget, 2, 5, 1, 1)

        self.label_7 = QLabel(self.widget_6)
        self.label_7.setObjectName(u"label_7")

        self.newModelLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.overtimeTotalMins = QLabel(self.widget_6)
        self.overtimeTotalMins.setObjectName(u"overtimeTotalMins")

        self.newModelLayout.addWidget(self.overtimeTotalMins, 2, 7, 1, 1)

        self.hourlyTotalMins = QLabel(self.widget_6)
        self.hourlyTotalMins.setObjectName(u"hourlyTotalMins")

        self.newModelLayout.addWidget(self.hourlyTotalMins, 1, 7, 1, 1)

        self.label_28 = QLabel(self.widget_6)
        self.label_28.setObjectName(u"label_28")

        self.newModelLayout.addWidget(self.label_28, 1, 8, 1, 1)

        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")

        self.newModelLayout.addWidget(self.label_8, 1, 2, 1, 1)

        self.label_24 = QLabel(self.widget_6)
        self.label_24.setObjectName(u"label_24")

        self.newModelLayout.addWidget(self.label_24, 2, 6, 1, 1)

        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")

        self.newModelLayout.addWidget(self.label_10, 0, 4, 1, 1)

        self.label_21 = QLabel(self.widget_6)
        self.label_21.setObjectName(u"label_21")

        self.newModelLayout.addWidget(self.label_21, 0, 6, 1, 1)

        self.label_29 = QLabel(self.widget_6)
        self.label_29.setObjectName(u"label_29")

        self.newModelLayout.addWidget(self.label_29, 2, 8, 1, 1)

        self.isHourlyWorking = QCheckBox(self.widget_6)
        self.isHourlyWorking.setObjectName(u"isHourlyWorking")
        self.isHourlyWorking.setFocusPolicy(Qt.NoFocus)
        self.isHourlyWorking.setChecked(False)

        self.newModelLayout.addWidget(self.isHourlyWorking, 1, 1, 1, 1)

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

        self.label_11 = QLabel(self.widget_6)
        self.label_11.setObjectName(u"label_11")

        self.newModelLayout.addWidget(self.label_11, 1, 4, 1, 1)

        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")

        self.newModelLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.hourlyEndWidget = QWidget(self.widget_6)
        self.hourlyEndWidget.setObjectName(u"hourlyEndWidget")
        self.horizontalLayout_11 = QHBoxLayout(self.hourlyEndWidget)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.hourlyEnd = QTimeEdit(self.hourlyEndWidget)
        self.hourlyEnd.setObjectName(u"hourlyEnd")

        self.horizontalLayout_11.addWidget(self.hourlyEnd)

        self.label_17 = QLabel(self.hourlyEndWidget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_11.addWidget(self.label_17)


        self.newModelLayout.addWidget(self.hourlyEndWidget, 1, 5, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_6)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.newModelLayout.addWidget(self.pushButton_2, 0, 9, 1, 1)

        self.shiftNameLineEdit = QComboBox(self.widget_6)
        self.shiftNameLineEdit.setObjectName(u"shiftNameLineEdit")
        self.shiftNameLineEdit.setEditable(True)
        self.shiftNameLineEdit.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.shiftNameLineEdit.setIconSize(QSize(12, 12))

        self.newModelLayout.addWidget(self.shiftNameLineEdit, 0, 1, 1, 1)


        self.horizontalLayout_17.addLayout(self.newModelLayout)


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

        self.widget_5 = QWidget(self.operationsHolder)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.widget_5)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_15.addWidget(self.label_25, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.timePaperDateEdit = QDateEdit(self.widget_5)
        self.timePaperDateEdit.setObjectName(u"timePaperDateEdit")
        self.timePaperDateEdit.setFocusPolicy(Qt.WheelFocus)
        self.timePaperDateEdit.setFrame(False)
        self.timePaperDateEdit.setAlignment(Qt.AlignCenter)
        self.timePaperDateEdit.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.timePaperDateEdit.setMinimumDateTime(QDateTime(QDate(1990, 9, 10), QTime(0, 0, 0)))

        self.horizontalLayout_15.addWidget(self.timePaperDateEdit)

        self.calendarBtn = QPushButton(self.widget_5)
        self.calendarBtn.setObjectName(u"calendarBtn")
        self.calendarBtn.setFocusPolicy(Qt.NoFocus)
        self.calendarBtn.setStyleSheet(u"*{\n"
"	padding: 0px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/Calendar--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.calendarBtn.setIcon(icon1)
        self.calendarBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.calendarBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.widget_5, 0, Qt.AlignLeft)

        self.modelAndOperationHolder = QWidget(self.operationsHolder)
        self.modelAndOperationHolder.setObjectName(u"modelAndOperationHolder")
        self.verticalLayout_13 = QVBoxLayout(self.modelAndOperationHolder)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.timePapersHolder = QWidget(self.modelAndOperationHolder)
        self.timePapersHolder.setObjectName(u"timePapersHolder")
        self.timePapersHolder.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.timePapersHolder)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.operationsLayout = QGridLayout()
        self.operationsLayout.setObjectName(u"operationsLayout")
        self.operationsLayout.setHorizontalSpacing(25)
        self.operationsLayout.setVerticalSpacing(8)
        self.addNewTimePaperBtn = QPushButton(self.timePapersHolder)
        self.addNewTimePaperBtn.setObjectName(u"addNewTimePaperBtn")
        self.addNewTimePaperBtn.setFocusPolicy(Qt.NoFocus)
        self.addNewTimePaperBtn.setStyleSheet(u"*{\n"
"	padding: 0px;\n"
"	background-color: #dfdfdf;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/app/assets/icons/Check-Square--Streamline-Solar-Broken-#008b69.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addNewTimePaperBtn.setIcon(icon2)
        self.addNewTimePaperBtn.setIconSize(QSize(24, 24))

        self.operationsLayout.addWidget(self.addNewTimePaperBtn, 4, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.clientModelsLineEdit = QLineEdit(self.timePapersHolder)
        self.clientModelsLineEdit.setObjectName(u"clientModelsLineEdit")
        self.clientModelsLineEdit.setMinimumSize(QSize(260, 0))

        self.operationsLayout.addWidget(self.clientModelsLineEdit, 2, 1, 1, 1)

        self.modelOperationLineEdit = QLineEdit(self.timePapersHolder)
        self.modelOperationLineEdit.setObjectName(u"modelOperationLineEdit")
        self.modelOperationLineEdit.setReadOnly(True)

        self.operationsLayout.addWidget(self.modelOperationLineEdit, 3, 1, 1, 1)

        self.label_34 = QLabel(self.timePapersHolder)
        self.label_34.setObjectName(u"label_34")

        self.operationsLayout.addWidget(self.label_34, 2, 4, 1, 1)

        self.modelPiecesLineEdit = QLineEdit(self.timePapersHolder)
        self.modelPiecesLineEdit.setObjectName(u"modelPiecesLineEdit")
        self.modelPiecesLineEdit.setMinimumSize(QSize(200, 0))
        self.modelPiecesLineEdit.setReadOnly(True)

        self.operationsLayout.addWidget(self.modelPiecesLineEdit, 2, 3, 1, 1)

        self.piecesTimeLineEdit = QLineEdit(self.timePapersHolder)
        self.piecesTimeLineEdit.setObjectName(u"piecesTimeLineEdit")
        self.piecesTimeLineEdit.setReadOnly(True)

        self.operationsLayout.addWidget(self.piecesTimeLineEdit, 3, 3, 1, 1)

        self.label_30 = QLabel(self.timePapersHolder)
        self.label_30.setObjectName(u"label_30")

        self.operationsLayout.addWidget(self.label_30, 2, 0, 1, 1)

        self.label_33 = QLabel(self.timePapersHolder)
        self.label_33.setObjectName(u"label_33")

        self.operationsLayout.addWidget(self.label_33, 3, 2, 1, 1)

        self.widget_14 = QWidget(self.timePapersHolder)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)

        self.operationsLayout.addWidget(self.widget_14, 0, 0, 1, 1, Qt.AlignLeft)

        self.isDefaultTimeCheckBox = QCheckBox(self.timePapersHolder)
        self.isDefaultTimeCheckBox.setObjectName(u"isDefaultTimeCheckBox")
        self.isDefaultTimeCheckBox.setFocusPolicy(Qt.NoFocus)
        self.isDefaultTimeCheckBox.setChecked(True)

        self.operationsLayout.addWidget(self.isDefaultTimeCheckBox, 2, 5, 1, 1)

        self.label_35 = QLabel(self.timePapersHolder)
        self.label_35.setObjectName(u"label_35")

        self.operationsLayout.addWidget(self.label_35, 3, 4, 1, 1)

        self.timeForPieceLineEdit = QLineEdit(self.timePapersHolder)
        self.timeForPieceLineEdit.setObjectName(u"timeForPieceLineEdit")
        self.timeForPieceLineEdit.setMaximumSize(QSize(55, 16777215))
        self.timeForPieceLineEdit.setFocusPolicy(Qt.NoFocus)
        self.timeForPieceLineEdit.setReadOnly(True)

        self.operationsLayout.addWidget(self.timeForPieceLineEdit, 3, 5, 1, 1)

        self.label_31 = QLabel(self.timePapersHolder)
        self.label_31.setObjectName(u"label_31")

        self.operationsLayout.addWidget(self.label_31, 3, 0, 1, 1)

        self.label_32 = QLabel(self.timePapersHolder)
        self.label_32.setObjectName(u"label_32")

        self.operationsLayout.addWidget(self.label_32, 2, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.operationsLayout)


        self.verticalLayout_13.addWidget(self.timePapersHolder)

        self.optionsHolder_2 = QFrame(self.modelAndOperationHolder)
        self.optionsHolder_2.setObjectName(u"optionsHolder_2")
        self.optionsHolder_2.setFrameShape(QFrame.StyledPanel)
        self.optionsHolder_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.optionsHolder_2)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 10)

        self.verticalLayout_13.addWidget(self.optionsHolder_2)


        self.verticalLayout_2.addWidget(self.modelAndOperationHolder)


        self.verticalLayout_4.addWidget(self.operationsHolder)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(customTimePapersWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1104, 472))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.timePaperTableHolder = QWidget(self.scrollAreaWidgetContents)
        self.timePaperTableHolder.setObjectName(u"timePaperTableHolder")
        self.verticalLayout_11 = QVBoxLayout(self.timePaperTableHolder)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")

        self.verticalLayout_12.addWidget(self.timePaperTableHolder)

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
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_18.addWidget(self.widget_2)

        self.widget_8 = QWidget(self.statusBar)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_18.addWidget(self.widget_8, 0, Qt.AlignLeft)

        self.widget_9 = QWidget(self.statusBar)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_20 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_20.setSpacing(45)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 20, 0)
        self.widget_16 = QWidget(self.widget_9)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_24.setSpacing(5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.widget_16)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_24.addWidget(self.label_36)

        self.label_37 = QLabel(self.widget_16)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_24.addWidget(self.label_37)


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

        self.label_39 = QLabel(self.widget_10)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_22.addWidget(self.label_39)


        self.horizontalLayout_20.addWidget(self.widget_10)

        self.widget_15 = QWidget(self.widget_9)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_23 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.widget_15)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_23.addWidget(self.label_41)

        self.label_40 = QLabel(self.widget_15)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_23.addWidget(self.label_40)


        self.horizontalLayout_20.addWidget(self.widget_15)


        self.horizontalLayout_18.addWidget(self.widget_9, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.statusBar)


        self.retranslateUi(customTimePapersWidget)

        QMetaObject.connectSlotsByName(customTimePapersWidget)
    # setupUi

    def retranslateUi(self, customTimePapersWidget):
        customTimePapersWidget.setWindowTitle(QCoreApplication.translate("customTimePapersWidget", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041b\u0418\u0421\u0422\u041e\u0412\u0415 \u0417\u0410 \u0412\u0420\u0415\u041c\u0415", None))
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customTimePapersWidget", u"admin", None))
        self.label.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a", None))
        self.label_2.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0418\u043c\u0435:", None))
        self.workerNameLineEdit.setText("")
        self.workerNameLineEdit.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.label_13.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041d\u043e\u043c\u0435\u0440:", None))
        self.label_12.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0420\u0430\u0431\u043e\u0442\u043d\u043e \u0412\u0440\u0435\u043c\u0435", None))
        self.label_22.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0414\u043b\u044a\u0436\u043d\u043e\u0441\u0442:", None))
        self.workerPositionLineEdit.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041d\u0435 \u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e", None))
        self.label_26.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0420\u0430\u0431.\u041c\u044f\u0441\u0442\u043e:", None))
        self.workerPlaceLineEdit.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041d\u0435 \u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e", None))
        self.label_5.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0421\u043c\u044f\u043d\u0430:", None))
        self.label_19.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0447.", None))
        self.label_27.setText(QCoreApplication.translate("customTimePapersWidget", u"\u043c\u0438\u043d.", None))
        self.shiftTotalMins.setText(QCoreApplication.translate("customTimePapersWidget", u"480", None))
        self.label_18.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041a\u0440\u0430\u0439:", None))
        self.label_16.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0447.", None))
        self.label_3.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.label_23.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041e\u0431\u0449\u043e", None))
        self.label_9.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041f\u043e\u0447\u0430\u0441\u043e\u0432\u0430 \u0420\u0430\u0431.:", None))
        self.isOvertimeWorking.setText("")
        self.label_20.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0447.", None))
        self.label_7.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.overtimeTotalMins.setText(QCoreApplication.translate("customTimePapersWidget", u"0", None))
        self.hourlyTotalMins.setText(QCoreApplication.translate("customTimePapersWidget", u"0", None))
        self.label_28.setText(QCoreApplication.translate("customTimePapersWidget", u"\u043c\u0438\u043d.", None))
        self.label_8.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041d\u0430\u0447\u0430\u043b\u043e:", None))
        self.label_24.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041e\u0431\u0449\u043e", None))
        self.label_10.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041a\u0440\u0430\u0439:", None))
        self.label_21.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041e\u0431\u0449\u043e:", None))
        self.label_29.setText(QCoreApplication.translate("customTimePapersWidget", u"\u043c\u0438\u043d.", None))
        self.isHourlyWorking.setText("")
        self.label_15.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0447.", None))
        self.label_14.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0447.", None))
        self.label_11.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041a\u0440\u0430\u0439:", None))
        self.label_6.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0418\u0437\u0432\u044a\u043d\u0440\u0435\u0434\u043d\u0430 \u0420\u0430\u0431.:", None))
        self.label_17.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0447.", None))
        self.pushButton_2.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041d\u043e\u0432\u0430 \u0421\u043c\u044f\u043d\u0430", None))
        self.shiftNameLineEdit.setPlaceholderText(QCoreApplication.translate("customTimePapersWidget", u"\u0420\u0435\u0434\u043e\u0432\u043d\u0430", None))
        self.label_25.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0414\u0430\u0442\u0430: ", None))
        self.timePaperDateEdit.setDisplayFormat(QCoreApplication.translate("customTimePapersWidget", u"d.M.yy '\u0433.'", None))
        self.calendarBtn.setText("")
        self.addNewTimePaperBtn.setText("")
        self.label_34.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0412\u0440\u0435\u043c\u0435\u041f\u043e\u041f\u043e\u0434.", None))
        self.piecesTimeLineEdit.setText(QCoreApplication.translate("customTimePapersWidget", u"0", None))
        self.label_30.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041c\u043e\u0434\u0435\u043b:", None))
        self.label_33.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0412\u0440\u0435\u043c\u0435", None))
        self.isDefaultTimeCheckBox.setText("")
        self.label_35.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0412\u0440\u0435\u043c\u0435 \u0437\u0430 \u0431\u0440.", None))
        self.label_31.setText(QCoreApplication.translate("customTimePapersWidget", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.label_32.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0411\u0440\u043e\u0439\u043a\u0438", None))
        self.label_36.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0420\u0435\u0434\u043e\u0432\u0435", None))
        self.label_37.setText(QCoreApplication.translate("customTimePapersWidget", u"0", None))
        self.label_38.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0412\u0440\u0435\u043c\u0435", None))
        self.label_39.setText(QCoreApplication.translate("customTimePapersWidget", u"0", None))
        self.label_41.setText(QCoreApplication.translate("customTimePapersWidget", u"\u0412\u0440\u0435\u043c\u0435", None))
        self.label_40.setText(QCoreApplication.translate("customTimePapersWidget", u"0", None))
    # retranslateUi

