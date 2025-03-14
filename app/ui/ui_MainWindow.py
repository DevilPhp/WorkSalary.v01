# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowPaanJx.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1129, 917)
        MainWindow.setMinimumSize(QSize(756, 670))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	color: #324b4c;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: #c9c9c9;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 0px 5px;\n"
"}\n"
"\n"
"#userLogoLabel {\n"
"	background-color: #dfdfdf;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #c9c9c9;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #aeaeae;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setPixmap(QPixmap(u":/logo/app/assets/logo/KnitexLogo3.png"))

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.logInHolder = QWidget(self.widget)
        self.logInHolder.setObjectName(u"logInHolder")
        self.logInHolder.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.logInHolder)
        self.verticalLayout_3.setSpacing(35)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.userLogoLabel = QPushButton(self.logInHolder)
        self.userLogoLabel.setObjectName(u"userLogoLabel")
        self.userLogoLabel.setFocusPolicy(Qt.NoFocus)
        self.userLogoLabel.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/User--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userLogoLabel.setIcon(icon)
        self.userLogoLabel.setIconSize(QSize(80, 80))

        self.verticalLayout_3.addWidget(self.userLogoLabel)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.label_4 = QLabel(self.logInHolder)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.logInHolder)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lineEdit = QLineEdit(self.logInHolder)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFocusPolicy(Qt.TabFocus)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.logInHolder)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFocusPolicy(Qt.TabFocus)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.pushButton = QPushButton(self.logInHolder)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        self.pushButton.setLayoutDirection(Qt.RightToLeft)
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/Log-In--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.logInHolder, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.widget_4, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.userLogoLabel.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0442\u0440\u0435\u0431\u0438\u0442\u0435\u043b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" \u0412\u0425\u041e\u0414", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

