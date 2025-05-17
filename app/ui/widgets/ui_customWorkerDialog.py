# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customWorkerDialoggheOBn.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDialog, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_CustomWorkerDialog(object):
    def setupUi(self, CustomWorkerDialog):
        if not CustomWorkerDialog.objectName():
            CustomWorkerDialog.setObjectName(u"CustomWorkerDialog")
        CustomWorkerDialog.resize(722, 398)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CustomWorkerDialog.sizePolicy().hasHeightForWidth())
        CustomWorkerDialog.setSizePolicy(sizePolicy)
        CustomWorkerDialog.setMinimumSize(QSize(0, 0))
        CustomWorkerDialog.setMouseTracking(True)
        CustomWorkerDialog.setStyleSheet(u"*{\n"
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
        self.verticalLayout_2 = QVBoxLayout(CustomWorkerDialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainWidget = QWidget(CustomWorkerDialog)
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
        self.widget.setMinimumSize(QSize(650, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.startDateEdit = QDateEdit(self.widget_5)
        self.startDateEdit.setObjectName(u"startDateEdit")
        self.startDateEdit.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_5.addWidget(self.startDateEdit)

        self.calStartBtn = QPushButton(self.widget_5)
        self.calStartBtn.setObjectName(u"calStartBtn")
        self.calStartBtn.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Calendar--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.calStartBtn.setIcon(icon)
        self.calStartBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.calStartBtn, 0, Qt.AlignLeft)

        self.startCheckBox = QCheckBox(self.widget_5)
        self.startCheckBox.setObjectName(u"startCheckBox")
        self.startCheckBox.setChecked(True)

        self.horizontalLayout_5.addWidget(self.startCheckBox, 0, Qt.AlignLeft)


        self.gridLayout.addWidget(self.widget_5, 1, 3, 1, 1, Qt.AlignLeft)

        self.cehoveComboBox = QComboBox(self.widget)
        self.cehoveComboBox.setObjectName(u"cehoveComboBox")
        self.cehoveComboBox.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.cehoveComboBox, 5, 1, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 5, 2, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 6, 2, 1, 1)

        self.paymentTypeComboBox = QComboBox(self.widget)
        self.paymentTypeComboBox.setObjectName(u"paymentTypeComboBox")
        self.paymentTypeComboBox.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.paymentTypeComboBox, 3, 3, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)

        self.workerTownAdress = QLineEdit(self.widget)
        self.workerTownAdress.setObjectName(u"workerTownAdress")

        self.gridLayout.addWidget(self.workerTownAdress, 5, 3, 1, 1)

        self.workerEGN = QLineEdit(self.widget)
        self.workerEGN.setObjectName(u"workerEGN")

        self.gridLayout.addWidget(self.workerEGN, 7, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 4, 2, 1, 1)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.leaveDateEdit = QDateEdit(self.widget_6)
        self.leaveDateEdit.setObjectName(u"leaveDateEdit")
        self.leaveDateEdit.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_6.addWidget(self.leaveDateEdit)

        self.calLeavingBtn = QPushButton(self.widget_6)
        self.calLeavingBtn.setObjectName(u"calLeavingBtn")
        self.calLeavingBtn.setFocusPolicy(Qt.NoFocus)
        self.calLeavingBtn.setIcon(icon)
        self.calLeavingBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.calLeavingBtn, 0, Qt.AlignLeft)

        self.leavingCheckBox = QCheckBox(self.widget_6)
        self.leavingCheckBox.setObjectName(u"leavingCheckBox")

        self.horizontalLayout_6.addWidget(self.leavingCheckBox)


        self.gridLayout.addWidget(self.widget_6, 2, 3, 1, 1, Qt.AlignLeft)

        self.positionComboBox = QComboBox(self.widget)
        self.positionComboBox.setObjectName(u"positionComboBox")
        self.positionComboBox.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.positionComboBox, 6, 1, 1, 1)

        self.workerNumber = QLineEdit(self.widget)
        self.workerNumber.setObjectName(u"workerNumber")

        self.gridLayout.addWidget(self.workerNumber, 4, 1, 1, 1)

        self.workerLastname = QLineEdit(self.widget)
        self.workerLastname.setObjectName(u"workerLastname")

        self.gridLayout.addWidget(self.workerLastname, 3, 1, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 3, 2, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.workerTel = QLineEdit(self.widget)
        self.workerTel.setObjectName(u"workerTel")

        self.gridLayout.addWidget(self.workerTel, 4, 3, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.workerStreetAdress = QLineEdit(self.widget)
        self.workerStreetAdress.setObjectName(u"workerStreetAdress")

        self.gridLayout.addWidget(self.workerStreetAdress, 6, 3, 1, 1)

        self.workerSirname = QLineEdit(self.widget)
        self.workerSirname.setObjectName(u"workerSirname")

        self.gridLayout.addWidget(self.workerSirname, 2, 1, 1, 1)

        self.workerName = QLineEdit(self.widget)
        self.workerName.setObjectName(u"workerName")

        self.gridLayout.addWidget(self.workerName, 1, 1, 1, 1)


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
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.yesBtn = QPushButton(self.buttonsWidget)
        self.yesBtn.setObjectName(u"yesBtn")
        self.yesBtn.setFont(font)
        self.yesBtn.setFocusPolicy(Qt.ClickFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/Check-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.yesBtn.setIcon(icon1)
        self.yesBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.yesBtn)


        self.verticalLayout.addWidget(self.buttonsWidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.mainWidget, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(CustomWorkerDialog)

        QMetaObject.connectSlotsByName(CustomWorkerDialog)
    # setupUi

    def retranslateUi(self, CustomWorkerDialog):
        CustomWorkerDialog.setWindowTitle(QCoreApplication.translate("CustomWorkerDialog", u"CustomYesNoDialog", None))
        self.dialogTitle.setText(QCoreApplication.translate("CustomWorkerDialog", u"\u0414\u0435\u0442\u0430\u0439\u043b\u0438 \u0437\u0430 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a", None))
        self.startDateEdit.setDisplayFormat(QCoreApplication.translate("CustomWorkerDialog", u"dd.MM.yy '\u0433.'", None))
        self.calStartBtn.setText("")
        self.startCheckBox.setText("")
        self.label_7.setText(QCoreApplication.translate("CustomWorkerDialog", u"\u0414\u043b\u044a\u0436\u043d\u043e\u0441\u0442", None))
        self.label_4.setText(QCoreApplication.translate("CustomWorkerDialog", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_13.setText(QCoreApplication.translate("CustomWorkerDialog", u"\u0410\u0434\u0440\u0435\u0441 \u0433\u0440.", None))
        self.label_9.setText(QCoreApplication.translate("CustomWorkerDialog", u"\u0414\u0430\u0442\u0430 \u041d\u0430\u043f\u0443\u0441\u043a\u0430\u043d\u0435", None))
        self.label_6.setText(QCoreApplication.translate("CustomWorkerDialog", u"\u0413\u0440\u0443\u043f\u0430", None))
        self.label_14.setText(QCoreApplication.translate("CustomWorkerDialog", u"\u0443\u043b.", None))
        self.label_10.setText(QCoreApplication.translate("CustomWorkerDialog", u"\u0414\u0430\u0442\u0430 \u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label_5.setText(QCoreApplication.translate("CustomWorkerDialog", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.label_12.setText(QCoreApplication.translate("CustomWorkerDialog", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.leaveDateEdit.setDisplayFormat(QCoreApplication.translate("CustomWorkerDialog", u"dd.MM.yy '\u0433.'", None))
        self.calLeavingBtn.setText("")
        self.leavingCheckBox.setText("")
        self.label_11.setText(QCoreApplication.translate("CustomWorkerDialog", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0437\u0430\u043f\u043b\u0430\u0449\u0430\u043d\u0435", None))
        self.label_8.setText(QCoreApplication.translate("CustomWorkerDialog", u"\u0415\u0413\u041d", None))
        self.label_3.setText(QCoreApplication.translate("CustomWorkerDialog", u"\u041f\u0440\u0435\u0437\u0438\u043c\u0435", None))
        self.label_2.setText(QCoreApplication.translate("CustomWorkerDialog", u"\u0418\u043c\u0435", None))
        self.yesBtn.setText(QCoreApplication.translate("CustomWorkerDialog", u" \u0414\u0410", None))
    # retranslateUi

