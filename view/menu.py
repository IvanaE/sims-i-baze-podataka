from PySide2 import QtWidgets, QtGui
from view.dock import StructureDock

class MenuBar(QtWidgets.QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_window = parent

        file_menu = QtWidgets.QMenu("&File", self)
        open_file_action = QtWidgets.QAction("&Open File", self,
                shortcut=QtGui.QKeySequence.Open,
                statusTip="Open", triggered=self.main_window.open_new_file_button)

        open_folder_action = QtWidgets.QAction("&Open Folder", self,
                shortcut=None,
                statusTip="Open", triggered=self.main_window.open_folder_button)

        save_action = QtWidgets.QAction("&Save", self,
                shortcut=QtGui.QKeySequence.Save,
                statusTip="Open", triggered=self.main_window.save_action)

        insert_action = QtWidgets.QAction("&Insert", self,
                shortcut=None,
                statusTip="Open", triggered=self.main_window.insert_action)

        delete_action = QtWidgets.QAction("&Delete", self,
                shortcut=None,
                statusTip="Open", triggered=self.main_window.delete_action)
        
        convert_action = QtWidgets.QAction("&Convert", self, 
                shortcut = None, 
                statusTip = "Convert to sequential", triggered = self.main_window.convert)

        file_menu.addAction(open_file_action)
        file_menu.addAction(open_folder_action)
        file_menu.addAction(save_action)
        file_menu.addAction(convert_action)

        edit_menu = QtWidgets.QMenu("Edit", self)
        edit_menu.addAction(insert_action)
        edit_menu.addAction(delete_action)

        
        view_menu = QtWidgets.QMenu("View", self)
        toggle_structure_dock_action = self.main_window.structure_dock.toggleViewAction()
        toggle_db_structure_dock_action = self.main_window.db_structure_dock.toggleViewAction()
        view_menu.addAction(toggle_structure_dock_action)
        view_menu.addAction(toggle_db_structure_dock_action)
        
        help_menu = QtWidgets.QMenu("Help", self)

        self.addMenu(file_menu)
        self.addMenu(edit_menu)
        self.addMenu(view_menu)
        self.addMenu(help_menu)