from student import Student
from nastavnik import Nastavnik
import pickle
from serial_file_handler import SerialFileHandler

data = []
metaData = None

with open("serijska", 'wb') as data_file:
    pickle.dump(data, data_file) #koristimo pickle da bismo serijalizovali u binarnu datoteku

serial_file_handler = SerialFileHandler("serijska", metaData)