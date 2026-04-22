# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customTimeChangeOpersDialogZmsAwK.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_CustomTimeChangeOpersDialog(object):
    def setupUi(self, CustomTimeChangeOpersDialog):
        if not CustomTimeChangeOpersDialog.objectName():
            CustomTimeChangeOpersDialog.setObjectName(u"CustomTimeChangeOpersDialog")
        CustomTimeChangeOpersDialog.resize(603, 766)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CustomTimeChangeOpersDialog.sizePolicy().hasHeightForWidth())
        CustomTimeChangeOpersDialog.setSizePolicy(sizePolicy)
        CustomTimeChangeOpersDialog.setMinimumSize(QSize(0, 0))
        CustomTimeChangeOpersDialog.setMouseTracking(True)
        CustomTimeChangeOpersDialog.setStyleSheet(u"*{\n"
"	font: 600 9pt \"Segoe UI\";\n"
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
"#mainWidget{\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#label {\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"#operPositionLabel {\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"\n"
"#noBtn:hover{\n"
"	icon: url(:/icons/app/assets/icons/Close-Square--Streamline-Solar-Broken-#c75f59.svg);\n"
"	color: #c75f59;\n"
"}\n"
"\n"
"#yesBtn:hover{\n"
"	icon: url(:/icons/app/assets/icons/Check-Square--Streamline-Solar-Broken-#008b69.svg);\n"
"	color: #008b69;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: none;\n"
"	font-size: 9pt;\n"
"	border-bottom: 1px solid #7c9399;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(CustomTimeChangeOpersDialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainWidget = QWidget(CustomTimeChangeOpersDialog)
        self.mainWidget.setObjectName(u"mainWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy1)
        self.mainWidget.setMinimumSize(QSize(300, 0))
        self.mainWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 10)
        self.widget = QWidget(self.mainWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Question-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(28, 28))

        self.horizontalLayout_3.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.iconAndTextWidget = QWidget(self.widget_2)
        self.iconAndTextWidget.setObjectName(u"iconAndTextWidget")
        sizePolicy.setHeightForWidth(self.iconAndTextWidget.sizePolicy().hasHeightForWidth())
        self.iconAndTextWidget.setSizePolicy(sizePolicy)
        self.iconAndTextWidget.setMinimumSize(QSize(0, 0))
        self.iconAndTextWidget.setMaximumSize(QSize(16777215, 650))
        self.verticalLayout_3 = QVBoxLayout(self.iconAndTextWidget)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 5, 5, 0)
        self.label = QLabel(self.iconAndTextWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.scrollArea = QScrollArea(self.iconAndTextWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 243, 69))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.operTimesLayout = QVBoxLayout()
        self.operTimesLayout.setObjectName(u"operTimesLayout")

        self.verticalLayout_5.addLayout(self.operTimesLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout_4.addWidget(self.iconAndTextWidget, 0, Qt.AlignTop)

        self.buttonsWidget = QWidget(self.widget_2)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        sizePolicy.setHeightForWidth(self.buttonsWidget.sizePolicy().hasHeightForWidth())
        self.buttonsWidget.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(False)
        self.buttonsWidget.setFont(font1)
        self.horizontalLayout_2 = QHBoxLayout(self.buttonsWidget)
        self.horizontalLayout_2.setSpacing(45)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.yesBtn = QPushButton(self.buttonsWidget)
        self.yesBtn.setObjectName(u"yesBtn")
        self.yesBtn.setFont(font1)
        self.yesBtn.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/Check-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.yesBtn.setIcon(icon1)
        self.yesBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.yesBtn)

        self.noBtn = QPushButton(self.buttonsWidget)
        self.noBtn.setObjectName(u"noBtn")
        self.noBtn.setFont(font1)
        self.noBtn.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/icons/app/assets/icons/Close-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.noBtn.setIcon(icon2)
        self.noBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.noBtn, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.buttonsWidget, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.widget)


        self.verticalLayout_2.addWidget(self.mainWidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(CustomTimeChangeOpersDialog)

        QMetaObject.connectSlotsByName(CustomTimeChangeOpersDialog)
    # setupUi

    def retranslateUi(self, CustomTimeChangeOpersDialog):
        CustomTimeChangeOpersDialog.setWindowTitle(QCoreApplication.translate("CustomTimeChangeOpersDialog", u"CustomYesNoDialog", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("CustomTimeChangeOpersDialog", u"\u0417\u0410\u041f\u0410\u0417\u0412\u0412\u0410\u041d\u0415 \u041d\u0410 \u041d\u041e\u0412\u0418 \u0412\u0420\u0415\u041c\u0415\u041d\u0410", None))
        self.yesBtn.setText(QCoreApplication.translate("CustomTimeChangeOpersDialog", u"\u0414\u0410", None))
        self.noBtn.setText(QCoreApplication.translate("CustomTimeChangeOpersDialog", u"\u041d\u0415", None))
    # retranslateUi

