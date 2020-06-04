import sys
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QGridLayout, QToolBar, QToolButton, QPlainTextEdit, QAction, QListWidget, QVBoxLayout, \
    QDockWidget, QTabWidget

from meta_model_handler import MetaModelHandler
from ui.list_dock import ListDock
from ui.meta_model_view_widget import MetaModelViewWidget

metaModelHandler = MetaModelHandler()

def exit():
    app.closeAllWindows()

def load():
    metaModelHandler.load()
    listDock.init(metaModelHandler, [])

def save():
    metaModelHandler.save()

def handleMetamodelClick(metaModel):
    metaModelWidget = MetaModelViewWidget(central_widget, metaModel)
    central_widget.addTab(metaModelWidget, QtGui.QIcon("icons8-edit-file-64.png"), metaModel.name + ' - Meta Model')

def delete_tab(index):
    central_widget.removeTab(index)

app = QtWidgets.QApplication(sys.argv)
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

listDock = ListDock('Meta Model list', main_window, handleMetamodelClick)
main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, listDock)

#central widget

central_widget = QTabWidget(main_window)
central_widget.setTabsClosable(True)
central_widget.tabCloseRequested.connect(delete_tab)
main_window.setCentralWidget(central_widget)

main_window.show()
sys.exit(app.exec_())

