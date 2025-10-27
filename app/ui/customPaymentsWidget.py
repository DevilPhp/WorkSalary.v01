from functools import partial

from PySide6.QtGui import QStandardItemModel, QStandardItem

from app.ui.customSortingMenuWidget import CustomSortingMenuWidget
from app.ui.widgets.ui_customPaymentsWidget import *
from app.models.tableModel import CustomTableViewWithMultiSelection
from app.models.sortingModel import CaseInsensitiveProxyModel, FilterableHeaderView
from app.ui.customCalendarWidget import CustomCalendarDialog
from app.services.workerServices import WorkerServices as WoS
from app.utils.utils import Utils


class CustomPaymentsWidget(QWidget, Ui_customPaymentsWidget):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.paymentsTableView = CustomTableViewWithMultiSelection()
        self.paymentsTableHolder.layout().addWidget(self.paymentsTableView)
        self.tablePaymentsModel = QStandardItemModel()
        self.tablePaymentsNames = ['ID', '№', 'Име', 'Зар. дни', 'В поч. дни', 'В Празници', 'Бр.',
                                   'Вр. Опер. в ч.', 'Почас. в ч.', 'Извънр. в ч.', 'Нощен в ч.', 'Бр./час', 'Лв.', '€']
        # self.excelTableNames = ['ID', '№', 'Име', 'Зар. дни', 'В поч. дни', 'В Празници', 'Бр.',
        #                            'Вр. Опер. в ч.', 'Почас. в ч.', 'Извънр. в ч.', 'Нощен в ч.', 'Бр./час', 'Лв.', '€']
        for i, tableHeaderName in enumerate(self.tablePaymentsNames):
            self.tablePaymentsModel.setHorizontalHeaderItem(i, QStandardItem(tableHeaderName))
            self.tablePaymentsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignLeft)
            self.tablePaymentsModel.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.proxyModelPaymentsTable = CaseInsensitiveProxyModel(numericColumns=[0, 1, 3, 4, 5, 6, 11, 12, 13],
                                                                    parent=self)
        self.setProxyModel(self.proxyModelPaymentsTable, self.tablePaymentsModel, self.paymentsTableView)
        # self.timePapersForDayTableView.setModel(self.tablePaymentsModel)
        self.paymentsTableView.horizontalHeader().setDefaultSectionSize(80)
        self.paymentsTableView.horizontalHeader().setStretchLastSection(True)
        self.setColumnWidths()

        self.paymentsTableView.selectedRows.connect(self.showPaymentDetails)
        self.paymentsTableView.clearCurrentSelection.connect(self.resetSelectedInfo)

        self.fromDateEdit.setDate(QDate.currentDate().addDays(-7))
        self.toDateEdit.setDate(QDate.currentDate())

        self.checkBoxFiltering = {}
        self.initialCheckBoxes = {}

        self.weekendDaysCheckBox.stateChanged.connect(self.onWeekendStateChanged)
        self.holidaysCheckBox.stateChanged.connect(self.onHolidaysStateChanged)
        self.hourlyCheckBox.stateChanged.connect(self.onHourlyStateChanged)
        self.overtimeCheckBox.stateChanged.connect(self.onOvertimeStateChanged)
        self.nightTimeCheckBox.stateChanged.connect(self.onNightTimeStateChanged)
        self.selectAllCheckBox.stateChanged.connect(self.onSelectAllStateChanged)

        self.exportToExcelBtn.clicked.connect(self.exportToExcel)

        # self.setPayPerMinComboBox()
        
        self.refreshPaymentsTable()
        self.setInitialColumns()

        self.fromCalendarBtn.clicked.connect(self.showCalendarDialog)
        self.toCalendarBtn.clicked.connect(self.showCalendarDialog)

        self.fromDateEdit.dateChanged.connect(self.checkFromDate)
        self.toDateEdit.dateChanged.connect(self.checkToDate)

        self.searchBtn.clicked.connect(self.refreshPaymentsTable)
        self.paymentsTableView.doubleClicked.connect(self.openPaymentDetails)

    # def setPayPerMinComboBox(self):
    #     paymentsPerMin = WoS.getPaymentsForMin()
    #     self.payPerMinComboBox.clear()

    def exportToExcel(self):
        """Export the current table view data to Excel file"""
        import openpyxl
        from openpyxl.styles import Font, Alignment, PatternFill
        from openpyxl.utils import get_column_letter
        import os
        from datetime import datetime
        from PySide6.QtWidgets import QFileDialog

        # Get save file location from user
        fileName, _ = QFileDialog.getSaveFileName(
            self,
            "Save Excel File",
            os.path.join(os.path.expanduser("~"), "Documents",
                         f"Payments_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"),
            "Excel Files (*.xlsx)"
        )

        if not fileName:
            return  # User canceled

        # Create a new workbook and select the active sheet
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Payments Report"

        # Add report title and date range
        ws.merge_cells('A1:N1')
        title_cell = ws['A1']
        title_cell.value = f"Payments Report ({self.fromDateEdit.date().toString('dd.MM.yyyy')} - {self.toDateEdit.date().toString('dd.MM.yyyy')})"
        title_cell.font = Font(size=14, bold=True)
        title_cell.alignment = Alignment(horizontal='center')

        # Add headers
        header_fill = PatternFill(start_color="DFDFDF", end_color="DFDFDF", fill_type="solid")

        columnHeaders = self.tablePaymentsNames.copy()
        print(columnHeaders)
        print(self.tablePaymentsNames)
        if not self.holidaysCheckBox.isChecked():
            columnHeaders.remove('В Празници')

        if not self.weekendDaysCheckBox.isChecked():
            columnHeaders.remove('В поч. дни')

        if not self.overtimeCheckBox.isChecked():
            columnHeaders.remove('Извънр. в ч.')

        if not self.nightTimeCheckBox.isChecked():
            columnHeaders.remove('Нощен в ч.')

        if not self.hourlyCheckBox.isChecked():
            columnHeaders.remove('Почас. в ч.')

        for col_idx, header_text in enumerate(columnHeaders):
            col_letter = get_column_letter(col_idx + 1)
            cell = ws[f"{col_letter}3"]
            cell.value = header_text
            cell.font = Font(bold=True)
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal='center')

        # self.excelTableNames = self.tablePaymentsNames

        print(columnHeaders)
        print(self.tablePaymentsNames)

        # Add data rows
        row_idx = 4  # Start from row 4 (after headers)
        for row in range(self.proxyModelPaymentsTable.rowCount()):
            viewColumns = 0
            for col in range(self.proxyModelPaymentsTable.columnCount()):
                # Skip hidden columns
                if self.paymentsTableView.isColumnHidden(col):
                    continue

                # Get data from the proxy model
                index = self.proxyModelPaymentsTable.index(row, col)
                value = self.proxyModelPaymentsTable.data(index, Qt.ItemDataRole.DisplayRole)

                # Convert to appropriate type
                if col in [0, 1, 3, 4, 5, 6]:  # Integer columns
                    try:
                        value = int(value) if value else 0
                    except ValueError:
                        pass
                elif col in [11, 12, 13]:  # Float columns
                    try:
                        value = float(value) if value else 0.0
                    except ValueError:
                        pass

                # Write to cell
                ws.cell(row=row_idx, column=viewColumns + 1, value=value)
                viewColumns += 1
                # print(f"View column: {viewColumns}, Value: {value}")

            row_idx += 1

        # Auto-adjust column widths
        # for col in ws.columns:
        #     max_length = 0
        #     column = col[0].column_letter
        #     for cell in col:
        #         if cell.value:
        #             cell_length = len(str(cell.value))
        #             if cell_length > max_length:
        #                 max_length = cell_length
        #     adjusted_width = (max_length + 2)
        #     ws.column_dimensions[column].width = adjusted_width

        # Add summary at the bottom
        summary_row = row_idx + 1
        ws.cell(row=summary_row, column=1, value="Total:").font = Font(bold=True)
        ws.cell(row=summary_row, column=2, value=self.totalViewRows.text()).font = Font(bold=True)

        # Add SUM formulas for Leva (column 13) and Euro (column 14)
        leva_col = get_column_letter(len(columnHeaders) - 1)  # Column M in Excel (index 12 + 1)
        euro_col = get_column_letter(len(columnHeaders))  # Column N in Excel (index 13 + 1)

        # Create SUM formulas that reference the data range
        leva_formula = f"=SUM({leva_col}4:{leva_col}{row_idx})"
        euro_formula = f"=SUM({euro_col}4:{euro_col}{row_idx})"

        # Add the formulas to the summary row
        leva_cell = ws.cell(row=summary_row, column=len(columnHeaders) - 1, value=leva_formula)
        euro_cell = ws.cell(row=summary_row, column=len(columnHeaders), value=euro_formula)

        # Apply bold formatting to the summary cells
        leva_cell.font = Font(bold=True)
        euro_cell.font = Font(bold=True)

        # Save the workbook
        try:
            wb.save(fileName)
            from app.ui.messagesManager import MessageManager as MM
            MM.showOnWidget(self, f"Успешен запис на {fileName}", "success")
        except Exception as e:
            from app.ui.messagesManager import MessageManager as MM
            MM.showOnWidget(self, f"Грешка при записване: {str(e)}", "error")

    def setInitialColumns(self):
        self.paymentsTableView.setColumnHidden(4, True)
        self.paymentsTableView.setColumnHidden(5, True)
        self.paymentsTableView.setColumnHidden(8, True)
        self.paymentsTableView.setColumnHidden(9, True)
        self.paymentsTableView.setColumnHidden(10, True)

    def checkAllstate(self):
        if (self.hourlyCheckBox.isChecked() and
                self.overtimeCheckBox.isChecked() and
                self.nightTimeCheckBox.isChecked() and
                self.weekendDaysCheckBox.isChecked() and
                self.holidaysCheckBox.isChecked()):
            self.selectAllCheckBox.setChecked(True)
        else:
            self.selectAllCheckBox.blockSignals(True)
            self.selectAllCheckBox.setChecked(False)
            self.selectAllCheckBox.blockSignals(False)

    def onSelectAllStateChanged(self, state):
        self.hourlyCheckBox.setChecked(state)
        self.overtimeCheckBox.setChecked(state)
        self.nightTimeCheckBox.setChecked(state)
        self.weekendDaysCheckBox.setChecked(state)
        self.holidaysCheckBox.setChecked(state)

    def onHourlyStateChanged(self, state):
        self.paymentsTableView.setColumnHidden(8, not state)
        self.checkAllstate()

    def onOvertimeStateChanged(self, state):
        self.paymentsTableView.setColumnHidden(9, not state)
        self.checkAllstate()

    def onNightTimeStateChanged(self, state):
        self.paymentsTableView.setColumnHidden(10, not state)
        self.checkAllstate()

    def onWeekendStateChanged(self, state):
        self.paymentsTableView.setColumnHidden(4, not state)
        self.checkAllstate()

    def onHolidaysStateChanged(self, state):
        self.paymentsTableView.setColumnHidden(5, not state)
        self.checkAllstate()

    def showCalendarDialog(self):
        calendarDialog = CustomCalendarDialog()
        Utils.calculatingIdealDialogShowPos(self, calendarDialog)
        if self.sender() == self.fromCalendarBtn:
            calendarDialog.calendarCustomWidget.setSelectedDate(self.fromDateEdit.date())
            calendarDialog.dateSelected.connect(self.updateFromDateLabel)
        elif self.sender() == self.toCalendarBtn:
            calendarDialog.calendarCustomWidget.setSelectedDate(self.fromDateEdit.date())
            calendarDialog.dateSelected.connect(self.updateToDateLabel)

        calendarDialog.exec_()

    def updateFromDateLabel(self, selectedDate):
        self.fromDateEdit.setDate(selectedDate)

    def updateToDateLabel(self, selectedDate):
        self.toDateEdit.setDate(selectedDate)

    def checkFromDate(self):
        if self.fromDateEdit.date() > self.toDateEdit.date():
            self.toDateEdit.setDate(self.fromDateEdit.date())

    def checkToDate(self):
        if self.toDateEdit.date() < self.fromDateEdit.date():
            self.fromDateEdit.setDate(self.toDateEdit.date())

    def showPaymentDetails(self, selectedRows):
        numberSelectedRows = len(selectedRows['payInEuro'])
        totalPayInLeva = 0
        totalPayInEuro = 0
        # avrLeva = 0
        # avrEuro = 0

        for key, row in selectedRows.items():
            if key == 'payInEuro':
                for item in row:
                    totalPayInEuro += float(item.data())
            else:
                for item in row:
                    totalPayInLeva += float(item.data())

        avrLeva = round(totalPayInLeva / len(selectedRows['payInLeva']), 2)
        avrEuro = round(totalPayInEuro / len(selectedRows['payInEuro']), 2)

        self.totalSelectedRows.setText(str(numberSelectedRows))
        self.totalLevaLabel.setText(str(round(totalPayInLeva, 2)))
        self.totalEuroLabel.setText(str(round(totalPayInEuro, 2)))
        self.avrLevaLabel.setText(str(avrLeva))
        self.avrEuroLabel.setText(str(avrEuro))

    def resetSelectedInfo(self):
        self.totalSelectedRows.setText("0")
        self.totalLevaLabel.setText("0.0")
        self.totalEuroLabel.setText("0.0")
        self.avrLevaLabel.setText("0.0")
        self.avrEuroLabel.setText("0.0")

    def setColumnWidths(self):
        self.paymentsTableView.setColumnWidth(0, 20)
        self.paymentsTableView.setColumnWidth(1, 40)
        self.paymentsTableView.setColumnWidth(2, 180)
        self.paymentsTableView.setColumnWidth(4, 100)
        self.paymentsTableView.setColumnWidth(5, 100)
        self.paymentsTableView.setColumnWidth(6, 40)
        self.paymentsTableView.setColumnWidth(7, 100)
        self.paymentsTableView.setColumnWidth(8, 100)
        self.paymentsTableView.setColumnWidth(9, 100)
        self.paymentsTableView.setColumnWidth(10, 100)

    def refreshPaymentsTable(self):
        self.tablePaymentsModel.setRowCount(0)
        count = 0
        # workerNumber = self.workerNameLineEdit.text()
        startDate = Utils.convertQDateToDate(self.fromDateEdit.date())
        endDate = Utils.convertQDateToDate(self.toDateEdit.date())
        paymentsData = WoS.getInfoForPayments(startDate, endDate)
        # for pay in paymentsData:
        #     print(pay, paymentsData[pay])
        #     return
        paymentForMin = WoS.getPaymentForMin()
        paymentForNightMin = WoS.getPaymentForNightMin()
        paymentInLeva = paymentForMin.PaymentValue
        paymentInEuro = paymentForMin.PaymentInEuro
        nightPayInLeva = paymentForNightMin.NightPaymentValue + paymentInLeva
        nightPayInEuro = paymentForNightMin.NightPaymentInEuro + paymentInEuro

        for workerPayment in paymentsData:
            count += 1
            workerId = workerPayment.split(' : ')[0]
            workerName = workerPayment.split(' : ')[1]
            workingDays = len(paymentsData[workerPayment])
            totalWeekEndWorkingDays = 0
            totalHolidaysWorking = 0
            totalPayInLev = 0
            totalPayInEuro = 0

            for timePaperPayment in paymentsData[workerPayment]:
                totalHourlyMins = 0
                totalOvertimeMins = 0
                totalPieces = 0
                totalTime = 0
                totalNightMins = 0
                currentPayment = 0
                currentPaymentInEuro = 0
                hourly = paymentsData[workerPayment][timePaperPayment]['hourly']
                overtime = paymentsData[workerPayment][timePaperPayment]['overtime']
                nightMins = paymentsData[workerPayment][timePaperPayment]['nightMins']
                pieces = paymentsData[workerPayment][timePaperPayment]['totalPieces']
                workingTime = paymentsData[workerPayment][timePaperPayment]['totalTime']
                paymentRatio = paymentsData[workerPayment][timePaperPayment]['paymentRatio']

                if paymentsData[workerPayment][timePaperPayment]['paymentRatio'] >= 1.75:
                    totalWeekEndWorkingDays += 1

                if paymentsData[workerPayment][timePaperPayment]['paymentRatio'] >= 2:
                    totalHolidaysWorking += 1

                if hourly:
                    for hourlyPayment in hourly:
                        hourlyEfficient = hourly[hourlyPayment][0]
                        hourlyRatio = hourly[hourlyPayment][1]
                        hourlyNightMins = hourly[hourlyPayment][2]
                        totalHourlyMins += hourlyEfficient
                        totalNightMins += hourlyNightMins
                        currentPayment += Utils.calculatePayment(hourlyEfficient - hourlyNightMins,
                                                                hourlyRatio, paymentRatio, paymentInLeva)
                        currentPaymentInEuro += Utils.calculatePayment(hourlyEfficient - hourlyNightMins,
                                                                      hourlyRatio, paymentRatio, paymentInEuro)
                        # print(workerId, currentPayment)

                        if hourlyNightMins > 0:
                            currentPayment += Utils.calculatePayment(hourlyNightMins, hourlyRatio,
                                                                    paymentRatio, nightPayInLeva)
                            currentPaymentInEuro += Utils.calculatePayment(hourlyNightMins, hourlyRatio,
                                                                          paymentRatio, nightPayInEuro)
                        # print(workerId, currentPayment)

                if overtime:
                    for overtimePayment in overtime:
                        overtimeEfficient = overtime[overtimePayment][0]
                        overtimeRatio = overtime[overtimePayment][1]
                        overtimeNightMins = overtime[overtimePayment][2]

                        currentPayment += Utils.calculatePayment((overtimeEfficient - overtimeNightMins), overtimeRatio,
                                                                paymentRatio, paymentInLeva)
                        currentPaymentInEuro += Utils.calculatePayment((overtimeEfficient - overtimeNightMins),
                                                                      overtimeRatio, paymentRatio, paymentInEuro)
                        # print(workerId, currentPayment)

                        if overtimeNightMins > 0:
                            currentPayment += Utils.calculatePayment(overtimeNightMins, overtimeRatio,
                                                                paymentRatio, nightPayInLeva)
                            currentPaymentInEuro += Utils.calculatePayment(overtimeNightMins, overtimeRatio,
                                                                          paymentRatio, nightPayInEuro)
                        # print(workerId, currentPayment)
                        totalOvertimeMins += overtimeEfficient
                        totalNightMins += overtimeNightMins

                if nightMins > 0:

                    currentPayment += Utils.calculatePayment(nightMins, 1, paymentRatio, nightPayInLeva)
                    currentPaymentInEuro += Utils.calculatePayment(nightMins, 1, paymentRatio, nightPayInEuro)
                    # print(workerId, currentPayment)

                currentPayment += Utils.calculatePayment(workingTime - nightMins, 1, paymentRatio, paymentInLeva)
                currentPaymentInEuro += Utils.calculatePayment(workingTime - nightMins, 1, paymentRatio, paymentInEuro)
                # print(workerId, currentPayment)

                totalPieces += pieces
                totalTime = round(totalTime + workingTime, 2)
                totalNightMins = round(totalNightMins + nightMins, 2)

                totalPayInLev += currentPayment
                totalPayInEuro += currentPaymentInEuro
            displayOperTime = '0'
            displayHourlyTime = '0'
            displayOverTime = '0'
            displayNightTime = '0'
            efficiency = 0
            totalTime = round(totalTime, 2)
            totalNightMins = round(totalNightMins, 2)
            if totalPieces != 0 or totalTime != 0:
                efficiency = round((totalTime / totalPieces), 2)
                displayOperTime = Utils.makeDispalyMins(totalTime)

            if totalOvertimeMins > 0:
                displayOverTime = Utils.makeDispalyMins(totalOvertimeMins)

            if totalHourlyMins > 0:
                displayHourlyTime = Utils.makeDispalyMins(totalHourlyMins)

            if totalNightMins > 0:
                displayNightTime = Utils.makeDispalyMins(totalNightMins)

            payInLeva = round(totalPayInLev, 2)
            payInEuro = round(totalPayInEuro, 2)
            # totalHours = QStandardItem(str(totalWeekEndWorkingDays))
            # totalHours.setBackground(QColor(208, 170, 167))

            row = [
                QStandardItem(str(count)),
                QStandardItem(str(workerId)),
                QStandardItem(workerName),
                QStandardItem(str(workingDays)),
                QStandardItem(str(totalWeekEndWorkingDays)),
                QStandardItem(str(totalHolidaysWorking)),
                QStandardItem(str(totalPieces)),
                QStandardItem(displayOperTime),
                QStandardItem(displayHourlyTime),
                QStandardItem(displayOverTime),
                QStandardItem(displayNightTime),
                QStandardItem(str(efficiency)),
                QStandardItem(str(payInLeva)),
                QStandardItem(str(payInEuro))
            ]
            self.tablePaymentsModel.appendRow(row)
        self.totalViewRows.setText(str(count))

    def closeEvent(self, event):
        self.mainWindow.closeAllPaymentsDetails()

    def openPaymentDetails(self, index):
        workerId = self.proxyModelPaymentsTable.mapToSource(index).siblingAtColumn(1).data(Qt.ItemDataRole.DisplayRole)
        totalLeva = self.proxyModelPaymentsTable.mapToSource(index).siblingAtColumn(12).data(Qt.ItemDataRole.DisplayRole)
        totalEuro = self.proxyModelPaymentsTable.mapToSource(index).siblingAtColumn(13).data(Qt.ItemDataRole.DisplayRole)
        startDate = self.fromDateEdit.date()
        endDate = self.toDateEdit.date()
        self.mainWindow.setPaymentsDetailsPage(workerId, startDate, endDate, totalLeva, totalEuro)

    def setProxyModel(self, proxyModel, model, table):
        proxyModel.setSourceModel(model)
        filterableHeaderView = FilterableHeaderView(Qt.Orientation.Horizontal, table)
        table.setHorizontalHeader(filterableHeaderView)
        filterableHeaderView.filterRequested.connect(partial(self.updateFilter, proxyModel, filterableHeaderView))
        table.setModel(proxyModel)
        table.setSortingEnabled(True)

    def updateFilter(self, proxyModel, header, column):
        if column < 3:
            # Create dictionaries to store column values and checked states if they don't exist
            if not hasattr(self, 'columnValues'):
                self.columnValues = {}
            if not hasattr(self, 'checkedStates'):
                self.checkedStates = {}
            if column not in self.checkBoxFiltering:
                self.checkBoxFiltering[column] = []

            items = []
            self.columnValues[column] = []

            for row in range(proxyModel.rowCount()):
                index = proxyModel.index(row, column)
                value = proxyModel.data(index, Qt.ItemDataRole.DisplayRole)
                if value not in self.columnValues[column]:
                    self.columnValues[column].append(value)
                    if value not in self.initialCheckBoxes:
                        self.initialCheckBoxes[value] = column

            for value in self.columnValues[column]:
                items.append(value)

            if items:
                menu = CustomSortingMenuWidget(header)
                for item in items:
                    checked = item in self.checkBoxFiltering[column]
                    menu.addItem(item, checked)
                menu.setMenuSize(len(items))
                menu.move(self.cursor().pos())
                menu.checkedCheckbox.connect(partial(self.applyFilter, proxyModel))

    def applyFilter(self, proxyModel, item):
        col = self.initialCheckBoxes[item.text()]
        if item.isChecked() and item.text() not in self.checkBoxFiltering[col]:
            self.checkBoxFiltering[col].append(item.text())
        elif not item.isChecked() and item.text() in self.checkBoxFiltering[col]:
            self.checkBoxFiltering[col].remove(item.text())

        if not self.checkBoxFiltering[col]:
            if col in proxyModel.columnFilters:
                del proxyModel.columnFilters[col]
        else:
            proxyModel.setFilterForColumn(col, self.checkBoxFiltering)
        proxyModel.invalidateFilter()
        self.totalViewRows.setText(str(proxyModel.rowCount()))
    
    