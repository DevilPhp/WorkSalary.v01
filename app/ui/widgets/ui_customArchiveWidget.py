# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customArchiveWidgetHXrwak.ui'
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
    QDateEdit, QFrame, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_customArchiveWidget(object):
    def setupUi(self, customArchiveWidget):
        if not customArchiveWidget.objectName():
            customArchiveWidget.setObjectName(u"customArchiveWidget")
        customArchiveWidget.resize(800, 580)
        customArchiveWidget.setMinimumSize(QSize(800, 580))
        customArchiveWidget.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 600 9pt \"Segoe UI\";\n"
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
"QLineEdit, QDateEdit{\n"
"	border: none;\n"
"	font-size: 9pt;\n"
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
"	font-size: 8pt;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"	background-color: #aeaeae;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #dfdfdf;\n"
"	border-bottom: 2px solid #7c9399;\n"
"	bor"
                        "der-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	image: url(':/icons/app/assets/icons/Alt-Arrow-Down--Streamline-Solar-Broken.svg');\n"
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
"}\n"
"\n"
"#modelHolder QLabel, #newModelInfoHolder * , #widget_11 *{\n"
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
"#userIcon, #logoutBtn, #fromCalendarBtn, #fromCalendarBtn_2, #toCalendarBtn, #toCalendarBtn_2 {\n"
"	background-color: #dfdfdf;\n"
"	padding: 0px;"
                        "\n"
"}\n"
"\n"
"#logoutBtn:hover{\n"
"	icon: url(:/icons/app/assets/icons/Log-Out--Streamline-Feather_#192626.svg);\n"
"}\n"
"\n"
"\n"
"#usernameLabel {\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"#workerPlaceLineEdit, #workerPositionLineEdit {\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"#widget_3 * {\n"
"	font-size: 9pt;\n"
"}")
        self.verticalLayout = QVBoxLayout(customArchiveWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(customArchiveWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.headerHolder = QWidget(self.widget)
        self.headerHolder.setObjectName(u"headerHolder")
        self.horizontalLayout = QHBoxLayout(self.headerHolder)
        self.horizontalLayout.setSpacing(10)
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

        self.widget_2 = QWidget(self.headerHolder)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.closeBtn = QPushButton(self.widget_5)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setStyleSheet(u"* {\n"
"	padding: 3px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Close-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon)
        self.closeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.closeBtn)


        self.horizontalLayout_11.addWidget(self.widget_5)

        self.userHolder = QWidget(self.widget_2)
        self.userHolder.setObjectName(u"userHolder")
        self.horizontalLayout_3 = QHBoxLayout(self.userHolder)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 5, 0)
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

        self.logoutBtn = QPushButton(self.userHolder)
        self.logoutBtn.setObjectName(u"logoutBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/app/assets/icons/Log-Out--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBtn.setIcon(icon2)
        self.logoutBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.logoutBtn)


        self.horizontalLayout_11.addWidget(self.userHolder)


        self.horizontalLayout.addWidget(self.widget_2, 0, Qt.AlignRight)


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
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 0, 0)
        self.modelsArchiveWidget = QWidget(self.workerInfoHolder)
        self.modelsArchiveWidget.setObjectName(u"modelsArchiveWidget")
        self.verticalLayout_7 = QVBoxLayout(self.modelsArchiveWidget)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.modelsArchiveWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.archiveModelsCheckBox = QCheckBox(self.widget_3)
        self.archiveModelsCheckBox.setObjectName(u"archiveModelsCheckBox")

        self.verticalLayout_3.addWidget(self.archiveModelsCheckBox)


        self.verticalLayout_7.addWidget(self.widget_3, 0, Qt.AlignHCenter)

        self.forYearModelsWidget = QWidget(self.modelsArchiveWidget)
        self.forYearModelsWidget.setObjectName(u"forYearModelsWidget")
        self.horizontalLayout_7 = QHBoxLayout(self.forYearModelsWidget)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.forYearModelsCheckBox = QCheckBox(self.forYearModelsWidget)
        self.forYearModelsCheckBox.setObjectName(u"forYearModelsCheckBox")
        self.forYearModelsCheckBox.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.forYearModelsCheckBox)

        self.forYearModelsComboBox = QComboBox(self.forYearModelsWidget)
        self.forYearModelsComboBox.setObjectName(u"forYearModelsComboBox")
        self.forYearModelsComboBox.setEnabled(False)
        self.forYearModelsComboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_7.addWidget(self.forYearModelsComboBox)


        self.verticalLayout_7.addWidget(self.forYearModelsWidget, 0, Qt.AlignLeft)

        self.forMonthModelsWidget = QWidget(self.modelsArchiveWidget)
        self.forMonthModelsWidget.setObjectName(u"forMonthModelsWidget")
        self.horizontalLayout_6 = QHBoxLayout(self.forMonthModelsWidget)
        self.horizontalLayout_6.setSpacing(7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.forMonthModlesCheckBox = QCheckBox(self.forMonthModelsWidget)
        self.forMonthModlesCheckBox.setObjectName(u"forMonthModlesCheckBox")
        self.forMonthModlesCheckBox.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.forMonthModlesCheckBox)

        self.forMonthModlesComboBox = QComboBox(self.forMonthModelsWidget)
        self.forMonthModlesComboBox.addItem("")
        self.forMonthModlesComboBox.addItem("")
        self.forMonthModlesComboBox.addItem("")
        self.forMonthModlesComboBox.addItem("")
        self.forMonthModlesComboBox.addItem("")
        self.forMonthModlesComboBox.addItem("")
        self.forMonthModlesComboBox.addItem("")
        self.forMonthModlesComboBox.addItem("")
        self.forMonthModlesComboBox.addItem("")
        self.forMonthModlesComboBox.addItem("")
        self.forMonthModlesComboBox.addItem("")
        self.forMonthModlesComboBox.addItem("")
        self.forMonthModlesComboBox.setObjectName(u"forMonthModlesComboBox")
        self.forMonthModlesComboBox.setEnabled(False)
        self.forMonthModlesComboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_6.addWidget(self.forMonthModlesComboBox)


        self.verticalLayout_7.addWidget(self.forMonthModelsWidget, 0, Qt.AlignLeft)

        self.forDatesModelsWidget = QWidget(self.modelsArchiveWidget)
        self.forDatesModelsWidget.setObjectName(u"forDatesModelsWidget")
        self.horizontalLayout_8 = QHBoxLayout(self.forDatesModelsWidget)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.forDatesModelsWidget)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.forDatesModlesCheckBox = QCheckBox(self.widget_10)
        self.forDatesModlesCheckBox.setObjectName(u"forDatesModlesCheckBox")
        self.forDatesModlesCheckBox.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.forDatesModlesCheckBox)


        self.horizontalLayout_8.addWidget(self.widget_10, 0, Qt.AlignLeft)

        self.widget_11 = QWidget(self.forDatesModelsWidget)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.fromDateModelsWidget = QWidget(self.widget_11)
        self.fromDateModelsWidget.setObjectName(u"fromDateModelsWidget")
        self.fromDateModelsWidget.setEnabled(False)
        self.horizontalLayout_13 = QHBoxLayout(self.fromDateModelsWidget)
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.fromDateEdit = QDateEdit(self.fromDateModelsWidget)
        self.fromDateEdit.setObjectName(u"fromDateEdit")
        self.fromDateEdit.setMaximumSize(QSize(70, 16777215))
        self.fromDateEdit.setFocusPolicy(Qt.WheelFocus)
        self.fromDateEdit.setFrame(False)
        self.fromDateEdit.setAlignment(Qt.AlignCenter)
        self.fromDateEdit.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.fromDateEdit.setMinimumDateTime(QDateTime(QDate(1990, 8, 22), QTime(0, 0, 0)))

        self.horizontalLayout_13.addWidget(self.fromDateEdit)

        self.fromCalendarBtn = QPushButton(self.fromDateModelsWidget)
        self.fromCalendarBtn.setObjectName(u"fromCalendarBtn")
        self.fromCalendarBtn.setFocusPolicy(Qt.NoFocus)
        self.fromCalendarBtn.setStyleSheet(u"*{\n"
"	padding: 0px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/app/assets/icons/Calendar--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fromCalendarBtn.setIcon(icon3)
        self.fromCalendarBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_13.addWidget(self.fromCalendarBtn)


        self.horizontalLayout_10.addWidget(self.fromDateModelsWidget)

        self.label = QLabel(self.widget_11)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label)

        self.toDateModelsWidget = QWidget(self.widget_11)
        self.toDateModelsWidget.setObjectName(u"toDateModelsWidget")
        self.toDateModelsWidget.setEnabled(False)
        self.horizontalLayout_14 = QHBoxLayout(self.toDateModelsWidget)
        self.horizontalLayout_14.setSpacing(3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.toDateEdit = QDateEdit(self.toDateModelsWidget)
        self.toDateEdit.setObjectName(u"toDateEdit")
        self.toDateEdit.setMaximumSize(QSize(70, 16777215))
        self.toDateEdit.setFocusPolicy(Qt.WheelFocus)
        self.toDateEdit.setFrame(False)
        self.toDateEdit.setAlignment(Qt.AlignCenter)
        self.toDateEdit.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.toDateEdit.setMinimumDateTime(QDateTime(QDate(1990, 8, 24), QTime(0, 0, 0)))

        self.horizontalLayout_14.addWidget(self.toDateEdit)

        self.toCalendarBtn = QPushButton(self.toDateModelsWidget)
        self.toCalendarBtn.setObjectName(u"toCalendarBtn")
        self.toCalendarBtn.setFocusPolicy(Qt.NoFocus)
        self.toCalendarBtn.setStyleSheet(u"*{\n"
"	padding: 0px;\n"
"}")
        self.toCalendarBtn.setIcon(icon3)
        self.toCalendarBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_14.addWidget(self.toCalendarBtn)


        self.horizontalLayout_10.addWidget(self.toDateModelsWidget)


        self.horizontalLayout_8.addWidget(self.widget_11, 0, Qt.AlignLeft)


        self.verticalLayout_7.addWidget(self.forDatesModelsWidget, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.modelsArchiveWidget, 0, Qt.AlignTop)

        self.timePapersArhiveWidget = QWidget(self.workerInfoHolder)
        self.timePapersArhiveWidget.setObjectName(u"timePapersArhiveWidget")
        self.verticalLayout_6 = QVBoxLayout(self.timePapersArhiveWidget)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.timePapersArhiveWidget)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.archiveTPCheckBox = QCheckBox(self.widget_6)
        self.archiveTPCheckBox.setObjectName(u"archiveTPCheckBox")

        self.verticalLayout_5.addWidget(self.archiveTPCheckBox)


        self.verticalLayout_6.addWidget(self.widget_6, 0, Qt.AlignHCenter)

        self.forYearTPWidget = QWidget(self.timePapersArhiveWidget)
        self.forYearTPWidget.setObjectName(u"forYearTPWidget")
        self.horizontalLayout_21 = QHBoxLayout(self.forYearTPWidget)
        self.horizontalLayout_21.setSpacing(17)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.forYearTPCheckBox = QCheckBox(self.forYearTPWidget)
        self.forYearTPCheckBox.setObjectName(u"forYearTPCheckBox")
        self.forYearTPCheckBox.setEnabled(False)

        self.horizontalLayout_21.addWidget(self.forYearTPCheckBox)

        self.forYearTPComboBox = QComboBox(self.forYearTPWidget)
        self.forYearTPComboBox.setObjectName(u"forYearTPComboBox")
        self.forYearTPComboBox.setEnabled(False)
        self.forYearTPComboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_21.addWidget(self.forYearTPComboBox)


        self.verticalLayout_6.addWidget(self.forYearTPWidget, 0, Qt.AlignLeft)

        self.forMonthTPWidget = QWidget(self.timePapersArhiveWidget)
        self.forMonthTPWidget.setObjectName(u"forMonthTPWidget")
        self.horizontalLayout_15 = QHBoxLayout(self.forMonthTPWidget)
        self.horizontalLayout_15.setSpacing(19)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.forMonthTPCheckBox = QCheckBox(self.forMonthTPWidget)
        self.forMonthTPCheckBox.setObjectName(u"forMonthTPCheckBox")
        self.forMonthTPCheckBox.setEnabled(False)

        self.horizontalLayout_15.addWidget(self.forMonthTPCheckBox)

        self.forMonthTPComboBox = QComboBox(self.forMonthTPWidget)
        self.forMonthTPComboBox.addItem("")
        self.forMonthTPComboBox.addItem("")
        self.forMonthTPComboBox.addItem("")
        self.forMonthTPComboBox.addItem("")
        self.forMonthTPComboBox.addItem("")
        self.forMonthTPComboBox.addItem("")
        self.forMonthTPComboBox.addItem("")
        self.forMonthTPComboBox.addItem("")
        self.forMonthTPComboBox.addItem("")
        self.forMonthTPComboBox.addItem("")
        self.forMonthTPComboBox.addItem("")
        self.forMonthTPComboBox.addItem("")
        self.forMonthTPComboBox.setObjectName(u"forMonthTPComboBox")
        self.forMonthTPComboBox.setEnabled(False)
        self.forMonthTPComboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_15.addWidget(self.forMonthTPComboBox)


        self.verticalLayout_6.addWidget(self.forMonthTPWidget, 0, Qt.AlignLeft)

        self.forDatesTPWidget = QWidget(self.timePapersArhiveWidget)
        self.forDatesTPWidget.setObjectName(u"forDatesTPWidget")
        self.horizontalLayout_16 = QHBoxLayout(self.forDatesTPWidget)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.forDatesTPWidget)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.forDatesTPCheckBox = QCheckBox(self.widget_15)
        self.forDatesTPCheckBox.setObjectName(u"forDatesTPCheckBox")
        self.forDatesTPCheckBox.setEnabled(False)

        self.horizontalLayout_17.addWidget(self.forDatesTPCheckBox)


        self.horizontalLayout_16.addWidget(self.widget_15, 0, Qt.AlignLeft)

        self.widget_16 = QWidget(self.forDatesTPWidget)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.fromDateTPWidget = QWidget(self.widget_16)
        self.fromDateTPWidget.setObjectName(u"fromDateTPWidget")
        self.fromDateTPWidget.setEnabled(False)
        self.horizontalLayout_19 = QHBoxLayout(self.fromDateTPWidget)
        self.horizontalLayout_19.setSpacing(3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.fromDateEdit_2 = QDateEdit(self.fromDateTPWidget)
        self.fromDateEdit_2.setObjectName(u"fromDateEdit_2")
        self.fromDateEdit_2.setMaximumSize(QSize(70, 16777215))
        self.fromDateEdit_2.setFocusPolicy(Qt.WheelFocus)
        self.fromDateEdit_2.setFrame(False)
        self.fromDateEdit_2.setAlignment(Qt.AlignCenter)
        self.fromDateEdit_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.fromDateEdit_2.setMinimumDateTime(QDateTime(QDate(1990, 8, 21), QTime(0, 0, 0)))

        self.horizontalLayout_19.addWidget(self.fromDateEdit_2)

        self.fromCalendarBtn_2 = QPushButton(self.fromDateTPWidget)
        self.fromCalendarBtn_2.setObjectName(u"fromCalendarBtn_2")
        self.fromCalendarBtn_2.setFocusPolicy(Qt.NoFocus)
        self.fromCalendarBtn_2.setStyleSheet(u"*{\n"
"	padding: 0px;\n"
"}")
        self.fromCalendarBtn_2.setIcon(icon3)
        self.fromCalendarBtn_2.setIconSize(QSize(18, 18))

        self.horizontalLayout_19.addWidget(self.fromCalendarBtn_2)


        self.horizontalLayout_18.addWidget(self.fromDateTPWidget)

        self.label_2 = QLabel(self.widget_16)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_2)

        self.toDateTPWidget = QWidget(self.widget_16)
        self.toDateTPWidget.setObjectName(u"toDateTPWidget")
        self.toDateTPWidget.setEnabled(False)
        self.horizontalLayout_20 = QHBoxLayout(self.toDateTPWidget)
        self.horizontalLayout_20.setSpacing(3)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.toDateEdit_2 = QDateEdit(self.toDateTPWidget)
        self.toDateEdit_2.setObjectName(u"toDateEdit_2")
        self.toDateEdit_2.setMaximumSize(QSize(70, 16777215))
        self.toDateEdit_2.setFocusPolicy(Qt.WheelFocus)
        self.toDateEdit_2.setFrame(False)
        self.toDateEdit_2.setAlignment(Qt.AlignCenter)
        self.toDateEdit_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.toDateEdit_2.setMinimumDateTime(QDateTime(QDate(1990, 8, 23), QTime(0, 0, 0)))

        self.horizontalLayout_20.addWidget(self.toDateEdit_2)

        self.toCalendarBtn_2 = QPushButton(self.toDateTPWidget)
        self.toCalendarBtn_2.setObjectName(u"toCalendarBtn_2")
        self.toCalendarBtn_2.setFocusPolicy(Qt.NoFocus)
        self.toCalendarBtn_2.setStyleSheet(u"*{\n"
"	padding: 0px;\n"
"}")
        self.toCalendarBtn_2.setIcon(icon3)
        self.toCalendarBtn_2.setIconSize(QSize(18, 18))

        self.horizontalLayout_20.addWidget(self.toCalendarBtn_2)


        self.horizontalLayout_18.addWidget(self.toDateTPWidget)


        self.horizontalLayout_16.addWidget(self.widget_16, 0, Qt.AlignLeft)


        self.verticalLayout_6.addWidget(self.forDatesTPWidget, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.timePapersArhiveWidget, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.workerInfoHolder)

        self.operationsHolder = QWidget(self.widget)
        self.operationsHolder.setObjectName(u"operationsHolder")
        sizePolicy.setHeightForWidth(self.operationsHolder.sizePolicy().hasHeightForWidth())
        self.operationsHolder.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.operationsHolder)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.optionsHolder = QFrame(self.operationsHolder)
        self.optionsHolder.setObjectName(u"optionsHolder")
        self.optionsHolder.setFrameShape(QFrame.StyledPanel)
        self.optionsHolder.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.optionsHolder)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 5)

        self.verticalLayout_2.addWidget(self.optionsHolder)


        self.verticalLayout_4.addWidget(self.operationsHolder)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(customArchiveWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 788, 421))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.archiveTableHolder = QWidget(self.scrollAreaWidgetContents)
        self.archiveTableHolder.setObjectName(u"archiveTableHolder")
        self.archiveTableHolder.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.archiveTableHolder)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 0)

        self.verticalLayout_12.addWidget(self.archiveTableHolder)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(customArchiveWidget)

        QMetaObject.connectSlotsByName(customArchiveWidget)
    # setupUi

    def retranslateUi(self, customArchiveWidget):
        customArchiveWidget.setWindowTitle(QCoreApplication.translate("customArchiveWidget", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("customArchiveWidget", u"\u0410\u0420\u0425\u0418\u0412\u0418\u0420\u0410\u041d\u0415", None))
        self.closeBtn.setText(QCoreApplication.translate("customArchiveWidget", u"\u0417\u0442\u0432\u043e\u0440\u0438", None))
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customArchiveWidget", u"admin", None))
        self.logoutBtn.setText("")
        self.archiveModelsCheckBox.setText(QCoreApplication.translate("customArchiveWidget", u"\u0410\u0440\u0445\u0438\u0432\u0438\u0440\u0430\u043d\u0435 \u043d\u0430 \u043c\u043e\u0434\u0435\u043b\u0438", None))
        self.forYearModelsCheckBox.setText(QCoreApplication.translate("customArchiveWidget", u"\u0417\u0430 \u0413\u043e\u0434\u0438\u043d\u0430", None))
        self.forMonthModlesCheckBox.setText(QCoreApplication.translate("customArchiveWidget", u"\u0417\u0430 \u041c\u0435\u0441\u0435\u0446", None))
        self.forMonthModlesComboBox.setItemText(0, QCoreApplication.translate("customArchiveWidget", u"\u042f\u043d\u0443\u0430\u0440\u0438", None))
        self.forMonthModlesComboBox.setItemText(1, QCoreApplication.translate("customArchiveWidget", u"\u0424\u0435\u0432\u0440\u0443\u0430\u0440\u0438", None))
        self.forMonthModlesComboBox.setItemText(2, QCoreApplication.translate("customArchiveWidget", u"\u041c\u0430\u0440\u0442", None))
        self.forMonthModlesComboBox.setItemText(3, QCoreApplication.translate("customArchiveWidget", u"\u0410\u043f\u0440\u0438\u043b", None))
        self.forMonthModlesComboBox.setItemText(4, QCoreApplication.translate("customArchiveWidget", u"\u041c\u0430\u0439", None))
        self.forMonthModlesComboBox.setItemText(5, QCoreApplication.translate("customArchiveWidget", u"\u042e\u043d\u0438", None))
        self.forMonthModlesComboBox.setItemText(6, QCoreApplication.translate("customArchiveWidget", u"\u042e\u043b\u0438", None))
        self.forMonthModlesComboBox.setItemText(7, QCoreApplication.translate("customArchiveWidget", u"\u0410\u0432\u0433\u0443\u0441\u0442", None))
        self.forMonthModlesComboBox.setItemText(8, QCoreApplication.translate("customArchiveWidget", u"\u0421\u0435\u043f\u0442\u0435\u043c\u0432\u0440\u0438", None))
        self.forMonthModlesComboBox.setItemText(9, QCoreApplication.translate("customArchiveWidget", u"\u041e\u043a\u0442\u043e\u043c\u0432\u0440\u0438", None))
        self.forMonthModlesComboBox.setItemText(10, QCoreApplication.translate("customArchiveWidget", u"\u041d\u043e\u0435\u043c\u0432\u0440\u0438", None))
        self.forMonthModlesComboBox.setItemText(11, QCoreApplication.translate("customArchiveWidget", u"\u0414\u0435\u043a\u0435\u043c\u0432\u0440\u0438", None))

        self.forDatesModlesCheckBox.setText(QCoreApplication.translate("customArchiveWidget", u"\u041e\u0442/\u0414\u043e \u0414\u0430\u0442\u0430:", None))
        self.fromDateEdit.setDisplayFormat(QCoreApplication.translate("customArchiveWidget", u"dd.MM.yy '\u0433.'", None))
        self.fromCalendarBtn.setText("")
        self.label.setText(QCoreApplication.translate("customArchiveWidget", u"  /  ", None))
        self.toDateEdit.setDisplayFormat(QCoreApplication.translate("customArchiveWidget", u"dd.MM.yy '\u0433.'", None))
        self.toCalendarBtn.setText("")
        self.archiveTPCheckBox.setText(QCoreApplication.translate("customArchiveWidget", u"\u0410\u0440\u0445\u0438\u0432\u0438\u0440\u0430\u043d\u0435 \u043d\u0430 \u041b\u0438\u0441\u0442\u043e\u0432\u0435 \u0437\u0430 \u0432\u0440\u0435\u043c\u0435", None))
        self.forYearTPCheckBox.setText(QCoreApplication.translate("customArchiveWidget", u"\u0417\u0430 \u0413\u043e\u0434\u0438\u043d\u0430", None))
        self.forMonthTPCheckBox.setText(QCoreApplication.translate("customArchiveWidget", u"\u0417\u0430 \u041c\u0435\u0441\u0435\u0446", None))
        self.forMonthTPComboBox.setItemText(0, QCoreApplication.translate("customArchiveWidget", u"\u042f\u043d\u0443\u0430\u0440\u0438", None))
        self.forMonthTPComboBox.setItemText(1, QCoreApplication.translate("customArchiveWidget", u"\u0424\u0435\u0432\u0440\u0443\u0430\u0440\u0438", None))
        self.forMonthTPComboBox.setItemText(2, QCoreApplication.translate("customArchiveWidget", u"\u041c\u0430\u0440\u0442", None))
        self.forMonthTPComboBox.setItemText(3, QCoreApplication.translate("customArchiveWidget", u"\u0410\u043f\u0440\u0438\u043b", None))
        self.forMonthTPComboBox.setItemText(4, QCoreApplication.translate("customArchiveWidget", u"\u041c\u0430\u0439", None))
        self.forMonthTPComboBox.setItemText(5, QCoreApplication.translate("customArchiveWidget", u"\u042e\u043d\u0438", None))
        self.forMonthTPComboBox.setItemText(6, QCoreApplication.translate("customArchiveWidget", u"\u042e\u043b\u0438", None))
        self.forMonthTPComboBox.setItemText(7, QCoreApplication.translate("customArchiveWidget", u"\u0410\u0432\u0433\u0443\u0441\u0442", None))
        self.forMonthTPComboBox.setItemText(8, QCoreApplication.translate("customArchiveWidget", u"\u0421\u0435\u043f\u0442\u0435\u043c\u0432\u0440\u0438", None))
        self.forMonthTPComboBox.setItemText(9, QCoreApplication.translate("customArchiveWidget", u"\u041e\u043a\u0442\u043e\u043c\u0432\u0440\u0438", None))
        self.forMonthTPComboBox.setItemText(10, QCoreApplication.translate("customArchiveWidget", u"\u041d\u043e\u0435\u043c\u0432\u0440\u0438", None))
        self.forMonthTPComboBox.setItemText(11, QCoreApplication.translate("customArchiveWidget", u"\u0414\u0435\u043a\u0435\u043c\u0432\u0440\u0438", None))

        self.forDatesTPCheckBox.setText(QCoreApplication.translate("customArchiveWidget", u"\u041e\u0442/\u0414\u043e \u0414\u0430\u0442\u0430:", None))
        self.fromDateEdit_2.setDisplayFormat(QCoreApplication.translate("customArchiveWidget", u"dd.MM.yy '\u0433.'", None))
        self.fromCalendarBtn_2.setText("")
        self.label_2.setText(QCoreApplication.translate("customArchiveWidget", u"  /  ", None))
        self.toDateEdit_2.setDisplayFormat(QCoreApplication.translate("customArchiveWidget", u"dd.MM.yy '\u0433.'", None))
        self.toCalendarBtn_2.setText("")
    # retranslateUi

