from datetime import datetime
from typing import Dict

from PySide6.QtCore import Signal
from PySide6.QtGui import QDoubleValidator

from app.ui.widgets.ui_customPayPerTimeDialog import *
from app.ui.customCalendarWidget import CustomCalendarDialog
from app.utils.utils import Utils
from PySide6.QtWidgets import QGraphicsDropShadowEffect


class CustomPayPerTimeDialog(QDialog, Ui_CustomPayPerTimeDialog):
    newEntryInfo = Signal(dict)
    def __init__(self, parent=None):
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

        self.levaForEuro = float(self.euroPerLevaLineEdit.text())

        self.yesBtn.clicked.connect(self.acceptNewInput)
        # self.noBtn.clicked.connect(self.close)

        validator = QDoubleValidator(0.1, float('inf'), 4)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)

        locale = QLocale(QLocale.Language.English)
        validator.setLocale(locale)
        self.levaPerMinLineEdit.setValidator(validator)
        self.euroPerMinLineEdit.setValidator(validator)
        self.euroPerLevaLineEdit.setValidator(validator)
        self.levaPerMinLineEdit.textChanged.connect(self.checkText)
        self.levaPerMinLineEdit.editingFinished.connect(self.updateText)
        self.euroPerMinLineEdit.textChanged.connect(self.checkText)
        self.euroPerMinLineEdit.editingFinished.connect(self.updateText)
        self.euroPerLevaLineEdit.textChanged.connect(self.checkText)
        self.euroPerLevaLineEdit.editingFinished.connect(self.updateText)

        self.activedDateLineEdit.setDate(QDate.currentDate())

        self.calBtn.clicked.connect(self.openCalendar)
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

    def acceptNewInput(self):
        if self.levaPerMinLineEdit.text() == '' or self.levaPerMinLineEdit.text() == '0':
            self.levaPerMinLineEdit.setFocus()
            self.levaPerMinLineEdit.selectAll()
            return
        levaPerMin = float(self.levaPerMinLineEdit.text())
        euroPerMin = float(self.euroPerMinLineEdit.text())
        dateActive = datetime.strptime(self.activedDateLineEdit.date().toString('dd.MM.yyyy'), "%d.%m.%Y")
        comment = self.commentLineEdit.text()
        returnedDict = {
            'levaPerMin': levaPerMin,
            'euroPerMin': euroPerMin,
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
        calDialog.calendarCustomWidget.setSelectedDate(self.activedDateLineEdit.date())
        Utils.calculatingIdealDialogShowPos(self, calDialog)
        calDialog.dateSelected.connect(self.updateDateLabel)
        calDialog.exec_()

    def updateDateLabel(self, date):
        self.activedDateLineEdit.setDate(date)

    def checkText(self, text):
        if ',' in text:
            text = text.split(',')[0]
            text = text + '.'
        self.sender().setText(text)

    def updateText(self):

        # if self.sender() == self.euroPerLevaLineEdit:
        #     self.levaForEuro = float(self.euroPerLevaLineEdit.text())
        #     if self.levaPerMinLineEdit.text() == "":
        #         self.levaPerMinLineEdit.setText("0")
        #     levaPerMin = float(self.levaPerMinLineEdit.text())
        #     self.euroPerMinLineEdit.setText(str(round(levaPerMin / self.levaForEuro, 5)))
        print('here')
        text = float(self.sender().text())
        self.sender().setText(str(text))

        if self.sender() == self.levaPerMinLineEdit:
            self.euroPerMinLineEdit.setText(str(round(text / self.levaForEuro, 5)))
            self.euroPerMinLineEdit.setFocus()
        elif self.sender() == self.euroPerMinLineEdit:
            self.levaPerMinLineEdit.setText(str(round(text * self.levaForEuro, 5)))
            self.euroPerLevaLineEdit.setFocus()
        elif self.sender() == self.euroPerLevaLineEdit:
            self.levaForEuro = float(self.euroPerLevaLineEdit.text())
            if self.levaPerMinLineEdit.text() == "":
                self.levaPerMinLineEdit.setText("0")
            levaPerMin = float(self.levaPerMinLineEdit.text())
            self.euroPerMinLineEdit.setText(str(round(levaPerMin / self.levaForEuro, 5)))

