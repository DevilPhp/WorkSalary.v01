# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customCheckBoxWidgetMkXbAB.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_customCheckBoxWidget(object):
    def setupUi(self, customCheckBoxWidget):
        if not customCheckBoxWidget.objectName():
            customCheckBoxWidget.setObjectName(u"customCheckBoxWidget")
        customCheckBoxWidget.resize(351, 22)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(customCheckBoxWidget.sizePolicy().hasHeightForWidth())
        customCheckBoxWidget.setSizePolicy(sizePolicy)
        customCheckBoxWidget.setMinimumSize(QSize(0, 0))
        customCheckBoxWidget.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 600 10pt \"Segoe UI\";\n"
"	color: #324b4c;\n"
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
"QPushButton:hover {\n"
"	background-color: #aeaeae;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"	color: #008b69;\n"
"}\n"
"\n"
"QCheckBox:disable {\n"
"	color: black;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-bottom: 1px solid #7c9399;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color: #87b0a6;\n"
"}\n"
"\n"
"QCheckBox::label {\n"
"	word-wrap: break-word;\n"
"}")
        self.verticalLayout = QVBoxLayout(customCheckBoxWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(customCheckBoxWidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setMinimumSize(QSize(260, 0))
        self.checkBox.setMaximumSize(QSize(260, 16777215))
        self.checkBox.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.checkBox, 0, Qt.AlignLeft)

        self.labelHolder = QWidget(self.widget)
        self.labelHolder.setObjectName(u"labelHolder")
        self.horizontalLayout_2 = QHBoxLayout(self.labelHolder)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.labelHolder)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(50, 0))
        self.lineEdit.setMaximumSize(QSize(40, 16777215))
        self.lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit.setMaxLength(7)
        self.lineEdit.setFrame(False)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label = QLabel(self.labelHolder)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.labelHolder, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignLeft|Qt.AlignTop)


        self.retranslateUi(customCheckBoxWidget)

        QMetaObject.connectSlotsByName(customCheckBoxWidget)
    # setupUi

    def retranslateUi(self, customCheckBoxWidget):
        customCheckBoxWidget.setWindowTitle(QCoreApplication.translate("customCheckBoxWidget", u"Form", None))
        self.checkBox.setText(QCoreApplication.translate("customCheckBoxWidget", u"asdasdasdasds asdasds asdasdsad asd ", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("customCheckBoxWidget", u"0", None))
        self.label.setText(QCoreApplication.translate("customCheckBoxWidget", u"\u043c\u0438\u043d.", None))
    # retranslateUi

