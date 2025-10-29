# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'workersPageCustomWidgetkKnjGT.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_workersPageWidget(object):
    def setupUi(self, workersPageWidget):
        if not workersPageWidget.objectName():
            workersPageWidget.setObjectName(u"workersPageWidget")
        workersPageWidget.resize(1108, 824)
        workersPageWidget.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 600 12pt \"Segoe UI\";\n"
"	color: #324b4c;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #c9c9c9;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #aeaeae;\n"
"}\n"
"\n"
"QTableView {\n"
"	alternate-background-color: #c1c4c9;\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"QTableView::Item:selected {\n"
"	background-color: rgba(50, 75, 76, 50);\n"
"	border: none;\n"
"	color: #324b4c;\n"
"}")
        self.verticalLayout = QVBoxLayout(workersPageWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(workersPageWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget_4)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Add-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.horizontalLayout.addWidget(self.widget_4, 0, Qt.AlignLeft)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.widget_3, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(workersPageWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QHeaderView:section{\n"
"	font: 700 10.5pt \"Segoe UI\";\n"
"	background-color: #dfdfdf;\n"
"	padding-left: 10px;\n"
"	padding-top:10px;\n"
"	padding-right:10px;\n"
"	selection-background-color: #7f7f7f;\n"
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
"            \n"
"QAbstractItemView::item:selected{\n"
"	background-color: rgba(198, 228, 254, 45);\n"
"}")
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setIconSize(QSize(5, 5))
        self.tableView.setShowGrid(False)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tableView)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(workersPageWidget)

        QMetaObject.connectSlotsByName(workersPageWidget)
    # setupUi

    def retranslateUi(self, workersPageWidget):
        workersPageWidget.setWindowTitle(QCoreApplication.translate("workersPageWidget", u"Form", None))
        self.pushButton.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("workersPageWidget", u"TEST", None))
        self.label.setText(QCoreApplication.translate("workersPageWidget", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("workersPageWidget", u"TextLabel", None))
    # retranslateUi

