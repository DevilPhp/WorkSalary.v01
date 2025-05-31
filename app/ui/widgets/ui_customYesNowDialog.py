# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customYesNowDialogxuSjvV.ui'
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
    QLayout, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_CustomYesNoDialog(object):
    def setupUi(self, CustomYesNoDialog):
        if not CustomYesNoDialog.objectName():
            CustomYesNoDialog.setObjectName(u"CustomYesNoDialog")
        CustomYesNoDialog.resize(641, 734)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CustomYesNoDialog.sizePolicy().hasHeightForWidth())
        CustomYesNoDialog.setSizePolicy(sizePolicy)
        CustomYesNoDialog.setMinimumSize(QSize(0, 0))
        CustomYesNoDialog.setMouseTracking(True)
        CustomYesNoDialog.setStyleSheet(u"*{\n"
"	font: 600 11pt \"Segoe UI\";\n"
"	border: none;\n"
"	background-color: #dfdfdf;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #324b4c;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 0px;\n"
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
"#mainTextLabel {\n"
"	font: 900 12pt \"Segoe UI\";\n"
"	padding-bottom: 10px;\n"
"}\n"
"\n"
"#nameTextLabel {\n"
"	font: 700 11pt \"Segoe UI\";\n"
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
"}")
        self.verticalLayout_2 = QVBoxLayout(CustomYesNoDialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainWidget = QWidget(CustomYesNoDialog)
        self.mainWidget.setObjectName(u"mainWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy1)
        self.mainWidget.setMinimumSize(QSize(350, 150))
        self.mainWidget.setMaximumSize(QSize(380, 16777215))
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
        self.normalIcon = QPushButton(self.widget)
        self.normalIcon.setObjectName(u"normalIcon")
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Question-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.normalIcon.setIcon(icon)
        self.normalIcon.setIconSize(QSize(38, 38))

        self.horizontalLayout_3.addWidget(self.normalIcon, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.warningIcon = QPushButton(self.widget)
        self.warningIcon.setObjectName(u"warningIcon")
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/Danger-Triangle--Streamline-Solar-Broken-#C75f59.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.warningIcon.setIcon(icon1)
        self.warningIcon.setIconSize(QSize(38, 38))

        self.horizontalLayout_3.addWidget(self.warningIcon)

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
        self.horizontalLayout = QHBoxLayout(self.iconAndTextWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.mainTextLabel = QLabel(self.iconAndTextWidget)
        self.mainTextLabel.setObjectName(u"mainTextLabel")
        sizePolicy.setHeightForWidth(self.mainTextLabel.sizePolicy().hasHeightForWidth())
        self.mainTextLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.mainTextLabel.setFont(font)
        self.mainTextLabel.setStyleSheet(u"")
        self.mainTextLabel.setAlignment(Qt.AlignCenter)
        self.mainTextLabel.setWordWrap(False)
        self.mainTextLabel.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_3.addWidget(self.mainTextLabel)

        self.questionTextLabel = QLabel(self.iconAndTextWidget)
        self.questionTextLabel.setObjectName(u"questionTextLabel")
        sizePolicy.setHeightForWidth(self.questionTextLabel.sizePolicy().hasHeightForWidth())
        self.questionTextLabel.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        self.questionTextLabel.setFont(font1)
        self.questionTextLabel.setStyleSheet(u"")
        self.questionTextLabel.setAlignment(Qt.AlignCenter)
        self.questionTextLabel.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.questionTextLabel)

        self.nameTextLabel = QLabel(self.iconAndTextWidget)
        self.nameTextLabel.setObjectName(u"nameTextLabel")
        self.nameTextLabel.setFont(font1)
        self.nameTextLabel.setStyleSheet(u"")
        self.nameTextLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.nameTextLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addWidget(self.iconAndTextWidget, 0, Qt.AlignVCenter)

        self.buttonsWidget = QWidget(self.widget_2)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        sizePolicy.setHeightForWidth(self.buttonsWidget.sizePolicy().hasHeightForWidth())
        self.buttonsWidget.setSizePolicy(sizePolicy)
        self.buttonsWidget.setFont(font1)
        self.horizontalLayout_2 = QHBoxLayout(self.buttonsWidget)
        self.horizontalLayout_2.setSpacing(45)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.yesBtn = QPushButton(self.buttonsWidget)
        self.yesBtn.setObjectName(u"yesBtn")
        self.yesBtn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/app/assets/icons/Check-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.yesBtn.setIcon(icon2)
        self.yesBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.yesBtn)

        self.noBtn = QPushButton(self.buttonsWidget)
        self.noBtn.setObjectName(u"noBtn")
        self.noBtn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/app/assets/icons/Close-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.noBtn.setIcon(icon3)
        self.noBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.noBtn, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.buttonsWidget, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.widget)


        self.verticalLayout_2.addWidget(self.mainWidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(CustomYesNoDialog)

        QMetaObject.connectSlotsByName(CustomYesNoDialog)
    # setupUi

    def retranslateUi(self, CustomYesNoDialog):
        CustomYesNoDialog.setWindowTitle(QCoreApplication.translate("CustomYesNoDialog", u"CustomYesNoDialog", None))
        self.normalIcon.setText("")
        self.warningIcon.setText("")
        self.mainTextLabel.setText(QCoreApplication.translate("CustomYesNoDialog", u"\u041f\u0420\u0415\u041c\u0410\u0425\u0412\u0410\u041d\u0415", None))
        self.questionTextLabel.setText(QCoreApplication.translate("CustomYesNoDialog", u"\u0421\u0438\u0433\u0443\u0440\u043d\u0438 \u043b\u0438 \u0441\u0442\u0435, \u0447\u0435 \u0438\u0441\u043a\u0430\u0442\u0435 \u0434\u0430 \u043f\u0440\u0435\u043c\u0430\u0445\u043d\u0435\u0442\u0435: ", None))
        self.nameTextLabel.setText(QCoreApplication.translate("CustomYesNoDialog", u"Name", None))
        self.yesBtn.setText(QCoreApplication.translate("CustomYesNoDialog", u"\u0414\u0410", None))
        self.noBtn.setText(QCoreApplication.translate("CustomYesNoDialog", u"\u041d\u0415", None))
    # retranslateUi

