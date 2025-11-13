# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customSortingMenuWidgetxhNWzb.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QLineEdit, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_customSortingMenuWidget(object):
    def setupUi(self, customSortingMenuWidget):
        if not customSortingMenuWidget.objectName():
            customSortingMenuWidget.setObjectName(u"customSortingMenuWidget")
        customSortingMenuWidget.resize(100, 39)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(customSortingMenuWidget.sizePolicy().hasHeightForWidth())
        customSortingMenuWidget.setSizePolicy(sizePolicy)
        customSortingMenuWidget.setMinimumSize(QSize(0, 0))
        customSortingMenuWidget.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 500 9pt \"Segoe UI\";\n"
"	color: #324b4c;\n"
"}\n"
"\n"
"customSortingMenuWidget{\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: none;\n"
"	font-size: 9pt;\n"
"	border-bottom: 1px solid #7c9399;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"        width: 20px;\n"
"        background: none;\n"
"    }\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"        background: #dfdfdf;\n"
"    }")
        self.verticalLayout = QVBoxLayout(customSortingMenuWidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget_3 = QWidget(customSortingMenuWidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.searchLineEdit = QLineEdit(self.widget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.verticalLayout_3.addWidget(self.searchLineEdit)


        self.verticalLayout_5.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.widget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 68, 16))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 3, 5, 2)
        self.menuItemsHolder = QVBoxLayout()
        self.menuItemsHolder.setSpacing(5)
        self.menuItemsHolder.setObjectName(u"menuItemsHolder")

        self.verticalLayout_6.addLayout(self.menuItemsHolder)


        self.verticalLayout_2.addWidget(self.widget_4, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.widget_2, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignTop)


        self.retranslateUi(customSortingMenuWidget)

        QMetaObject.connectSlotsByName(customSortingMenuWidget)
    # setupUi

    def retranslateUi(self, customSortingMenuWidget):
        customSortingMenuWidget.setWindowTitle(QCoreApplication.translate("customSortingMenuWidget", u"Form", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("customSortingMenuWidget", u"\u0422\u044a\u0440\u0441\u0435\u043d\u0435...", None))
    # retranslateUi

