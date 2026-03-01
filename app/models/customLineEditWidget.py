from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLineEdit


class CustomLineEdit(QLineEdit):
    doubleClicked = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.setMaximumWidth(34)
        # self.setMinimumWidth(34)
        # self.setText('Hello')

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.selectAll()

    def focusOutEvent(self, event):
        if self.parent().objectName() == 'widget_25':
            self.editingFinished.emit()
        super().focusOutEvent(event)

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key.Key_Tab:
    #         print('hello')
    #     else:
    #         super().keyPressEvent(event)

    # def mouseDoubleClickEvent(self, event):
    #     self.doubleClicked.emit()
    #     super().mouseDoubleClickEvent(event)

