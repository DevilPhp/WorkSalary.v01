from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QLineEdit, QGraphicsDropShadowEffect, QPushButton


class MainMenuPage:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

        for index in range(self.mainWindow.ui.mainMenuLayout.count()):
            widget = self.mainWindow.ui.mainMenuLayout.itemAt(index).widget()
            if isinstance(widget, QPushButton):
                self.setShadowEffect(widget)

        # self.mainWindow.ui.setDefaultOperBtn.clicked.connect(lambda: self.setDefaultOper())

    def setShadowEffect(self, widget):
        shadow = QGraphicsDropShadowEffect(widget)
        shadow.setBlurRadius(15)
        shadow.setXOffset(2)
        shadow.setYOffset(2)
        shadow.setColor(QColor("#7f7f7f"))
        widget.setGraphicsEffect(shadow)


