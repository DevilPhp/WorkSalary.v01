from app.ui.widgets.ui_customWorkersWidget import *


class CustomWorkersWidget(QWidget, Ui_customWorkersEditWidget):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setWindowTitle("Персонал")
