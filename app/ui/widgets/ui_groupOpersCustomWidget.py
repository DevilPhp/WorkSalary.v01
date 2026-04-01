# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'groupOpersCustomWidgetwvQJsw.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_customWidgetGroupOpers(object):
    def setupUi(self, customWidgetGroupOpers):
        if not customWidgetGroupOpers.objectName():
            customWidgetGroupOpers.setObjectName(u"customWidgetGroupOpers")
        customWidgetGroupOpers.resize(1139, 699)
        customWidgetGroupOpers.setMinimumSize(QSize(800, 580))
        customWidgetGroupOpers.setStyleSheet(u"*{\n"
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
"#modelWorkPlacesBtn {\n"
"	padding: 3px;\n"
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
"	font: 600 8"
                        "pt \"Segoe UI\";\n"
"	height: 10px;  \n"
"	border: 4px solid transparent;\n"
"	padding: 0px 4px 0px 4px;\n"
"}")
        self.verticalLayout = QVBoxLayout(customWidgetGroupOpers)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 5, 10, 5)
        self.mainWidget = QWidget(customWidgetGroupOpers)
        self.mainWidget.setObjectName(u"mainWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.mainWidget)
        self.verticalLayout_4.setSpacing(10)
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
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 5)
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

        self.paramsWidget = QWidget(self.mainWidget)
        self.paramsWidget.setObjectName(u"paramsWidget")
        self.paramsWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_9 = QHBoxLayout(self.paramsWidget)
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.addModelTypeWidget = QWidget(self.paramsWidget)
        self.addModelTypeWidget.setObjectName(u"addModelTypeWidget")
        self.horizontalLayout_8 = QHBoxLayout(self.addModelTypeWidget)
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.addTypeBtn = QPushButton(self.addModelTypeWidget)
        self.addTypeBtn.setObjectName(u"addTypeBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/app/assets/icons/Add-Square--Streamline-Solar-Broken.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addTypeBtn.setIcon(icon4)
        self.addTypeBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_8.addWidget(self.addTypeBtn)

        self.typeComboBox = QComboBox(self.addModelTypeWidget)
        self.typeComboBox.setObjectName(u"typeComboBox")
        self.typeComboBox.setMinimumSize(QSize(150, 0))
        self.typeComboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_8.addWidget(self.typeComboBox)


        self.horizontalLayout_9.addWidget(self.addModelTypeWidget)

        self.addGaugeWidget = QWidget(self.paramsWidget)
        self.addGaugeWidget.setObjectName(u"addGaugeWidget")
        self.horizontalLayout_7 = QHBoxLayout(self.addGaugeWidget)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.addGaugeBtn = QPushButton(self.addGaugeWidget)
        self.addGaugeBtn.setObjectName(u"addGaugeBtn")
        self.addGaugeBtn.setIcon(icon4)
        self.addGaugeBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_7.addWidget(self.addGaugeBtn)

        self.gaugeComboBox = QComboBox(self.addGaugeWidget)
        self.gaugeComboBox.setObjectName(u"gaugeComboBox")
        self.gaugeComboBox.setMinimumSize(QSize(80, 0))
        self.gaugeComboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_7.addWidget(self.gaugeComboBox)


        self.horizontalLayout_9.addWidget(self.addGaugeWidget)

        self.addGroupOperWidget = QWidget(self.paramsWidget)
        self.addGroupOperWidget.setObjectName(u"addGroupOperWidget")
        self.horizontalLayout_6 = QHBoxLayout(self.addGroupOperWidget)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.addGroupBtn = QPushButton(self.addGroupOperWidget)
        self.addGroupBtn.setObjectName(u"addGroupBtn")
        self.addGroupBtn.setIcon(icon4)
        self.addGroupBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_6.addWidget(self.addGroupBtn)

        self.groupComboBox = QComboBox(self.addGroupOperWidget)
        self.groupComboBox.setObjectName(u"groupComboBox")
        self.groupComboBox.setMinimumSize(QSize(120, 0))
        self.groupComboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_6.addWidget(self.groupComboBox)


        self.horizontalLayout_9.addWidget(self.addGroupOperWidget)

        self.addStructWidget = QWidget(self.paramsWidget)
        self.addStructWidget.setObjectName(u"addStructWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.addStructWidget)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.addStructBtn = QPushButton(self.addStructWidget)
        self.addStructBtn.setObjectName(u"addStructBtn")
        self.addStructBtn.setIcon(icon4)
        self.addStructBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.addStructBtn)

        self.structComboBox = QComboBox(self.addStructWidget)
        self.structComboBox.setObjectName(u"structComboBox")
        self.structComboBox.setMinimumSize(QSize(150, 0))
        self.structComboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_5.addWidget(self.structComboBox)


        self.horizontalLayout_9.addWidget(self.addStructWidget)


        self.verticalLayout_4.addWidget(self.paramsWidget, 0, Qt.AlignLeft)

        self.operationsHolder = QWidget(self.mainWidget)
        self.operationsHolder.setObjectName(u"operationsHolder")
        sizePolicy.setHeightForWidth(self.operationsHolder.sizePolicy().hasHeightForWidth())
        self.operationsHolder.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.operationsHolder)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.optionsHolder = QFrame(self.operationsHolder)
        self.optionsHolder.setObjectName(u"optionsHolder")
        self.optionsHolder.setFrameShape(QFrame.StyledPanel)
        self.optionsHolder.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.optionsHolder)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 5)

        self.verticalLayout_2.addWidget(self.optionsHolder)

        self.operationsInfoHolder = QWidget(self.operationsHolder)
        self.operationsInfoHolder.setObjectName(u"operationsInfoHolder")
        sizePolicy.setHeightForWidth(self.operationsInfoHolder.sizePolicy().hasHeightForWidth())
        self.operationsInfoHolder.setSizePolicy(sizePolicy)
        self.operationsInfoHolder.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_10 = QHBoxLayout(self.operationsInfoHolder)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.operationViewWidget = QWidget(self.operationsInfoHolder)
        self.operationViewWidget.setObjectName(u"operationViewWidget")
        sizePolicy.setHeightForWidth(self.operationViewWidget.sizePolicy().hasHeightForWidth())
        self.operationViewWidget.setSizePolicy(sizePolicy)
        self.operationViewWidget.setMinimumSize(QSize(350, 0))
        self.operationViewWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.operationViewWidget)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.searchWidget = QWidget(self.operationViewWidget)
        self.searchWidget.setObjectName(u"searchWidget")
        sizePolicy.setHeightForWidth(self.searchWidget.sizePolicy().hasHeightForWidth())
        self.searchWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_12 = QHBoxLayout(self.searchWidget)
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 5, 0, 0)
        self.label = QLabel(self.searchWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_12.addWidget(self.label)

        self.searchHolderWidget = QWidget(self.searchWidget)
        self.searchHolderWidget.setObjectName(u"searchHolderWidget")
        self.searchHolderWidget.setMinimumSize(QSize(220, 0))
        self.horizontalLayout_15 = QHBoxLayout(self.searchHolderWidget)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_12.addWidget(self.searchHolderWidget)


        self.verticalLayout_5.addWidget(self.searchWidget, 0, Qt.AlignLeft|Qt.AlignTop)

        self.operationListViewWidget = QWidget(self.operationViewWidget)
        self.operationListViewWidget.setObjectName(u"operationListViewWidget")
        sizePolicy.setHeightForWidth(self.operationListViewWidget.sizePolicy().hasHeightForWidth())
        self.operationListViewWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.operationListViewWidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.operationListViewWidget)


        self.horizontalLayout_10.addWidget(self.operationViewWidget, 0, Qt.AlignLeft)

        self.widget_2 = QWidget(self.operationsInfoHolder)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_7.addWidget(self.widget_5, 0, Qt.AlignHCenter)

        self.modelInfoWidget = QWidget(self.widget_2)
        self.modelInfoWidget.setObjectName(u"modelInfoWidget")
        self.verticalLayout_8 = QVBoxLayout(self.modelInfoWidget)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 5)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.modelInfoWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_10 = QLabel(self.modelInfoWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 1, 4, 1, 1)

        self.label_8 = QLabel(self.modelInfoWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)

        self.label_5 = QLabel(self.modelInfoWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.cehoveBtn = QPushButton(self.modelInfoWidget)
        self.cehoveBtn.setObjectName(u"cehoveBtn")

        self.gridLayout.addWidget(self.cehoveBtn, 1, 3, 1, 1)

        self.yarnLineEdit = QLineEdit(self.modelInfoWidget)
        self.yarnLineEdit.setObjectName(u"yarnLineEdit")

        self.gridLayout.addWidget(self.yarnLineEdit, 2, 3, 1, 1)

        self.dateLineEdit = QLineEdit(self.modelInfoWidget)
        self.dateLineEdit.setObjectName(u"dateLineEdit")

        self.gridLayout.addWidget(self.dateLineEdit, 2, 1, 1, 1)

        self.label_11 = QLabel(self.modelInfoWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 2, 4, 1, 1)

        self.piecesLineEdit = QLineEdit(self.modelInfoWidget)
        self.piecesLineEdit.setObjectName(u"piecesLineEdit")

        self.gridLayout.addWidget(self.piecesLineEdit, 0, 3, 1, 1)

        self.label_9 = QLabel(self.modelInfoWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 4, 1, 1)

        self.modelNameLineEdit = QLineEdit(self.modelInfoWidget)
        self.modelNameLineEdit.setObjectName(u"modelNameLineEdit")

        self.gridLayout.addWidget(self.modelNameLineEdit, 0, 1, 1, 1)

        self.label_7 = QLabel(self.modelInfoWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.label_3 = QLabel(self.modelInfoWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.modelInfoWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.clientNameLineEdit = QLineEdit(self.modelInfoWidget)
        self.clientNameLineEdit.setObjectName(u"clientNameLineEdit")

        self.gridLayout.addWidget(self.clientNameLineEdit, 1, 1, 1, 1)

        self.commentLineEdit = QLineEdit(self.modelInfoWidget)
        self.commentLineEdit.setObjectName(u"commentLineEdit")

        self.gridLayout.addWidget(self.commentLineEdit, 0, 5, 1, 1)

        self.actualCheckBox = QCheckBox(self.modelInfoWidget)
        self.actualCheckBox.setObjectName(u"actualCheckBox")

        self.gridLayout.addWidget(self.actualCheckBox, 1, 5, 1, 1)

        self.forProdCheckBox = QCheckBox(self.modelInfoWidget)
        self.forProdCheckBox.setObjectName(u"forProdCheckBox")

        self.gridLayout.addWidget(self.forProdCheckBox, 2, 5, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout)

        self.widget_10 = QWidget(self.modelInfoWidget)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.saveBtn = QPushButton(self.widget_10)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout_11.addWidget(self.saveBtn)

        self.deleteBtn = QPushButton(self.widget_10)
        self.deleteBtn.setObjectName(u"deleteBtn")

        self.horizontalLayout_11.addWidget(self.deleteBtn)


        self.verticalLayout_8.addWidget(self.widget_10, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.modelInfoWidget, 0, Qt.AlignLeft)

        self.operViewHolderWidget = QWidget(self.widget_2)
        self.operViewHolderWidget.setObjectName(u"operViewHolderWidget")
        sizePolicy.setHeightForWidth(self.operViewHolderWidget.sizePolicy().hasHeightForWidth())
        self.operViewHolderWidget.setSizePolicy(sizePolicy)
        self.operViewHolderWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.operViewHolderWidget)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.operViewHolderWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_17 = QHBoxLayout(self.widget)
        self.horizontalLayout_17.setSpacing(3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 10, 0, 0)
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_17.addWidget(self.label_12)

        self.searchTreeHolderWidget = QWidget(self.widget)
        self.searchTreeHolderWidget.setObjectName(u"searchTreeHolderWidget")
        self.searchTreeHolderWidget.setMinimumSize(QSize(220, 0))
        self.searchTreeHolderWidget.setMaximumSize(QSize(350, 16777215))
        self.horizontalLayout_16 = QHBoxLayout(self.searchTreeHolderWidget)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_17.addWidget(self.searchTreeHolderWidget)


        self.verticalLayout_9.addWidget(self.widget, 0, Qt.AlignLeft|Qt.AlignTop)

        self.operViewWidget = QWidget(self.operViewHolderWidget)
        self.operViewWidget.setObjectName(u"operViewWidget")
        self.verticalLayout_10 = QVBoxLayout(self.operViewWidget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.operViewWidget)


        self.verticalLayout_7.addWidget(self.operViewHolderWidget)


        self.horizontalLayout_10.addWidget(self.widget_2, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.operationsInfoHolder)


        self.verticalLayout_4.addWidget(self.operationsHolder)


        self.verticalLayout.addWidget(self.mainWidget, 0, Qt.AlignTop)


        self.retranslateUi(customWidgetGroupOpers)

        QMetaObject.connectSlotsByName(customWidgetGroupOpers)
    # setupUi

    def retranslateUi(self, customWidgetGroupOpers):
        customWidgetGroupOpers.setWindowTitle(QCoreApplication.translate("customWidgetGroupOpers", u"Form", None))
        self.operationsGroupsReturnBtn.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.pageTitle.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u041e\u041f\u0415\u0420\u0410\u0426\u0418\u0418 \u0417\u0410 \u041c\u041e\u0414\u0415\u041b\u0418", None))
        self.closeBtn.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0417\u0442\u0432\u043e\u0440\u0438", None))
        self.userIcon.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("customWidgetGroupOpers", u"admin", None))
        self.logoutBtn.setText("")
        self.addTypeBtn.setText("")
        self.typeComboBox.setPlaceholderText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0412\u0438\u0434 \u0418\u0437\u0434\u0435\u043b\u0438\u0435", None))
        self.addGaugeBtn.setText("")
        self.gaugeComboBox.setPlaceholderText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0424\u0430\u0439\u043d", None))
        self.addGroupBtn.setText("")
        self.groupComboBox.setPlaceholderText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0413\u0440\u0443\u043f\u0430", None))
        self.addStructBtn.setText("")
        self.structComboBox.setPlaceholderText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430", None))
        self.label.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0422\u044a\u0440\u0441\u0435\u043d\u0435: ", None))
        self.label_2.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u041c\u043e\u0434\u0435\u043b", None))
        self.label_6.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0411\u0440\u043e\u0439:", None))
        self.label_10.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0410\u043a\u0442\u0443\u0430\u043b\u0435\u043d:", None))
        self.label_8.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u041f\u0440\u0435\u0436\u0434\u0430:", None))
        self.label_5.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0414\u0430\u0442\u0430:", None))
        self.cehoveBtn.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0418\u0437\u0431\u0438\u0440\u0430\u043d\u0435", None))
        self.label_11.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0417\u0430 \u043f\u0440\u043e\u0438\u0437\u0432.:", None))
        self.label_9.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u041a\u043e\u043c\u0435\u043d.:", None))
        self.label_7.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0426\u0435\u0445:", None))
        self.label_3.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0418\u043c\u0435:", None))
        self.label_4.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u041a\u043b\u0438\u0435\u043d\u0442:", None))
        self.actualCheckBox.setText("")
        self.forProdCheckBox.setText("")
        self.saveBtn.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0417\u0430\u043f\u0430\u0437\u0432\u0430\u043d\u0435", None))
        self.deleteBtn.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0418\u0437\u0442\u0440\u0438\u0432\u0430\u043d\u0435", None))
        self.label_12.setText(QCoreApplication.translate("customWidgetGroupOpers", u"\u0422\u044a\u0440\u0441\u0435\u043d\u0435: ", None))
    # retranslateUi

