from PySide6.QtGui import QStandardItemModel, QStandardItem, QDoubleValidator

from app.ui.widgets.ui_customShiftsEditWidget import *
from app.services.workerServices import WorkerServices as WoS
from app.utils.utils import Utils
from app.models.sortingModel import CaseInsensitiveProxyModel
from app.ui.messagesManager import MessageManager as MM
from datetime import datetime


class CustomShiftsEditWidget(QWidget, Ui_customWorkingShiftsWidget):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.workingShifts = None
        self.workingShiftsNames = {}
        validatorInt = QDoubleValidator(0, 999999, 0)
        self.shiftBreakLineEdit.setValidator(validatorInt)

        self.workingShiftsModel = QStandardItemModel()
        self.workingShiftsHeaderNames = ['ID', 'Име', 'Начало', 'Край', 'Почивка', 'Ефективност', 'Дата модификации']
        for i, tableHeaderName in enumerate(self.workingShiftsHeaderNames):
            self.workingShiftsModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.workingShiftsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.workingShiftsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelShifts = CaseInsensitiveProxyModel(numericColumns=[0, 4, 5], parent=self)
        self.proxyModelShifts.setSourceModel(self.workingShiftsModel)
        self.workingShiftsTableView.setModel(self.proxyModelShifts)
        self.workingShiftsTableView.setSortingEnabled(True)
        # self.timePapersForDayTableView.setModel(self.tableTimePapersModel)
        self.workingShiftsTableView.horizontalHeader().setStretchLastSection(True)
        self.workingShiftsTableView.horizontalHeader().setMinimumWidth(80)

        self.refreshWorkingShiftsTable()

        self.workingShiftsTableView.selectionModel().selectionChanged.connect(self.selectionChanged)
        self.shiftStart.timeChanged.connect(self.updateShiftDuration)
        self.shiftEnd.timeChanged.connect(self.updateShiftDuration)
        self.shiftBreakLineEdit.textChanged.connect(self.updateShiftDuration)
        self.acceptWorkingShiftsBtn.clicked.connect(self.acceptWorkingShifts)

        self.workingShiftsNameLineEdit.setFocus()

    def acceptWorkingShifts(self):
        shiftName = self.workingShiftsNameLineEdit.text()
        if shiftName != '':
            if self.workingShiftsTableView.currentIndex().isValid():
                selectedShiftId = self.workingShiftsTableView.selectedIndexes()[0].data()
                startShiftTime = datetime.strptime(self.shiftStart.time().toString('hh:mm'), '%H:%M').time()
                endShiftTime = datetime.strptime(self.shiftEnd.time().toString('hh:mm'), '%H:%M').time()
                updatedShift = [
                    shiftName,
                    startShiftTime,
                    endShiftTime,
                    int(self.shiftBreakLineEdit.text()) if self.shiftBreakLineEdit.text() else 60,
                    float(self.shiftTotalMins.text())
                ]
                success = WoS.updateWorkingShift(selectedShiftId, updatedShift)
                if success:
                    MM.showOnWidget(self, f'Успешна промяна на {shiftName}',
                                    'success')
                    self.refreshWorkingShiftsTable()
                    self.resetShiftInfo()
            else:
                if shiftName not in self.workingShiftsNames:
                    startShiftTime = datetime.strptime(self.shiftStart.time().toString('hh:mm'), '%H:%M').time()
                    endShiftTime = datetime.strptime(self.shiftEnd.time().toString('hh:mm'), '%H:%M').time()
                    newShift = [
                        shiftName,
                        startShiftTime,
                        endShiftTime,
                        int(self.shiftBreakLineEdit.text()) if self.shiftBreakLineEdit.text() else 60,
                        float(self.shiftTotalMins.text()),
                        self.usernameLabel.text()
                    ]
                    success = WoS.addWorkingShift(newShift)
                    if success:
                        MM.showOnWidget(self, f'Успешно добавена смяна {shiftName}', 'success')
                        self.refreshWorkingShiftsTable()
                        self.resetShiftInfo()
        else:
            MM.showOnWidget(self, f'Въведени е невалидно име за смяна \n{shiftName}', 'warning')

    def resetShiftInfo(self):
        self.workingShiftsNameLineEdit.clear()
        self.shiftStart.setTime(QTime(8, 0))
        self.shiftEnd.setTime(QTime(17, 0))
        self.shiftBreakLineEdit.clear()
        self.workingShiftsTableView.selectionModel().clearSelection()

    def updateShiftDuration(self):
        breakTime = int(self.shiftBreakLineEdit.text()) if self.shiftBreakLineEdit.text() != '' else 60
        duration = Utils.calculateMinutes(self.shiftStart, self.shiftEnd, breakTime)
        self.shiftTotalMins.setText(str(duration))

    def selectionChanged(self, selection):
        if selection:
            name = selection.indexes()[1].data()
            startTime = selection.indexes()[2].data()
            endTime = selection.indexes()[3].data()
            breakTime = selection.indexes()[4].data()
            self.workingShiftsNameLineEdit.setText(name)
            self.shiftStart.setTime(QTime.fromString(startTime, 'hh:mm'))
            self.shiftEnd.setTime(QTime.fromString(endTime, 'hh:mm'))
            self.shiftBreakLineEdit.setText(str(breakTime))
        else:
            self.resetShiftInfo()

    def refreshWorkingShiftsTable(self):
        self.workingShiftsModel.setRowCount(0)
        self.workingShiftsNames = {}
        self.workingShifts = WoS.getWorkingShiftsForEdit()
        for shift in self.workingShifts:
            row = [
                QStandardItem(str(shift.id)),
                QStandardItem(shift.ShiftName),
                QStandardItem(shift.StartTime.strftime('%H:%M')),
                QStandardItem(shift.EndTime.strftime('%H:%M')),
                QStandardItem(str(shift.BreakTime)),
                QStandardItem(str(shift.Efficiency)),
                QStandardItem(shift.DateUpdated.strftime('%d.%m.%Y'))
            ]
            self.workingShiftsNames[shift.ShiftName] = shift.id
            self.workingShiftsModel.appendRow(row)
