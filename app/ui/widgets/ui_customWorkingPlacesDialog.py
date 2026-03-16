# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customWorkingPlacesDialogsRDYJn.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_CustomWorkPlacesDialog(object):
    def setupUi(self, CustomWorkPlacesDialog):
        if not CustomWorkPlacesDialog.objectName():
            CustomWorkPlacesDialog.setObjectName(u"CustomWorkPlacesDialog")
        CustomWorkPlacesDialog.resize(499, 382)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CustomWorkPlacesDialog.sizePolicy().hasHeightForWidth())
        CustomWorkPlacesDialog.setSizePolicy(sizePolicy)
        CustomWorkPlacesDialog.setMinimumSize(QSize(0, 0))
        CustomWorkPlacesDialog.setMouseTracking(True)
        CustomWorkPlacesDialog.setStyleSheet(u"*{\n"
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
"#mainTextLabel {\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"#nameTextLabel {\n"
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
        self.verticalLayout_2 = QVBoxLayout(CustomWorkPlacesDialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainWidget = QWidget(CustomWorkPlacesDialog)
        self.mainWidget.setObjectName(u"mainWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy1)
        self.mainWidget.setMinimumSize(QSize(300, 0))
        self.mainWidget.setMaximumSize(QSize(350, 16777215))
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
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.mainTextLabel = QLabel(self.iconAndTextWidget)
        self.mainTextLabel.setObjectName(u"mainTextLabel")
        sizePolicy.setHeightForWidth(self.mainTextLabel.sizePolicy().hasHeightForWidth())
        self.mainTextLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
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
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(False)
        self.questionTextLabel.setFont(font1)
        self.questionTextLabel.setStyleSheet(u"")
        self.questionTextLabel.setAlignment(Qt.AlignCenter)
        self.questionTextLabel.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.questionTextLabel)

        self.modelNameLabel = QLabel(self.iconAndTextWidget)
        self.modelNameLabel.setObjectName(u"modelNameLabel")

        self.verticalLayout_3.addWidget(self.modelNameLabel, 0, Qt.AlignHCenter)

        self.widget_4 = QWidget(self.iconAndTextWidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.selectAllCheckBox = QCheckBox(self.widget_4)
        self.selectAllCheckBox.setObjectName(u"selectAllCheckBox")

        self.horizontalLayout_4.addWidget(self.selectAllCheckBox, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.iconAndTextWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.cehoveLayout = QGridLayout()
        self.cehoveLayout.setObjectName(u"cehoveLayout")
        self.cehoveLayout.setHorizontalSpacing(10)
        self.cehoveLayout.setVerticalSpacing(5)

        self.verticalLayout_5.addLayout(self.cehoveLayout)


        self.verticalLayout_3.addWidget(self.widget_3)


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
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Check-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.yesBtn.setIcon(icon)
        self.yesBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.yesBtn)

        self.noBtn = QPushButton(self.buttonsWidget)
        self.noBtn.setObjectName(u"noBtn")
        self.noBtn.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/Close-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.noBtn.setIcon(icon1)
        self.noBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.noBtn, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.buttonsWidget, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.widget)


        self.verticalLayout_2.addWidget(self.mainWidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(CustomWorkPlacesDialog)

        QMetaObject.connectSlotsByName(CustomWorkPlacesDialog)
    # setupUi

    def retranslateUi(self, CustomWorkPlacesDialog):
        CustomWorkPlacesDialog.setWindowTitle(QCoreApplication.translate("CustomWorkPlacesDialog", u"CustomYesNoDialog", None))
        self.mainTextLabel.setText(QCoreApplication.translate("CustomWorkPlacesDialog", u"\u0426\u0415\u0425\u041e\u0412\u0415", None))
        self.questionTextLabel.setText(QCoreApplication.translate("CustomWorkPlacesDialog", u"\u0414\u043e\u0431\u0430\u0432\u044f\u043d\u0435 \u043d\u0430 \u0446\u0435\u0445\u043e\u0432\u0435 \u0437\u0430 \u043c\u043e\u0434\u0435\u043b", None))
        self.modelNameLabel.setText("")
        self.selectAllCheckBox.setText(QCoreApplication.translate("CustomWorkPlacesDialog", u"\u0412\u0441\u0438\u0447\u043a\u0438", None))
        self.yesBtn.setText(QCoreApplication.translate("CustomWorkPlacesDialog", u"\u0414\u0410", None))
        self.noBtn.setText(QCoreApplication.translate("CustomWorkPlacesDialog", u"\u041d\u0415", None))
    # retranslateUi

