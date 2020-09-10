from PySide2 import QtWidgets, QtGui, QtCore
from view.dock import StructureDock

class ToolBar(QtWidgets.QToolBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_window = parent
        

        new_file = QtWidgets.QAction(QtGui.QIcon("view/icons/create_file.png"), "Create new file", self, shortcut = None, statusTip = "Create new file", triggered = self.main_window.new_atributes)
        new_database = QtWidgets.QAction(QtGui.QIcon("view/icons/database.jpg"), "Create new database", self, shortcut = None, statusTip = "Create new database", triggered = self.main_window.new_tables)
        delete_file = QtWidgets.QAction(QtGui.QIcon("view/icons/delete_file.jpg"),"Delete file", self,
                shortcut=None,
                statusTip="Delete row", triggered=self.main_window.delete_file_form)
        save_action = QtWidgets.QAction(QtGui.QIcon("view/icons/save.png"),"Save changes", self,
                shortcut=None,
                statusTip="Save changes", triggered=self.main_window.save_action)
        insert_action = QtWidgets.QAction(QtGui.QIcon("view/icons/insert.png"),"Insert row", self,
                shortcut=None,
                statusTip="Insert row", triggered=self.main_window.insert_action)
        delete_action = QtWidgets.QAction(QtGui.QIcon("view/icons/delete.jpg"),"Delete row", self,
                shortcut=None,
                statusTip="Delete row", triggered=self.main_window.delete_action)
        search_action = QtWidgets.QAction(QtGui.QIcon("view/icons/search.png"), "Search", self, shortcut = None, statusTip = "Search", triggered = self.main_window.search)

        self.addAction(new_file)
        self.addAction(new_database)
        self.addAction(save_action)

        self.addAction(delete_file)
        self.addAction(insert_action)
        self.addAction(delete_action)
        self.addAction(search_action)
