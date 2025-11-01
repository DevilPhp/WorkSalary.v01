from PySide6.QtGui import QIntValidator, QDoubleValidator

from app.ui.widgets.ui_customParametersRowWidget import *


class CustomParametersRowWidget(Ui_customParametersRowWidget, QWidget):
    def __init__(self, type, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.intValidator = QIntValidator(1, 99999999)
        self.floatValidator = QDoubleValidator(0.1, float('inf'), 4)
        self.floatValidator.setNotation(QDoubleValidator.Notation.StandardNotation)
        locale = QLocale(QLocale.Language.English)
        self.floatValidator.setLocale(locale)
        self.type = type
        if self.type == "numeric":
            self.inputLineEdit.setValidator(self.intValidator)
        elif self.type == "float":
            self.inputLineEdit.setValidator(self.floatValidator)
            self.inputLineEdit.returnPressed.connect(self.checkFloatChange)
            self.inputLineEdit.editingFinished.connect(self.checkFloatChange)
            self.inputLineEdit.textChanged.connect(self.checkFloat)

    def checkFloatChange(self):
        text = self.inputLineEdit.text()
        try:
            text = float(text)
            self.inputLineEdit.setText(str(text))
        except ValueError:
            self.inputLineEdit.setText("")

    def checkFloat(self, text):
        if ',' in text:
            text = text.split(',')[0]
            text = text + '.'
        self.inputLineEdit.setText(text)
