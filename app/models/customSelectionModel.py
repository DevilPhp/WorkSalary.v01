from PySide6.QtCore import QItemSelectionModel, QModelIndex, Qt


class SingleMultiSelectionModel(QItemSelectionModel):
    """
    A custom selection model that clears previous selections when a new
    selection is made without modifier keys.
    """

    def __init__(self, model, parent=None):
        super().__init__(model, parent)
        self.selecting = False

    def select(self, index, command):
        """
        Override the select method to change the behavior when making selections.
        - If Ctrl or Shift is pressed, behave normally (extend selection)
        - Otherwise, clear other selections
        """
        # Check if this is part of a normal click (without Ctrl or Shift)
        if command & QItemSelectionModel.SelectCurrent:
            # Clear previous selection
            super().select(QModelIndex(), QItemSelectionModel.Clear)

            # Set our actual selection command to include rows
            command |= QItemSelectionModel.Current

        # Call the parent implementation with our modified command
        return super().select(index, command)
