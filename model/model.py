from PySide2 import QtCore, QtGui

import operator

class GenericModel(QtCore.QAbstractTableModel):
    def __init__(self, parent = None, metadata = [], elements = []):
        super().__init__(parent)
        self.read_only = 0
        self.elements = elements
        self.metadata = metadata


        for column in range(len(self.metadata["columns"])):
            if self.metadata["columns"][column] == self.metadata["key"]:
                self.read_only = column
    

    def get_element(self, index):

        return self.elements[index.row()]

    def get_unique_data(self, index):
        subtable_key = self.metadata['subtable_key']
        selected = self.elements[index.row()]
        return selected[subtable_key]

    def get_subtable_metadata(self):
        metadata = self.metadata["subtable_key"]
        metadata += "_metadata.json"
        return metadata


    def rowCount(self, index):
        return len(self.elements)
        
    def columnCount(self, index):
        return len(self.metadata['columns'])

    def data(self, index, role = QtCore.Qt.DisplayRole):

        element = self.get_element(index)
        if role == QtCore.Qt.DisplayRole:
            ret_column = self.metadata['columns'][index.column()]
            return element[ret_column]
        if role == QtCore.Qt.BackgroundRole and index.column() == self.read_only:
            return QtGui.QBrush(QtGui.QColor(201,175,175))
        return None

    def setData(self, index, value, role = QtCore.Qt.EditRole):

        element = self.get_element(index)
        if value == " ":
            return False

        if role == QtCore.Qt.EditRole:
            element[self.metadata['columns'][index.column()]] = value
            return True

        return False

    def headerData(self, section, orientation, role = QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.metadata['columns'][section]

        return None

    def sort(self, col, order):

        sort_by = self.metadata['columns'][col]
        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
        self.elements = sorted(self.elements, key=operator.itemgetter(sort_by))
        if order == QtCore.Qt.DescendingOrder:
            self.elements.reverse()
        self.emit(QtCore.SIGNAL("layoutChanged()"))

    def flags(self, index):
        if index.column() == self.read_only:
            return super().flags(index) | QtCore.Qt.ItemIsSelectable
        else:
            return super().flags(index) | QtCore.Qt.ItemIsEditable


