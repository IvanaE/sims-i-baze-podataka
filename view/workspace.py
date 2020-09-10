from PySide2 import QtWidgets, QtGui, QtCore
from model.model import GenericModel
import os
import json


class Workspace(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.selected = 0
        self.tab_widget = None
        self.subtable_model = None
        self.search_column = None
        self.search_value = None
        self.new_element_values = []
        self.file_handler = None
        self.new_element = {}
        self.inserting_column = None
        self.insert_data = {}
        self.matching = []
        self.number_of_tables = 0
        self.number_of_atributes = 0
        self.new_columns = []
        self.new_tables = []
        self.new_table = {}
        self.create_tab_widget()

        self.main_table = QtWidgets.QTableView(self.tab_widget)
        self.main_table.setSortingEnabled(True)
        self.main_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.main_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.main_table.setModel(None)

        self.main_table.clicked.connect(self.show_tabs)
        self.main_table.clicked.connect(self.row_selected)
        
        self.subtable = QtWidgets.QTableView(self.tab_widget)
        self.subtable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.subtable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.tab_widget.addTab(self.subtable, QtGui.QIcon("icons8-edit-file-64.png"), "Povezana Tabela")
        self.main_layout.addWidget(self.main_table)

        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    

    def show_tabs(self):
        self.tab_widget.addTab(self.subtable, QtGui.QIcon("icons8-edit-file-64.png"), "Povezana Tabela")

    def row_selected(self, index):
        self.selected = index.row()
        model = self.main_table.model()

        selected_data = model.get_element(index)
        selected_data_key_value = selected_data[self.file_handler.metadata["key"]]
        try:

            subtable_elements = []

            subtable_search_key = self.subtable_file_handler.metadata["search_key"]

            for element in self.subtable_elements:
                current = element[subtable_search_key]
                if current == selected_data_key_value:
                    subtable_elements.append(element)
            subtable_model = GenericModel(self, self.subtable_file_handler.metadata, subtable_elements)
            self.subtable.setModel(subtable_model)
        except Exception as err:
            pass


    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    def refresh_table(self, file_handler): 
        generic_model = GenericModel(self, file_handler.metadata)
        generic_model.elements = file_handler.get_all()
        self.main_table_elements = generic_model.elements
        self.file_handler = file_handler
        self.main_table.setModel(generic_model)

    def refresh_subtable(self, file_handler): 
        generic_model = GenericModel(self, file_handler.metadata)
        generic_model.elements = file_handler.get_all()
        self.subtable_elements = generic_model.elements
        self.subtable_file_handler = file_handler
        self.subtable.setModel(generic_model)


    def delete_form(self):
        self.message = QtWidgets.QMessageBox()
        self.message.setWindowTitle("Brisanje reda")

        self.message.setText("Da li stvarno zelite da obrisete red?")
        self.button = QtWidgets.QPushButton("Obrisi")
        self.message.addButton(self.button, QtWidgets.QMessageBox.ActionRole)
        self.message.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        

        self.button.clicked.connect(self.delete)
        self.message.exec()
        
    def delete(self):
        indexes = self.main_table.selectedIndexes()
        subtable_indexes = self.subtable.selectedIndexes()
        if len(indexes) == 0 and len(subtable_indexes) == 0:
            return False

        if len(indexes) > 0 and len(subtable_indexes) == 0:
            row_num = indexes[0].row()
            element = self.main_table.model().elements[row_num]
            self.file_handler.delete_one(element[self.file_handler.metadata['key']])
            self.refresh_table(self.file_handler)

        if len(subtable_indexes) > 0:
            row_num = subtable_indexes[0].row()
            element = self.subtable.model().elements[row_num]
            self.subtable_file_handler.delete_one(getattr(element, self.subtable_file_handler.metadata['key']))
            self.refresh_subtable(self.subtable_file_handler)
        
    def save(self):
        self.file_handler.save()
        self.subtable_file_handler.save()
        

    def insert(self):
        model = self.main_table.model()
        #elem_type = type(model.elements[0]) 
        #temp = elem_type()
        temp = {}
        for column in self.file_handler.metadata['columns']:
            #setattr(temp, column, self.insert_dict[column].text())
            temp[column] = self.insert_data[column].text()
        model.elements.append(temp)
        self.file_handler.save()
        self.main_table.setModel(model)
        self.refresh_table(self.file_handler)
        self.dialog.accept()

    def insert_form(self):
        self.dialog = QtWidgets.QDialog()
        self.button = QtWidgets.QPushButton("Dodaj")
        layout = QtWidgets.QVBoxLayout()
        self.new_element = {}

        for column in self.file_handler.metadata["columns"]:
            horizontal = QtWidgets.QHBoxLayout()
            label = QtWidgets.QLabel(column)
            self.value = QtWidgets.QLineEdit()
            self.insert_data[column] = self.value
            horizontal.addWidget(label)
            horizontal.addStretch(300)
            horizontal.addWidget(self.value)

            layout.addLayout(horizontal)
            self.inserting_column = column

        key = self.file_handler.metadata["key"]
        found = False
        for element in self.main_table_elements:
            current = element[key]
            if current == self.insert_data[key]:
                found = True
        layout.addWidget(self.button)
        self.dialog.setWindowTitle("Unos novog reda")
        self.dialog.setWhatsThis("Unesite vrednosti kolona")
        self.dialog.setLayout(layout)

        self.button.clicked.connect(self.insert)
        self.dialog.show()

        if found == True:
            self.dialog.reject()
            message_alert = QtWidgets.QMessageBox()
            message_alert.setWindowTitle("Greska")
            message_alert.setText("Uneli ste kljuc koji vec postoji!")

            butt = QtWidgets.QPushButton("Ponovo")
            message_alert.addButton(butt, QtWidgets.QMessageBox.ActionRole)
            message_alert.setStandardButtons(QtWidgets.QMessageBox.Cancel)
            butt.clicked.connect(self.insert_form)
            message_alert.exec()

    def search(self):
        
        self.dialog = QtWidgets.QDialog()
        self.ui_search = QtWidgets.QLineEdit()
        self.ui_search.setPlaceholderText('Unesite tekst')
        self.button = QtWidgets.QPushButton("Pretrazi")

        self.combo = QtWidgets.QComboBox(self)
        self.combo.resize(100, 50)
        for column in self.file_handler.metadata["columns"]:
            self.combo.addItem(column)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.ui_search)
        layout.addWidget(self.combo)
        layout.addWidget(self.button)

        self.dialog.setWindowTitle("Pretraga")
        self.dialog.setWhatsThis("Izaberite kolonu po kojoj zelite da pretrazujete")
        self.dialog.setLayout(layout)

        self.ui_search.textChanged.connect(self.search_changed)
        self.combo.currentTextChanged.connect(self.combo_changed)
        self.button.clicked.connect(self.find_elements)
        self.dialog.show()

    def search_changed(self, text):
        self.search_value = text
    
    def combo_changed(self, text):
        self.search_column = str(self.combo.currentText())

    def find_elements(self):
        self.matching = []
        try:
            for element in self.main_table_elements:
                attribute = element[self.search_column];
                if isinstance(attribute, int):
                    attribute = str(attribute)
                
                if self.search_value.lower() in attribute.lower():
                    self.matching.append(element)
                
            self.dialog.accept()
            self.refresh_after_search(self.file_handler)

        except Exception as err:
            pass

        
    def refresh_after_search(self, file_handler):
        generic_model = GenericModel(self, file_handler.metadata)
        if len(self.matching) == 0:
            generic_model.elements = file_handler.get_all()

        else:
            generic_model.elements = self.matching
        
        self.main_table_elements = generic_model.elements
        self.file_handler = file_handler
        self.main_table.setModel(generic_model)


    def delete_file(self, path):
        os.remove(path)

    def column_number(self):
        i, ok_pressed = QtWidgets.QInputDialog.getInt(self, "Izaberite broj atributa koji zelite","Broj atributa:", 0, 0, 100, 1)
        self.number_of_atributes = i
        
        if ok_pressed:
            self.create_file_form()

    def tables_number(self):
        i, ok_pressed = QtWidgets.QInputDialog.getInt(self, "Izaberite broj tabela koji zelite", "Broj tabela: ", 0, 0, 10000, 1)
        self.number_of_tables = i

        if ok_pressed:
            self.create_database_form()

        
    def create_file_form(self):
        number = 0

        while number < self.number_of_atributes:
            text, ok_pressed = QtWidgets.QInputDialog.getText(self, "Unos atributa","Naziv atributa:", QtWidgets.QLineEdit.Normal, "")

            if ok_pressed and text != "":
                self.new_columns.append(text)
                number+=1

        
        self.file_name, ok_pressed = QtWidgets.QInputDialog.getText(self, "Unos naziva fajla","Naziv fajla:", QtWidgets.QLineEdit.Normal, "")

        if ok_pressed and self.file_name != "":
            self.dialog = QtWidgets.QDialog()
            self.button = QtWidgets.QPushButton("Kreiraj")

            self.key_input = QtWidgets.QLabel("Izaberite kljuc: ")
            self.key = QtWidgets.QComboBox(self)
            self.key.resize(100, 50)

            for column in self.new_columns:
                self.key.addItem(column)

            self.type_input = QtWidgets.QLabel("Izaberite tip datoteke: ")
            self.type = QtWidgets.QComboBox(self)
            self.type.resize(100, 50)
            self.type.addItem("serijska")
            self.type.addItem("sekvencijalna")

            self.linked_files_input = QtWidgets.QLabel("Izaberite povezanu datoteku: ")
            self.linked = QtWidgets.QComboBox(self)
            self.linked.resize(100, 80)

            
            with open("data/files.txt", 'r') as fp:
                for line in fp:
                    self.linked.addItem(line)


            #Fali dodavanje linked_files-a i subtable_key-a

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(self.key_input)
            layout.addWidget(self.key)
            layout.addWidget(self.type_input)
            layout.addWidget(self.type)
            layout.addWidget(self.linked)
            layout.addWidget(self.button)

            self.button.clicked.connect(self.create_file)

            self.dialog.setWindowTitle("Popunjavanje metapodataka")
            self.dialog.setWhatsThis("Popunite metapodatke")
            self.dialog.setLayout(layout)

            self.dialog.show()

    def create_database_form(self):
        number = 0

        while number < self.number_of_tables:
            name, ok_pressed = QtWidgets.QInputDialog.getText(self, "Unos tabele","Naziv tabele:", QtWidgets.QLineEdit.Normal, "")

            if ok_pressed and name != "":
                key, ok_pressed = QtWidgets.QInputDialog.getText(self, "Unos kljuca","Naziv kljuca:", QtWidgets.QLineEdit.Normal, "")

                if ok_pressed and key != "":
                    
                    # self.new_table["name"] = name
                    # self.new_table["key"] = key
                    # self.new_tables.append(self.new_table)
                    self.new_tables.append({"name" : name, "key": key})
                    number+=1

       
        
        
            
        self.user, ok_pressed = QtWidgets.QInputDialog.getText(self, "Unos korisnika","User:", QtWidgets.QLineEdit.Normal, "")
        
        if ok_pressed and self.user != "":

            self.password, ok_pressed = QtWidgets.QInputDialog.getText(self, "Unos lozinke","Password:", QtWidgets.QLineEdit.Normal, "")

            if ok_pressed:

                self.host, ok_pressed = QtWidgets.QInputDialog.getText(self, "Unos host-a","Host:", QtWidgets.QLineEdit.Normal, "")

                if ok_pressed and self.host != "":

                    self.database, ok_pressed = QtWidgets.QInputDialog.getText(self, "Unos baze podataka","Naziv baze:", QtWidgets.QLineEdit.Normal, "")

                    if ok_pressed and self.database != "":
                        
                        self.create_database()

    def create_file(self):
        data_path = "data/" + self.file_name + "_data"
        f = open(data_path, "w")
        f.close()

        metadata = {}
        metadata["columns"] = self.new_columns
        metadata["key"] = self.key.currentText()
        metadata["type"] = self.type.currentText()
        metadata["linked_files"] = []
        str_len = len(self.linked.currentText())
        linked_path = self.linked.currentText()
        linked_path = linked_path[0:str_len-1]
        #metadata["linked_files"].append(self.linked.currentText())
        metadata["linked_files"].append(linked_path)

        metadata_path = "data/" + self.file_name + "_metadata.json"
        with open(metadata_path, "w") as meta_file:
            json.dump(metadata, meta_file)

        with open("data/files.txt", 'a') as fp:
            fp.write("\n" + self.file_name)
        self.dialog.accept()

    def create_database(self):
        metadata = {}
        metadata["user"] = self.user
        metadata["password"] = self.password
        metadata["host"] = self.host
        metadata["database"] = self.database
        metadata["tables"] = self.new_tables

        metadatabase_path = "database/" + self.database + "_metadata.json"

        with open(metadatabase_path, "w") as meta_file:
            json.dump(metadata, meta_file)

    def convert(self):
        elements = self.file_handler.data
        self.file_handler.delete_all()
        
        new_type = "sekvencijalna"
        

        self.file_handler.metadata["type"] = new_type
        path = self.file_handler.meta_filepath
        data_path = self.file_handler.file_path
        meta_dict = {}

        

        with open(path, "r") as meta:
            meta_dict = json.load(meta)
            meta_dict["type"] = new_type

        with open(path, "w") as meta:
            json.dump(meta_dict, meta)

        handler_parameters = []
        handler_parameters.append(new_type)
        handler_parameters.append(data_path)
        handler_parameters.append(path)
        handler_parameters.append(elements)

        return handler_parameters
            


        
        




