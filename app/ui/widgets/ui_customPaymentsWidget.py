# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customPaymentsWidgetQWIYLu.ui'
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
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_customPaymentsWidget(object):
    def setupUi(self, customPaymentsWidget):
        if not customPaymentsWidget.objectName():
            customPaymentsWidget.setObjectName(u"customPaymentsWidget")
        customPaymentsWidget.resize(1173, 915)
        customPaymentsWidget.setMinimumSize(QSize(900, 800))
        customPaymentsWidget.setStyleSheet(u"*{\n"
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
                        "Holder *{\n"
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
"#userIcon, #fromCalendarBtn, #toCalendarBtn {\n"
"	background-color: #dfdfdf;\n"
"}\n"
"\n"
"#refreshShiftsBtn {\n"
"	padding: 0px;\n"
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
"#widget_3 QCheckBox {\n"
"	font-size: 10pt;\n"
"	padding: 0px;\n"
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
""
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
"	padding: 0px 8px 0px 8px;\n"
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
        self.horizontalLayout_8.setSpacing(45)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_5)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.widget_12)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_7.addWidget(self.label_25)

        self.fromDateEdit = QDateEdit(self.widget_12)
        self.fromDateEdit.setObjectName(u"fromDateEdit")
        self.fromDateEdit.setFocusPolicy(Qt.WheelFocus)
        self.fromDateEdit.setFrame(False)
        self.fromDateEdit.setAlignment(Qt.AlignCenter)
        self.fromDateEdit.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.fromDateEdit.setMinimumDateTime(QDateTime(QDate(1990, 9, 4), QTime(0, 0, 0)))

        self.horizontalLayout_7.addWidget(self.fromDateEdit)

        self.fromCalendarBtn = QPushButton(self.widget_12)
        self.fromCalendarBtn.setObjectName(u"fromCalendarBtn")
        self.fromCalendarBtn.setFocusPolicy(Qt.NoFocus)
        self.fromCalendarBtn.setStyleSheet(u"*{\n"
"	padding: 0px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/Calendar--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fromCalendarBtn.setIcon(icon1)
        self.fromCalendarBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.fromCalendarBtn)


        self.horizontalLayout_8.addWidget(self.widget_12)

        self.widget_11 = QWidget(self.widget_5)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.widget_11)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_6.addWidget(self.label_26)

        self.toDateEdit = QDateEdit(self.widget_11)
        self.toDateEdit.setObjectName(u"toDateEdit")
        self.toDateEdit.setFocusPolicy(Qt.WheelFocus)
        self.toDateEdit.setFrame(False)
        self.toDateEdit.setAlignment(Qt.AlignCenter)
        self.toDateEdit.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.toDateEdit.setMinimumDateTime(QDateTime(QDate(1990, 9, 5), QTime(0, 0, 0)))

        self.horizontalLayout_6.addWidget(self.toDateEdit)

        self.toCalendarBtn = QPushButton(self.widget_11)
        self.toCalendarBtn.setObjectName(u"toCalendarBtn")
        self.toCalendarBtn.setFocusPolicy(Qt.NoFocus)
        self.toCalendarBtn.setStyleSheet(u"*{\n"
"	padding: 0px;\n"
"}")
        self.toCalendarBtn.setIcon(icon1)
        self.toCalendarBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.toCalendarBtn)


        self.horizontalLayout_8.addWidget(self.widget_11)

        self.searchBtn = QPushButton(self.widget_5)
        self.searchBtn.setObjectName(u"searchBtn")

        self.horizontalLayout_8.addWidget(self.searchBtn)

        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_8.addWidget(self.pushButton)

        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.selectAllCheckBox = QCheckBox(self.widget_3)
        self.selectAllCheckBox.setObjectName(u"selectAllCheckBox")

        self.verticalLayout_3.addWidget(self.selectAllCheckBox)

        self.overtimeCheckBox = QCheckBox(self.widget_3)
        self.overtimeCheckBox.setObjectName(u"overtimeCheckBox")

        self.verticalLayout_3.addWidget(self.overtimeCheckBox)

        self.hourlyCheckBox = QCheckBox(self.widget_3)
        self.hourlyCheckBox.setObjectName(u"hourlyCheckBox")

        self.verticalLayout_3.addWidget(self.hourlyCheckBox)

        self.nightTimeCheckBox = QCheckBox(self.widget_3)
        self.nightTimeCheckBox.setObjectName(u"nightTimeCheckBox")

        self.verticalLayout_3.addWidget(self.nightTimeCheckBox)


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


        self.verticalLayout_4.addWidget(self.operationsHolder)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(customPaymentsWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1161, 719))
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


        self.retranslateUi(customPaymentsWidget)

        QMetaObject.connectSlotsByName(customPaymentsWidget)
    # setupUi

    def retranslateUi(self, customPaymentsWidget):
        customPaymentsWidget.setWindowTitle(QCoreApplication.translate("customPaymentsWidget", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("customPaymentsWidget", u"\u041d\u0410\u0427\u0418\u0421\u041b\u0415\u041d\u0418\u042f", None))
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customPaymentsWidget", u"admin", None))
        self.label_25.setText(QCoreApplication.translate("customPaymentsWidget", u"\u041e\u0442 \u0414\u0430\u0442\u0430: ", None))
        self.fromDateEdit.setDisplayFormat(QCoreApplication.translate("customPaymentsWidget", u"dd.MM.yy '\u0433.'", None))
        self.fromCalendarBtn.setText("")
        self.label_26.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0414\u043e \u0414\u0430\u0442\u0430: ", None))
        self.toDateEdit.setDisplayFormat(QCoreApplication.translate("customPaymentsWidget", u"dd.MM.yy '\u0433.'", None))
        self.toCalendarBtn.setText("")
        self.searchBtn.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0422\u044a\u0440\u0441\u0435\u043d\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("customPaymentsWidget", u"Excel", None))
        self.selectAllCheckBox.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0412\u0441\u0438\u0447\u043a\u0438", None))
        self.overtimeCheckBox.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0418\u0437\u0432\u044a\u043d\u0440\u0435\u0434\u0435\u043d", None))
        self.hourlyCheckBox.setText(QCoreApplication.translate("customPaymentsWidget", u"\u041f\u043e\u0447\u0430\u0441\u043e\u0432\u043e", None))
        self.nightTimeCheckBox.setText(QCoreApplication.translate("customPaymentsWidget", u"\u041d\u043e\u0449\u0435\u043d", None))
        self.label_42.setText(QCoreApplication.translate("customPaymentsWidget", u"\u041e\u0431\u0449\u043e \u0440\u0435\u0434\u043e\u0432\u0435:", None))
        self.totalViewRows.setText(QCoreApplication.translate("customPaymentsWidget", u"0", None))
        self.label_43.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0417\u0430\u0432\u044a\u0440\u0448\u0435\u043d\u0438 \u0431\u0440 \u0437\u0430 \u0434\u0435\u043d\u044f:", None))
        self.totalProducedPieces.setText(QCoreApplication.translate("customPaymentsWidget", u"0", None))
        self.label_36.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0420\u0435\u0434\u043e\u0432\u0435:", None))
        self.totalSelectedRows.setText(QCoreApplication.translate("customPaymentsWidget", u"0", None))
        self.label_38.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0411\u0440\u043e\u0439\u043a\u0438:", None))
        self.totalSelectedPieces.setText(QCoreApplication.translate("customPaymentsWidget", u"0", None))
        self.label_37.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0412\u0440\u0435\u043c\u0435:", None))
        self.totalSelectedTime.setText(QCoreApplication.translate("customPaymentsWidget", u"0.0", None))
        self.label_39.setText(QCoreApplication.translate("customPaymentsWidget", u"\u0421\u0440. \u0412\u0440\u0435\u043c\u0435 \u0437\u0430 \u0431\u0440.:", None))
        self.avrTimePerPiece.setText(QCoreApplication.translate("customPaymentsWidget", u"0.0", None))
    # retranslateUi

