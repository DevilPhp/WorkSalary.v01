# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customMessageWidgetYSPDIB.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_customMessageWidget(object):
    def setupUi(self, customMessageWidget):
        if not customMessageWidget.objectName():
            customMessageWidget.setObjectName(u"customMessageWidget")
        customMessageWidget.resize(280, 160)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(customMessageWidget.sizePolicy().hasHeightForWidth())
        customMessageWidget.setSizePolicy(sizePolicy)
        customMessageWidget.setMinimumSize(QSize(0, 0))
        customMessageWidget.setStyleSheet(u"*{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	font: 600 11pt \"Segoe UI\";\n"
"	color: #324b4c;\n"
"}\n"
"\n"
"#widget {\n"
"	border-radius: 15px;\n"
"	background-color: #c1c4c9;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"#titleWidget * {\n"
"	font-size: 13pt;\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"QTextBrowser {\n"
"	border: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(customMessageWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(customMessageWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(280, 160))
        self.widget.setMaximumSize(QSize(280, 160))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = QWidget(self.widget)
        self.titleWidget.setObjectName(u"titleWidget")
        self.titleWidget.setMinimumSize(QSize(200, 45))
        self.titleWidget.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout = QHBoxLayout(self.titleWidget)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.widget_3 = QWidget(self.titleWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.widget_3)

        self.widget_2 = QWidget(self.titleWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setMaximumSize(QSize(100, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.iconHolder = QPushButton(self.widget_2)
        self.iconHolder.setObjectName(u"iconHolder")
        self.iconHolder.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Question-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.iconHolder.setIcon(icon)
        self.iconHolder.setIconSize(QSize(36, 36))

        self.horizontalLayout_3.addWidget(self.iconHolder)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.widget_2)


        self.horizontalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addWidget(self.titleWidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.textWidget = QWidget(self.widget)
        self.textWidget.setObjectName(u"textWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.textWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.textHolder = QTextBrowser(self.textWidget)
        self.textHolder.setObjectName(u"textHolder")
        self.textHolder.setAcceptRichText(False)

        self.horizontalLayout_2.addWidget(self.textHolder)


        self.verticalLayout_2.addWidget(self.textWidget, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(customMessageWidget)

        QMetaObject.connectSlotsByName(customMessageWidget)
    # setupUi

    def retranslateUi(self, customMessageWidget):
        customMessageWidget.setWindowTitle(QCoreApplication.translate("customMessageWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("customMessageWidget", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.iconHolder.setText("")
        self.textHolder.setHtml(QCoreApplication.translate("customMessageWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0435\u0441\u0442\u043e\u0432\u043e \u0441\u044a\u043e\u0431\u0449\u0435\u043d\u0438\u0435. \u041d\u0435\u043a\u0430 \u0434\u0430 \u0441\u0435 \u0434\u043e\u0431\u0430\u0432\u0438</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0447\u0435 \u0432\u0441\u0438\u0447\u043a\u043e \u0438"
                        " \u0432\u0441\u0438\u0447\u043a\u0438 \u0441\u0430 \u041e\u041a!</p></body></html>", None))
    # retranslateUi

