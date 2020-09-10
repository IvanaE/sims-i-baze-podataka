import json
from PySide2 import QtCore, QtWidgets, QtGui
from view.workspace import Workspace
from view.database_workspace import DbWorkspace
from view.dock import StructureDock
from view.database_dock import DbStructureDock
from view.menu import MenuBar
from view.toolbar import ToolBar
from util.serial_file_handler import SerialFileHandler
from util.sequential_file_handler import SequentialFileHandler

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init()


    def open_folder_button(self):

        path_to_folder = QtWidgets.QFileDialog.getExistingDirectory(self, self.tr("Open Folder"))
        self.structure_dock.set_root_path(path_to_folder)

    def open_new_file_button(self):

        path_to_data_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open Data File"), self.tr("~/Desktop/"), "JSON(*.JSON)")
        self.open_new_file(path_to_data_file)

    def open_new_file(self, filepath):

        meta_data_file_path = filepath.replace("_data", "_metadata.json")
        with open(meta_data_file_path) as meta:
            metadata = json.load(meta)
        file_handler = self.get_file_handler(metadata['type'], filepath, meta_data_file_path)

        linked_files = metadata['linked_files']
        if len(linked_files) != 0:
            linked_path = filepath[:filepath.rindex("/")]
            linked_data_file_path = linked_path + "/" + linked_files[0]
            linked_meta_data_file_path = linked_data_file_path.replace("_data", "_metadata.json")
            with open(linked_meta_data_file_path) as linked_meta:
                linked_meta = json.load(linked_meta)
            
            linked_file_handler = self.get_file_handler(linked_meta['type'], linked_data_file_path, linked_meta_data_file_path)
            self.workspace.refresh_subtable(linked_file_handler)

        self.workspace.refresh_table(file_handler)

    def get_file_handler(self, file_type, data_file_path, meta_data_file_path):

        if file_type == "serijska":
            return SerialFileHandler(data_file_path, meta_data_file_path)
        elif file_type == "sekvencijalna":
            return SequentialFileHandler(data_file_path, meta_data_file_path)
        else: 
            return None

    def set_workspace(self):
        self.is_db_workspace = False
        self.central_widget = QtWidgets.QTabWidget(self)
        self.workspace = Workspace(self.central_widget)
        self.central_widget.addTab(self.workspace, QtGui.QIcon("view/icons/icons8-edit-file-64.png"), "Prikaz tabele")
        self.central_widget.setTabsClosable(True)
        self.setCentralWidget(self.central_widget)

    def set_db_workspace(self):
        self.is_db_workspace = True
        self.central_widget = QtWidgets.QTabWidget(self)
        self.workspace = DbWorkspace(self.central_widget)
        self.central_widget.addTab(self.workspace, QtGui.QIcon("view/icons/icons8-edit-file-64.png"), "Prikaz tabele")
        self.central_widget.setTabsClosable(True)
        self.setCentralWidget(self.central_widget)

    def show_sql_table(self, repo):
        self.workspace.refresh_table(repo)

    def save_action(self):
        self.workspace.save()

    def insert_action(self):
        self.workspace.insert_form()

    def delete_action(self):
        self.workspace.delete_form()

    def search(self):
        self.workspace.search()

    def delete_file_form(self):
        self.message = QtWidgets.QMessageBox()
        self.message.setWindowTitle("Brisanje fajla")
        self.message.setText("Da li stvarno zelite da obrisete fajl?")
        self.button = QtWidgets.QPushButton("Obrisi")
        self.message.addButton(self.button, QtWidgets.QMessageBox.ActionRole)
        self.message.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        

        self.button.clicked.connect(self.delete_file)
        self.message.exec()
    
    def delete_file(self):
        path = self.structure_dock.file_path
        data_path = self.structure_dock.data_filepath
        self.workspace.delete_file(path)
        self.workspace.delete_file(data_path)

    def new_tables(self):
        self.workspace.tables_number()


    def new_atributes(self):
        self.workspace.column_number()


    def convert(self):
        file_handler_params = self.workspace.convert()
        handler_type = file_handler_params[0]
        handler_filepath = file_handler_params[1]
        handler_metapath = file_handler_params[2]
        handler_elements = file_handler_params[3]

        file_handler = self.get_file_handler(handler_type, handler_filepath, handler_metapath)
        file_handler.insert_many(handler_elements)

        

        
    def init(self):
        self.is_db_workspace = False
        self.resize(1000, 750)
        self.setWindowTitle("Editor podataka")
        self.setWindowIcon(QtGui.QIcon("view/icons/icons8-edit-file-64.png"))

        self.structure_dock = StructureDock("File browser", self)
        self.structure_dock.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.db_structure_dock = DbStructureDock("Database browser", self)
        self.menu_bar = MenuBar(self)
        self.menu_bar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tool_bar = ToolBar(self)
        self.tool_bar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.central_widget = QtWidgets.QTabWidget(self)
        self.workspace = Workspace(self.central_widget)
        self.status_bar = QtWidgets.QStatusBar(self)
        self.status_bar.showMessage("Status bar je prikazan!")
        self.central_widget.addTab(self.workspace, QtGui.QIcon("view/icons/icons8-edit-file-64.png"), "Prikaz tabele")
        self.central_widget.setTabsClosable(True)

        self.setMenuBar(self.menu_bar)
        self.addToolBar(self.tool_bar)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.structure_dock)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.db_structure_dock)
        self.setCentralWidget(self.central_widget)
        self.setStatusBar(self.status_bar)



