from app.ui.widgets.ui_customWorkerDialog import *
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from app.ui.customCalendarWidget import CustomCalendarDialog
from app.services.workerServices import WorkerServices as WoS


class CustomWorkerDialog(QDialog, Ui_CustomWorkerDialog):
    def __init__(self, workerId=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint |
                            Qt.WindowType.WindowStaysOnTopHint |
                            Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.workerId = workerId
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
        # self.yesBtn.clicked.connect(self.accept)

        if workerId:
            self.loadWorkerData()

        self.setChanges()

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
