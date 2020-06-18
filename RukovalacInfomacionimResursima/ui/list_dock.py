import os

from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QDir
from PySide2.QtWidgets import QVBoxLayout, QWidget, QPushButton, QFileSystemModel, QTreeView

from data_source_type import DataSourceType
from ui.add_model_form import AddModelForm


class ListDock(QtWidgets.QDockWidget):
    metaModelHandler = None
    modelHandler = None

    def __init__(self, title, parent, handleModelClick):
        super().__init__(title, parent)

        self.selectedMetaModel = None
        self.selectedModel = None

        self.main_layout = QVBoxLayout()
        self.widget = QWidget()

        self.handleModelClick = handleModelClick

        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath(QDir.currentPath())
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.file_system_model)
        self.tree_view.setRootIndex(
            self.file_system_model.index(QDir.currentPath() + '/data'))
        self.tree_view.clicked.connect(self.file_clicked_handler)
        self.main_layout.addWidget(self.tree_view)

        self.addModelButton = QPushButton('Add Model')
        self.addModelButton.setIcon(QtGui.QIcon('icons8-add-image-96.png'))
        self.addModelButton.clicked.connect(self.addModel)
        self.main_layout.addWidget(self.addModelButton)

        self.deleteModelButton = QPushButton('Delete Model')
        self.deleteModelButton.setIcon(QtGui.QIcon('icons8-delete-96.png'))
        self.deleteModelButton.clicked.connect(self.deleteModel)
        self.main_layout.addWidget(self.deleteModelButton)

        self.widget.setLayout(self.main_layout)

        self.setWidget(self.widget)

    def init(self, metaModelHandler, modelHandler):

        self.metaModelHandler = metaModelHandler
        self.modelHandler = modelHandler


    def deleteModel(self):

        if self.selectedModel == None:
            return

        self.modelHandler.delete(self.selectedModel)

        self.listDockModel.layoutChanged.emit()

    def addModel(self):

        self.form = AddModelForm(self.metaModelHandler, self.addModelOk)
        self.form.show()


    def addModelOk(self, name, source, sourceType, metaModel):
        self.modelHandler.addModel(name, source, self.getSourceTypeWithName(sourceType),
                                   self.getMetaModelWithName(metaModel))
        self.form.close()
        self.listDockModel.layoutChanged.emit()

    def file_clicked_handler(self, index):
        index = self.tree_view.currentIndex()
        file_clicked_param = os.path.basename(
            self.file_system_model.filePath(index))

        [name, type] = file_clicked_param.split('.')


        model = self.modelHandler.getModelFromFile(name, self.getSourceTypeWithName(type))

        self.handleModelClick(model)

    def getMetaModelWithName(self, name):

        for metaModel in self.metaModelHandler.metaModels:
             if metaModel.name == name:
                 return metaModel

        return None

    def getSourceTypeWithName(self, name):

        if name == 'Serial':
            return DataSourceType.SERIAL
        if name == 'Seq':
            return DataSourceType.SEQ

        return DataSourceType.MYSQL