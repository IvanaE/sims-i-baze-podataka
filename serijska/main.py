from student import Student
from nastavnik import Nastavnik
import pickle
from serial_file_handler import SerialFileHandler

data = []
data.append(Student("2018/123", "Marko", "Markovic", "1.1.2001", []))
data.append(Student("2018/456", "Pera", "Peric", "1.1.2001", []))
data.append(Student("2018/789", "Stanko", "Stankovic", "1.1.2001", []))


n_data = []
n_data.append(Nastavnik("12", "Darko", "Darkovic", "1.1.2002", "P"))
n_data.append(Nastavnik("14", "Petar", "Petrovic", "1.1.2002", "A"))


with open("student_data", 'wb') as data_file:
    pickle.dump(data, data_file) #koristimo pickle da bismo serijalizovali u binarnu datoteku

with open("nastavnik_data", 'wb') as data_file:
    pickle.dump(n_data, data_file)

serial_file_handler = SerialFileHandler("student_data", "student_metadata.json") #pri instanciranju samo prosledimo putanje do datoteka sa podacima i sa metapodacima
#ovo bi se moglo smanjiti na jedan argument za konstrukciju filehandler-a, ukoliko uvedemo neku konvenciju za imenovanje datoteka

print(serial_file_handler.get_one("2018/123").ime)

serial_file_handler.insert(Student("2018/124", "Milan", "Milanovic", "1.1.2001", ["1", "15"]))

print(serial_file_handler.get_one("2018/124").predmeti)

nastavnik_file_handler = SerialFileHandler("nastavnik_data", "nastavnik_metadata.json")

print(nastavnik_file_handler.get_one("14").ime)


    
