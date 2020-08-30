import sys
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QToolBar, QToolButton, QTabWidget, QWidget, QVBoxLayout, QMenu, QMainWindow

from view.main_window import MainWindow
from view.meta_model_handler import MetaModelHandler
from view.model_handler import ModelHandler
from view.list_dock import ListDock
from view.login_form import LoginForm
from view.model_view_widget import ModelViewWidget
from view.user_widget import UserWidget
from view.user_handler import UserHandler

userHandler = UserHandler()

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
    toolExitButton.setIcon(QtGui.QIcon("view/icons/icons8-exit-96.png"))
    toolExitButton.clicked.connect(exit)
    toolBar.addWidget(toolExitButton)

    if userHandler.user.type == 'admin':
        toolUserButton = QToolButton()
        toolUserButton.setIcon(QtGui.QIcon("view/icons/icons8-user-folder-96.png"))
        toolUserButton.clicked.connect(main_window.userClick)
        toolBar.addWidget(toolUserButton)

    main_window.addToolBar(toolBar)

    main_window.showMaximized()
    main_window.show()
    app.exec_()
    main_window.save()
    userHandler.save()
    sys.exit()
