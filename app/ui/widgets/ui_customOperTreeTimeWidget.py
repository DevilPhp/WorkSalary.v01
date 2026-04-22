# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customOperTreeTimeWidgetEcMXnf.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_customOperTreeTimeWidget(object):
    def setupUi(self, customOperTreeTimeWidget):
        if not customOperTreeTimeWidget.objectName():
            customOperTreeTimeWidget.setObjectName(u"customOperTreeTimeWidget")
        customOperTreeTimeWidget.resize(325, 23)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(customOperTreeTimeWidget.sizePolicy().hasHeightForWidth())
        customOperTreeTimeWidget.setSizePolicy(sizePolicy)
        customOperTreeTimeWidget.setMinimumSize(QSize(0, 0))
        customOperTreeTimeWidget.setStyleSheet(u"*{\n"
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
"#label {\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"#operPositionLabel {\n"
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
        self.verticalLayout = QVBoxLayout(customOperTreeTimeWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(customOperTreeTimeWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.operPositionLabel = QLabel(self.widget)
        self.operPositionLabel.setObjectName(u"operPositionLabel")

        self.verticalLayout_2.addWidget(self.operPositionLabel, 0, Qt.AlignHCenter)

        self.opersGridLayout = QGridLayout()
        self.opersGridLayout.setObjectName(u"opersGridLayout")
        self.opersGridLayout.setHorizontalSpacing(5)
        self.opersGridLayout.setVerticalSpacing(0)

        self.verticalLayout_2.addLayout(self.opersGridLayout)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(customOperTreeTimeWidget)

        QMetaObject.connectSlotsByName(customOperTreeTimeWidget)
    # setupUi

    def retranslateUi(self, customOperTreeTimeWidget):
        customOperTreeTimeWidget.setWindowTitle(QCoreApplication.translate("customOperTreeTimeWidget", u"Form", None))
        self.operPositionLabel.setText(QCoreApplication.translate("customOperTreeTimeWidget", u"\u0422\u0438\u043f>\u0424\u0430\u0439\u043d>\u0413\u0440\u0443\u043f\u0430", None))
    # retranslateUi

