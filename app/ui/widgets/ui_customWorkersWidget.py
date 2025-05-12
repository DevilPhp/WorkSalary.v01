# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customWorkersWidgetNjcbJp.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_customWorkersEditWidget(object):
    def setupUi(self, customWorkersEditWidget):
        if not customWorkersEditWidget.objectName():
            customWorkersEditWidget.setObjectName(u"customWorkersEditWidget")
        customWorkersEditWidget.resize(900, 800)
        customWorkersEditWidget.setMinimumSize(QSize(900, 800))
        customWorkersEditWidget.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 600 11pt \"Segoe UI\";\n"
"	color: #324b4c;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"        width: 20px;\n"
"        background: none;\n"
"    }\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"        background: #dfdfdf;\n"
"    }\n"
"\n"
"QPushButton {\n"
"	background-color: #c9c9c9;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-size: 12pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #aeaeae;\n"
"}\n"
"\n"
"#addNewTimePaperBtn {\n"
"	font-size: 11pt;\n"
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
"#statusBar {\n"
"	border: 1px solid #7c9399;\n"
"}\n"
"#statusBar *{\n"
"	font-size: 9pt;\n"
"}\n"
"\n"
"#avrTimePerPiece, #totalSelectedPieces, #totalSelectedTime, #totalSelectedRows, #totalViewRows, #totalWorkingMins,\n"
"#piecesForPro"
                        "dLineEdit, #piecesProducedLineEdit {\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"#modelHolder QLabel, #newModelInfoHolder * , #widget_11 *{\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"#overtimeWarning {\n"
"	background-color: #dfdfdf;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"#optionsHolder, #optionsHolder_2 {\n"
"	border-bottom: 2px dashed #7c9399;\n"
"}\n"
"\n"
"#pageTitle {\n"
"	font: 700 13pt \"Segoe UI\";\n"
"}\n"
"\n"
"#userIcon, #calendarBtn {\n"
"	background-color: #dfdfdf;\n"
"}\n"
"\n"
"#refreshShiftsBtn {\n"
"	padding: 0px;\n"
"	background-color: #dfdfdf;\n"
"}\n"
"\n"
"#usernameLabel {\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"#workerPlaceLineEdit, #workerPositionLineEdit {\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"#widget_3 * {\n"
"	font-size: 10pt;\n"
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
"	height: 18p"
                        "x;\n"
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
"	font: 700 10pt \"Segoe UI\";\n"
"	height: 11px;  \n"
"	border: 4px solid transparent;\n"
"	padding: 0px 8px 0px 8px;\n"
"}")
        self.verticalLayout = QVBoxLayout(customWorkersEditWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(customWorkersEditWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.headerHolder = QWidget(self.widget)
        self.headerHolder.setObjectName(u"headerHolder")
        self.horizontalLayout = QHBoxLayout(self.headerHolder)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.headerHolder)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.widget_4, 0, Qt.AlignLeft)

        self.pageTitle = QLabel(self.headerHolder)
        self.pageTitle.setObjectName(u"pageTitle")

        self.horizontalLayout.addWidget(self.pageTitle, 0, Qt.AlignHCenter)

        self.userHolder = QWidget(self.headerHolder)
        self.userHolder.setObjectName(u"userHolder")
        self.horizontalLayout_3 = QHBoxLayout(self.userHolder)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 5, 0)
        self.userIcon = QPushButton(self.userHolder)
        self.userIcon.setObjectName(u"userIcon")
        self.userIcon.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/User--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userIcon.setIcon(icon)
        self.userIcon.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.userIcon)

        self.usernameLabel = QLabel(self.userHolder)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.horizontalLayout_3.addWidget(self.usernameLabel)


        self.horizontalLayout.addWidget(self.userHolder, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.headerHolder)

        self.workerInfoHolder = QWidget(self.widget)
        self.workerInfoHolder.setObjectName(u"workerInfoHolder")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workerInfoHolder.sizePolicy().hasHeightForWidth())
        self.workerInfoHolder.setSizePolicy(sizePolicy)
        self.workerInfoHolder.setMinimumSize(QSize(400, 200))
        self.verticalLayout_2 = QVBoxLayout(self.workerInfoHolder)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.workerInfoHolder)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget_3 = QWidget(self.workerInfoHolder)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.comboBox = QComboBox(self.widget_3)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 3, 1, 1)

        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 0, 4, 1, 1)

        self.lineEdit_7 = QLineEdit(self.widget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 2, 3, 1, 1)

        self.lineEdit_4 = QLineEdit(self.widget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.widget_3)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 1, 3, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 1, 4, 1, 1)

        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.lineEdit = QLineEdit(self.widget_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)

        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.dateEdit = QDateEdit(self.widget_3)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 0, 5, 1, 1)

        self.dateEdit_2 = QDateEdit(self.widget_3)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.gridLayout.addWidget(self.dateEdit_2, 1, 5, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout_4.addWidget(self.workerInfoHolder, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(customWorkersEditWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 888, 534))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.workersHolder = QWidget(self.scrollAreaWidgetContents)
        self.workersHolder.setObjectName(u"workersHolder")
        self.verticalLayout_11 = QVBoxLayout(self.workersHolder)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 0)

        self.verticalLayout_12.addWidget(self.workersHolder)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(customWorkersEditWidget)

        QMetaObject.connectSlotsByName(customWorkersEditWidget)
    # setupUi

    def retranslateUi(self, customWorkersEditWidget):
        customWorkersEditWidget.setWindowTitle(QCoreApplication.translate("customWorkersEditWidget", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0420\u0410\u0411\u041e\u0422\u041d\u0418\u0426\u0418", None))
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customWorkersEditWidget", u"admin", None))
        self.label.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u041d\u043e\u0432 \u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a", None))
        self.label_5.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.label_10.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0414\u0430\u0442\u0430 \u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u041f\u0440\u0435\u0437\u0438\u043c\u0435", None))
        self.label_9.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0414\u0430\u0442\u0430 \u041d\u0430\u043f\u0443\u0441\u043a\u0430\u043d\u0435", None))
        self.label_6.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0413\u0440\u0443\u043f\u0430", None))
        self.label_2.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0418\u043c\u0435", None))
        self.label_4.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_8.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0415\u0413\u041d", None))
        self.label_7.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0414\u043b\u044a\u0436\u043d\u043e\u0441\u0442", None))
    # retranslateUi

