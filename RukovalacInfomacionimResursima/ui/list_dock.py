from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QListWidget, QListView, QVBoxLayout, QWidget, QPushButton

from data_source_type import DataSourceType
from ui.add_model_form import AddModelForm
from ui.list_dock_meta_model import ListDockMetaModel
from ui.list_dock_model import ListDockModel


class ListDock(QtWidgets.QDockWidget):
    metaModelHandler = None
    modelHandler = None

    def __init__(self, title, parent, handleMetamodelClick, handleModelClick):
        super().__init__(title, parent)

        self.main_layout = QVBoxLayout()
        self.widget = QWidget()

        self.handleMetamodelClick = handleMetamodelClick
        self.handleModelClick = handleModelClick

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

        self.addModelButton = QPushButton('Add Model')
        self.addModelButton.clicked.connect(self.addModel)
        self.main_layout.addWidget(self.addModelButton)

        self.widget.setLayout(self.main_layout)

        self.setWidget(self.widget)

    def init(self, metaModelHandler, modelHandler):

        self.metaModelHandler = metaModelHandler
        self.modelHandler = modelHandler
        self.listDockMetaModel.init(metaModelHandler)
        self.listDockMetaModel.layoutChanged.emit()

        self.listDockModel.init(modelHandler)
        self.listDockModel.layoutChanged.emit()

    def itemClickMetaModel(self, item):
        self.handleMetamodelClick(self.metaModelHandler.metaModels[item.row()])

    def itemClickModel(self, item):
        self.handleModelClick(self.modelHandler.models[item.row()])

    def addModel(self):

        self.form = AddModelForm(self.metaModelHandler, self.addModelOk)
        self.form.show()

    def addModelOk(self, name, source, sourceType, metaModel):
        self.modelHandler.addModel(name, source, self.getSourceTypeWithName(sourceType),
                                   self.getMetaModelWithName(metaModel))
        self.form.close()
        self.listDockModel.layoutChanged.emit()

    def getMetaModelWithName(self, name):

        for metaModel in self.metaModelHandler.metaModels:
             if metaModel.name == name:
                 return metaModel

        return None

    def getSourceTypeWithName(self, name):

        if name == 'Serial':
            return DataSourceType.SERIAL
        if name == 'Sequential':
            return DataSourceType.SEQ

        return DataSourceType.MYSQL