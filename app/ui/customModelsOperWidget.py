from app.logger import logger
from app.ui.widgets.ui_operToModelTypeCustomWidget import *
from app.ui.customWidgetForDefaultOper import CustomCheckboxWidget


class CustomWidgetForModelOper(QWidget, Ui_customWidgetForModelOper):
    def __init__(self, parent=None):
        super(self).__init__(parent)
        self.setupUi(self)
