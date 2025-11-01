# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customHolidaysWidgetmVHuoi.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QDateEdit,
    QFormLayout, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)
import resources_rc

class Ui_customHolidaysWidget(object):
    def setupUi(self, customHolidaysWidget):
        if not customHolidaysWidget.objectName():
            customHolidaysWidget.setObjectName(u"customHolidaysWidget")
        customHolidaysWidget.resize(900, 800)
        customHolidaysWidget.setMinimumSize(QSize(900, 800))
        customHolidaysWidget.setStyleSheet(u"*{\n"
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
"#newHolidayCalBtn {\n"
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
        self.verticalLayout = QVBoxLayout(customHolidaysWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(customHolidaysWidget)
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

        self.holidayNameLineEdit = QLineEdit(self.widget_7)
        self.holidayNameLineEdit.setObjectName(u"holidayNameLineEdit")

        self.modeLayout.setWidget(0, QFormLayout.FieldRole, self.holidayNameLineEdit)

        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")

        self.modeLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.widget_2 = QWidget(self.widget_7)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.newHolidayDate = QDateEdit(self.widget_2)
        self.newHolidayDate.setObjectName(u"newHolidayDate")
        self.newHolidayDate.setFocusPolicy(Qt.WheelFocus)
        self.newHolidayDate.setFrame(False)
        self.newHolidayDate.setAlignment(Qt.AlignCenter)
        self.newHolidayDate.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.newHolidayDate.setMinimumDateTime(QDateTime(QDate(1990, 9, 3), QTime(0, 0, 0)))

        self.horizontalLayout_9.addWidget(self.newHolidayDate)

        self.newHolidayCalBtn = QPushButton(self.widget_2)
        self.newHolidayCalBtn.setObjectName(u"newHolidayCalBtn")
        self.newHolidayCalBtn.setFocusPolicy(Qt.NoFocus)
        self.newHolidayCalBtn.setStyleSheet(u"*{\n"
"	padding: 0px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/app/assets/icons/Calendar--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newHolidayCalBtn.setIcon(icon2)
        self.newHolidayCalBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.newHolidayCalBtn, 0, Qt.AlignLeft)


        self.modeLayout.setWidget(1, QFormLayout.FieldRole, self.widget_2)


        self.verticalLayout_7.addLayout(self.modeLayout)

        self.addNewHolidayBtn = QPushButton(self.widget_7)
        self.addNewHolidayBtn.setObjectName(u"addNewHolidayBtn")

        self.verticalLayout_7.addWidget(self.addNewHolidayBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.widget_7)


        self.horizontalLayout_5.addWidget(self.workerHolder, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.workerInfoHolder, 0, Qt.AlignLeft)

        self.yearsHolder = QWidget(self.widget)
        self.yearsHolder.setObjectName(u"yearsHolder")
        sizePolicy.setHeightForWidth(self.yearsHolder.sizePolicy().hasHeightForWidth())
        self.yearsHolder.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.yearsHolder)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.optionsHolder = QFrame(self.yearsHolder)
        self.optionsHolder.setObjectName(u"optionsHolder")
        self.optionsHolder.setFrameShape(QFrame.StyledPanel)
        self.optionsHolder.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.optionsHolder)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 10)

        self.verticalLayout_2.addWidget(self.optionsHolder)

        self.widget_3 = QWidget(self.yearsHolder)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.widget_3, 0, Qt.AlignHCenter)

        self.yearsBtnsHolder = QWidget(self.yearsHolder)
        self.yearsBtnsHolder.setObjectName(u"yearsBtnsHolder")
        self.yearsBtnsHolder.setMinimumSize(QSize(0, 32))
        self.horizontalLayout_8 = QHBoxLayout(self.yearsBtnsHolder)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.yearsBtnsHolder, 0, Qt.AlignLeft)

        self.optionsHolder_2 = QFrame(self.yearsHolder)
        self.optionsHolder_2.setObjectName(u"optionsHolder_2")
        self.optionsHolder_2.setFrameShape(QFrame.StyledPanel)
        self.optionsHolder_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.optionsHolder_2)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 10)

        self.verticalLayout_2.addWidget(self.optionsHolder_2)


        self.verticalLayout_4.addWidget(self.yearsHolder)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(customHolidaysWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 888, 513))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.holidaysTableHolder = QWidget(self.scrollAreaWidgetContents)
        self.holidaysTableHolder.setObjectName(u"holidaysTableHolder")
        self.verticalLayout_11 = QVBoxLayout(self.holidaysTableHolder)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 0)
        self.holidaysTableView = QTableView(self.holidaysTableHolder)
        self.holidaysTableView.setObjectName(u"holidaysTableView")
        self.holidaysTableView.setStyleSheet(u"QHeaderView:section{\n"
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
        self.holidaysTableView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.holidaysTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.holidaysTableView.setCornerButtonEnabled(False)
        self.holidaysTableView.verticalHeader().setVisible(False)

        self.verticalLayout_11.addWidget(self.holidaysTableView)


        self.verticalLayout_12.addWidget(self.holidaysTableHolder)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(customHolidaysWidget)

        QMetaObject.connectSlotsByName(customHolidaysWidget)
    # setupUi

    def retranslateUi(self, customHolidaysWidget):
        customHolidaysWidget.setWindowTitle(QCoreApplication.translate("customHolidaysWidget", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("customHolidaysWidget", u"\u041f\u0420\u0410\u0417\u041d\u0418\u0427\u041d\u0418 \u0414\u041d\u0418", None))
        self.logoutBtn.setText("")
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customHolidaysWidget", u"admin", None))
        self.label.setText(QCoreApplication.translate("customHolidaysWidget", u"\u0414\u043e\u0431\u0430\u0432\u044f\u043d\u0435 \u043d\u0430 \u043f\u0440\u0430\u0437\u043d\u0438\u043a", None))
        self.label_2.setText(QCoreApplication.translate("customHolidaysWidget", u"\u0418\u043c\u0435:", None))
        self.holidayNameLineEdit.setText("")
        self.holidayNameLineEdit.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("customHolidaysWidget", u"\u0414\u0430\u0442\u0430:", None))
        self.newHolidayDate.setDisplayFormat(QCoreApplication.translate("customHolidaysWidget", u"dd.MM.yy '\u0433.'", None))
        self.newHolidayCalBtn.setText("")
        self.addNewHolidayBtn.setText(QCoreApplication.translate("customHolidaysWidget", u"\u0414\u043e\u0431\u0430\u0432\u044f\u043d\u0435", None))
        self.label_3.setText(QCoreApplication.translate("customHolidaysWidget", u"\u0413\u043e\u0434\u0438\u043d\u0430", None))
    # retranslateUi

