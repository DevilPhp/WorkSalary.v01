# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customCheckBoxWidgetGIFqju.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_customCheckBoxWidget(object):
    def setupUi(self, customCheckBoxWidget):
        if not customCheckBoxWidget.objectName():
            customCheckBoxWidget.setObjectName(u"customCheckBoxWidget")
        customCheckBoxWidget.resize(139, 31)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(customCheckBoxWidget.sizePolicy().hasHeightForWidth())
        customCheckBoxWidget.setSizePolicy(sizePolicy)
        customCheckBoxWidget.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 600 12pt \"Segoe UI\";\n"
"	color: #324b4c;\n"
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
"QLineEdit {\n"
"	border-bottom: 1px solid #7c9399;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color: #87b0a6;\n"
"}")
        self.verticalLayout = QVBoxLayout(customCheckBoxWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(customCheckBoxWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.checkBox)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(40, 0))
        self.lineEdit.setMaximumSize(QSize(40, 16777215))
        self.lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit.setMaxLength(7)
        self.lineEdit.setFrame(False)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.retranslateUi(customCheckBoxWidget)

        QMetaObject.connectSlotsByName(customCheckBoxWidget)
    # setupUi

    def retranslateUi(self, customCheckBoxWidget):
        customCheckBoxWidget.setWindowTitle(QCoreApplication.translate("customCheckBoxWidget", u"Form", None))
        self.checkBox.setText(QCoreApplication.translate("customCheckBoxWidget", u"CheckBox", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("customCheckBoxWidget", u"0", None))
    # retranslateUi

