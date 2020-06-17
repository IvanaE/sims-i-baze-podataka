from PySide2 import QtCore
from PySide2.QtCore import QAbstractTableModel


class ModelTableModel(QAbstractTableModel):
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model

    # pomocna metoda
    def get_element(self, index):
        return self.model.data[index.row()]

    def rowCount(self, index):
        return len(self.model.data)

    def columnCount(self, index):
        return len(self.model.metaModel.metadata)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        model = self.get_element(index)
        key = self.model.metaModel.metadata[index.column()].name
        if role == QtCore.Qt.DisplayRole:
            return model[key]
        return None

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.model.metaModel.metadata[section].columnName
        return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        model = self.get_element(index)
        key = self.model.metaModel.metadata[index.column()].name
        if value == "":
            return False
        if role == QtCore.Qt.EditRole:
            model[key] = value
            return True
        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable  # ili nad bitovima

