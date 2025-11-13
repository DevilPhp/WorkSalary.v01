# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customServerMessageDialogLDAuGa.ui'
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

class Ui_customServerMessageDialog(object):
    def setupUi(self, customServerMessageDialog):
        if not customServerMessageDialog.objectName():
            customServerMessageDialog.setObjectName(u"customServerMessageDialog")
        customServerMessageDialog.resize(380, 603)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(customServerMessageDialog.sizePolicy().hasHeightForWidth())
        customServerMessageDialog.setSizePolicy(sizePolicy)
        customServerMessageDialog.setMinimumSize(QSize(0, 0))
        customServerMessageDialog.setMouseTracking(True)
        customServerMessageDialog.setStyleSheet(u"*{\n"
"	font: 600 9pt \"Segoe UI\";\n"
"	border: none;\n"
"	background-color: #dfdfdf;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #324b4c;\n"
"}\n"
"\n"
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
"	padding-bottom: 8px;\n"
"}\n"
"\n"
"#questionTextLabel {\n"
"	font: 600 9pt \"Segoe UI\";\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(customServerMessageDialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainWidget = QWidget(customServerMessageDialog)
        self.mainWidget.setObjectName(u"mainWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy1)
        self.mainWidget.setMinimumSize(QSize(250, 120))
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
        self.warningIcon = QPushButton(self.widget)
        self.warningIcon.setObjectName(u"warningIcon")
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Danger-Triangle--Streamline-Solar-Broken-#C75f59.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.warningIcon.setIcon(icon)
        self.warningIcon.setIconSize(QSize(28, 28))

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
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.yesBtn = QPushButton(self.buttonsWidget)
        self.yesBtn.setObjectName(u"yesBtn")
        self.yesBtn.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/Log-Out--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.yesBtn.setIcon(icon1)
        self.yesBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.yesBtn)


        self.verticalLayout_4.addWidget(self.buttonsWidget, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.widget)


        self.verticalLayout_2.addWidget(self.mainWidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(customServerMessageDialog)

        QMetaObject.connectSlotsByName(customServerMessageDialog)
    # setupUi

    def retranslateUi(self, customServerMessageDialog):
        customServerMessageDialog.setWindowTitle(QCoreApplication.translate("customServerMessageDialog", u"CustomYesNoDialog", None))
        self.warningIcon.setText("")
        self.mainTextLabel.setText(QCoreApplication.translate("customServerMessageDialog", u"\u0413\u0420\u0415\u0428\u041a\u0410", None))
        self.questionTextLabel.setText(QCoreApplication.translate("customServerMessageDialog", u"\u041d\u044f\u043c\u0430 \u0432\u0440\u044a\u0437\u043a\u0430 \u0441\u044a\u0441 \u0441\u044a\u0440\u0432\u044a\u0440\u0430!", None))
        self.yesBtn.setText(QCoreApplication.translate("customServerMessageDialog", u"\u0418\u0437\u0445\u043e\u0434", None))
    # retranslateUi

