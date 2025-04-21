from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGraphicsDropShadowEffect

from app.ui.widgets.ui_customCalendarDialog import *


class CustomCalendarDialog(QDialog, Ui_CustomCalendarDialog):
    dateSelected = Signal(QDate)

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

        self.calendarCustomWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.todayBtn.clicked.connect(self.onTodayBtnClicked)

        self.calendarCustomWidget.activated.connect(self.onDateDoubleClicked)

    def onTodayBtnClicked(self):
        self.calendarCustomWidget.setSelectedDate(QDate.currentDate())
        self.onDateDoubleClicked()

    def onDateDoubleClicked(self):
        # print(self.calendarCustomWidget.selectedDate())
        formattedDate = self.calendarCustomWidget.selectedDate()
        self.dateSelected.emit(formattedDate)
        self.close()
        # self.deleteLater()
