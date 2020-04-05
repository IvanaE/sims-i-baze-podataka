from PySide2 import QtWidgets, QtCore
from serijska.serial_file_handler import SerialFileHandler
from student import Student
from model.student_model import StudentModel

class IzmenaStudenta(StudentModel):
    def __init__(self):
        super().__init__()

    # ove metode definisu editabilni model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        student = self.get_element(index)
        serial_file_handler = SerialFileHandler("serijska/student_data", "serijska/student_metadata.json")
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole: #broj indeksa
            return False
        elif index.column() == 1 and role == QtCore.Qt.EditRole: 
            student.ime_prezime = value
            st = Student(student.broj_indeksa, value)
            serial_file_handler.edit(st.broj_indeksa, st)
            return True
        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable 


        