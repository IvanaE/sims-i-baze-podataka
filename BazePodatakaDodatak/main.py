from student import Student
from nastavnik import Nastavnik
from predmet import Predmet
import pickle 
from serial_file_handler import SerialFileHandler

data = []
data.append(Student("2018/956", "Ivana", "Ivanovic", "20.02.2000", []))
data.append(Student("2018/987", "Ilija", "Ilic", "01.01.1999", []))
data.append(Student("2018/912", "Mira", "Tot", "14.05.2002", []))

n_data = []
n_data.append(Nastavnik("8", "Petar", "Peric", "20.02.2000", "P"))
n_data.append(Nastavnik("2", "Ivona", "Jovic", "01.01.1999", "A"))
n_data.append(Nastavnik("12", "Sanja", "Savic", "14.05.2002", "P"))

p_data = []
p_data.append(Predmet("323", "OOP", "3", "SII", "2", []))
p_data.append(Predmet("123", "Engleski", "2", "IT", "4", []))

with open("student_data", 'wb') as data_file:
    pickle.dump(data, data_file)

with open("nastavnik_data", 'wb') as data_file:
    pickle.dump(n_data, data_file)

with open("predmet_data", 'wb') as data_file:
    pickle.dump(p_data, data_file)

serial_file_handler = SerialFileHandler("student_data", "student_metadata.json")
print(serial_file_handler.get_one("2018/987").ime)

serial_file_handler.insert(Student("2018/912", "Mira", "Tot", "20.02.2000", ["123","465"]))
print (serial_file_handler.get_one("2018/912").predmeti)

nastavnik_file_handler = SerialFileHandler("nastavnik_data", "nastavnik_metadata.json")
print(nastavnik_file_handler.get_one("12").ime)