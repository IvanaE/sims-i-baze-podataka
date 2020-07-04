import sys
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QToolBar, QToolButton, QTabWidget, QWidget, QVBoxLayout, QMenuBar, QMenu, QMainWindow

from meta_model_handler import MetaModelHandler
from model_handler import ModelHandler
from ui.list_dock import ListDock
from ui.login_form import LoginForm
from ui.model_view_widget import ModelViewWidget
from ui.user_widget import UserWidget
from user_handler import UserHandler

userHandler = UserHandler()

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(840, 680)
        self.setWindowTitle("InfHandler")
        self.setWindowIcon(QtGui.QIcon("icons8-edit-file-64.png"))

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
        self.mainTabWidget.addTab(self.userWidget, QtGui.QIcon("icons8-edit-file-64.png"), 'Users')

    def load(self):
        self.metaModelHandler.load()
        self.modelHandler.load()
        self.listDock.init(self.metaModelHandler, self.modelHandler)

    def save(self):
        self.metaModelHandler.save()
        self.modelHandler.save()

    def handleModelClick(self, model):
        self.modelWidget = ModelViewWidget(self.mainTabWidget, model)
        self.mainTabWidget.addTab(self.modelWidget, QtGui.QIcon("icons8-edit-file-64.png"), model.name + ' - Model')

        for metaData in model.metaModel.metadata:

            if metaData.type == 'string' or metaData.type == 'int' or metaData.type == 'double':
                continue

            connectedModel = self.modelHandler.getModelWithName(metaData.type)

            if connectedModel == None:
                continue

            connectedModelWidget = ModelViewWidget(self.connectedTabWidget, connectedModel)
            self.connectedTabWidget.addTab(connectedModelWidget, QtGui.QIcon("icons8-edit-file-64.png"),
                                      connectedModel.name + ' - Model')

    def delete_tab_main(self, index):
        self.mainTabWidget.removeTab(index)

    def delete_tab_connected(self, index):
        self.connectedTabWidget.removeTab(index)


def exit():
    app.closeAllWindows()


def login(logedUser):
    userHandler.user = logedUser
    loginForm.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginForm = LoginForm(login, userHandler)
    main_window = MainWindow()

    toolBar = QToolBar()

    loginForm.show()
    loginForm.exec_()

    main_window.load()

    toolExitButton = QToolButton()
    toolExitButton.setIcon(QtGui.QIcon("icons8-exit-96.png"))
    toolExitButton.clicked.connect(exit)
    toolBar.addWidget(toolExitButton)

    if userHandler.user.type == 'admin':
        toolUserButton = QToolButton()
        toolUserButton.setIcon(QtGui.QIcon("icons8-user-folder-96.png"))
        toolUserButton.clicked.connect(main_window.userClick)
        toolBar.addWidget(toolUserButton)

    main_window.addToolBar(toolBar)

    main_window.showMaximized()
    main_window.show()
    app.exec_()
    main_window.save()
    userHandler.save()
    sys.exit()
