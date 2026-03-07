# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'operToModelTypeCustomWidgetFlAhDI.ui'
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
        customWidgetForModelOper.resize(994, 677)
        customWidgetForModelOper.setMinimumSize(QSize(800, 580))
        customWidgetForModelOper.setStyleSheet(u"*{\n"
"	background-color: #dfdfdf;\n"
"	font: 600 9pt \"Segoe UI\";\n"
"	color: #324b4c;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #c9c9c9;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-size: 8pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #aeaeae;\n"
"}\n"
"\n"
"#operationsHolder QCheckBox:checked, #modelHolder QCheckBox:checked{\n"
"	color: #008b69;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: none;\n"
"	font-size: 8pt;\n"
"	border-bottom: 1px solid #7c9399;\n"
"}\n"
"\n"
"#modelHolder QLabel, #newModelInfoHolder *, #operationsGroupsHolder *, #widget_3 * {\n"
"	font-size: 8pt;\n"
"}\n"
"\n"
"#widget_4 *, #saveOpertaionsGroupsBtn, #saveNewModel, #deleteOperetionGroupsBtn {\n"
"	font-size: 8pt;\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"#modelNameLabel {\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"#optionsHolder {\n"
"	border-bottom: 2px dashed #7c9399;\n"
"}\n"
"\n"
"#pageTitle {\n"
"	font: 700 11pt \"Segoe UI\";\n"
"}\n"
"\n"
"#userIcon, #logoutBtn {\n"
"	background-color:"
                        " #dfdfdf;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"#logoutBtn:hover{\n"
"	icon: url(:/icons/app/assets/icons/Log-Out--Streamline-Feather_#192626.svg);\n"
"}\n"
"\n"
"#deleteModelBtn {\n"
"	background-color: #dfdfdf;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"#deleteModelBtn:hover{\n"
"	background-color: #aeaeae;\n"
"}\n"
"\n"
"#usernameLabel {\n"
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
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	color: #2b2b2c;\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	border-radius: 0px;\n"
"	alternate-background-color: #2c313c;\n"
"}\n"
"QComboBox::item:selected{\n"
"	color: #2b2b2c;\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	border-radius: 0px;\n"
"}\n"
"QComboBox::item{\n"
"	color: #324b4c;\n"
"	font: 600 8pt \"Segoe UI\";\n"
"	height: 10px;  \n"
"	border: 4px s"
                        "olid transparent;\n"
"	padding: 0px 4px 0px 4px;\n"
"}")
        self.verticalLayout = QVBoxLayout(customWidgetForModelOper)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.mainWidget = QWidget(customWidgetForModelOper)
        self.mainWidget.setObjectName(u"mainWidget")
        self.verticalLayout_4 = QVBoxLayout(self.mainWidget)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.headerHolder = QWidget(self.mainWidget)
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
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 5)
        self.operationsGroupViewBtn = QPushButton(self.widget_4)
        self.operationsGroupViewBtn.setObjectName(u"operationsGroupViewBtn")

        self.horizontalLayout_2.addWidget(self.operationsGroupViewBtn)

        self.operationsGroupsReturnBtn = QPushButton(self.widget_4)
        self.operationsGroupsReturnBtn.setObjectName(u"operationsGroupsReturnBtn")
        icon = QIcon()
        icon.addFile(u":/icons/app/assets/icons/Alt-Arrow-Left--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.operationsGroupsReturnBtn.setIcon(icon)
        self.operationsGroupsReturnBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.operationsGroupsReturnBtn)


        self.horizontalLayout.addWidget(self.widget_4, 0, Qt.AlignLeft)

        self.pageTitle = QLabel(self.headerHolder)
        self.pageTitle.setObjectName(u"pageTitle")

        self.horizontalLayout.addWidget(self.pageTitle, 0, Qt.AlignHCenter)

        self.widget_6 = QWidget(self.headerHolder)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.closeBtn = QPushButton(self.widget_8)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setStyleSheet(u"* {\n"
"	padding: 3px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/app/assets/icons/Close-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon1)
        self.closeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.closeBtn)


        self.horizontalLayout_13.addWidget(self.widget_8)

        self.userHolder = QWidget(self.widget_6)
        self.userHolder.setObjectName(u"userHolder")
        self.horizontalLayout_3 = QHBoxLayout(self.userHolder)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 5, 0)
        self.userIcon = QPushButton(self.userHolder)
        self.userIcon.setObjectName(u"userIcon")
        self.userIcon.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/icons/app/assets/icons/User--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userIcon.setIcon(icon2)
        self.userIcon.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.userIcon)

        self.usernameLabel = QLabel(self.userHolder)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.horizontalLayout_3.addWidget(self.usernameLabel)

        self.logoutBtn = QPushButton(self.userHolder)
        self.logoutBtn.setObjectName(u"logoutBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/app/assets/icons/Log-Out--Streamline-Feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBtn.setIcon(icon3)
        self.logoutBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.logoutBtn)


        self.horizontalLayout_13.addWidget(self.userHolder)


        self.horizontalLayout.addWidget(self.widget_6, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.headerHolder)

        self.widget_2 = QWidget(self.mainWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.modelInfoHolder = QWidget(self.widget_2)
        self.modelInfoHolder.setObjectName(u"modelInfoHolder")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelInfoHolder.sizePolicy().hasHeightForWidth())
        self.modelInfoHolder.setSizePolicy(sizePolicy)
        self.modelInfoHolder.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_5 = QHBoxLayout(self.modelInfoHolder)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 0, 5)
        self.modelHolder = QWidget(self.modelInfoHolder)
        self.modelHolder.setObjectName(u"modelHolder")
        self.modelHolder.setMinimumSize(QSize(240, 0))
        self.verticalLayout_5 = QVBoxLayout(self.modelHolder)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.modelHolder)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"* {\n"
"	font-size: 10pt;\n"
"}")

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_7 = QWidget(self.modelHolder)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_7 = QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.modeLayout = QFormLayout()
        self.modeLayout.setObjectName(u"modeLayout")
        self.modeLayout.setHorizontalSpacing(10)
        self.modeLayout.setVerticalSpacing(3)
        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName(u"label_2")

        self.modeLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")

        self.modeLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.label_13 = QLabel(self.widget_7)
        self.label_13.setObjectName(u"label_13")

        self.modeLayout.setWidget(3, QFormLayout.LabelRole, self.label_13)

        self.dataUpdatedLabel = QLabel(self.widget_7)
        self.dataUpdatedLabel.setObjectName(u"dataUpdatedLabel")

        self.modeLayout.setWidget(3, QFormLayout.FieldRole, self.dataUpdatedLabel)

        self.clientsWidget = QWidget(self.widget_7)
        self.clientsWidget.setObjectName(u"clientsWidget")
        self.horizontalLayout_10 = QHBoxLayout(self.clientsWidget)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.modeLayout.setWidget(0, QFormLayout.FieldRole, self.clientsWidget)

        self.modelsWidget = QWidget(self.widget_7)
        self.modelsWidget.setObjectName(u"modelsWidget")
        self.horizontalLayout_11 = QHBoxLayout(self.modelsWidget)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.modeLayout.setWidget(1, QFormLayout.FieldRole, self.modelsWidget)

        self.label_17 = QLabel(self.widget_7)
        self.label_17.setObjectName(u"label_17")

        self.modeLayout.setWidget(2, QFormLayout.LabelRole, self.label_17)

        self.inProductionCheckBox = QCheckBox(self.widget_7)
        self.inProductionCheckBox.setObjectName(u"inProductionCheckBox")

        self.modeLayout.setWidget(2, QFormLayout.FieldRole, self.inProductionCheckBox)


        self.verticalLayout_7.addLayout(self.modeLayout)


        self.verticalLayout_5.addWidget(self.widget_7)


        self.horizontalLayout_5.addWidget(self.modelHolder, 0, Qt.AlignLeft|Qt.AlignTop)

        self.newModelHolder = QWidget(self.modelInfoHolder)
        self.newModelHolder.setObjectName(u"newModelHolder")
        self.newModelHolder.setMinimumSize(QSize(0, 0))
        self.verticalLayout_6 = QVBoxLayout(self.newModelHolder)
        self.verticalLayout_6.setSpacing(5)
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
        self.newModelCheckBox.setFocusPolicy(Qt.ClickFocus)
        self.newModelCheckBox.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.newModelCheckBox)

        self.editModelHolder = QWidget(self.widget_3)
        self.editModelHolder.setObjectName(u"editModelHolder")
        self.editModelHolder.setMinimumSize(QSize(150, 0))
        self.horizontalLayout_9 = QHBoxLayout(self.editModelHolder)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.editModelCheckBox = QCheckBox(self.editModelHolder)
        self.editModelCheckBox.setObjectName(u"editModelCheckBox")

        self.horizontalLayout_9.addWidget(self.editModelCheckBox)

        self.modelNameLabel = QLabel(self.editModelHolder)
        self.modelNameLabel.setObjectName(u"modelNameLabel")

        self.horizontalLayout_9.addWidget(self.modelNameLabel)

        self.deleteModelBtn = QPushButton(self.editModelHolder)
        self.deleteModelBtn.setObjectName(u"deleteModelBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/app/assets/icons/Trash-Bin-Trash--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteModelBtn.setIcon(icon4)
        self.deleteModelBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.deleteModelBtn)


        self.horizontalLayout_6.addWidget(self.editModelHolder)


        self.verticalLayout_6.addWidget(self.widget_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.newModelInfoHolder = QWidget(self.newModelHolder)
        self.newModelInfoHolder.setObjectName(u"newModelInfoHolder")
        self.newModelInfoHolder.setMinimumSize(QSize(0, 0))
        self.verticalLayout_8 = QVBoxLayout(self.newModelInfoHolder)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.modelInfoWidget = QWidget(self.newModelInfoHolder)
        self.modelInfoWidget.setObjectName(u"modelInfoWidget")
        self.verticalLayout_11 = QVBoxLayout(self.modelInfoWidget)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.newModelLayout = QGridLayout()
        self.newModelLayout.setObjectName(u"newModelLayout")
        self.newModelLayout.setHorizontalSpacing(10)
        self.newModelLayout.setVerticalSpacing(3)
        self.modelTypeComboBox = QComboBox(self.modelInfoWidget)
        self.modelTypeComboBox.setObjectName(u"modelTypeComboBox")
        self.modelTypeComboBox.setMaximumSize(QSize(150, 16777215))
        self.modelTypeComboBox.setFocusPolicy(Qt.NoFocus)
        self.modelTypeComboBox.setDuplicatesEnabled(True)

        self.newModelLayout.addWidget(self.modelTypeComboBox, 0, 3, 1, 1)

        self.label_5 = QLabel(self.modelInfoWidget)
        self.label_5.setObjectName(u"label_5")

        self.newModelLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_10 = QLabel(self.modelInfoWidget)
        self.label_10.setObjectName(u"label_10")

        self.newModelLayout.addWidget(self.label_10, 1, 4, 1, 1)

        self.label_8 = QLabel(self.modelInfoWidget)
        self.label_8.setObjectName(u"label_8")

        self.newModelLayout.addWidget(self.label_8, 1, 2, 1, 1)

        self.label_11 = QLabel(self.modelInfoWidget)
        self.label_11.setObjectName(u"label_11")

        self.newModelLayout.addWidget(self.label_11, 2, 4, 1, 1)

        self.newModelLineEdit = QLineEdit(self.modelInfoWidget)
        self.newModelLineEdit.setObjectName(u"newModelLineEdit")
        self.newModelLineEdit.setMaximumSize(QSize(150, 16777215))

        self.newModelLayout.addWidget(self.newModelLineEdit, 0, 1, 1, 1)

        self.clientsComboBox = QComboBox(self.modelInfoWidget)
        self.clientsComboBox.setObjectName(u"clientsComboBox")
        self.clientsComboBox.setFocusPolicy(Qt.NoFocus)

        self.newModelLayout.addWidget(self.clientsComboBox, 0, 5, 1, 1)

        self.machineComboBox = QComboBox(self.modelInfoWidget)
        self.machineComboBox.setObjectName(u"machineComboBox")
        self.machineComboBox.setMaximumSize(QSize(150, 16777215))
        self.machineComboBox.setFocusPolicy(Qt.NoFocus)
        self.machineComboBox.setDuplicatesEnabled(True)

        self.newModelLayout.addWidget(self.machineComboBox, 2, 1, 1, 1)

        self.piecesLineEdit = QLineEdit(self.modelInfoWidget)
        self.piecesLineEdit.setObjectName(u"piecesLineEdit")
        self.piecesLineEdit.setMaximumSize(QSize(150, 16777215))

        self.newModelLayout.addWidget(self.piecesLineEdit, 1, 1, 1, 1)

        self.label_7 = QLabel(self.modelInfoWidget)
        self.label_7.setObjectName(u"label_7")

        self.newModelLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.descrLineEdit = QLineEdit(self.modelInfoWidget)
        self.descrLineEdit.setObjectName(u"descrLineEdit")
        self.descrLineEdit.setMaximumSize(QSize(200, 16777215))

        self.newModelLayout.addWidget(self.descrLineEdit, 1, 5, 1, 1)

        self.label_16 = QLabel(self.modelInfoWidget)
        self.label_16.setObjectName(u"label_16")

        self.newModelLayout.addWidget(self.label_16, 0, 4, 1, 1)

        self.yarnComboBox = QComboBox(self.modelInfoWidget)
        self.yarnComboBox.setObjectName(u"yarnComboBox")
        self.yarnComboBox.setMaximumSize(QSize(150, 16777215))
        self.yarnComboBox.setFocusPolicy(Qt.NoFocus)
        self.yarnComboBox.setDuplicatesEnabled(True)

        self.newModelLayout.addWidget(self.yarnComboBox, 1, 3, 1, 1)

        self.label_3 = QLabel(self.modelInfoWidget)
        self.label_3.setObjectName(u"label_3")

        self.newModelLayout.addWidget(self.label_3, 2, 2, 1, 1)

        self.actualCheckBox = QCheckBox(self.modelInfoWidget)
        self.actualCheckBox.setObjectName(u"actualCheckBox")
        self.actualCheckBox.setFocusPolicy(Qt.ClickFocus)
        self.actualCheckBox.setLayoutDirection(Qt.LeftToRight)

        self.newModelLayout.addWidget(self.actualCheckBox, 2, 5, 1, 1)

        self.label_6 = QLabel(self.modelInfoWidget)
        self.label_6.setObjectName(u"label_6")

        self.newModelLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_9 = QLabel(self.modelInfoWidget)
        self.label_9.setObjectName(u"label_9")

        self.newModelLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.machineGaugeLineEdit = QLineEdit(self.modelInfoWidget)
        self.machineGaugeLineEdit.setObjectName(u"machineGaugeLineEdit")
        self.machineGaugeLineEdit.setMaximumSize(QSize(150, 16777215))

        self.newModelLayout.addWidget(self.machineGaugeLineEdit, 2, 3, 1, 1)


        self.verticalLayout_11.addLayout(self.newModelLayout)


        self.verticalLayout_8.addWidget(self.modelInfoWidget)

        self.effectChangesWidget = QWidget(self.newModelInfoHolder)
        self.effectChangesWidget.setObjectName(u"effectChangesWidget")
        self.effectChangesWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_10 = QVBoxLayout(self.effectChangesWidget)
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.effectChangesWidget)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_10.addWidget(self.label_15)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.effectChangesComboBox = QComboBox(self.effectChangesWidget)
        self.effectChangesComboBox.addItem("")
        self.effectChangesComboBox.addItem("")
        self.effectChangesComboBox.addItem("")
        self.effectChangesComboBox.addItem("")
        self.effectChangesComboBox.addItem("")
        self.effectChangesComboBox.addItem("")
        self.effectChangesComboBox.addItem("")
        self.effectChangesComboBox.addItem("")
        self.effectChangesComboBox.addItem("")
        self.effectChangesComboBox.addItem("")
        self.effectChangesComboBox.addItem("")
        self.effectChangesComboBox.addItem("")
        self.effectChangesComboBox.setObjectName(u"effectChangesComboBox")
        self.effectChangesComboBox.setMinimumSize(QSize(120, 0))

        self.gridLayout_2.addWidget(self.effectChangesComboBox, 0, 1, 1, 1)

        self.effectChangesCheckBox = QCheckBox(self.effectChangesWidget)
        self.effectChangesCheckBox.setObjectName(u"effectChangesCheckBox")

        self.gridLayout_2.addWidget(self.effectChangesCheckBox, 0, 0, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_2)


        self.verticalLayout_8.addWidget(self.effectChangesWidget, 0, Qt.AlignLeft)

        self.saveNewModel = QPushButton(self.newModelInfoHolder)
        self.saveNewModel.setObjectName(u"saveNewModel")
        self.saveNewModel.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_8.addWidget(self.saveNewModel, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.newModelInfoHolder)


        self.horizontalLayout_5.addWidget(self.newModelHolder)


        self.horizontalLayout_7.addWidget(self.modelInfoHolder, 0, Qt.AlignLeft|Qt.AlignTop)

        self.operationsGroupsHolder = QWidget(self.widget_2)
        self.operationsGroupsHolder.setObjectName(u"operationsGroupsHolder")
        self.operationsGroupsHolder.setMinimumSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.operationsGroupsHolder)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setContentsMargins(-1, 5, -1, 5)
        self.label_12 = QLabel(self.operationsGroupsHolder)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)

        self.operationGroupLineEdit = QLineEdit(self.operationsGroupsHolder)
        self.operationGroupLineEdit.setObjectName(u"operationGroupLineEdit")
        self.operationGroupLineEdit.setMinimumSize(QSize(180, 0))

        self.gridLayout.addWidget(self.operationGroupLineEdit, 0, 1, 1, 1)

        self.label_14 = QLabel(self.operationsGroupsHolder)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.operationsGroupsHolder)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.forModelLineEdit = QLineEdit(self.widget_5)
        self.forModelLineEdit.setObjectName(u"forModelLineEdit")

        self.horizontalLayout_8.addWidget(self.forModelLineEdit)

        self.forModelCheckBox = QCheckBox(self.widget_5)
        self.forModelCheckBox.setObjectName(u"forModelCheckBox")

        self.horizontalLayout_8.addWidget(self.forModelCheckBox)


        self.gridLayout.addWidget(self.widget_5, 1, 1, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout)

        self.widget = QWidget(self.operationsGroupsHolder)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_12 = QHBoxLayout(self.widget)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.saveOpertaionsGroupsBtn = QPushButton(self.widget)
        self.saveOpertaionsGroupsBtn.setObjectName(u"saveOpertaionsGroupsBtn")

        self.horizontalLayout_12.addWidget(self.saveOpertaionsGroupsBtn)

        self.deleteOperetionGroupsBtn = QPushButton(self.widget)
        self.deleteOperetionGroupsBtn.setObjectName(u"deleteOperetionGroupsBtn")

        self.horizontalLayout_12.addWidget(self.deleteOperetionGroupsBtn)


        self.verticalLayout_9.addWidget(self.widget, 0, Qt.AlignLeft)


        self.horizontalLayout_7.addWidget(self.operationsGroupsHolder, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.widget_2, 0, Qt.AlignLeft)

        self.operationsHolder = QWidget(self.mainWidget)
        self.operationsHolder.setObjectName(u"operationsHolder")
        sizePolicy.setHeightForWidth(self.operationsHolder.sizePolicy().hasHeightForWidth())
        self.operationsHolder.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.operationsHolder)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 15, 0)
        self.optionsHolder = QFrame(self.operationsHolder)
        self.optionsHolder.setObjectName(u"optionsHolder")
        self.optionsHolder.setFrameShape(QFrame.StyledPanel)
        self.optionsHolder.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.optionsHolder)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 5)
        self.selectAllCheckbox = QCheckBox(self.optionsHolder)
        self.selectAllCheckbox.setObjectName(u"selectAllCheckbox")
        self.selectAllCheckbox.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_4.addWidget(self.selectAllCheckbox)


        self.verticalLayout_2.addWidget(self.optionsHolder)

        self.operationsCheckBoxHolder = QWidget(self.operationsHolder)
        self.operationsCheckBoxHolder.setObjectName(u"operationsCheckBoxHolder")
        sizePolicy.setHeightForWidth(self.operationsCheckBoxHolder.sizePolicy().hasHeightForWidth())
        self.operationsCheckBoxHolder.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.operationsCheckBoxHolder)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.operationsLayout = QGridLayout()
        self.operationsLayout.setObjectName(u"operationsLayout")
        self.operationsLayout.setHorizontalSpacing(25)
        self.operationsLayout.setVerticalSpacing(3)

        self.verticalLayout_3.addLayout(self.operationsLayout)


        self.verticalLayout_2.addWidget(self.operationsCheckBoxHolder, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.operationsHolder)


        self.verticalLayout.addWidget(self.mainWidget, 0, Qt.AlignTop)


        self.retranslateUi(customWidgetForModelOper)

        QMetaObject.connectSlotsByName(customWidgetForModelOper)
    # setupUi

    def retranslateUi(self, customWidgetForModelOper):
        customWidgetForModelOper.setWindowTitle(QCoreApplication.translate("customWidgetForModelOper", u"Form", None))
        self.operationsGroupViewBtn.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0413\u0440\u0443\u043f\u0438\u0440\u0430\u043d\u0435", None))
        self.operationsGroupsReturnBtn.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.pageTitle.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041e\u041f\u0415\u0420\u0410\u0426\u0418\u0418 \u0417\u0410 \u041c\u041e\u0414\u0415\u041b\u0418", None))
        self.closeBtn.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0417\u0442\u0432\u043e\u0440\u0438", None))
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customWidgetForModelOper", u"admin", None))
        self.logoutBtn.setText("")
        self.label.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0422\u044a\u0440\u0441\u0435\u043d\u0435", None))
        self.label_2.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041a\u043b\u0438\u0435\u043d\u0442:", None))
        self.label_4.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041c\u043e\u0434\u0435\u043b:", None))
        self.label_13.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0414\u0430\u0442\u0430:", None))
        self.dataUpdatedLabel.setText("")
        self.label_17.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0412 \u043f\u0440\u043e\u0438\u0437\u0432.", None))
        self.inProductionCheckBox.setText("")
        self.newModelCheckBox.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0421\u044a\u0437\u0434\u0430\u0432\u0430\u043d\u0435 \u043d\u0430 \u043d\u043e\u0432 \u043c\u043e\u0434\u0435\u043b", None))
        self.editModelCheckBox.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u0430\u043d\u0435 \u043d\u0430:", None))
        self.modelNameLabel.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041c\u043e\u0434\u0435\u043b", None))
        self.deleteModelBtn.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0418\u0437\u0442\u0440\u0438\u0432\u0430\u043d\u0435", None))
        self.label_5.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0418\u043c\u0435/\u041f\u043e\u0440\u044a\u0447\u043a\u0430\u2116", None))
        self.label_10.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_8.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041f\u0440\u0435\u0436\u0434\u0430", None))
        self.label_11.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0410\u043a\u0442\u0443\u0430\u043b\u0435\u043d", None))
        self.piecesLineEdit.setPlaceholderText(QCoreApplication.translate("customWidgetForModelOper", u"0", None))
        self.label_7.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0412\u0438\u0434 \u041c\u043e\u0434\u0435\u043b", None))
        self.label_16.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0417\u0430 \u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.label_3.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0424\u0430\u0439\u043d", None))
        self.actualCheckBox.setText("")
        self.label_6.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041c\u0430\u0448\u0438\u043d\u0430/\u0426\u0435\u0445", None))
        self.label_9.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0411\u0440\u043e\u0439", None))
        self.label_15.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u041a\u043e\u0440\u0435\u043a\u0446\u0438\u044f \u043d\u0430 \u043b\u0438\u0441\u0442\u043e\u0432\u0435 \u0437\u0430 \u0432\u0440\u0435\u043c\u0435", None))
        self.effectChangesComboBox.setItemText(0, QCoreApplication.translate("customWidgetForModelOper", u"\u042f\u043d\u0443\u0430\u0440\u0438", None))
        self.effectChangesComboBox.setItemText(1, QCoreApplication.translate("customWidgetForModelOper", u"\u0424\u0435\u0432\u0440\u0443\u0430\u0440\u0438", None))
        self.effectChangesComboBox.setItemText(2, QCoreApplication.translate("customWidgetForModelOper", u"\u041c\u0430\u0440\u0442", None))
        self.effectChangesComboBox.setItemText(3, QCoreApplication.translate("customWidgetForModelOper", u"\u0410\u043f\u0440\u0438\u043b", None))
        self.effectChangesComboBox.setItemText(4, QCoreApplication.translate("customWidgetForModelOper", u"\u041c\u0430\u0439", None))
        self.effectChangesComboBox.setItemText(5, QCoreApplication.translate("customWidgetForModelOper", u"\u042e\u043d\u0438", None))
        self.effectChangesComboBox.setItemText(6, QCoreApplication.translate("customWidgetForModelOper", u"\u042e\u043b\u0438", None))
        self.effectChangesComboBox.setItemText(7, QCoreApplication.translate("customWidgetForModelOper", u"\u0410\u0432\u0433\u0443\u0441\u0442", None))
        self.effectChangesComboBox.setItemText(8, QCoreApplication.translate("customWidgetForModelOper", u"\u0421\u0435\u043f\u0442\u0435\u043c\u0432\u0440\u0438", None))
        self.effectChangesComboBox.setItemText(9, QCoreApplication.translate("customWidgetForModelOper", u"\u041e\u043a\u0442\u043e\u043c\u0432\u0440\u0438", None))
        self.effectChangesComboBox.setItemText(10, QCoreApplication.translate("customWidgetForModelOper", u"\u041d\u043e\u0435\u043c\u0432\u0440\u0438", None))
        self.effectChangesComboBox.setItemText(11, QCoreApplication.translate("customWidgetForModelOper", u"\u0414\u0435\u043a\u0435\u043c\u0432\u0440\u0438", None))

        self.effectChangesCheckBox.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0417\u0430 \u043c\u0435\u0441\u0435\u0446", None))
        self.saveNewModel.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0414\u043e\u0431\u0430\u0432\u044f\u043d\u0435", None))
        self.label_12.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0418\u043c\u0435:", None))
        self.label_14.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0417\u0430 \u041c\u043e\u0434\u0435\u043b:", None))
        self.forModelCheckBox.setText("")
        self.saveOpertaionsGroupsBtn.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0417\u0430\u043f\u0430\u0437\u0432\u0430\u043d\u0435", None))
        self.deleteOperetionGroupsBtn.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0418\u0437\u0442\u0440\u0438\u0432\u0430\u043d\u0435", None))
        self.selectAllCheckbox.setText(QCoreApplication.translate("customWidgetForModelOper", u"\u0412\u0441\u0438\u0447\u043a\u0438", None))
    # retranslateUi

