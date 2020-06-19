from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QPushButton

from ui.model_table_model import ModelTableModel
from ui.user_table_model import UserTableModel
from user import User


class UserWidget(QWidget):
    def __init__(self, parent, userHandler):
        super().__init__(parent)

        self.userHandler = userHandler
        self.selectedData = None

        self.main_layout = QVBoxLayout()

        self.table = QtWidgets.QTableView(self)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableModel = UserTableModel(userHandler.users)
        self.table.setModel(self.tableModel)

        self.table.clicked.connect(self.select)

        self.addRowButton = QPushButton('Add')
        self.addRowButton.setIcon(QtGui.QIcon('icons8-add-image-96.png'))
        self.addRowButton.clicked.connect(self.addRow)

        self.deleteRowButton = QPushButton('Delete')
        self.deleteRowButton.setIcon(QtGui.QIcon('icons8-delete-96.png'))
        self.deleteRowButton.clicked.connect(self.delete)

        self.main_layout.addWidget(self.table)
        self.main_layout.addWidget(self.addRowButton)
        self.main_layout.addWidget(self.deleteRowButton)
        self.setLayout(self.main_layout)

    def addRow(self):


        self.userHandler.users.append(User('', '', '', '', ''))
        self.tableModel.layoutChanged.emit()

    def select(self, index):
        self.selectedData = self.userHandler.users[index.row()]

    def delete(self):

        if self.selectedData == None:
            return

        self.userHandler.users.remove(self.selectedData)
        self.tableModel.layoutChanged.emit()
        self.selectedData = None