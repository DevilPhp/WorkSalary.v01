from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit




class CustomLineEdit(QLineEdit):
    clearButtonClicked = Signal(bool)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPlaceholderText("Enter your text here")

    def clear(self):
        self.setText('')
        self.clearButtonClicked.emit(True)  # Emit the signal when the clear button is clicked
