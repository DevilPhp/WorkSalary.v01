# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customAddPayPerMinWidgetCWphGT.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_customAddPayPerMinWidget(object):
    def setupUi(self, customAddPayPerMinWidget):
        if not customAddPayPerMinWidget.objectName():
            customAddPayPerMinWidget.setObjectName(u"customAddPayPerMinWidget")
        customAddPayPerMinWidget.resize(438, 334)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(customAddPayPerMinWidget.sizePolicy().hasHeightForWidth())
        customAddPayPerMinWidget.setSizePolicy(sizePolicy)
        customAddPayPerMinWidget.setStyleSheet(u"*{\n"
"	font: 600 11pt \"Segoe UI\";\n"
"	border: none;\n"
"	background-color: #dfdfdf;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #324b4c;\n"
"}\n"
"\n"
"#customAddPayPerMinWidget{\n"
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
""
                        "	color: #324b4c;\n"
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
"#yesBtn, #noBtn {\n"
"	padding: 0px;\n"
"}\n"
"\n"
"#yesBtn:hover{\n"
"	icon: url(:/icons/app/assets/icons/Check-Square--Streamline-Solar-Broken-#008b69.svg);\n"
"	color: #008b69;\n"
"	padding: 0px;\n"
"}\n"
"#noBtn:hover {\n"
"	icon:url(:/icons/app/assets/icons/Close-Square--Streamline-Solar-Broken-#c75f59.svg);\n"
"	color: #c75f59;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	width: 20px;\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"	background: #dfdfdf;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(customAddPayPerMinWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainWidget = QWidget(customAddPayPerMinWidget)
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
        self.widget.setMinimumSize(QSize(350, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.activedDteEdit = QDateEdit(self.widget_5)
        self.activedDteEdit.setObjectName(u"activedDteEdit")
        self.activedDteEdit.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_5.addWidget(self.activedDteEdit)

        self.calBtn = QPushButton(self.widget_5)
        self.calBtn.setObjectName(u"calBtn")
        self.calBtn.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Calendar--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.calBtn.setIcon(icon)
        self.calBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.calBtn, 0, Qt.AlignLeft)


        self.gridLayout.addWidget(self.widget_5, 5, 1, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.commentLineEdit = QLineEdit(self.widget)
        self.commentLineEdit.setObjectName(u"commentLineEdit")
        self.commentLineEdit.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.commentLineEdit, 6, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.levaPerMinLineEdit = QLineEdit(self.widget)
        self.levaPerMinLineEdit.setObjectName(u"levaPerMinLineEdit")
        self.levaPerMinLineEdit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.levaPerMinLineEdit, 1, 1, 1, 1)

        self.euroForMinLineEdit = QLineEdit(self.widget)
        self.euroForMinLineEdit.setObjectName(u"euroForMinLineEdit")
        self.euroForMinLineEdit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.euroForMinLineEdit, 3, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.euroPerMinLineEdit = QLineEdit(self.widget)
        self.euroPerMinLineEdit.setObjectName(u"euroPerMinLineEdit")
        self.euroPerMinLineEdit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.euroPerMinLineEdit, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


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
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.yesBtn = QPushButton(self.buttonsWidget)
        self.yesBtn.setObjectName(u"yesBtn")
        self.yesBtn.setFont(font)
        self.yesBtn.setFocusPolicy(Qt.ClickFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/Check-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.yesBtn.setIcon(icon1)
        self.yesBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.yesBtn)

        self.noBtn = QPushButton(self.buttonsWidget)
        self.noBtn.setObjectName(u"noBtn")
        self.noBtn.setFont(font)
        self.noBtn.setFocusPolicy(Qt.ClickFocus)
        icon2 = QIcon()
        icon2.addFile(u":/icons/app/assets/icons/Close-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.noBtn.setIcon(icon2)
        self.noBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.noBtn)


        self.verticalLayout.addWidget(self.buttonsWidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.mainWidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(customAddPayPerMinWidget)

        QMetaObject.connectSlotsByName(customAddPayPerMinWidget)
    # setupUi

    def retranslateUi(self, customAddPayPerMinWidget):
        customAddPayPerMinWidget.setWindowTitle(QCoreApplication.translate("customAddPayPerMinWidget", u"Form", None))
        self.dialogTitle.setText(QCoreApplication.translate("customAddPayPerMinWidget", u"\u0414\u0435\u0442\u0430\u0439\u043b\u0438 \u0437\u0430 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a", None))
        self.label_10.setText(QCoreApplication.translate("customAddPayPerMinWidget", u"\u0414\u0430\u0442\u0430 \u0410\u043a\u0442\u0438\u0432\u043d\u0430", None))
        self.label_4.setText(QCoreApplication.translate("customAddPayPerMinWidget", u"\u041a\u0443\u0440\u0441", None))
        self.activedDteEdit.setDisplayFormat(QCoreApplication.translate("customAddPayPerMinWidget", u"dd.MM.yy '\u0433.'", None))
        self.calBtn.setText("")
        self.label_7.setText(QCoreApplication.translate("customAddPayPerMinWidget", u"\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440", None))
        self.label_3.setText(QCoreApplication.translate("customAddPayPerMinWidget", u"\u20ac/\u041c\u0438\u043d", None))
        self.euroForMinLineEdit.setText(QCoreApplication.translate("customAddPayPerMinWidget", u"1.9586", None))
        self.label_2.setText(QCoreApplication.translate("customAddPayPerMinWidget", u"\u041b\u0432/\u041c\u0438\u043d", None))
        self.yesBtn.setText(QCoreApplication.translate("customAddPayPerMinWidget", u" \u0414\u0410", None))
        self.noBtn.setText(QCoreApplication.translate("customAddPayPerMinWidget", u"\u041d\u0415", None))
    # retranslateUi

