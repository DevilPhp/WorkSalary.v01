from PySide6.QtCore import Signal
from PySide6.QtGui import QStandardItemModel, QStandardItem, QDoubleValidator
from PySide6.QtWidgets import QMenu, QDialog

from app.models.tableModel import CustomTableViewWithMultiSelection
from app.models.sortingModel import CaseInsensitiveProxyModel
from app.ui.widgets.ui_customArchiveWidget import *


class CustomArchiveWidget(QWidget, Ui_customArchiveWidget):
    logoutSignal = Signal(bool)

    def __init__(self, mainWindow, user, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.usernameLabel.setText(user)
        self.user = user

        self.archiveModelsCheckBox.stateChanged.connect(self.setForModelsWidgets)

        self.closeBtn.clicked.connect(self.close)
        self.logoutBtn.clicked.connect(self.logout)

    def setForModelsWidgets(self, state):
        print(state)
        self.forYearModelsCheckBox.setEnabled(state)
        self.forMonthModlesCheckBox.setEnabled(state)
        self.forDatesModlesCheckBox.setEnabled(state)

        if state == 0:
            self.resetForModelsWidgets()

    def resetForModelsWidgets(self):
        self.forYearModelsCheckBox.setCheckState(Qt.CheckState.Unchecked)
        self.forMonthModlesCheckBox.setCheckState(Qt.CheckState.Unchecked)
        self.forDatesModlesCheckBox.setCheckState(Qt.CheckState.Unchecked)

        self.forYearModelsComboBox.setCurrentIndex(-1)
        self.forMonthModlesComboBox.setCurrentIndex(0)

    def logout(self):
        self.logoutSignal.emit(True)
