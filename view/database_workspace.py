from PySide2 import QtWidgets, QtGui, QtCore
from model.sql_model import SqlModel
from model import *

class DbWorkspace(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.selected = 0
        self.main_layout = QtWidgets.QVBoxLayout()

        self.search_column = None
        self.search_value = None
        self.tab_widget = None
        self.new_element = {}
        self.sql_handler = None

        self.insert_data = {}
        self.inserting_column = None


        self.matching = []
        self.new_element_values = []
        self.create_tab_widget()

        self.main_table = QtWidgets.QTableView(self.tab_widget)
        self.main_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.main_table.setSortingEnabled(True)
        self.main_table.setModel(None)
        self.main_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.main_table.clicked.connect(self.row_selected)

        self.main_layout.addWidget(self.main_table)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def row_selected(self, index):
        self.selected = index.row()
        model = self.main_table.model()
        selected_data = model.get_element(index)


    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    def refresh_table(self, sql_handler): 
        sql_model = SqlModel(self, sql_handler, sql_handler.get_all())
        sql_model.elements = sql_handler.get_all()
        self.main_table_elements = sql_model.elements
        self.sql_handler = sql_handler
        self.main_table.setModel(sql_model)


    def save(self):
        self.sql_handler.save()

    def delete_form(self):
        self.message = QtWidgets.QMessageBox()
        self.message.setText("Da li zelite da obrisete red?")
        self.message.setWindowTitle("Brisanje reda")
        self.button = QtWidgets.QPushButton("Obrisi")
        self.message.addButton(self.button, QtWidgets.QMessageBox.ActionRole)
        self.message.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        

        self.button.clicked.connect(self.delete)
        self.message.exec()

    def insert_form(self):
        self.dialog = QtWidgets.QDialog()
        self.button = QtWidgets.QPushButton("Dodaj")

        layout = QtWidgets.QVBoxLayout()
        self.new_element = {}

        for column in self.sql_handler.column_names:
            h = QtWidgets.QHBoxLayout()
            label = QtWidgets.QLabel(column)
            self.value = QtWidgets.QLineEdit()
            self.insert_data[column] = self.value

            h.addWidget(label)
            h.addStretch(300)
            h.addWidget(self.value)
            
            layout.addLayout(h)
            self.inserting_column = column
        
        layout.addWidget(self.button)
        self.dialog.setWindowTitle("Unos novog reda")
        self.dialog.setWhatsThis("Unesite vrednosti kolona")
        self.dialog.setLayout(layout)

        self.button.clicked.connect(self.insert)
        self.dialog.show()

    def insert(self):
        try:
            model = self.main_table.model()
            temp_list = []
            for column in self.sql_handler.column_names:
                temp_list.append(self.insert_data[column].text())

            temp = tuple(temp_list)
            model.elements.append(temp)
            inserted = self.sql_handler.insert(temp)

            self.main_table.setModel(model)
            self.dialog.accept()
            sql_model = SqlModel(self, self.sql_handler, self.sql_handler.get_all())
            sql_model.elements = self.sql_handler.get_all()

            self.main_table_elements = sql_model.elements
            self.main_table.setModel(sql_model)
        except Exception as error:
            self.dialog.accept()
            self.message = QtWidgets.QMessageBox()
            self.message.setWindowTitle("Dodavanje reda.")
            self.message.setStandardButtons(QtWidgets.QMessageBox.Cancel)
            self.message.exec()

    def delete(self):
        indexes = self.main_table.selectedIndexes()
        if len(indexes) == 0:
            return False

        if len(indexes) > 0:
            row_num = indexes[0].row()
            element = self.main_table.model().elements[row_num]
            self.sql_handler.delete_one(element[0])
            self.refresh_table(self.sql_handler)

    def search(self):
        
        self.dialog = QtWidgets.QDialog()
        self.ui_search = QtWidgets.QLineEdit()
        self.ui_search.setPlaceholderText('Unesite tekst')
        self.button = QtWidgets.QPushButton("Pretrazi")

        self.combo = QtWidgets.QComboBox(self)
        self.combo.resize(100, 50)

        for column in self.sql_handler.column_names:
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
        self.search_column = str(self.combo.currentText())

    def combo_changed(self, text):
        self.search_column = str(self.combo.currentText())

    def find_elements(self):
        self.matching = []
        search_index = self.sql_handler.column_names.index(self.search_column)
        for element in self.main_table_elements:
            if self.search_value.lower() in element[search_index].lower():
                self.matching.append(element)

        self.dialog.accept()
        self.refresh_after_search(self.sql_handler)

    def refresh_after_search(self, sql_handler):
        sql_model = SqlModel(self, sql_handler, sql_handler.get_all())
        if len(self.matching) != 0:
            sql_model.elements = self.matching
        else:
            sql_model.elements = sql_handler.get_all()

        
        self.main_table_elements = sql_model.elements
        self.sql_handler = sql_handler
        self.main_table.setModel(sql_model)
        


        
        




