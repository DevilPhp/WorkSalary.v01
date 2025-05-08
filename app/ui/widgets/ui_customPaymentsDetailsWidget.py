# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customPaymentsDetailsWidgetsxJPKs.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_customPaymentsDetailsWidget(object):
    def setupUi(self, customPaymentsDetailsWidget):
        if not customPaymentsDetailsWidget.objectName():
            customPaymentsDetailsWidget.setObjectName(u"customPaymentsDetailsWidget")
        customPaymentsDetailsWidget.resize(1173, 915)
        customPaymentsDetailsWidget.setMinimumSize(QSize(900, 800))
        customPaymentsDetailsWidget.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 700 10pt \"Segoe UI\";\n"
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
"QLineEdit{\n"
"	border: none;\n"
"	border-bottom: 1px solid #7c9399;\n"
"	max-width: 40px;\n"
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
"#modelHolder QLabel, #newModelInfoHolder *{\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"#optionsHolder, #optionsHolder_2 {\n"
"	border-"
                        "bottom: 2px dashed #7c9399;\n"
"}\n"
"\n"
"#pageTitle {\n"
"	font: 700 13pt \"Segoe UI\";\n"
"}\n"
"\n"
"#userIcon, #fromCalendarBtn, #toCalendarBtn {\n"
"	background-color: #dfdfdf;\n"
"}\n"
"\n"
"#usernameLabel {\n"
"	font-size: 11pt;\n"
"}")
        self.verticalLayout = QVBoxLayout(customPaymentsDetailsWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(customPaymentsDetailsWidget)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.workerHolder.sizePolicy().hasHeightForWidth())
        self.workerHolder.setSizePolicy(sizePolicy1)
        self.workerHolder.setMinimumSize(QSize(320, 100))
        self.horizontalLayout_9 = QHBoxLayout(self.workerHolder)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.workerInfoLayout = QGridLayout()
        self.workerInfoLayout.setObjectName(u"workerInfoLayout")
        self.workerInfoLayout.setHorizontalSpacing(8)
        self.workerInfoLayout.setVerticalSpacing(5)
        self.workerOvertimeLabel = QLabel(self.workerHolder)
        self.workerOvertimeLabel.setObjectName(u"workerOvertimeLabel")

        self.workerInfoLayout.addWidget(self.workerOvertimeLabel, 2, 8, 1, 1)

        self.label_3 = QLabel(self.workerHolder)
        self.label_3.setObjectName(u"label_3")

        self.workerInfoLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_15 = QLabel(self.workerHolder)
        self.label_15.setObjectName(u"label_15")

        self.workerInfoLayout.addWidget(self.label_15, 2, 5, 1, 1)

        self.workerPositionLabel = QLabel(self.workerHolder)
        self.workerPositionLabel.setObjectName(u"workerPositionLabel")
        self.workerPositionLabel.setMinimumSize(QSize(160, 0))

        self.workerInfoLayout.addWidget(self.workerPositionLabel, 2, 3, 1, 1)

        self.label_18 = QLabel(self.workerHolder)
        self.label_18.setObjectName(u"label_18")

        self.workerInfoLayout.addWidget(self.label_18, 2, 9, 1, 1)

        self.label_12 = QLabel(self.workerHolder)
        self.label_12.setObjectName(u"label_12")

        self.workerInfoLayout.addWidget(self.label_12, 0, 7, 1, 1)

        self.label_19 = QLabel(self.workerHolder)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(35, 0))

        self.workerInfoLayout.addWidget(self.label_19, 0, 10, 1, 1)

        self.label_30 = QLabel(self.workerHolder)
        self.label_30.setObjectName(u"label_30")

        self.workerInfoLayout.addWidget(self.label_30, 0, 13, 1, 1)

        self.workerWorkingTimeLabel = QLabel(self.workerHolder)
        self.workerWorkingTimeLabel.setObjectName(u"workerWorkingTimeLabel")
        self.workerWorkingTimeLabel.setMinimumSize(QSize(35, 0))

        self.workerInfoLayout.addWidget(self.workerWorkingTimeLabel, 0, 8, 1, 1)

        self.workerEfficLabel = QLabel(self.workerHolder)
        self.workerEfficLabel.setObjectName(u"workerEfficLabel")

        self.workerInfoLayout.addWidget(self.workerEfficLabel, 2, 6, 1, 1)

        self.label_2 = QLabel(self.workerHolder)
        self.label_2.setObjectName(u"label_2")

        self.workerInfoLayout.addWidget(self.label_2, 1, 5, 1, 1)

        self.label_13 = QLabel(self.workerHolder)
        self.label_13.setObjectName(u"label_13")

        self.workerInfoLayout.addWidget(self.label_13, 1, 7, 1, 1)

        self.label_28 = QLabel(self.workerHolder)
        self.label_28.setObjectName(u"label_28")

        self.workerInfoLayout.addWidget(self.label_28, 1, 12, 1, 1)

        self.workerLastNameLabel = QLabel(self.workerHolder)
        self.workerLastNameLabel.setObjectName(u"workerLastNameLabel")

        self.workerInfoLayout.addWidget(self.workerLastNameLabel, 0, 3, 1, 1)

        self.label_6 = QLabel(self.workerHolder)
        self.label_6.setObjectName(u"label_6")

        self.workerInfoLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.workerNumberLabel = QLabel(self.workerHolder)
        self.workerNumberLabel.setObjectName(u"workerNumberLabel")

        self.workerInfoLayout.addWidget(self.workerNumberLabel, 1, 1, 1, 1)

        self.spacer = QLabel(self.workerHolder)
        self.spacer.setObjectName(u"spacer")
        self.spacer.setMinimumSize(QSize(40, 0))

        self.workerInfoLayout.addWidget(self.spacer, 0, 4, 1, 1)

        self.workerPiecesLabel = QLabel(self.workerHolder)
        self.workerPiecesLabel.setObjectName(u"workerPiecesLabel")
        self.workerPiecesLabel.setMinimumSize(QSize(35, 0))

        self.workerInfoLayout.addWidget(self.workerPiecesLabel, 0, 6, 1, 1)

        self.workerOperationsTypesLabel = QLabel(self.workerHolder)
        self.workerOperationsTypesLabel.setObjectName(u"workerOperationsTypesLabel")

        self.workerInfoLayout.addWidget(self.workerOperationsTypesLabel, 1, 6, 1, 1)

        self.label_5 = QLabel(self.workerHolder)
        self.label_5.setObjectName(u"label_5")

        self.workerInfoLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_24 = QLabel(self.workerHolder)
        self.label_24.setObjectName(u"label_24")

        self.workerInfoLayout.addWidget(self.label_24, 2, 10, 1, 1)

        self.label_8 = QLabel(self.workerHolder)
        self.label_8.setObjectName(u"label_8")

        self.workerInfoLayout.addWidget(self.label_8, 2, 2, 1, 1)

        self.label_14 = QLabel(self.workerHolder)
        self.label_14.setObjectName(u"label_14")

        self.workerInfoLayout.addWidget(self.label_14, 2, 7, 1, 1)

        self.label_23 = QLabel(self.workerHolder)
        self.label_23.setObjectName(u"label_23")

        self.workerInfoLayout.addWidget(self.label_23, 1, 10, 1, 1)

        self.label_20 = QLabel(self.workerHolder)
        self.label_20.setObjectName(u"label_20")

        self.workerInfoLayout.addWidget(self.label_20, 0, 11, 1, 1)

        self.label_21 = QLabel(self.workerHolder)
        self.label_21.setObjectName(u"label_21")

        self.workerInfoLayout.addWidget(self.label_21, 1, 11, 1, 1)

        self.label_29 = QLabel(self.workerHolder)
        self.label_29.setObjectName(u"label_29")

        self.workerInfoLayout.addWidget(self.label_29, 2, 12, 1, 1)

        self.label_27 = QLabel(self.workerHolder)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(35, 0))

        self.workerInfoLayout.addWidget(self.label_27, 0, 12, 1, 1)

        self.label_16 = QLabel(self.workerHolder)
        self.label_16.setObjectName(u"label_16")

        self.workerInfoLayout.addWidget(self.label_16, 0, 9, 1, 1)

        self.workerHourPaidTimeLabel = QLabel(self.workerHolder)
        self.workerHourPaidTimeLabel.setObjectName(u"workerHourPaidTimeLabel")

        self.workerInfoLayout.addWidget(self.workerHourPaidTimeLabel, 1, 8, 1, 1)

        self.label_4 = QLabel(self.workerHolder)
        self.label_4.setObjectName(u"label_4")

        self.workerInfoLayout.addWidget(self.label_4, 0, 5, 1, 1)

        self.workerPlaceLabel = QLabel(self.workerHolder)
        self.workerPlaceLabel.setObjectName(u"workerPlaceLabel")
        self.workerPlaceLabel.setMinimumSize(QSize(160, 0))

        self.workerInfoLayout.addWidget(self.workerPlaceLabel, 2, 1, 1, 1)

        self.workerNameLabel = QLabel(self.workerHolder)
        self.workerNameLabel.setObjectName(u"workerNameLabel")

        self.workerInfoLayout.addWidget(self.workerNameLabel, 0, 1, 1, 1)

        self.label_17 = QLabel(self.workerHolder)
        self.label_17.setObjectName(u"label_17")

        self.workerInfoLayout.addWidget(self.label_17, 1, 9, 1, 1)

        self.label = QLabel(self.workerHolder)
        self.label.setObjectName(u"label")

        self.workerInfoLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_22 = QLabel(self.workerHolder)
        self.label_22.setObjectName(u"label_22")

        self.workerInfoLayout.addWidget(self.label_22, 2, 11, 1, 1)

        self.workerWorkingTimeKoefLineEdit = QLineEdit(self.workerHolder)
        self.workerWorkingTimeKoefLineEdit.setObjectName(u"workerWorkingTimeKoefLineEdit")

        self.workerInfoLayout.addWidget(self.workerWorkingTimeKoefLineEdit, 0, 14, 1, 1)

        self.workerHourTimeKoefLineEdit = QLineEdit(self.workerHolder)
        self.workerHourTimeKoefLineEdit.setObjectName(u"workerHourTimeKoefLineEdit")

        self.workerInfoLayout.addWidget(self.workerHourTimeKoefLineEdit, 1, 14, 1, 1)

        self.workerOvertimeKoefLineEdit = QLineEdit(self.workerHolder)
        self.workerOvertimeKoefLineEdit.setObjectName(u"workerOvertimeKoefLineEdit")

        self.workerInfoLayout.addWidget(self.workerOvertimeKoefLineEdit, 2, 14, 1, 1)

        self.label_31 = QLabel(self.workerHolder)
        self.label_31.setObjectName(u"label_31")

        self.workerInfoLayout.addWidget(self.label_31, 1, 13, 1, 1)

        self.label_32 = QLabel(self.workerHolder)
        self.label_32.setObjectName(u"label_32")

        self.workerInfoLayout.addWidget(self.label_32, 2, 13, 1, 1)


        self.horizontalLayout_9.addLayout(self.workerInfoLayout)


        self.horizontalLayout_5.addWidget(self.workerHolder, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.workerInfoHolder, 0, Qt.AlignLeft)

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

        self.verticalLayout_2.addWidget(self.optionsHolder)

        self.widget_5 = QWidget(self.operationsHolder)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setSpacing(65)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_5)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_25 = QLabel(self.widget_12)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_7.addWidget(self.label_25)

        self.label_10 = QLabel(self.widget_12)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)


        self.horizontalLayout_8.addWidget(self.widget_12)

        self.widget_11 = QWidget(self.widget_5)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_26 = QLabel(self.widget_11)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_6.addWidget(self.label_26)

        self.label_11 = QLabel(self.widget_11)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)


        self.horizontalLayout_8.addWidget(self.widget_11)


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

        self.scrollArea = QScrollArea(customPaymentsDetailsWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1161, 613))
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


        self.retranslateUi(customPaymentsDetailsWidget)

        QMetaObject.connectSlotsByName(customPaymentsDetailsWidget)
    # setupUi

    def retranslateUi(self, customPaymentsDetailsWidget):
        customPaymentsDetailsWidget.setWindowTitle(QCoreApplication.translate("customPaymentsDetailsWidget", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0414\u0415\u0422\u0410\u0419\u041b\u0418", None))
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"admin", None))
        self.workerOvertimeLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_3.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.label_15.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0415\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442:", None))
        self.workerPositionLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041d\u0435 \u0435 \u043f\u043e\u0441\u043e\u0447\u0435\u043d\u043e", None))
        self.label_18.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041d\u0430\u0447. \u043b\u0432.:", None))
        self.label_12.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0420\u0430\u0431. \u0412\u0440\u0435\u043c\u0435:", None))
        self.label_19.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_30.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041a\u043e\u0435\u0444.", None))
        self.workerWorkingTimeLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.workerEfficLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_2.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0412\u0438\u0434\u043e\u0432\u0435 \u041e\u043f\u0435\u0440.:", None))
        self.label_13.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041f\u043e\u0447\u0430\u0441. \u0420\u0430\u0431.:", None))
        self.label_28.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.workerLastNameLabel.setText("")
        self.label_6.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0426\u0435\u0445:", None))
        self.workerNumberLabel.setText("")
        self.spacer.setText("")
        self.workerPiecesLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.workerOperationsTypesLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_5.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041d\u043e\u043c\u0435\u0440:", None))
        self.label_24.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_8.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0414\u043b\u044a\u0436\u043d.", None))
        self.label_14.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0418\u0437\u0432\u044a\u043d\u0440\u0435\u0434\u0435\u043d:", None))
        self.label_23.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_20.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041d\u0430\u0447. \u20ac:", None))
        self.label_21.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041d\u0430\u0447. \u20ac:", None))
        self.label_29.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_27.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_16.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041d\u0430\u0447. \u043b\u0432.:", None))
        self.workerHourPaidTimeLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_4.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0411\u0440\u043e\u0439\u043a\u0438:", None))
        self.workerPlaceLabel.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041d\u0435 \u0435 \u043f\u043e\u0441\u043e\u0447\u0435\u043d\u043e", None))
        self.workerNameLabel.setText("")
        self.label_17.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041d\u0430\u0447. \u043b\u0432.:", None))
        self.label.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0418\u043c\u0435:", None))
        self.label_22.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041d\u0430\u0447. \u20ac:", None))
        self.workerWorkingTimeKoefLineEdit.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"1.00", None))
        self.workerWorkingTimeKoefLineEdit.setPlaceholderText(QCoreApplication.translate("customPaymentsDetailsWidget", u"1", None))
        self.workerHourTimeKoefLineEdit.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"1.00", None))
        self.workerOvertimeKoefLineEdit.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"1.00", None))
        self.label_31.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041a\u043e\u0435\u0444.", None))
        self.label_32.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041a\u043e\u0435\u0444.", None))
        self.label_25.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041e\u0442 \u0414\u0430\u0442\u0430: ", None))
        self.label_10.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"1.1.25", None))
        self.label_26.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0414\u043e \u0414\u0430\u0442\u0430: ", None))
        self.label_11.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"1.1.25", None))
        self.label_42.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u041e\u0431\u0449\u043e \u0440\u0435\u0434\u043e\u0432\u0435:", None))
        self.totalViewRows.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_43.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0417\u0430\u0432\u044a\u0440\u0448\u0435\u043d\u0438 \u0431\u0440 \u0437\u0430 \u0434\u0435\u043d\u044f:", None))
        self.totalProducedPieces.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_36.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0420\u0435\u0434\u043e\u0432\u0435:", None))
        self.totalSelectedRows.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_38.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0411\u0440\u043e\u0439\u043a\u0438:", None))
        self.totalSelectedPieces.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0", None))
        self.label_37.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0412\u0440\u0435\u043c\u0435:", None))
        self.totalSelectedTime.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0.0", None))
        self.label_39.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"\u0421\u0440. \u0412\u0440\u0435\u043c\u0435 \u0437\u0430 \u0431\u0440.:", None))
        self.avrTimePerPiece.setText(QCoreApplication.translate("customPaymentsDetailsWidget", u"0.0", None))
    # retranslateUi

