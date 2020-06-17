import sys
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QGridLayout, QToolBar, QToolButton, QPlainTextEdit, QAction, QListWidget, QVBoxLayout, \
    QDockWidget, QTabWidget, QMenu, QMenuBar

from meta_model_handler import MetaModelHandler
from model_handler import ModelHandler
from ui.list_dock import ListDock
from ui.login_form import LoginForm
from ui.model_view_widget import ModelViewWidget

metaModelHandler = MetaModelHandler()
modelHandler = ModelHandler(metaModelHandler)

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
    modelWidget = ModelViewWidget(central_widget, model)
    central_widget.addTab(modelWidget, QtGui.QIcon("icons8-edit-file-64.png"), model.name + ' - Model')

def delete_tab(index):
    central_widget.removeTab(index)

def login():
    loginForm.close()


app = QtWidgets.QApplication(sys.argv)
loginForm = LoginForm(login)
main_window = QtWidgets.QMainWindow()
main_window.resize(840, 680)
main_window.setWindowTitle("InfHandler")
main_window.setWindowIcon(QtGui.QIcon("icons8-edit-file-64.png"))
metaModelHandler.load()
toolBar = QToolBar()


toolLoadButton = QToolButton()
toolLoadButton.setText('Load')
toolLoadButton.clicked.connect(load)
toolBar.addWidget(toolLoadButton)

toolSaveButton = QToolButton()
toolSaveButton.setText('Save')
toolSaveButton.clicked.connect(save)
toolBar.addWidget(toolSaveButton)

toolExitButton = QToolButton()
toolExitButton.setText('Exit')
toolExitButton.clicked.connect(exit)
toolBar.addWidget(toolExitButton)
main_window.addToolBar(toolBar)

#metamodel list

listDock = ListDock('Meta Model list', main_window, handleModelClick)
main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, listDock)

#central widget

central_widget = QTabWidget(main_window)
central_widget.setTabsClosable(True)
central_widget.tabCloseRequested.connect(delete_tab)
main_window.showMaximized()
main_window.setCentralWidget(central_widget)

#loginForm.show()
#loginForm.exec_()

load()

main_window.show()
app.exec_()
save()
sys.exit()


