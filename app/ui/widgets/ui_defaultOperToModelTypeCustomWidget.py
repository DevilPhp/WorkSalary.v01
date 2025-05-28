# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'defaultOperToModelTypeCustomWidgetpqSxUJ.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_customWidgetForDefaultOper(object):
    def setupUi(self, customWidgetForDefaultOper):
        if not customWidgetForDefaultOper.objectName():
            customWidgetForDefaultOper.setObjectName(u"customWidgetForDefaultOper")
        customWidgetForDefaultOper.resize(1184, 893)
        customWidgetForDefaultOper.setMinimumSize(QSize(800, 700))
        customWidgetForDefaultOper.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 600 11pt \"Segoe UI\";\n"
"	color: #324b4c;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #c9c9c9;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-size: 10.5pt;\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #aeaeae;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"	color: #008b69;\n"
"}\n"
"\n"
"#optionsHolder {\n"
"	border: none;\n"
"	border-bottom: 2px dashed #7c9399;\n"
"}\n"
"\n"
"#pageTitle {\n"
"	font: 700 13pt \"Segoe UI\";\n"
"}\n"
"\n"
"#userIcon {\n"
"	background-color: #dfdfdf;\n"
"}\n"
"\n"
"#usernameLabel {\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"#delDefModelTypeBtn {\n"
"	padding: 2px;\n"
"}")
        self.verticalLayout = QVBoxLayout(customWidgetForDefaultOper)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.widget = QWidget(customWidgetForDefaultOper)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.saveBtn = QPushButton(self.widget_4)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.saveBtn)

        self.addNewOperation = QPushButton(self.widget_4)
        self.addNewOperation.setObjectName(u"addNewOperation")

        self.horizontalLayout_2.addWidget(self.addNewOperation)

        self.addNeModelType = QPushButton(self.widget_4)
        self.addNeModelType.setObjectName(u"addNeModelType")

        self.horizontalLayout_2.addWidget(self.addNeModelType)


        self.horizontalLayout.addWidget(self.widget_4, 0, Qt.AlignLeft)

        self.pageTitle = QLabel(self.widget_2)
        self.pageTitle.setObjectName(u"pageTitle")

        self.horizontalLayout.addWidget(self.pageTitle, 0, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 5, 0)
        self.userIcon = QPushButton(self.widget_3)
        self.userIcon.setObjectName(u"userIcon")
        self.userIcon.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/User--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userIcon.setIcon(icon)
        self.userIcon.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.userIcon)

        self.usernameLabel = QLabel(self.widget_3)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.horizontalLayout_3.addWidget(self.usernameLabel)


        self.horizontalLayout.addWidget(self.widget_3, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 15, 0)
        self.defaultModelTypeComboBox = QComboBox(self.widget_5)
        self.defaultModelTypeComboBox.setObjectName(u"defaultModelTypeComboBox")
        self.defaultModelTypeComboBox.setFocusPolicy(Qt.NoFocus)
        self.defaultModelTypeComboBox.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.defaultModelTypeComboBox, 0, Qt.AlignHCenter)

        self.optionsHolder = QFrame(self.widget_5)
        self.optionsHolder.setObjectName(u"optionsHolder")
        self.optionsHolder.setFrameShape(QFrame.StyledPanel)
        self.optionsHolder.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.optionsHolder)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.selectAllCheckbox = QCheckBox(self.optionsHolder)
        self.selectAllCheckbox.setObjectName(u"selectAllCheckbox")
        self.selectAllCheckbox.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_4.addWidget(self.selectAllCheckbox, 0, Qt.AlignLeft)

        self.delDefModelTypeBtn = QPushButton(self.optionsHolder)
        self.delDefModelTypeBtn.setObjectName(u"delDefModelTypeBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/Trash-Bin-Trash--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delDefModelTypeBtn.setIcon(icon1)
        self.delDefModelTypeBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_4.addWidget(self.delDefModelTypeBtn, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.optionsHolder, 0, Qt.AlignVCenter)

        self.operationsCheckBoxHolder = QWidget(self.widget_5)
        self.operationsCheckBoxHolder.setObjectName(u"operationsCheckBoxHolder")
        self.verticalLayout_3 = QVBoxLayout(self.operationsCheckBoxHolder)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.operationsLayout = QGridLayout()
        self.operationsLayout.setObjectName(u"operationsLayout")
        self.operationsLayout.setHorizontalSpacing(25)
        self.operationsLayout.setVerticalSpacing(8)

        self.verticalLayout_3.addLayout(self.operationsLayout)


        self.verticalLayout_2.addWidget(self.operationsCheckBoxHolder, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)


        self.retranslateUi(customWidgetForDefaultOper)

        QMetaObject.connectSlotsByName(customWidgetForDefaultOper)
    # setupUi

    def retranslateUi(self, customWidgetForDefaultOper):
        customWidgetForDefaultOper.setWindowTitle(QCoreApplication.translate("customWidgetForDefaultOper", u"Form", None))
        self.saveBtn.setText(QCoreApplication.translate("customWidgetForDefaultOper", u"\u0417\u0430\u043f\u0430\u0437\u0432\u0430\u043d\u0435", None))
        self.addNewOperation.setText(QCoreApplication.translate("customWidgetForDefaultOper", u"\u041d\u043e\u0432\u0430 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.addNeModelType.setText(QCoreApplication.translate("customWidgetForDefaultOper", u"\u041d\u043e\u0432 \u0432\u0438\u0434", None))
        self.pageTitle.setText(QCoreApplication.translate("customWidgetForDefaultOper", u"\u041e\u041f\u0415\u0420\u0410\u0426\u0418\u0418 \u0418 \u0412\u0418\u0414\u041e\u0412\u0415 \u041c\u041e\u0414\u0415\u041b\u0418", None))
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customWidgetForDefaultOper", u"admin", None))
        self.selectAllCheckbox.setText(QCoreApplication.translate("customWidgetForDefaultOper", u"\u0412\u0441\u0438\u0447\u043a\u0438", None))
        self.delDefModelTypeBtn.setText("")
    # retranslateUi

