# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customParametersRowWidgetBwBtSp.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_customParametersRowWidget(object):
    def setupUi(self, customParametersRowWidget):
        if not customParametersRowWidget.objectName():
            customParametersRowWidget.setObjectName(u"customParametersRowWidget")
        customParametersRowWidget.resize(793, 23)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(customParametersRowWidget.sizePolicy().hasHeightForWidth())
        customParametersRowWidget.setSizePolicy(sizePolicy)
        customParametersRowWidget.setMinimumSize(QSize(0, 0))
        customParametersRowWidget.setStyleSheet(u"*{\n"
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
"	font: 72"
                        "0 10.5pt \"Segoe UI\";\n"
"	border-radius: 0px;\n"
"	alternate-background-color: #2c313c;\n"
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
"}\n"
"QComboBox:header{\n"
"	color: black;\n"
"}")
        self.verticalLayout = QVBoxLayout(customParametersRowWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(customParametersRowWidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(300, 0))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.nameLabel = QLabel(self.widget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.nameLabel)

        self.inputLineEdit = QLineEdit(self.widget)
        self.inputLineEdit.setObjectName(u"inputLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inputLineEdit.sizePolicy().hasHeightForWidth())
        self.inputLineEdit.setSizePolicy(sizePolicy1)
        self.inputLineEdit.setMinimumSize(QSize(200, 0))
        self.inputLineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.inputLineEdit.setFocusPolicy(Qt.StrongFocus)
        self.inputLineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.inputLineEdit.setMaxLength(120)
        self.inputLineEdit.setFrame(False)

        self.horizontalLayout.addWidget(self.inputLineEdit)

        self.inputComboBox = QComboBox(self.widget)
        self.inputComboBox.setObjectName(u"inputComboBox")
        self.inputComboBox.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.inputComboBox)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignLeft|Qt.AlignTop)


        self.retranslateUi(customParametersRowWidget)

        QMetaObject.connectSlotsByName(customParametersRowWidget)
    # setupUi

    def retranslateUi(self, customParametersRowWidget):
        customParametersRowWidget.setWindowTitle(QCoreApplication.translate("customParametersRowWidget", u"Form", None))
        self.nameLabel.setText(QCoreApplication.translate("customParametersRowWidget", u"\u0418\u043c\u0435", None))
        self.inputLineEdit.setText("")
        self.inputLineEdit.setPlaceholderText("")
    # retranslateUi

