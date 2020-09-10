from PySide2 import QtWidgets, QtGui, QtCore

from database.repository import GenericRepository
import json

class DbStructureDock(QtWidgets.QDockWidget):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.main = parent
        self.model = QtWidgets.QFileSystemModel()
        self.database_metadata = None

        self.path = None

        skip = ["*.json"]
        self.tree = QtWidgets.QTreeView()
        self.tree.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    
        self.model.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllEntries)
        self.model.setNameFilterDisables(False)
        self.model.setNameFilters(skip)
        self.model.setRootPath(QtCore.QDir.currentPath())

        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QtCore.QDir.currentPath() + "/database"))

        self.setWidget(self.tree)
        self.tree.clicked.connect(self.standard_item_model)


    def set_items(self, tree):
        parent =  QtGui.QStandardItem('SqlDatabase') 

        with open(self.path, "rb") as metadata:
            self.database_metadata = json.load(metadata)

        for table in self.database_metadata["tables"]:
            table_name = table["name"]
            row = QtGui.QStandardItem(table_name)
            parent.appendRow(row)

        button_row = QtGui.QStandardItem("Vrati nazad")
        parent.appendRow(button_row)
        tree.appendRow(parent)

    def standard_item_model(self, index):
        self.path = self.model.filePath(index)
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Sql Database'])
        self.tree.setModel(self.model)
        self.set_items(self.model)
        self.tree.clicked.connect(self.item_clicked)


    def item_clicked(self, index):
        try:
            repo = self.get_repository(index.data())

            if repo is None:
                self.show_metadata()

            if(self.main.is_db_workspace != True):
                self.main.set_db_workspace()

            self.main.show_sql_table(repo)
        except Exception as e:
            pass

    def show_metadata(self):
        self.model = QtWidgets.QFileSystemModel()
        skip = ["*.json"]
        self.tree = QtWidgets.QTreeView()
        self.tree.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    
        self.model.setRootPath(QtCore.QDir.currentPath())
        self.model.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllEntries)
        self.model.setNameFilters(skip)
        self.model.setNameFilterDisables(False)

        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QtCore.QDir.currentPath() + "/database"))

        self.setWidget(self.tree)
        self.tree.clicked.connect(self.standard_item_model)


    def get_repository(self, repo_name):
        for table in self.database_metadata["tables"]:
            if repo_name == table["name"]:

                return GenericRepository(table["name"], table["key"], self.path)
            
                
        

    
