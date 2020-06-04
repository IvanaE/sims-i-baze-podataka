from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QPushButton

from ui.meta_model_table_model import MetaModelTableModel


class MetaModelViewWidget(QWidget):
    def __init__(self, parent, metaModel):
        super().__init__(parent)

        self.metaModel = metaModel

        self.main_layout = QVBoxLayout()

        self.table = QtWidgets.QTableView(self)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.model = MetaModelTableModel(metaModel.metadata)
        self.table.setModel(self.model)

        self.addRowButton = QPushButton('Add')
        self.addRowButton.clicked.connect(self.addRow)

        self.main_layout.addWidget(self.table)
        self.main_layout.addWidget(self.addRowButton)
        self.setLayout(self.main_layout)

    def addRow(self):

        self.metaModel.addMetaData()
        self.model.layoutChanged.emit()

