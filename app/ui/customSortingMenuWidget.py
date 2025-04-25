from functools import partial

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QCheckBox

from app.ui.widgets.ui_customSortingMenuWidget import *


class CustomSortingMenuWidget(QWidget, Ui_customSortingMenuWidget):
    checkedCheckbox = Signal(QWidget)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Popup)
        self.checkBoxes = []
        self.minHeight = 20
        self.minWidth = 80
        # self.move(0, 0)
        self.show()

    def addItems(self, items):
        for item in items:
            self.addItem(item)

    def addItem(self, item, checked=False):
        checkBox = QCheckBox(item, self)
        checkBox.setChecked(checked)
        checkBox.stateChanged.connect(lambda: self.emitCurrentItem(checkBox))
        self.menuItemsHolder.addWidget(checkBox)
        self.checkBoxes.append(checkBox)
        if self.minWidth < checkBox.sizeHint().width():
            self.minWidth = checkBox.sizeHint().width()

    def setMenuSize(self, count):
        if count > 10:
            self.minHeight = 20 * 10
        else:
            self.minHeight = 20 * count
        self.scrollArea.setMinimumSize(QSize(self.minWidth + 20, self.minHeight + 20))


    def emitCurrentItem(self, checkBox):
        self.checkedCheckbox.emit(checkBox)
