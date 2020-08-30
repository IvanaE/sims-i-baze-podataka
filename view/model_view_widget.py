from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QPushButton

from view.model_table_model import ModelTableModel


class ModelViewWidget(QWidget):
    def __init__(self, parent, model):
        super().__init__(parent)

        self.model = model
        self.selectedData = None

        self.main_layout = QVBoxLayout()

        self.table = QtWidgets.QTableView(self)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableModel = ModelTableModel(model)
        self.table.setModel(self.tableModel)

        self.table.clicked.connect(self.select)

        self.addRowButton = QPushButton('Add')
        self.addRowButton.setIcon(QtGui.QIcon('view/icons/icons8-add-image-96.png'))
        self.addRowButton.clicked.connect(self.addRow)

        self.deleteRowButton = QPushButton('Delete')
        self.deleteRowButton.setIcon(QtGui.QIcon('view/icons/icons8-delete-96.png'))
        self.deleteRowButton.clicked.connect(self.delete)

        self.main_layout.addWidget(self.table)
        self.main_layout.addWidget(self.addRowButton)
        self.main_layout.addWidget(self.deleteRowButton)
        self.setLayout(self.main_layout)

    def addRow(self):

        data = {}

        for item in self.model.metaModel.metadata:
            data[item.name] = ''

        self.model.data.append(data)
        self.tableModel.layoutChanged.emit()

    def select(self, index):
        self.selectedData = self.model.data[index.row()]

    def delete(self):

        if self.selectedData == None:
            return

        self.model.data.remove(self.selectedData)
        self.tableModel.layoutChanged.emit()
        self.selectedData = None
