from PySide6.QtWidgets import QGraphicsDropShadowEffect

from app.ui.widgets.ui_customTimeChangeOpersDialog import *
from app.ui.widgets.ui_customOperTreeTimeWidget import *
from datetime import datetime


class CustomTimeChangeOpersDialog(QDialog, Ui_CustomTimeChangeOpersDialog):
    def __init__(self, operations, showEffectModel=True, parent=None):
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
        if showEffectModel:
            self.effectModelsWidget.setVisible(True)
        else:
            self.effectModelsWidget.setVisible(False)

        self.setOperationsTimes()
        self.currentMonth = datetime.now().month
        self.effectMonthComboBox.setCurrentIndex(self.currentMonth - 1)
        self.effectMonthComboBox.setEnabled(False)

        self.effectTPCheckBox.stateChanged.connect(self.effectTPCheckBoxChanged)

        self.yesBtn.clicked.connect(self.accept)
        self.noBtn.clicked.connect(self.reject)

    def effectTPCheckBoxChanged(self, state):
        if state == 2:
            self.effectMonthComboBox.setEnabled(True)
        else:
            self.effectMonthComboBox.setEnabled(False)

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
