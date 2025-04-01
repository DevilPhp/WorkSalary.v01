# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customMessageWidgetelexCb.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_customMessageWidget(object):
    def setupUi(self, customMessageWidget):
        if not customMessageWidget.objectName():
            customMessageWidget.setObjectName(u"customMessageWidget")
        customMessageWidget.resize(260, 120)
        customMessageWidget.setMinimumSize(QSize(0, 0))
        customMessageWidget.setMaximumSize(QSize(16777215, 16777215))
        customMessageWidget.setStyleSheet(u"*{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	font: 600 11pt \"Segoe UI\";\n"
"	color: #324b4c;\n"
"}\n"
"\n"
"#widget {\n"
"	border-radius: 15px;\n"
"	background-color: #c1c4c9;\n"
"	border: 3px solid #324b4c;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"#titleWidget * {\n"
"	font-size: 12pt;\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"#textHolder {\n"
"	font: 600 10pt \"Segoe UI\";\n"
"	padding: 5px;\n"
"}")
        self.verticalLayout = QVBoxLayout(customMessageWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(customMessageWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(260, 120))
        self.widget.setMaximumSize(QSize(260, 120))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = QWidget(self.widget)
        self.titleWidget.setObjectName(u"titleWidget")
        self.horizontalLayout = QHBoxLayout(self.titleWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.iconHolder = QPushButton(self.titleWidget)
        self.iconHolder.setObjectName(u"iconHolder")
        self.iconHolder.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Question-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.iconHolder.setIcon(icon)
        self.iconHolder.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.iconHolder, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.title = QLabel(self.titleWidget)
        self.title.setObjectName(u"title")

        self.horizontalLayout.addWidget(self.title)


        self.verticalLayout_3.addWidget(self.titleWidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.textWidget = QWidget(self.widget)
        self.textWidget.setObjectName(u"textWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textWidget.sizePolicy().hasHeightForWidth())
        self.textWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.textWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textHolder = QLabel(self.textWidget)
        self.textHolder.setObjectName(u"textHolder")
        self.textHolder.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.textHolder.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.textHolder)


        self.verticalLayout_3.addWidget(self.textWidget)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignHCenter)


        self.retranslateUi(customMessageWidget)

        QMetaObject.connectSlotsByName(customMessageWidget)
    # setupUi

    def retranslateUi(self, customMessageWidget):
        customMessageWidget.setWindowTitle(QCoreApplication.translate("customMessageWidget", u"Form", None))
        self.iconHolder.setText("")
        self.title.setText(QCoreApplication.translate("customMessageWidget", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.textHolder.setText(QCoreApplication.translate("customMessageWidget", u"Test text kljaksjd alksjdlkajs alksjdlk ajas kjasd kjsa djaks", None))
    # retranslateUi

