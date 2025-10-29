from datetime import datetime
from typing import Dict

from PySide6.QtCore import Signal
from PySide6.QtGui import QDoubleValidator, QIntValidator

from app.ui.widgets.ui_customPayPerTimeDialog import *
from app.ui.customCalendarWidget import CustomCalendarDialog
from app.utils.utils import Utils
from PySide6.QtWidgets import QGraphicsDropShadowEffect


class CustomPayPerTimeDialog(QDialog, Ui_CustomPayPerTimeDialog):
    newEntryInfo = Signal(dict)

    def __init__(self, currentLev, currentEuro, parent=None):
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
        # self.slot = slot
        self.levaPerMinLineEdit.setText(str(currentLev))
        self.euroPerMinLineEdit.setText(str(currentEuro))
        self.levaForEuro = float(self.euroPerLevaLineEdit.text())
        self.percentageLineEdit.setEnabled(False)
        self.percentageCheckBox.stateChanged.connect(self.percentageCheckBoxChange)

        self.yesBtn.clicked.connect(self.acceptNewInput)
        # self.noBtn.clicked.connect(self.close)

        validator = QDoubleValidator(0.1, float('inf'), 4)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        locale = QLocale(QLocale.Language.English)
        validator.setLocale(locale)
        validator2 = QIntValidator(-100, 100)
        validator.setLocale(locale)

        self.levaPerMinLineEdit.setValidator(validator)
        self.euroPerMinLineEdit.setValidator(validator)
        self.euroPerLevaLineEdit.setValidator(validator)

        self.percentageLineEdit.setValidator(validator2)

        self.levaPerMinLineEdit.textChanged.connect(self.checkText)
        self.levaPerMinLineEdit.editingFinished.connect(self.updateText)
        self.euroPerMinLineEdit.textChanged.connect(self.checkText)
        self.euroPerMinLineEdit.editingFinished.connect(self.updateText)
        self.euroPerLevaLineEdit.textChanged.connect(self.checkText)
        self.euroPerLevaLineEdit.editingFinished.connect(self.updateText)
        self.levaPerMinUpdated = False

        self.activedDateDateEdit.setDate(QDate.currentDate())

        self.calBtn.clicked.connect(self.openCalendar)
        self.percentageLineEdit.editingFinished.connect(self.updateValuesPerMin)
        # self.levaPerMinLineEdit.returnPressed.connect(self.updateText)

        # self.euroPerMinLineEdit.returnPressed.connect(self.updateText)
        # self.euroPerLevaLineEdit.editingFinished.connect(self.updateEuroPerLeva)

        self.levaPerMinLineEdit.setFocus()

        # self.show()

    # def updateEuroPerLeva(self):
    #     self.levaForEuro = float(self.euroPerLevaLineEdit.text())
    #     if self.levaPerMinLineEdit.text() == "":
    #         self.levaPerMinLineEdit.setText("0")
    #     levaPerMin = float(self.levaPerMinLineEdit.text())
    #     self.euroPerMinLineEdit.setText(str(round(levaPerMin / self.levaForEuro, 5)))
    #     # self.euroPerMinLineEdit.setFocus()

    def updateValuesPerMin(self):
        percentage = float(self.percentageLineEdit.text()) / 100
        levaPerMin = float(self.levaPerMinLineEdit.text()) if self.levaPerMinLineEdit.text() != '' else 0
        euroPerMin = float(self.euroPerMinLineEdit.text()) if self.euroPerMinLineEdit.text() != '' else 0
        levUpdated = round(levaPerMin + (percentage * levaPerMin), 4)
        euroUpdated = round(euroPerMin + (percentage * euroPerMin), 4)
        self.levaPerMinLineEdit.setText(str(levUpdated))
        self.euroPerMinLineEdit.setText(str(euroUpdated))

    def percentageCheckBoxChange(self):
        if self.percentageCheckBox.isChecked():
            self.percentageLineEdit.setEnabled(True)
            self.percentageLineEdit.setFocus()
        # self.percentageLineEdit.setEnabled(self.percentageCheckBox.isChecked())
        else:
            self.percentageLineEdit.setEnabled(False)
            self.percentageLineEdit.clear()
            self.levaPerMinLineEdit.setFocus()
        # if self.percentageLineEdit.isEnabled():
        #     self.percentageLineEdit.setFocus()
        # else:
        #     self.levaPerMinLineEdit.setFocus()

    def acceptNewInput(self):
        if self.euroPerMinLineEdit.text() == '' or self.euroPerMinLineEdit.text() == '0':
            self.euroPerMinLineEdit.setFocus()
            self.euroPerMinLineEdit.selectAll()
            return
        elif self.euroPerLevaLineEdit.text() == '' or self.euroPerLevaLineEdit.text() == '0':
            self.euroPerLevaLineEdit.setFocus()
            self.euroPerLevaLineEdit.selectAll()
            return
        elif self.levaPerMinLineEdit.text() == '' or self.levaPerMinLineEdit.text() == '0':
            self.levaPerMinLineEdit.setFocus()
            self.levaPerMinLineEdit.selectAll()
            return
        levaPerMin = float(self.levaPerMinLineEdit.text())
        euroPerMin = float(self.euroPerMinLineEdit.text())
        levaPerEuro = float(self.euroPerLevaLineEdit.text())
        dateActive = datetime.strptime(self.activedDateDateEdit.date().toString('dd.MM.yyyy'), "%d.%m.%Y")
        comment = self.commentLineEdit.text()
        returnedDict = {
            'levaPerMin': levaPerMin,
            'euroPerMin': euroPerMin,
            'levaPerEuro': levaPerEuro,
            'dateActive': dateActive,
            'comment': comment
        }
        # returnedDict = [levaPerMin, euroPerMin, dateActive, comment
        # returnedDict = 'hello'
        # print(returnedDict)
        self.newEntryInfo.emit(returnedDict)
        self.close()

    def openCalendar(self):
        calDialog = CustomCalendarDialog()
        calDialog.calendarCustomWidget.setSelectedDate(self.activedDateDateEdit.date())
        Utils.calculatingIdealDialogShowPos(self, calDialog)
        calDialog.dateSelected.connect(self.updateDateLabel)
        calDialog.exec_()

    def updateDateLabel(self, date):
        self.activedDateDateEdit.setDate(date)

    def checkText(self, text):
        if ',' in text:
            text = text.split(',')[0]
            text = text + '.'
        self.sender().setText(text)

        if self.levaPerMinUpdated:
            self.levaPerMinUpdated = False

    def updateText(self):

        # if self.sender() == self.euroPerLevaLineEdit:
        #     self.levaForEuro = float(self.euroPerLevaLineEdit.text())
        #     if self.levaPerMinLineEdit.text() == "":
        #         self.levaPerMinLineEdit.setText("0")
        #     levaPerMin = float(self.levaPerMinLineEdit.text())
        #     self.euroPerMinLineEdit.setText(str(round(levaPerMin / self.levaForEuro, 5)))
        # print('here')
        text = float(self.sender().text())
        self.sender().setText(str(text))
        # print(text)

        if self.sender() == self.levaPerMinLineEdit:
            if not self.levaPerMinUpdated:
                self.euroPerMinLineEdit.blockSignals(True)
                self.euroPerMinLineEdit.setText(str(round(text / self.levaForEuro, 4)))
                self.euroPerMinLineEdit.blockSignals(False)
                self.euroPerMinLineEdit.setFocus()
                self.levaPerMinUpdated = True
        elif self.sender() == self.euroPerMinLineEdit:
            if not self.levaPerMinUpdated:
                self.levaPerMinLineEdit.blockSignals(True)
                self.levaPerMinLineEdit.setText(str(round(text * self.levaForEuro, 4)))
                self.levaPerMinLineEdit.blockSignals(False)
                self.activedDateDateEdit.setFocus()
                self.levaPerMinUpdated = True
        elif self.sender() == self.euroPerLevaLineEdit:
            self.levaForEuro = float(self.euroPerLevaLineEdit.text())
            if self.levaPerMinLineEdit.text() == "":
                self.levaPerMinLineEdit.setText("0")
            levaPerMin = float(self.levaPerMinLineEdit.text())
            self.euroPerMinLineEdit.blockSignals(True)
            self.euroPerMinLineEdit.setText(str(round(levaPerMin / self.levaForEuro, 4)))
            self.euroPerMinLineEdit.blockSignals(False)

