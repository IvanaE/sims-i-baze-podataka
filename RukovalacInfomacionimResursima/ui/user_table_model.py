from PySide2 import QtCore
from PySide2.QtCore import QAbstractTableModel


class UserTableModel(QAbstractTableModel):
    def __init__(self, users, parent=None):
        super().__init__(parent)
        self.users = users

    # pomocna metoda
    def get_element(self, index):
        return self.users[index.row()]

    def rowCount(self, index):
        return len(self.users)

    def columnCount(self, index):
        return 5

    def data(self, index, role=QtCore.Qt.DisplayRole):
        model = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return model.firstName
        if index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return model.lastName
        if index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return model.username
        if index.column() == 3 and role == QtCore.Qt.DisplayRole:
            return model.password
        if index.column() == 4 and role == QtCore.Qt.DisplayRole:
            return model.type
        return None

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return 'First Name'
        if section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return 'Last Name'
        if section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return 'Username'
        if section == 3 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return 'Password'
        if section == 4 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return 'Type'

        return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        user = self.get_element(index)
        if value == "":
            return False
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            user.firstName = value
        if index.column() == 1 and role == QtCore.Qt.EditRole:
            user.lastName = value
        if index.column() == 2 and role == QtCore.Qt.EditRole:
            user.username = value
        if index.column() == 3 and role == QtCore.Qt.EditRole:
            user.password = value
        if index.column() == 4 and role == QtCore.Qt.EditRole:
            user.type = value
        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable  # ili nad bitovima

