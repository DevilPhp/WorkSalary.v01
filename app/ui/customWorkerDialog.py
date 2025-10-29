from datetime import datetime

from PySide6.QtCore import Signal
from PySide6.QtGui import QIntValidator

from app.ui.widgets.ui_customWorkerDialog import *
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QCompleter
from app.ui.customCalendarWidget import CustomCalendarDialog
from app.services.workerServices import WorkerServices as WoS
from app.utils.utils import Utils


class CustomWorkerDialog(QDialog, Ui_CustomWorkerDialog):
    workerInfo = Signal(dict)

    def __init__(self, workerId=None, existingWorkers=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint |
                            Qt.WindowType.WindowStaysOnTopHint |
                            Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.workerId = workerId if workerId else None
        self.existingWorkers = existingWorkers if existingWorkers else None

        self.isDialogChanged = False
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setXOffset(2)
        shadow.setYOffset(2)
        shadow.setColor(QColor("#7f7f7f"))
        self.setGraphicsEffect(shadow)
        self.startDateEdit.setDate(QDate.currentDate())
        self.leaveDateEdit.setDate(QDate.currentDate())
        self.leaveDateEdit.setEnabled(False)
        self.calLeavingBtn.setEnabled(False)

        validator = QIntValidator(1, 99999)
        self.workerNumber.setValidator(validator)

        self.setComboBoxes()

        self.inputsList = [
            self.workerName,
            self.workerSirname,
            self.workerLastname,
            self.workerNumber,
            self.cehoveComboBox,
            self.positionComboBox,
            self.workerEGN,
            self.paymentTypeComboBox,
            self.workerTel,
            self.workerTownAdress,
            self.workerStreetAdress
        ]
        self.setTabOrderForInputs()
        self.calStartBtn.clicked.connect(lambda: self.showCustomCalendar(self.startDateEdit))
        self.calLeavingBtn.clicked.connect(lambda: self.showCustomCalendar(self.leaveDateEdit))
        self.startCheckBox.stateChanged.connect(self.toggleStartDate)
        self.leavingCheckBox.stateChanged.connect(self.toggleLeaveDate)
        self.workerNumber.editingFinished.connect(self.checkWorkerNumber)
        self.workerName.returnPressed.connect(self.setFocusForWorkerName)
        self.workerSirname.returnPressed.connect(self.setFocusForWorkerSirname)
        self.workerLastname.returnPressed.connect(self.setFocusForWorkerLastname)
        self.workerEGN.returnPressed.connect(self.setFocusForWorkerEGN)
        self.workerEGN.textChanged.connect(self.checkWorkerEGN)
        self.workerTel.returnPressed.connect(self.setFocusForWorkerTel)
        self.workerTel.textChanged.connect(self.checkWorkerTel)
        self.workerTownAdress.returnPressed.connect(self.setFocusForWorkerTownAdress)
        self.workerStreetAdress.returnPressed.connect(self.setFocusForWorkerStreetAdress)
        # self.workerNumber.textChanged.connect(self.checkWorkerNumber)
        # self.yesBtn.clicked.connect(self.accept)

        if workerId:
            self.loadWorkerData()

        self.setChanges()

        self.yesBtn.clicked.connect(self.emitWorkerInfo)
        Utils.setupCompleter(self.existingWorkers, self.workerNumber)

        self.workerName.setFocus()

    def checkWorkerEGN(self, text):
        currentText = text
        if not currentText.isdigit():
            currentText = currentText[:-1]
            self.workerEGN.setText(currentText)

        if len(currentText) == 11:
            self.workerEGN.setText(currentText[:10])

    def checkWorkerTel(self, text):
        currentText = text
        if len(currentText) == 1 and currentText == '+':
            self.workerTel.setText('00')
        elif not currentText.isdigit():
            currentText = currentText[:-1]
            self.workerTel.setText(currentText)

    def setFocusForWorkerName(self):
        self.workerSirname.selectAll()
        self.workerSirname.setFocus()

    def setFocusForWorkerSirname(self):
        self.workerLastname.selectAll()
        self.workerLastname.setFocus()

    def setFocusForWorkerLastname(self):
        self.workerNumber.selectAll()
        self.workerNumber.setFocus()

    def setFocusForWorkerEGN(self):
        self.workerTel.selectAll()
        self.workerTel.setFocus()

    def setFocusForWorkerTel(self):
        self.workerTownAdress.selectAll()
        self.workerTownAdress.setFocus()

    def setFocusForWorkerTownAdress(self):
        self.workerStreetAdress.selectAll()
        self.workerStreetAdress.setFocus()

    def setFocusForWorkerStreetAdress(self):
        self.workerName.selectAll()
        self.workerName.setFocus()

    def checkWorkerNumber(self):
        if self.existingWorkers:
            if self.workerNumber.text() in self.existingWorkers:
                self.workerNumber.setText('')
                self.workerNumber.setFocus()
            else:
                self.workerEGN.selectAll()
                self.workerEGN.setFocus()

    def emitWorkerInfo(self):
        workerData = {}
        isNewWorker = False
        if self.isDialogChanged:

            if self.workerName.text() == '':
                self.workerName.setFocus()
                return
            elif self.workerNumber.text() == '':
                self.workerNumber.setFocus()
                return

            if not self.workerId and self.workerNumber.text() != '':
                self.workerId = int(self.workerNumber.text())
                isNewWorker = True
            # elif not self.workerId and self.workerNumber.text() == '':
            #     self.workerId = None
            #     isNewWorker = True

            startDate = datetime.strptime(self.startDateEdit.date().toString('yyyy-MM-dd'), '%Y-%m-%d') \
                if self.startDateEdit.date().isValid() and self.startCheckBox.isChecked() else None
            endDate = datetime.strptime(self.leaveDateEdit.date().toString('yyyy-MM-dd'), '%Y-%m-%d') \
                if self.leaveDateEdit.date().isValid() and self.leavingCheckBox.isChecked() else None

            workerData = {
                'isNew': isNewWorker,
                'id': self.workerId,
                'firstName': self.workerName.text(),
                'middleName': self.workerSirname.text() if self.workerSirname.text() != '' else None,
                'lastName': self.workerLastname.text() if self.workerLastname.text() != '' else None,
                'cehId': self.cehoveComboBox.currentIndex() + 1 if self.cehoveComboBox.currentIndex() >= 0 else None,
                'positionId': self.positionComboBox.currentIndex() + 1
                if self.positionComboBox.currentIndex() >= 0 else None,
                'EGN': self.workerEGN.text() if self.workerEGN.text() != '' else None,
                'paymentTypeId': self.paymentTypeComboBox.currentIndex(),
                'workerPhone': self.workerTel.text() if self.workerTel.text() != '' else None,
                'startDate': startDate,
                'endDate': endDate,
                'town': self.workerTownAdress.text() if self.workerTownAdress.text() != '' else None,
                'address': self.workerStreetAdress.text() if self.workerStreetAdress.text() != '' else None,
            }

            # self.workerInfo.emit(workerData)
        else:
            self.close()
        self.workerInfo.emit(workerData)

    def setChanges(self):
        for input in self.inputsList:
            if isinstance(input, QLineEdit):
                input.textChanged.connect(self.markAsChanged)
            if isinstance(input, QComboBox):
                input.currentIndexChanged.connect(self.markAsChanged)
        self.startDateEdit.dateChanged.connect(self.markAsChanged)
        self.leaveDateEdit.dateChanged.connect(self.markAsChanged)

    def markAsChanged(self):
        self.isDialogChanged = True

    def setComboBoxes(self):
        self.cehoveComboBox.addItems(WoS.getCehove())
        self.positionComboBox.addItems(WoS.getPositions())
        self.paymentTypeComboBox.addItems(WoS.getPaymentTypes())

    def loadWorkerData(self):
        worker = WoS.getWorkerInfo(self.workerId)
        self.workerName.setText(worker.Име if worker.Име else "")
        self.workerSirname.setText(worker.Презиме if worker.Презиме else "")
        self.workerLastname.setText(worker.Фамилия if worker.Фамилия else "")
        self.workerNumber.setText(str(worker.Номер))
        self.cehoveComboBox.setCurrentIndex(worker.Група - 1 if worker.Група else -1)
        self.positionComboBox.setCurrentIndex(worker.Длъжност - 1 if worker.Длъжност else -1)
        self.workerEGN.setText(worker.ЕГН)
        self.startDateEdit.setDate(QDate.fromString(worker.ДатаНаПостъпване.strftime("%d.%m.%Y"), "dd.MM.yyyy")
                                   if worker.ДатаНаПостъпване else QDate.currentDate())
        self.leaveDateEdit.setDate(QDate.fromString(worker.ДатаНаНапускане.strftime("%d.%m.%Y"), "dd.MM.yyyy")
                                   if worker.ДатаНаНапускане else QDate.currentDate())

        self.paymentTypeComboBox.setCurrentIndex(worker.СистемаЗаплащане if worker.СистемаЗаплащане else 0)
        self.workerTel.setText(worker.Телефон if worker.Телефон else "")
        self.workerTownAdress.setText(worker.гр_с if worker.гр_с else "")
        self.workerStreetAdress.setText(worker.Адрес if worker.Адрес else "")

        if not worker.ДатаНаПостъпване:
            self.startCheckBox.setCheckState(Qt.CheckState.Unchecked)
        else:
            self.startCheckBox.setCheckState(Qt.CheckState.Checked)

        if not worker.ДатаНаНапускане:
            self.leavingCheckBox.setCheckState(Qt.CheckState.Unchecked)
        else:
            self.leavingCheckBox.setCheckState(Qt.CheckState.Checked)

        self.workerName.setFocus()
        self.workerName.selectAll()
        if self.workerId:
            self.workerNumber.setReadOnly(True)

    def toggleStartDate(self, state):
        self.startDateEdit.setEnabled(state)
        self.calStartBtn.setEnabled(state)

    def toggleLeaveDate(self, state):
        self.leaveDateEdit.setEnabled(state)
        self.calLeavingBtn.setEnabled(state)

    def showCustomCalendar(self, widget):
        customCalendar = CustomCalendarDialog()
        customCalendar.dateSelected.connect(lambda date: widget.setDate(date))
        customCalendar.exec_()

    def setTabOrderForInputs(self):
        for i in range(len(self.inputsList) - 1):
            self.setTabOrder(self.inputsList[i], self.inputsList[i + 1])
