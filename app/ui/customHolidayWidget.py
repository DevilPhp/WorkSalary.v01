from functools import partial

from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMenu, QDialog
from PySide6.QtCore import Qt, QDate
from datetime import datetime

from app.ui.customYesNoMessage import CustomYesNowDialog
from app.ui.widgets.ui_customHolidaysWidget import *
from app.services.paymentsServices import PaymentServices as Ps
from app.ui.customCalendarWidget import CustomCalendarDialog
from app.utils.utils import Utils
from app.ui.messagesManager import MessageManager as MM
from app.models.sortingModel import CaseInsensitiveProxyModel

class CustomHolidaysWidget(QWidget, Ui_customHolidaysWidget):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle("Празнични Дни")

        self.yearsBtns = Ps.getHolidaysYears()
        # print(self.yearsBtns)
        self.newHolidayDate.setDate(QDate.currentDate())
        self.yearsHolder.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.yearsHolder.customContextMenuRequested.connect(self.yearsHolderContextMenuRequested)

        self.holodaysTableModel = QStandardItemModel()
        self.holidaysHeaderNames = [
            'Номер', 'Име', 'Дата'
        ]
        for i, tableHeaderName in enumerate(self.holidaysHeaderNames):
            self.holodaysTableModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.holodaysTableModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.holodaysTableModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelHolidays = CaseInsensitiveProxyModel(numericColumns=[0], parent=self)
        self.proxyModelHolidays.setSourceModel(self.holodaysTableModel)
        self.holidaysTableView.setModel(self.proxyModelHolidays)
        self.holidaysTableView.setSortingEnabled(True)
        # self.timePapersForDayTableView.setModel(self.tableTimePapersModel)
        self.holidaysTableView.horizontalHeader().setStretchLastSection(True)
        self.holidaysTableView.horizontalHeader().setMinimumWidth(80)

        self.holidaysTableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.holidaysTableView.customContextMenuRequested.connect(self.holidaysTableViewContextMenuRequested)

        self.currentSelectedYear = None
        self.setYearsBtns()

        # self.refreshHolidaysTableView()

        self.newHolidayCalBtn.clicked.connect(self.showCalendar)
        self.addNewHolidayBtn.clicked.connect(self.addNewHoliday)

        # Add your code here to initialize the custom holidays widget

    def addNewHoliday(self):
        holidayName = self.holidayNameLineEdit.text()
        stringDate = self.newHolidayDate.date().toString("dd.MM.yyyy")
        holidayDate = datetime.strptime(stringDate, "%d.%m.%Y")
        user = self.usernameLabel.text()

        if holidayName and holidayDate:
            if self.currentSelectedYear:
                # print(f'Adding new holiday: {holidayName} - {holidayDate.toString("dd.MM.yyyy")}')
                Ps.addHoliday(holidayName, holidayDate, user, self.currentSelectedYear)
                self.holidayNameLineEdit.clear()
                self.newHolidayDate.setDate(QDate.currentDate())
                self.refreshHolidaysTableView()
                MM.showOnWidget(self, f"{holidayName} -дата: {stringDate} добавен успешно!", 'success')
            else:
                MM.showOnWidget(self, "Моля изберете година!", 'error')
        else:
            MM.showOnWidget(self, "Моля въведете име и дата за нов празник!", 'error')

    def refreshHolidaysTableView(self):
        self.holodaysTableModel.setRowCount(0)
        holidays = Ps.getHolidaysForYear(self.currentSelectedYear)
        for i, holiday in enumerate(holidays):
            holidayId = QStandardItem(str(i + 1))
            print(holiday['id'])
            holidayId.setData(holiday['id'], Qt.ItemDataRole.UserRole)
            row = [
                holidayId,
                QStandardItem(holiday['name']),
                QStandardItem(holiday['date'].strftime("%d.%m.%Y"))
            ]
            self.holodaysTableModel.appendRow(row)

    def setYearsBtns(self):
        for year in self.yearsBtns:
            btn = QPushButton(str(year), self)
            btn.clicked.connect(partial(self.yearBtnClicked, year, btn))
            self.yearsBtnsHolder.layout().addWidget(btn)
            if btn.text() == QDate.currentDate().toString("yyyy"):
                btn.click()

    def refreshYearsBtns(self):
        self.deleteYearsBtns()
        self.yearsBtns = Ps.getHolidaysYears()
        self.setYearsBtns()

    def yearBtnClicked(self, year, btn):
        if self.currentSelectedYear == year:
            return
        self.refreshStyleSheets()
        self.currentSelectedYear = year
        # print(f'Year {year} clicked')
        btn.setStyleSheet("background-color: #92b1a8;")
        self.refreshHolidaysTableView()

    def refreshStyleSheets(self):
        for btn in self.yearsBtnsHolder.findChildren(QPushButton):
            btn.setStyleSheet("")
            self.currentSelectedYear = None

    def deleteYearsBtns(self):
        for btn in self.yearsBtnsHolder.findChildren(QPushButton):
            btn.deleteLater()

    def yearsHolderContextMenuRequested(self, position):
        menu = QMenu(self)
        addAction = menu.addAction('Добавяне')
        editAction = menu.addAction('Редактиране')
        action = menu.exec_(self.yearsHolder.mapToGlobal(position))

        if action == addAction:
            self.addYear()
        if action == editAction:
            print('Edit action triggered')

    def holidaysTableViewContextMenuRequested(self, position):
        menu = QMenu(self)
        deleteAction = menu.addAction('Изтриване')
        action = menu.exec_(self.holidaysTableView.mapToGlobal(position))

        if action == deleteAction:
            selectedRowId = self.holidaysTableView.selectionModel().selectedRows(0)[0].data(Qt.ItemDataRole.UserRole)
            selectedName = self.holidaysTableView.selectionModel().selectedRows(1)[0].data(Qt.ItemDataRole.DisplayRole)
            selectedDate = self.holidaysTableView.selectionModel().selectedRows(2)[0].data(Qt.ItemDataRole.DisplayRole)
            # selectedHoliday = self.proxyModelHolidays.data(self.proxyModelHolidays.index(selectedRow, 0))
            # print(selectedRow)
            # print(f'Deleting holiday: {selectedHoliday}')
            # return
            dialog = CustomYesNowDialog()
            message = f'Изтриване на: {selectedName} - {selectedDate}'
            dialog.setMessage(name='', message=message, mode='deleting')
            result = dialog.exec()
            if result == QDialog.Accepted:
                if Ps.deleteHoliday(selectedRowId, self.currentSelectedYear, self.usernameLabel.text()):
                    MM.showOnWidget(self, f'Успешно изтрит празник {selectedName} - {selectedDate}',
                                    'success')
                    self.refreshHolidaysTableView()
                else:
                    MM.showOnWidget(self, 'Грешка при изтриване', 'error')

    def addYear(self):
        newYear = self.yearsBtns[-1] + 1 if len(self.yearsBtns) > 0 else datetime.now().year
        # print(f'Adding year {lastYear}')
        # return
        # newYear = lastYear + 1
        # self.yearsBtns.append(newYear)
        Ps.addHolidaysYear(newYear, self.usernameLabel.text())
        self.refreshYearsBtns()
        # newBtn = QPushButton(str(newYear), self)
        # self.yearsBtnsHolder.layout().addWidget(newBtn)

    def showCalendar(self):
        calendarDialog = CustomCalendarDialog()
        calendarDialog.calendarCustomWidget.setSelectedDate(datetime.now())
        Utils.calculatingIdealDialogShowPos(self, calendarDialog)
        calendarDialog.dateSelected.connect(self.updateDateLabel)
        calendarDialog.exec_()

    def updateDateLabel(self, date):
        self.newHolidayDate.setDate(date)
        # strDate = date.toString('dd.MM.yyyy')
        # print(f'Selected date: {strDate}')
