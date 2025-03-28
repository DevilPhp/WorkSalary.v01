from PySide6.QtWidgets import QCompleter
from PySide6.QtCore import Qt


class Utils:
    @staticmethod
    def setupCompleter(listNames, widget):
        completer = QCompleter(listNames, widget)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        widget.setCompleter(completer)
        # widget.completer().setCompletionMode(QCompleter.InlineCompletion)
