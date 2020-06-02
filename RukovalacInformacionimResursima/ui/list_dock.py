from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QListWidget, QListView

from ui.list_dock_model import ListDockModel


class ListDock(QtWidgets.QDockWidget):
    metaModelHandler = None

    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.list = QListView()
        self.model = ListDockModel()
        self.list.setModel(self.model)
        self.list.clicked.connect(self.itemClick)
        self.setWidget(self.list)

    def init(self, metaModelHandler):

        self.metaModelHandler = metaModelHandler
        self.model.init(metaModelHandler)
        self.model.layoutChanged.emit()

    def itemClick(self, item):
        print(item.row())