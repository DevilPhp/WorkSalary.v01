# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customPositionGroupWidgetUnZilY.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_customPositionGroupWidget(object):
    def setupUi(self, customPositionGroupWidget):
        if not customPositionGroupWidget.objectName():
            customPositionGroupWidget.setObjectName(u"customPositionGroupWidget")
        customPositionGroupWidget.resize(800, 580)
        customPositionGroupWidget.setMinimumSize(QSize(800, 580))
        customPositionGroupWidget.setStyleSheet(u"*{\n"
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
        self.verticalLayout = QVBoxLayout(customPositionGroupWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(customPositionGroupWidget)
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


        self.horizontalLayout.addWidget(self.widget_2, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.headerHolder)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(customPositionGroupWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 788, 532))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.posGroupsTableHolder = QWidget(self.scrollAreaWidgetContents)
        self.posGroupsTableHolder.setObjectName(u"posGroupsTableHolder")
        self.posGroupsTableHolder.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.posGroupsTableHolder)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 0)

        self.verticalLayout_12.addWidget(self.posGroupsTableHolder)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(customPositionGroupWidget)

        QMetaObject.connectSlotsByName(customPositionGroupWidget)
    # setupUi

    def retranslateUi(self, customPositionGroupWidget):
        customPositionGroupWidget.setWindowTitle(QCoreApplication.translate("customPositionGroupWidget", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("customPositionGroupWidget", u"\u0413\u0420\u0423\u041f\u0418 \u041a\u042a\u041c \u041f\u041e\u0417\u0418\u0426\u0418\u0418", None))
        self.closeBtn.setText(QCoreApplication.translate("customPositionGroupWidget", u"\u0417\u0442\u0432\u043e\u0440\u0438", None))
    # retranslateUi

