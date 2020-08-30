from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget, QMenu

from view.list_dock import ListDock
from view.meta_model_handler import MetaModelHandler
from view.model_handler import ModelHandler
from view.model_view_widget import ModelViewWidget


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(840, 680)
        self.setWindowTitle("InfHandler")
        self.setWindowIcon(QtGui.QIcon("view/icons/icons8-edit-file-64.png"))

        self.metaModelHandler = MetaModelHandler()
        self.modelHandler = ModelHandler(self.metaModelHandler)

        self.listDock = ListDock('Data', self, self.handleModelClick)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.listDock)

        self.mainTabWidget = QTabWidget(self)
        self.mainTabWidget.setTabsClosable(True)
        self.mainTabWidget.tabCloseRequested.connect(self.delete_tab_main)

        self.connectedTabWidget = QTabWidget(self)
        self.connectedTabWidget.setTabsClosable(True)
        self.connectedTabWidget.tabCloseRequested.connect(self.delete_tab_connected)

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.mainTabWidget)
        self.main_layout.addWidget(self.connectedTabWidget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.central_widget)

        self.menuBar = self.menuBar()
        self.menuBar.addMenu(QMenu('File'))
        self.menuBar.addMenu(QMenu('View'))
        self.menuBar.addMenu(QMenu('Edit'))
        self.menuBar.addMenu(QMenu('Help'))
    def userClick(self):
        self.userWidget = UserWidget(self.mainTabWidget, userHandler)
        self.mainTabWidget.addTab(self.userWidget, QtGui.QIcon("view/icons/icons8-edit-file-64.png"), 'Users')

    def load(self):
        self.metaModelHandler.load()
        self.modelHandler.load()
        self.listDock.init(self.metaModelHandler, self.modelHandler)

    def save(self):
        self.metaModelHandler.save()
        self.modelHandler.save()

    def handleModelClick(self, model):

        if model is None:
            return

        self.modelWidget = ModelViewWidget(self.mainTabWidget, model)
        self.mainTabWidget.addTab(self.modelWidget, QtGui.QIcon("view/icons/icons8-edit-file-64.png"), model.name + ' - Model')

        for metaData in model.metaModel.metadata:

            if metaData.type == 'string' or metaData.type == 'int' or metaData.type == 'double':
                continue

            connectedModel = self.modelHandler.getModelWithName(metaData.type)

            if connectedModel == None:
                continue

            connectedModelWidget = ModelViewWidget(self.connectedTabWidget, connectedModel)
            self.connectedTabWidget.addTab(connectedModelWidget, QtGui.QIcon("view/icons/icons8-edit-file-64.png"),
                                      connectedModel.name + ' - Model')

    def delete_tab_main(self, index):
        self.mainTabWidget.removeTab(index)

    def delete_tab_connected(self, index):
        self.connectedTabWidget.removeTab(index)