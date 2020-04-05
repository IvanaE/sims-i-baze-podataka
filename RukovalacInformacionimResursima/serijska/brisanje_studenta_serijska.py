from PySide2 import QtWidgets, QtCore
from serijska.serial_file_handler import SerialFileHandler
import pickle
from student import Student

class BrisanjeStudenta(QtWidgets.QDialog):


    def __init__(self):
        
        super().__init__()
        formLayout = QtWidgets.QFormLayout()
    

        formLayout.addRow(QtWidgets.QLabel("Broj indeksa: "), self.input1)
        formLayout.addRow(QtWidgets.QLabel("Ime i prezime: "), self.input2)
        
        btnOk = QtWidgets.QPushButton("OBRISI")
        btnOk.clicked.connect(self.okAction)
        btnCancel = QtWidgets.QPushButton("ODUSTANI")
        #salje false nakon exec_()
        btnCancel.clicked.connect(self.reject)
        
        group = QtWidgets.QDialogButtonBox()
        group.addButton(btnOk, QtWidgets.QDialogButtonBox.AcceptRole)
        group.addButton(btnCancel, QtWidgets.QDialogButtonBox.RejectRole)
        
        formLayout.addRow(group)
        
        self.setLayout(formLayout)
        
    def okAction(self):
        if self.input1.text() == "" or self.input2.text() == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Morate popuniti sva polja.")
            msgBox.exec()
        else:   
            serial_file_handler = SerialFileHandler("serijska/student_data", "serijska/student_metadata.json")
            stud = (Student( self.input1.text(), self.input2.text(), [], []))
            serial_file_handler.insert(stud)
        #salje true nakon exec_()
        self.accept()
        