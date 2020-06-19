import sys
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QToolBar, QToolButton, QTabWidget, QWidget, QVBoxLayout, QMenuBar, QMenu

from meta_model_handler import MetaModelHandler
from model_handler import ModelHandler
from ui.list_dock import ListDock
from ui.login_form import LoginForm
from ui.model_view_widget import ModelViewWidget
from ui.user_widget import UserWidget
from user_handler import UserHandler

metaModelHandler = MetaModelHandler()
modelHandler = ModelHandler(metaModelHandler)
userHandler = UserHandler()

def exit():
    app.closeAllWindows()

def load():
    metaModelHandler.load()
    modelHandler.load()
    listDock.init(metaModelHandler, modelHandler)

def save():
    metaModelHandler.save()
    modelHandler.save()

def handleModelClick(model):
    modelWidget = ModelViewWidget(mainTabWidget, model)
    mainTabWidget.addTab(modelWidget, QtGui.QIcon("icons8-edit-file-64.png"), model.name + ' - Model')

    for metaData in model.metaModel.metadata:

        if metaData.type == 'string' or metaData.type == 'int' or metaData.type == 'double':
            continue

        connectedModel = modelHandler.getModelWithName(metaData.type)

        if connectedModel == None:
            continue

        connectedModelWidget = ModelViewWidget(connectedTabWidget, connectedModel)
        connectedTabWidget.addTab(connectedModelWidget, QtGui.QIcon("icons8-edit-file-64.png"),
                                  connectedModel.name + ' - Model')



def delete_tab_main(index):
    mainTabWidget.removeTab(index)

def delete_tab_connected(index):
    connectedTabWidget.removeTab(index)

def login(logedUser):
    userHandler.user = logedUser
    loginForm.close()

def userClick():
    userWidget = UserWidget(mainTabWidget, userHandler)
    mainTabWidget.addTab(userWidget, QtGui.QIcon("icons8-edit-file-64.png"), 'Users')

app = QtWidgets.QApplication(sys.argv)
loginForm = LoginForm(login, userHandler)
main_window = QtWidgets.QMainWindow()
main_window.resize(840, 680)
main_window.setWindowTitle("InfHandler")
main_window.setWindowIcon(QtGui.QIcon("icons8-edit-file-64.png"))
metaModelHandler.load()
toolBar = QToolBar()


listDock = ListDock('Data', main_window, handleModelClick)
main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, listDock)

mainTabWidget = QTabWidget(main_window)
mainTabWidget.setTabsClosable(True)
mainTabWidget.tabCloseRequested.connect(delete_tab_main)

connectedTabWidget = QTabWidget(main_window)
connectedTabWidget.setTabsClosable(True)
connectedTabWidget.tabCloseRequested.connect(delete_tab_connected)

main_layout = QVBoxLayout()

main_layout.addWidget(mainTabWidget)
main_layout.addWidget(connectedTabWidget)

central_widget = QWidget()
central_widget.setLayout(main_layout)

main_window.setCentralWidget(central_widget)

menuBar = main_window.menuBar()
menuBar.addMenu(QMenu('File'))
menuBar.addMenu(QMenu('View'))
menuBar.addMenu(QMenu('Edit'))
menuBar.addMenu(QMenu('Help'))

main_window.menuBar()

loginForm.show()
loginForm.exec_()

load()


toolExitButton = QToolButton()
toolExitButton.setIcon(QtGui.QIcon("icons8-exit-96.png"))
toolExitButton.clicked.connect(exit)
toolBar.addWidget(toolExitButton)

if userHandler.user.type == 'admin':
    toolUserButton = QToolButton()
    toolUserButton.setIcon(QtGui.QIcon("icons8-user-folder-96.png"))
    toolUserButton.clicked.connect(userClick)
    toolBar.addWidget(toolUserButton)

main_window.addToolBar(toolBar)

main_window.showMaximized()
main_window.show()
app.exec_()
save()
userHandler.save()
sys.exit()


