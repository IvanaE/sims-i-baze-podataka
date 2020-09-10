from PySide2 import QtCore, QtGui
import operator

class SqlModel(QtCore.QAbstractTableModel):
    def __init__(self, parent = None, repository = None, elements = []):
        super().__init__(parent)
        self.elements = elements
        self.repository = repository
        self.read_only_column = 0
        self.read_only_column = repository.key
    
    def get_element(self, index):
        return self.elements[index.row()]

    def rowCount(self, index):
        return len(self.elements)
        
    def columnCount(self, index):
        return len(self.repository.column_names)

    def data(self, index, role = QtCore.Qt.DisplayRole):
        element = self.get_element(index)
        if role == QtCore.Qt.DisplayRole:
            return str(element[index.column()])
        if role == QtCore.Qt.BackgroundRole and index.column() == self.read_only_column:
            return QtGui.QBrush(QtGui.QColor(201,175,175))
        return None

    def headerData(self, section, orientation, role = QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.repository.column_names[section]

        return None

    def flags(self, index):
        if index.column() == self.read_only_column:
            return super().flags(index) | QtCore.Qt.ItemIsSelectable
        else:
            return super().flags(index) | QtCore.Qt.ItemIsEditable

    def sort(self, col, order):
        sort_by = self.repository.column_names[col]
        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
        self.elements = sorted(self.elements, key=0)        
        if order == QtCore.Qt.DescendingOrder:
            self.elements.reverse()
        self.emit(QtCore.SIGNAL("layoutChanged()"))

    def setData(self, index, value, role = QtCore.Qt.EditRole):
        element = self.get_element(index)
        if value == " ":
            return False

        if role == QtCore.Qt.EditRole:
            temp = list(element)
            temp[index.column()] = value
            element = tuple(temp)
            self.elements[index.row()] = element
            self.repository.edit(element, self.repository.column_names[index.column()], value)
            return True

        return False