from PySide2 import QtWidgets, QtGui, QtCore
from student import Student
from polozeni_predmet import PolozeniPredmet
from nepolozeni_predmet import NepolozeniPredmet
from model.student_model import StudentModel
from model.polozeni_predmet_model import PolozeniPredmetModel
from model.nepolozeni_predmet_model import NepolozeniPredmetModel
from serijska.serial_file_handler import SerialFileHandler
import pickle
from dodaj_studenta_dijalog import InputDialog
from serijska.izmena_studenta_serijska import IzmenaStudenta
from serijska.brisanje_studenta_serijska import BrisanjeStudenta

class WorkspaceWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()

        self.student_model = self.ucitavanje_studenata()
        
        self.student_model = self.ucitavanje_studenata()
        self.dodaj_studenta_dijalog = InputDialog()

        # self.dodaj_studenta_dijalog.show()
        self.tab_widget.addTab(self.dodaj_studenta_dijalog, "Dodaj studenta")
        #self.students = self.dodaj_studenta_dijalog.result()
        
        # tabele kao atributi a ne kao lokalne promenljive
        self.table1 = QtWidgets.QTableView(self.tab_widget)
        self.table1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table1.setModel(self.student_model)
        #self.table1.clicked.connect(self.obrisi_studenta)

        
        self.subtable1 = QtWidgets.QTableView(self.tab_widget)
        self.subtable1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.subtable1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table1.clicked.connect(self.student_selected)

        self.subtable2 = QtWidgets.QTableView(self.tab_widget)

        self.tab_widget.addTab(self.subtable1, QtGui.QIcon("icons8-edit-file-64.png"), "Polozeni predmeti")
        self.tab_widget.addTab(self.subtable2, QtGui.QIcon("icons8-edit-file-64.png"), "Nepolozeni predmeti")
        
        self.main_layout.addWidget(self.table1)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def student_selected(self, index):
        model = self.table1.model()
        student = model.get_element(index)

        polozeni_predmeti_model = self.create_polozeni_predmeti_model(student)
        self.subtable1.setModel(polozeni_predmeti_model)

        nepolozeni_predmeti_model = self.create_nepolozeni_predmeti_model(student)
        self.subtable2.setModel(nepolozeni_predmeti_model)

        self.tab_widget.addTab(self.subtable1, QtGui.QIcon("icons8-edit-file-64.png"), "Polozeni predmeti")
        self.tab_widget.addTab(self.subtable2, QtGui.QIcon("icons8-edit-file-64.png"), "Nepolozeni predmeti")
        
    def create_table(self, rows, columns):
        table_widget = QtWidgets.QTableWidget(rows, columns, self)

        for i in range(rows):
            for j in range(columns):
                table_widget.setItem(i, j, QtWidgets.QTableWidgetItem("Celija " + str(i) + str(j)))
        labels = []
        for i in range(columns):
            labels.append("Kolona" + str(i))
        table_widget.setHorizontalHeaderLabels(labels)
        return table_widget   

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    def create_polozeni_predmeti_model(self, student):
        """
        Za odabranog studenta pravi model za tabelu polozenih predmeta
        """
        polozeni_predmeti_model = PolozeniPredmetModel()
        polozeni_predmeti_model.polozeni_predmeti = student.polozeni_predmeti

        return polozeni_predmeti_model
        

    def create_nepolozeni_predmeti_model(self, student):
        """
        Za odabranog studenta pravi model za tabelu nepolozenih predmeta
        """
        nepolozeni_predmeti_model = NepolozeniPredmetModel()
        nepolozeni_predmeti_model.nepolozeni_predmeti = student.nepolozeni_predmeti

        return nepolozeni_predmeti_model
        

    def ucitavanje_studenata(self):
        #ovo mram da pozvem bar jednom da bih ubacila nesot u tu  binarnu datoteku   
        """
        pp_data = []
        pp_data.append(PolozeniPredmet( "56", "OOP", "", 7))
        pp_data.append(PolozeniPredmet( "23", "BP", "", 6))
        pp_data.append(PolozeniPredmet( "13", "SIMS", "", 9))
        with open("serijska/predmet_data", 'wb') as data_file:
            pickle.dump(pp_data, data_file) #koristimo pickle da bismo serijalizovali u binarnu datoteku

        np_data = []
        np_data.append(NepolozeniPredmet( "5", "Diskretna matematika", "", 5))
        np_data.append(NepolozeniPredmet( "3", "OOP", "", 1))
        np_data.append(NepolozeniPredmet( "1", "Engleski", "", 3))
        with open("serijska/predmet_data", 'wb') as data_file:
            pickle.dump(np_data, data_file) #koristimo pickle da bismo serijalizovali u binarnu datoteku

        data = []
        data.append(Student( "2018/456", "Mira Tot", pp_data, np_data))
        data.append(Student( "2018/123", "Ilija Ilic", [], []))
        data.append(Student( "2018/123", "Sanja Savic", [], []))
        with open("serijska/student_data", 'wb') as data_file:
            pickle.dump(data, data_file) #koristimo pickle da bismo serijalizovali u binarnu datoteku
        """
        student_model = IzmenaStudenta()
        
        #ovo je zapravo deo fje koji nam treba, koji ucitava iz serijsk datoteke i kreira student mode
        try:
            serial_file_handler = SerialFileHandler("serijska/student_data", "serijska/student_metadata.json")
            student_model.students = serial_file_handler.get_all()
        except(Exception):
            student_model.students = []
        return student_model
    
    def obrisi_studenta(self):
        obrisi_studenta = BrisanjeStudenta()
        self.tab_widget.addTab(obrisi_studenta, "Obrisi studenta")