from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QListWidget, QListView, QVBoxLayout, QWidget

from ui.list_dock_meta_model import ListDockMetaModel
from ui.list_dock_model import ListDockModel


class ListDock(QtWidgets.QDockWidget):
    metaModelHandler = None

    def __init__(self, title, parent, handleMetamodelClick):
        super().__init__(title, parent)

        self.main_layout = QVBoxLayout()
        self.widget = QWidget()

        self.handleMetamodelClick = handleMetamodelClick

        self.listMetaModel = QListView()
        self.listDockMetaModel = ListDockMetaModel()
        self.listMetaModel.setModel(self.listDockMetaModel)
        self.listMetaModel.clicked.connect(self.itemClickMetaModel)
        self.main_layout.addWidget(self.listMetaModel)

        self.listModel = QListView()
        self.listDockModel = ListDockModel()
        self.listModel.setModel(self.listDockModel)
        self.listModel.clicked.connect(self.itemClickModel)

        self.main_layout.addWidget(self.listModel)
        self.widget.setLayout(self.main_layout)

        self.setWidget(self.widget)

    def init(self, metaModelHandler, models):

        self.metaModelHandler = metaModelHandler
        self.listDockMetaModel.init(metaModelHandler)
        self.listDockMetaModel.layoutChanged.emit()

    def itemClickMetaModel(self, item):
        self.handleMetamodelClick(self.metaModelHandler.metaModels[item.row()])

    def itemClickModel(self, item):
        print()
        #self.handleMetamodelClick(self.metaModelHandler.metaModels[item.row()])