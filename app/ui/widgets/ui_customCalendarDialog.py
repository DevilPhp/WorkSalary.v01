# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customCalendarDialognAeXfH.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDialog, QFrame,
    QHBoxLayout, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_CustomCalendarDialog(object):
    def setupUi(self, CustomCalendarDialog):
        if not CustomCalendarDialog.objectName():
            CustomCalendarDialog.setObjectName(u"CustomCalendarDialog")
        CustomCalendarDialog.resize(342, 353)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CustomCalendarDialog.sizePolicy().hasHeightForWidth())
        CustomCalendarDialog.setSizePolicy(sizePolicy)
        CustomCalendarDialog.setMinimumSize(QSize(0, 0))
        CustomCalendarDialog.setMouseTracking(True)
        CustomCalendarDialog.setStyleSheet(u"*{\n"
"	font-family: \"Segoe UI\";\n"
"	border-radius: 10px;\n"
"	background-color: #dfdfdf;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #324b4c;\n"
"	selection-background-color: #dfdfdf;\n"
"	selection-color: #324b4c;\n"
"}\n"
"QDialog{\n"
"	background-color: transperent;\n"
"	background: transperent;\n"
"\n"
"}\n"
"#mainWidget{\n"
"	background-color: #dfdfdf;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(CustomCalendarDialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainWidget = QWidget(CustomCalendarDialog)
        self.mainWidget.setObjectName(u"mainWidget")
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.mainWidget.setMinimumSize(QSize(0, 0))
        self.mainWidget.setMaximumSize(QSize(260, 245))
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.calFrame = QFrame(self.mainWidget)
        self.calFrame.setObjectName(u"calFrame")
        self.calFrame.setMaximumSize(QSize(16777215, 16777215))
        self.calFrame.setFrameShape(QFrame.StyledPanel)
        self.calFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.calFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.calendarCustomWidget = QCalendarWidget(self.calFrame)
        self.calendarCustomWidget.setObjectName(u"calendarCustomWidget")
        self.calendarCustomWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.calendarCustomWidget.sizePolicy().hasHeightForWidth())
        self.calendarCustomWidget.setSizePolicy(sizePolicy1)
        self.calendarCustomWidget.setMinimumSize(QSize(245, 0))
        self.calendarCustomWidget.setMaximumSize(QSize(245, 16777215))
        self.calendarCustomWidget.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(False)
        self.calendarCustomWidget.setFont(font)
        self.calendarCustomWidget.setMouseTracking(True)
        self.calendarCustomWidget.setFocusPolicy(Qt.NoFocus)
        self.calendarCustomWidget.setAutoFillBackground(False)
        self.calendarCustomWidget.setStyleSheet(u"QToolButton{\n"
"font: 700 11pt \"Segoe UI\";\n"
"padding: 5px;\n"
"}\n"
"QAbstractItemView{\n"
"background-color: #dfdfdf;\n"
"selection-background-color: #dfdfdf;\n"
"selection-color: #2b2b2c;\n"
"focus: none;\n"
"}\n"
"QAbstractItemView:disabled{\n"
"background-color: #dfdfdf;\n"
"color: #495466;\n"
"}\n"
"#qt_calendar_prevmonth {\n"
"    background-color: #dfdfdf;\n"
"    icon-size: 24px;\n"
"    qproperty-icon: url(:/icons/app/assets/icons/Alt-Arrow-Left--Streamline-Solar-Broken.svg);\n"
"}\n"
"#qt_calendar_nextmonth {\n"
"    background-color: #dfdfdf;\n"
"    icon-size: 24px;\n"
"    qproperty-icon: url(:/icons/app/assets/icons/Alt-Arrow-Right--Streamline-Solar-Broken.svg);\n"
"}\n"
"QMenu{\n"
"min-height:fit-content;\n"
"min-width:fit-content; \n"
"border: none;\n"
"border-bottom: 1px solid #7f7f7f;\n"
"border-right: 1px solid #7f7f7f;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QMenu::item:selected{\n"
"color: #2b2b2c;\n"
"font: 900 10.5pt \"Segoe UI\";\n"
"border-radius: 0px\n"
"}\n"
"QMenu::item{\n"
"col"
                        "or: #324b4c;\n"
"font: 700 10pt \"Segoe UI\";\n"
"height: 11px;  \n"
"border: 4px solid transparent;\n"
"padding: 0px 8px 0px 8px;\n"
"}\n"
"QTableView::item:selected{\n"
"border:2.5px solid #324b4c;\n"
"border-radius:11px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*#666c79; */\n"
"\n"
"")
        self.calendarCustomWidget.setLocale(QLocale(QLocale.Bulgarian, QLocale.Bulgaria))
        self.calendarCustomWidget.setMinimumDate(QDate(2023, 1, 1))
        self.calendarCustomWidget.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendarCustomWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarCustomWidget.setNavigationBarVisible(True)
        self.calendarCustomWidget.setDateEditEnabled(False)

        self.horizontalLayout.addWidget(self.calendarCustomWidget)


        self.verticalLayout.addWidget(self.calFrame)

        self.widget = QWidget(self.mainWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.todayBtn = QPushButton(self.widget)
        self.todayBtn.setObjectName(u"todayBtn")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.todayBtn.setFont(font1)
        self.todayBtn.setFocusPolicy(Qt.NoFocus)
        self.todayBtn.setStyleSheet(u"* {\n"
"	font-weight: 900;\n"
"}")

        self.verticalLayout_3.addWidget(self.todayBtn, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.widget)


        self.verticalLayout_2.addWidget(self.mainWidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(CustomCalendarDialog)
        self.calendarCustomWidget.activated.connect(CustomCalendarDialog.exec)

        QMetaObject.connectSlotsByName(CustomCalendarDialog)
    # setupUi

    def retranslateUi(self, CustomCalendarDialog):
        CustomCalendarDialog.setWindowTitle(QCoreApplication.translate("CustomCalendarDialog", u"CustomYesNoDialog", None))
        self.todayBtn.setText(QCoreApplication.translate("CustomCalendarDialog", u"\u0414\u043d\u0435\u0441", None))
    # retranslateUi

