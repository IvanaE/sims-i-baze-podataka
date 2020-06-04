import sys
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QGridLayout, QToolBar, QToolButton, QPlainTextEdit, QAction, QListWidget, QVBoxLayout, \
    QDockWidget

from meta_model_handler import MetaModelHandler
from ui.list_dock import ListDock

metaModelHandler = MetaModelHandler()

def exit():
    app.closeAllWindows()

def load():
    metaModelHandler.load()
    listDock.init(metaModelHandler)

def save():
    metaModelHandler.save()

app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()
main_window.resize(640, 480)
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

listDock = ListDock('Meta Model list', main_window)

main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, listDock)

main_window.show()
sys.exit(app.exec_())

