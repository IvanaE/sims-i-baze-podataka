import sys
from PySide2 import QtWidgets, QtGui, QtCore

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.resize(640, 480)
    main_window.setWindowTitle("InfHandler")
    main_window.setWindowIcon(QtGui.QIcon("icons8-edit-file-64.png"))

    menu_bar = QtWidgets.QMenuBar(main_window)
    file_menu = QtWidgets.QMenu("File", menu_bar)
    edit_menu = QtWidgets.QMenu("Edit", menu_bar)
    view_menu = QtWidgets.QMenu("View", menu_bar)
    help_menu = QtWidgets.QMenu("Help", menu_bar)

    menu_bar.addMenu(file_menu)
    menu_bar.addMenu(edit_menu)
    menu_bar.addMenu(view_menu)
    menu_bar.addMenu(help_menu)

    tool_bar = QtWidgets.QToolBar(main_window)

    central_widget = QtWidgets.QTabWidget(main_window)


    main_window.setMenuBar(menu_bar)
    main_window.addToolBar(tool_bar)
    main_window.setCentralWidget(central_widget)
    main_window.show()
    # menu_bar.setParent(main_window)
    sys.exit(app.exec_())

