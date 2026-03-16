from PySide6.QtCore import Signal

from app.ui.widgets.ui_customWorkingPlacesDialog import *
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QCheckBox
from app.services.workerServices import WorkerServices as WoS


class CustomWorkingPlaceDialog(QDialog, Ui_CustomWorkPlacesDialog):
    workPlaces = Signal(list)

    def __init__(self, modelName, existingWorkPlaces, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setXOffset(2)
        shadow.setYOffset(2)
        shadow.setColor(QColor("#7f7f7f"))
        self.setGraphicsEffect(shadow)
        self.modelName = modelName
        self.workingPlaces = None
        self.cehCheckBoxesList = {}
        self.checkedCheckBoxes = []
        self.existingWorkingPlaces = existingWorkPlaces

        self.populateWorkingPlaces()

        self.selectAllCheckBox.stateChanged.connect(self.selectAll)
        self.yesBtn.clicked.connect(self.acceptWorkingPlaces)
        self.noBtn.clicked.connect(self.reject)

    def acceptWorkingPlaces(self):
        # print(self.checkedCheckBoxes)
        self.workPlaces.emit(self.checkedCheckBoxes)
        self.accept()

    def populateWorkingPlaces(self):
        self.modelNameLabel.setText(self.modelName)
        self.workingPlaces = WoS.getWorkingPlaces()
        if self.workingPlaces:
            for index, place in enumerate(self.workingPlaces):
                row = index % 6
                col = index // 6
                cehCheckBox = QCheckBox()
                cehCheckBox.setObjectName(str(place['id']))
                cehCheckBox.setText(place['group'])
                self.cehoveLayout.addWidget(cehCheckBox, row, col)
                cehCheckBox.stateChanged.connect(self.checkBoxStateChanged)
                if place['id'] in self.existingWorkingPlaces:
                    cehCheckBox.blockSignals(True)
                    cehCheckBox.setCheckState(Qt.CheckState.Checked)
                    self.checkedCheckBoxes.append(int(cehCheckBox.objectName()))
                    cehCheckBox.blockSignals(False)
                self.cehCheckBoxesList[place['id']] = cehCheckBox
            self.checkAllCheckBox()

    def selectAll(self, state):
        for cehCheckBox in self.cehCheckBoxesList.values():
            if state == 2:
                cehCheckBox.blockSignals(True)
                cehCheckBox.setCheckState(Qt.CheckState.Checked)
                if int(cehCheckBox.objectName()) not in self.checkedCheckBoxes:
                    self.checkedCheckBoxes.append(int(cehCheckBox.objectName()))
                cehCheckBox.blockSignals(False)
            else:
                cehCheckBox.blockSignals(True)
                cehCheckBox.setCheckState(Qt.CheckState.Unchecked)
                self.checkedCheckBoxes.remove(int(cehCheckBox.objectName()))
                cehCheckBox.blockSignals(False)

    def checkBoxStateChanged(self, state):
        if state == 2:
            self.checkedCheckBoxes.append(int(self.sender().objectName()))
        else:
            self.checkedCheckBoxes.remove(int(self.sender().objectName()))

        self.checkAllCheckBox()

    def checkAllCheckBox(self):
        isAllChecked = True
        for cehCheckBox in self.cehCheckBoxesList.values():
            if not cehCheckBox.isChecked():
                isAllChecked = False
                break
        # print(isAllChecked)
        if isAllChecked:
            self.selectAllCheckBox.blockSignals(True)
            self.selectAllCheckBox.setCheckState(Qt.CheckState.Checked)
            self.selectAllCheckBox.blockSignals(False)
        else:
            self.selectAllCheckBox.blockSignals(True)
            self.selectAllCheckBox.setCheckState(Qt.CheckState.Unchecked)
            self.selectAllCheckBox.blockSignals(False)

        # print(self.checkedCheckBoxes)
