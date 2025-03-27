# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'operToModelTypeCustomWidgetaDJXuy.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_customWidgetForModelOper(object):
    def setupUi(self, customWidgetForModelOper):
        if not customWidgetForModelOper.objectName():
            customWidgetForModelOper.setObjectName(u"customWidgetForModelOper")
        customWidgetForModelOper.resize(1184, 893)
        customWidgetForModelOper.setMinimumSize(QSize(800, 700))
        customWidgetForModelOper.setStyleSheet(u"*{\n"
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
"	font-size: 12pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #aeaeae;\n"
"}\n"
"\n"
"#operationsHolder QCheckBox:checked {\n"
"	color: #008b69;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: none;\n"
"	font-size: 11pt;\n"
"	border-bottom: 1px solid #7c9399;\n"
"}\n"
"\n"
"#modelHolder QLabel, #newModelInfoHolder * {\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"#optionsHolder {\n"
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
"#widget_3 * {\n"
"	font-size: 11pt;\n"
"}")
        self.verticalLayout = QVBoxLayout(customWidgetForModelOper)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.widget = QWidget(customWidgetForModelOper)
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
        self.saveBtn = QPushButton(self.widget_4)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.saveBtn)


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

        self.modelInfoHolder = QWidget(self.widget)
        self.modelInfoHolder.setObjectName(u"modelInfoHolder")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelInfoHolder.sizePolicy().hasHeightForWidth())
        self.modelInfoHolder.setSizePolicy(sizePolicy)
        self.modelInfoHolder.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_5 = QHBoxLayout(self.modelInfoHolder)
        self.horizontalLayout_5.setSpacing(35)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 5)
        self.modelHolder = QWidget(self.modelInfoHolder)
        self.modelHolder.setObjectName(u"modelHolder")
        self.modelHolder.setMinimumSize(QSize(320, 0))
        self.verticalLayout_5 = QVBoxLayout(self.modelHolder)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.modelHolder)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"* {\n"
"	font-size: 11pt;\n"
"}")

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_7 = QWidget(self.modelHolder)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_7 = QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.modeLayout = QFormLayout()
        self.modeLayout.setObjectName(u"modeLayout")
        self.modeLayout.setHorizontalSpacing(10)
        self.modeLayout.setVerticalSpacing(10)
        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName(u"label_2")

        self.modeLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.widget_7)
        self.lineEdit.setObjectName(u"lineEdit")

        self.modeLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")

        self.modeLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_2 = QLineEdit(self.widget_7)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.modeLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)


        self.verticalLayout_7.addLayout(self.modeLayout)


        self.verticalLayout_5.addWidget(self.widget_7)


        self.horizontalLayout_5.addWidget(self.modelHolder, 0, Qt.AlignLeft|Qt.AlignTop)

        self.newModelHolder = QWidget(self.modelInfoHolder)
        self.newModelHolder.setObjectName(u"newModelHolder")
        self.verticalLayout_6 = QVBoxLayout(self.newModelHolder)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.newModelHolder)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.newModelCheckBox = QCheckBox(self.widget_3)
        self.newModelCheckBox.setObjectName(u"newModelCheckBox")
        self.newModelCheckBox.setMinimumSize(QSize(0, 0))
        self.newModelCheckBox.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.newModelCheckBox)

        self.likeModelCheckBox = QCheckBox(self.widget_3)
        self.likeModelCheckBox.setObjectName(u"likeModelCheckBox")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.likeModelCheckBox.setFont(font)

        self.horizontalLayout_6.addWidget(self.likeModelCheckBox)


        self.verticalLayout_6.addWidget(self.widget_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.newModelInfoHolder = QWidget(self.newModelHolder)
        self.newModelInfoHolder.setObjectName(u"newModelInfoHolder")
        self.newModelInfoHolder.setMinimumSize(QSize(0, 0))
        self.verticalLayout_8 = QVBoxLayout(self.newModelInfoHolder)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.newModelLayout = QGridLayout()
        self.newModelLayout.setSpacing(10)
        self.newModelLayout.setObjectName(u"newModelLayout")
        self.label_9 = QLabel(self.newModelInfoHolder)
        self.label_9.setObjectName(u"label_9")

        self.newModelLayout.addWidget(self.label_9, 1, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.newModelInfoHolder)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.newModelLayout.addWidget(self.lineEdit_3, 1, 3, 1, 1)

        self.label_5 = QLabel(self.newModelInfoHolder)
        self.label_5.setObjectName(u"label_5")

        self.newModelLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.newModelInfoHolder)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.newModelLayout.addWidget(self.lineEdit_4, 2, 3, 1, 1)

        self.label_10 = QLabel(self.newModelInfoHolder)
        self.label_10.setObjectName(u"label_10")

        self.newModelLayout.addWidget(self.label_10, 2, 2, 1, 1)

        self.machineComboBox = QComboBox(self.newModelInfoHolder)
        self.machineComboBox.setObjectName(u"machineComboBox")

        self.newModelLayout.addWidget(self.machineComboBox, 1, 1, 1, 1)

        self.modelTypeComboBox = QComboBox(self.newModelInfoHolder)
        self.modelTypeComboBox.setObjectName(u"modelTypeComboBox")

        self.newModelLayout.addWidget(self.modelTypeComboBox, 2, 1, 1, 1)

        self.label_7 = QLabel(self.newModelInfoHolder)
        self.label_7.setObjectName(u"label_7")

        self.newModelLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_8 = QLabel(self.newModelInfoHolder)
        self.label_8.setObjectName(u"label_8")

        self.newModelLayout.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_11 = QLabel(self.newModelInfoHolder)
        self.label_11.setObjectName(u"label_11")

        self.newModelLayout.addWidget(self.label_11, 0, 4, 1, 1)

        self.operNoLineEdit = QLineEdit(self.newModelInfoHolder)
        self.operNoLineEdit.setObjectName(u"operNoLineEdit")

        self.newModelLayout.addWidget(self.operNoLineEdit, 0, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.newModelInfoHolder)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.newModelLayout.addWidget(self.checkBox_2, 0, 5, 1, 1)

        self.label_6 = QLabel(self.newModelInfoHolder)
        self.label_6.setObjectName(u"label_6")

        self.newModelLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.yarnComboBox = QComboBox(self.newModelInfoHolder)
        self.yarnComboBox.setObjectName(u"yarnComboBox")

        self.newModelLayout.addWidget(self.yarnComboBox, 0, 3, 1, 1)


        self.verticalLayout_8.addLayout(self.newModelLayout)

        self.saveNewModel = QPushButton(self.newModelInfoHolder)
        self.saveNewModel.setObjectName(u"saveNewModel")

        self.verticalLayout_8.addWidget(self.saveNewModel, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.newModelInfoHolder)


        self.horizontalLayout_5.addWidget(self.newModelHolder)


        self.verticalLayout_4.addWidget(self.modelInfoHolder, 0, Qt.AlignLeft)

        self.operationsHolder = QWidget(self.widget)
        self.operationsHolder.setObjectName(u"operationsHolder")
        sizePolicy.setHeightForWidth(self.operationsHolder.sizePolicy().hasHeightForWidth())
        self.operationsHolder.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.operationsHolder)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 15, 0)
        self.optionsHolder = QFrame(self.operationsHolder)
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

        self.horizontalLayout_4.addWidget(self.selectAllCheckbox)


        self.verticalLayout_2.addWidget(self.optionsHolder)

        self.operationsCheckBoxHolder = QWidget(self.operationsHolder)
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


        self.verticalLayout_4.addWidget(self.operationsHolder)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)


        self.retranslateUi(customWidgetForModelOper)

        QMetaObject.connectSlotsByName(customWidgetForModelOper)
    # setupUi

    def retranslateUi(self, customWidgetForModelOper):
        customWidgetForModelOper.setWindowTitle(QCoreApplication.translate("customWidgetForModelOper", u"Form", None))
        self.saveBtn.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0417\u0430\u043f\u0430\u0437\u0432\u0430\u043d\u0435", None))
        self.pageTitle.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041e\u041f\u0415\u0420\u0410\u0426\u0418\u0418 \u0417\u0410 \u041c\u041e\u0414\u0415\u041b\u0418", None))
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customWidgetForModelOper", u"admin", None))
        self.label.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0422\u044a\u0440\u0441\u0435\u043d\u0435", None))
        self.label_2.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041a\u043b\u0438\u0435\u043d\u0442:", None))
        self.lineEdit.setText("")
        self.label_4.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041c\u043e\u0434\u0435\u043b:", None))
        self.newModelCheckBox.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0421\u044a\u0437\u0434\u0430\u0432\u0430\u043d\u0435 \u043d\u0430 \u043d\u043e\u0432 \u043c\u043e\u0434\u0435\u043b", None))
        self.likeModelCheckBox.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041a\u0430\u0442\u043e \u041c\u043e\u0434\u0435\u043b", None))
        self.label_9.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0411\u0440\u043e\u0439", None))
        self.label_5.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0418\u043c\u0435/\u041f\u043e\u0440\u044a\u0447\u043a\u0430\u2116", None))
        self.label_10.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_7.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0412\u0438\u0434 \u041c\u043e\u0434\u0435\u043b", None))
        self.label_8.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041f\u0440\u0435\u0436\u0434\u0430", None))
        self.label_11.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0410\u043a\u0442\u0443\u0430\u043b\u0435\u043d", None))
        self.checkBox_2.setText("")
        self.label_6.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041c\u0430\u0448\u0438\u043d\u0430/\u0426\u0435\u0445", None))
        self.saveNewModel.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0414\u043e\u0431\u0430\u0432\u044f\u043d\u0435", None))
        self.selectAllCheckbox.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0412\u0441\u0438\u0447\u043a\u0438", None))
    # retranslateUi

