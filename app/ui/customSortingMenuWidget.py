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
        # self.move(0, 0)
        self.show()

    def addItems(self, items):
        minWidth = 80
        if len(items) > 10:
            minHeight = 20 * 10
        else:
            minHeight = 20 * len(items)
        for item in items:
            checkBox = QCheckBox(item, self)
            checkBox.setMaximumHeight(20)
            self.menuItemsHolder.addWidget(checkBox)
            checkBox.stateChanged.connect(partial(self.emitCurrentItem, checkBox))
            if minWidth < checkBox.sizeHint().width():
                minWidth = checkBox.sizeHint().width()
        self.scrollArea.setMinimumSize(QSize(minWidth + 20, minHeight + 20))

    def emitCurrentItem(self, checkBox, state):
        self.checkedCheckbox.emit(checkBox)
