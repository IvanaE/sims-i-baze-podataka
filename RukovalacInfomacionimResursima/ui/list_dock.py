from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QListWidget, QListView, QVBoxLayout, QWidget, QPushButton

from data_source_type import DataSourceType
from ui.add_meta_model_form import AddMetaModelForm
from ui.add_model_form import AddModelForm
from ui.list_dock_meta_model import ListDockMetaModel
from ui.list_dock_model import ListDockModel


class ListDock(QtWidgets.QDockWidget):
    metaModelHandler = None
    modelHandler = None

    def __init__(self, title, parent, handleMetamodelClick, handleModelClick):
        super().__init__(title, parent)

        self.selectedMetaModel = None
        self.selectedModel = None

        self.main_layout = QVBoxLayout()
        self.widget = QWidget()

        self.handleMetamodelClick = handleMetamodelClick
        self.handleModelClick = handleModelClick

        self.listMetaModel = QListView()
        self.listDockMetaModel = ListDockMetaModel()
        self.listMetaModel.setModel(self.listDockMetaModel)
        self.listMetaModel.clicked.connect(self.itemClickMetaModel)
        self.main_layout.addWidget(self.listMetaModel)

        self.addMetaModelButton = QPushButton('Add Meta Model')
        self.addMetaModelButton.clicked.connect(self.addMetaModel)
        self.main_layout.addWidget(self.addMetaModelButton)

        self.deleteMetaModelButton = QPushButton('Delete Meta Model')
        self.deleteMetaModelButton.clicked.connect(self.deleteMetaModel)
        self.main_layout.addWidget(self.deleteMetaModelButton)

        self.listModel = QListView()
        self.listDockModel = ListDockModel()
        self.listModel.setModel(self.listDockModel)
        self.listModel.clicked.connect(self.itemClickModel)

        self.main_layout.addWidget(self.listModel)

        self.addModelButton = QPushButton('Add Model')
        self.addModelButton.clicked.connect(self.addModel)
        self.main_layout.addWidget(self.addModelButton)

        self.deleteModelButton = QPushButton('Delete Model')
        self.deleteModelButton.clicked.connect(self.deleteModel)
        self.main_layout.addWidget(self.deleteModelButton)

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
        self.selectedMetaModel = self.metaModelHandler.metaModels[item.row()]
        self.handleMetamodelClick(self.metaModelHandler.metaModels[item.row()])

    def itemClickModel(self, item):
        self.selectedModel = self.modelHandler.models[item.row()]
        self.handleModelClick(self.modelHandler.models[item.row()])

    def deleteMetaModel(self):

        if self.selectedMetaModel == None:
            return

        self.metaModelHandler.delete(self.selectedMetaModel)

        self.listDockMetaModel.layoutChanged.emit()

    def deleteModel(self):

        if self.selectedModel == None:
            return

        self.modelHandler.delete(self.selectedModel)

        self.listDockModel.layoutChanged.emit()

    def addModel(self):

        self.form = AddModelForm(self.metaModelHandler, self.addModelOk)
        self.form.show()

    def addMetaModel(self):

        self.metaModelForm = AddMetaModelForm(self.metaModelHandler, self.addMetaModelOk)
        self.metaModelForm.show()

    def addModelOk(self, name, source, sourceType, metaModel):
        self.modelHandler.addModel(name, source, self.getSourceTypeWithName(sourceType),
                                   self.getMetaModelWithName(metaModel))
        self.form.close()
        self.listDockModel.layoutChanged.emit()

    def addMetaModelOk(self, name, key):
        self.metaModelHandler.addMetaModel(name, key)

        self.metaModelForm.close()
        self.listDockMetaModel.layoutChanged.emit()

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