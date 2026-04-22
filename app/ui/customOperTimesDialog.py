from PySide6.QtWidgets import QGraphicsDropShadowEffect

from app.ui.widgets.ui_customTimeChangeOpersDialog import *
from app.ui.widgets.ui_customOperTreeTimeWidget import *


class CustomTimeChangeOpersDialog(QDialog, Ui_CustomTimeChangeOpersDialog):
    def __init__(self, operations, parent=None):
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

        self.operations = operations

        self.setOperationsTimes()

        self.yesBtn.clicked.connect(self.accept)
        self.noBtn.clicked.connect(self.reject)

    def setOperationsTimes(self):
        for key, value in self.operations.items():
            customWidget = CustomOperTreeTimeWidget(key)
            customWidget.setOperationTime(value)
            self.operTimesLayout.addWidget(customWidget)


class CustomOperTreeTimeWidget(QWidget, Ui_customOperTreeTimeWidget):
    def __init__(self, parents, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.operPositionLabel.setText(parents)

    def setOperationTime(self, operations):
        count = 0
        for catalogId, operation in operations.items():
            numberLabel = QLabel(str(count + 1))
            operNameLabel = QLabel(operation['operName'])
            operNameLabel.setObjectName(str(operation['operId']))
            operTimeLabel = QLabel(str(operation['newTime']))
            operTimeLabel.setObjectName(str(catalogId))
            minsLabel = QLabel("мин.")
            self.opersGridLayout.addWidget(numberLabel, count, 0)
            self.opersGridLayout.addWidget(operNameLabel, count, 1)
            self.opersGridLayout.addWidget(operTimeLabel, count, 2)
            self.opersGridLayout.addWidget(minsLabel, count, 3)
            count += 1
