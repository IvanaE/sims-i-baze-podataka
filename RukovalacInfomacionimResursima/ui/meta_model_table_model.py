from PySide2 import QtCore
from PySide2.QtCore import QAbstractTableModel


class MetaModelTableModel(QAbstractTableModel):
    def __init__(self, metadata, parent=None):
        super().__init__(parent)
        self.metadata = metadata

    # pomocna metoda
    def get_element(self, index):
        return self.metadata[index.row()]

    def rowCount(self, index):
        return len(self.metadata)

    def columnCount(self, index):
        return 4

    def data(self, index, role=QtCore.Qt.DisplayRole):
        # TODO: dodati obradu uloga (role)
        metadata = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return metadata.name
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return metadata.columnName
        elif index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return metadata.type
        elif index.column() == 3 and role == QtCore.Qt.DisplayRole:
            return metadata.index
        return None

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Name"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Column Name"
        elif section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Type"
        elif section == 3 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Index"
        return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        metadata = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            metadata.name = value
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            metadata.columnName = value
            return True
        elif index.column() == 2 and role == QtCore.Qt.EditRole:
            metadata.type = value
            return True
        elif index.column() == 3 and role == QtCore.Qt.EditRole:
            metadata.index = value
            return True
        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable  # ili nad bitovima

