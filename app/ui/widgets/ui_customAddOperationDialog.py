# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customAddOperationDialogXqQADN.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_customAddOperationDialog(object):
    def setupUi(self, customAddOperationDialog):
        if not customAddOperationDialog.objectName():
            customAddOperationDialog.setObjectName(u"customAddOperationDialog")
        customAddOperationDialog.resize(410, 292)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(customAddOperationDialog.sizePolicy().hasHeightForWidth())
        customAddOperationDialog.setSizePolicy(sizePolicy)
        customAddOperationDialog.setMinimumSize(QSize(0, 0))
        customAddOperationDialog.setMouseTracking(True)
        customAddOperationDialog.setStyleSheet(u"*{\n"
"	font: 600 11pt \"Segoe UI\";\n"
"	border: none;\n"
"	background-color: #dfdfdf;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #324b4c;\n"
"}\n"
"\n"
"QDialog{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"\n"
"}\n"
"\n"
"QDateEdit::up-button, QDateEdit::down-button{\n"
"	width: 0px;\n"
"}\n"
"\n"
"\n"
"QLineEdit, QDateEdit{\n"
"	border: none;\n"
"	font-size: 10pt;\n"
"	border-bottom: 1px solid #7c9399;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #dfdfdf;\n"
"	border-bottom: 1px solid #7c9399;\n"
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
"	font: 720 10.5pt \"Segoe UI\";\n"
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
""
                        "	font: 700 10pt \"Segoe UI\";\n"
"	height: 11px;  \n"
"	border: 4px solid transparent;\n"
"	padding: 0px 8px 0px 8px;\n"
"}\n"
"\n"
"#calStartBtn, #calLeavingBtn {\n"
"	background-color: #dfdfdf;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"#mainWidget{\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#widget * {\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"#dialogTitle {\n"
"	font-size: 12pt;\n"
"	font-weight: 700;\n"
"}\n"
"#yesBtn {\n"
"	padding: 0px;\n"
"}\n"
"\n"
"#yesBtn:hover{\n"
"	icon: url(:/icons/app/assets/icons/Check-Square--Streamline-Solar-Broken-#008b69.svg);\n"
"	color: #008b69;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"	width: 20px;\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"	background: #dfdfdf;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(customAddOperationDialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainWidget = QWidget(customAddOperationDialog)
        self.mainWidget.setObjectName(u"mainWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy1)
        self.mainWidget.setMinimumSize(QSize(0, 0))
        self.mainWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.widget_2 = QWidget(self.mainWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 10)
        self.dialogTitle = QLabel(self.widget_2)
        self.dialogTitle.setObjectName(u"dialogTitle")

        self.horizontalLayout.addWidget(self.dialogTitle)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignHCenter)

        self.widget = QWidget(self.mainWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.addOperationLayout = QFormLayout()
        self.addOperationLayout.setObjectName(u"addOperationLayout")
        self.addOperationLayout.setHorizontalSpacing(15)
        self.addOperationLayout.setVerticalSpacing(10)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.addOperationLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.addOperationLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.operationNameLineEdit = QLineEdit(self.widget)
        self.operationNameLineEdit.setObjectName(u"operationNameLineEdit")
        self.operationNameLineEdit.setMinimumSize(QSize(200, 0))

        self.addOperationLayout.setWidget(0, QFormLayout.FieldRole, self.operationNameLineEdit)

        self.operTypeComboBox = QComboBox(self.widget)
        self.operTypeComboBox.setObjectName(u"operTypeComboBox")

        self.addOperationLayout.setWidget(1, QFormLayout.FieldRole, self.operTypeComboBox)


        self.verticalLayout_3.addLayout(self.addOperationLayout)


        self.verticalLayout.addWidget(self.widget)

        self.buttonsWidget = QWidget(self.mainWidget)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        sizePolicy.setHeightForWidth(self.buttonsWidget.sizePolicy().hasHeightForWidth())
        self.buttonsWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.buttonsWidget.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.buttonsWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.yesBtn = QPushButton(self.buttonsWidget)
        self.yesBtn.setObjectName(u"yesBtn")
        self.yesBtn.setFont(font)
        self.yesBtn.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Check-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.yesBtn.setIcon(icon)
        self.yesBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.yesBtn)


        self.verticalLayout.addWidget(self.buttonsWidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.mainWidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(customAddOperationDialog)

        QMetaObject.connectSlotsByName(customAddOperationDialog)
    # setupUi

    def retranslateUi(self, customAddOperationDialog):
        customAddOperationDialog.setWindowTitle(QCoreApplication.translate("customAddOperationDialog", u"CustomYesNoDialog", None))
        self.dialogTitle.setText(QCoreApplication.translate("customAddOperationDialog", u"\u0414\u043e\u0431\u0430\u0432\u044f\u043d\u0435 \u043d\u0430 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("customAddOperationDialog", u"\u0418\u043c\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("customAddOperationDialog", u"\u0414\u043b\u044a\u0436\u043d\u043e\u0441\u0442", None))
        self.yesBtn.setText(QCoreApplication.translate("customAddOperationDialog", u" \u0414\u0410", None))
    # retranslateUi

