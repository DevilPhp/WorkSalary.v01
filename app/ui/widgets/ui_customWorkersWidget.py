# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customWorkersWidgetvVRJtC.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)
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
"#calStartBtn, #calLeavingBtn {\n"
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
""
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
        self.workerInfoHolder.setMinimumSize(QSize(750, 200))
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
        self.gridLayout.setHorizontalSpacing(10)
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.worker_5_EGN = QLineEdit(self.widget_3)
        self.worker_5_EGN.setObjectName(u"worker_5_EGN")

        self.gridLayout.addWidget(self.worker_5_EGN, 2, 3, 1, 1)

        self.cehoveComboBox = QComboBox(self.widget_3)
        self.cehoveComboBox.setObjectName(u"cehoveComboBox")
        self.cehoveComboBox.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.cehoveComboBox, 0, 3, 1, 1)

        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 4, 1, 1)

        self.worker_2_sirname = QLineEdit(self.widget_3)
        self.worker_2_sirname.setObjectName(u"worker_2_sirname")

        self.gridLayout.addWidget(self.worker_2_sirname, 1, 1, 1, 1)

        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)

        self.worker_4_number = QLineEdit(self.widget_3)
        self.worker_4_number.setObjectName(u"worker_4_number")

        self.gridLayout.addWidget(self.worker_4_number, 3, 1, 1, 1)

        self.worker_1_name = QLineEdit(self.widget_3)
        self.worker_1_name.setObjectName(u"worker_1_name")

        self.gridLayout.addWidget(self.worker_1_name, 0, 1, 1, 1)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.startDateEdit = QDateEdit(self.widget_5)
        self.startDateEdit.setObjectName(u"startDateEdit")
        self.startDateEdit.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_5.addWidget(self.startDateEdit)

        self.calStartBtn = QPushButton(self.widget_5)
        self.calStartBtn.setObjectName(u"calStartBtn")
        self.calStartBtn.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/Calendar--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.calStartBtn.setIcon(icon1)
        self.calStartBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.calStartBtn, 0, Qt.AlignLeft)


        self.gridLayout.addWidget(self.widget_5, 0, 5, 1, 1)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 1, 4, 1, 1)

        self.worker_3_lastname = QLineEdit(self.widget_3)
        self.worker_3_lastname.setObjectName(u"worker_3_lastname")

        self.gridLayout.addWidget(self.worker_3_lastname, 2, 1, 1, 1)

        self.paymentTypeComboBox = QComboBox(self.widget_3)
        self.paymentTypeComboBox.setObjectName(u"paymentTypeComboBox")
        self.paymentTypeComboBox.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.paymentTypeComboBox, 3, 3, 1, 1)

        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 0, 4, 1, 1)

        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 3, 2, 1, 1)

        self.worker_6_tel = QLineEdit(self.widget_3)
        self.worker_6_tel.setObjectName(u"worker_6_tel")

        self.gridLayout.addWidget(self.worker_6_tel, 2, 5, 1, 1)

        self.positionComboBox = QComboBox(self.widget_3)
        self.positionComboBox.setObjectName(u"positionComboBox")
        self.positionComboBox.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.positionComboBox, 1, 3, 1, 1)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.leaveDateEdit = QDateEdit(self.widget_6)
        self.leaveDateEdit.setObjectName(u"leaveDateEdit")
        self.leaveDateEdit.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_6.addWidget(self.leaveDateEdit)

        self.calLeavingBtn = QPushButton(self.widget_6)
        self.calLeavingBtn.setObjectName(u"calLeavingBtn")
        self.calLeavingBtn.setFocusPolicy(Qt.NoFocus)
        self.calLeavingBtn.setIcon(icon1)
        self.calLeavingBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.calLeavingBtn, 0, Qt.AlignLeft)


        self.gridLayout.addWidget(self.widget_6, 1, 5, 1, 1)

        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 1)

        self.worker_7_townAdress = QLineEdit(self.widget_3)
        self.worker_7_townAdress.setObjectName(u"worker_7_townAdress")

        self.gridLayout.addWidget(self.worker_7_townAdress, 4, 1, 1, 1)

        self.worker_8_streetAdress = QLineEdit(self.widget_3)
        self.worker_8_streetAdress.setObjectName(u"worker_8_streetAdress")

        self.gridLayout.addWidget(self.worker_8_streetAdress, 4, 3, 1, 1)

        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 4, 2, 1, 1)


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
        self.workersTableView = QTableView(self.workersHolder)
        self.workersTableView.setObjectName(u"workersTableView")
        self.workersTableView.setFocusPolicy(Qt.NoFocus)
        self.workersTableView.setStyleSheet(u"QHeaderView:section{\n"
"	font: 700 10.5pt \"Segoe UI\";\n"
"	background-color: #dfdfdf;\n"
"	padding-left: 10px;\n"
"	padding-top:10px;\n"
"	padding-right:10px;\n"
"}\n"
"QVerticalView:section{\n"
"	min-height: 30;\n"
"}\n"
"QAbstractItemView{\n"
"	alternate-background-color: #d3d3d3;\n"
"	font: 10.5pt \"Segoe UI\";\n"
"	selection-background-color: rgba(198, 228, 254, 45);\n"
"	selection-color: #324b4c;\n"
"}\n"
"QAbstractItemView:item{\n"
"	selection-background-color: rgba(198, 228, 254, 45);\n"
"	selection-color: #324b4c;\n"
"}\n"
"QAbstractItemView::item:selected{\n"
"	background-color: rgba(198, 228, 254, 45);\n"
"}")
        self.workersTableView.setCornerButtonEnabled(False)
        self.workersTableView.verticalHeader().setVisible(False)

        self.verticalLayout_11.addWidget(self.workersTableView)


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
        self.label_6.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0413\u0440\u0443\u043f\u0430", None))
        self.label_12.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_8.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0415\u0413\u041d", None))
        self.label_4.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_5.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.label_3.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u041f\u0440\u0435\u0437\u0438\u043c\u0435", None))
        self.startDateEdit.setDisplayFormat(QCoreApplication.translate("customWorkersEditWidget", u"dd.MM.yy '\u0433.'", None))
        self.calStartBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0418\u043c\u0435", None))
        self.label_9.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0414\u0430\u0442\u0430 \u041d\u0430\u043f\u0443\u0441\u043a\u0430\u043d\u0435", None))
        self.label_10.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0414\u0430\u0442\u0430 \u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label_11.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0437\u0430\u043f\u043b\u0430\u0449\u0430\u043d\u0435", None))
        self.leaveDateEdit.setDisplayFormat(QCoreApplication.translate("customWorkersEditWidget", u"dd.MM.yy '\u0433.'", None))
        self.calLeavingBtn.setText("")
        self.label_7.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0414\u043b\u044a\u0436\u043d\u043e\u0441\u0442", None))
        self.label_13.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0410\u0434\u0440\u0435\u0441 \u0433\u0440.", None))
        self.label_14.setText(QCoreApplication.translate("customWorkersEditWidget", u"\u0443\u043b.", None))
    # retranslateUi

