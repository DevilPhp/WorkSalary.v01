from PySide6.QtWidgets import QTreeView


class CustomTreeView(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet('''
                    QHeaderView:section{
                        font: 700 10.5pt "Segoe UI";
                        background-color: #dfdfdf;
                        padding-left: 10px;
                        padding-top:10px;
                        padding-right:10px;
                        selection-background-color: #7f7f7f;
                    }
                    QAbstractItemView{
                        font: 10.5pt "Segoe UI";
                        selection-background-color: #545454;
                        selection-color: #fefefe;
                    }
                    QAbstractItemView:item{
                        selection-background-color: #545454;
                        selection-color: #fefefe;
                    }
                ''')
