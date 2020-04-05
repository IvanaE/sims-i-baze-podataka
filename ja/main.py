import sys
from PySide2 import QtWidgets, QtGui, QtCore
from workspace_widget import WorkspaceWidget
from dodaj_studenta_dijalog import InputDialog

def porkeni_dijalog():
    dijalog = InputDialog()
    dijalog.show()                                  #treba pozvati dijalog
    
def prikazi_workspace():
    central_widget = QtWidgets.QTabWidget(main_window)
    workspace = WorkspaceWidget(central_widget)
    central_widget.addTab(workspace, QtGui.QIcon("icons8-edit-file-64.png"), "Prikaz tabele")
    central_widget.setTabsClosable(True)
    main_window.setCentralWidget(central_widget)

if __name__ == "__main__":

    def file_clicked(index):
        print(file_system_model.filePath(index))

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.resize(640, 480)
    main_window.setWindowTitle("Editor generickih podataka")
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
    #========================================================== dodajem akcije u tooolbar

   
    ###
    prikaz_studenta = QtWidgets.QAction(tool_bar)
    prikaz_studenta.setText('Prikazi')
    
    prikaz_studenta.triggered.connect(prikazi_workspace)
    tool_bar.addAction(prikaz_studenta)

    dodaj_studenta = QtWidgets.QAction(tool_bar)
    dodaj_studenta.setText('Dodaj')
    dodaj_studenta.triggered.connect(porkeni_dijalog)
    tool_bar.addAction(dodaj_studenta)
    
    structure_dock = QtWidgets.QDockWidget("Structure dock", main_window)

    file_system_model = QtWidgets.QFileSystemModel()
    file_system_model.setRootPath(QtCore.QDir.currentPath())

    tree_view = QtWidgets.QTreeView()
    tree_view.setModel(file_system_model)

    tree_view.setRootIndex(file_system_model.index(QtCore.QDir.currentPath()))

    structure_dock.setWidget(tree_view)

    toggle_structure_dock_action = structure_dock.toggleViewAction()
    view_menu.addAction(toggle_structure_dock_action)

    tree_view.clicked.connect(file_clicked)

    #============================================================================
    #hocu da ucitam serijsku datoteku
    otvori_serijsku_datoteku = file_menu.addAction("Otvori serijsku datoteku")

    status_bar = QtWidgets.QStatusBar(main_window)
    status_bar.showMessage("Status bar je prikazan!")

    main_window.setMenuBar(menu_bar)
    main_window.addToolBar(tool_bar)
    main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, structure_dock)
    
    main_window.setStatusBar(status_bar)
    main_window.show()
    # menu_bar.setParent(main_window)
    sys.exit(app.exec_())
