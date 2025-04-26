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
        self.searchLineEdit.setFocus()
        self.searchLineEdit.textChanged.connect(self.updateMenuItems)
        self.searchLineEdit.returnPressed.connect(self.setCheckedItem)
        # self.move(0, 0)
        self.show()

    def setCheckedItem(self):
        for checkBox in self.checkBoxes:
            if checkBox.isVisible():
                checkBox.setChecked(True)
                self.close()
                break

    def updateMenuItems(self):
        text = self.searchLineEdit.text()
        for checkBox in self.checkBoxes:
            checkBox.setVisible(text.lower() in checkBox.text().lower())

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
        self.scrollArea.setMinimumSize(QSize(self.minWidth + 20, self.minHeight + 35))

    def emitCurrentItem(self, checkBox):
        self.checkedCheckbox.emit(checkBox)
