from PySide6.QtCore import QAbstractTableModel, Qt, Signal, QItemSelection, QItemSelectionModel
from PySide6.QtWidgets import QTreeView, QAbstractItemView


class CustomTreeView(QTreeView):
    selectedRows = Signal(dict)
    clearCurrentSelection = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSelectionBehavior(QTreeView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QTreeView.SelectionMode.ExtendedSelection)

        self.setDragEnabled(False)
        self.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setAlternatingRowColors(True)
        # self.doubleClicked.connect(self.doubleClickedItem)

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
                        alternate-background-color: #d3d3d3;
                        font: 10.5pt "Segoe UI";
                        selection-background-color: #aeaeae;
                        selection-color: #fefefe;
                    }
                    QAbstractItemView:item{
                        selection-background-color: #aeaeae;
                        selection-color: #fefefe;
                        border-bottom: 1px solid #aeaeae;
                    }
                    
                    QAbstractItemView::item:selected{
                        background-color: #aeaeae;
                    }
                ''')

    # def doubleClickedItem(self, indexRow):
    #     if not self.isExpanded(indexRow):
    #         print('yes')
    #         self.expand(indexRow)
    #     else:
    #         self.collapse(indexRow)
