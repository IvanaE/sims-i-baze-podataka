
import pickle
from serial_file_handler import SerialFileHandler

data = []
metaData = None

with open("serijska", 'wb') as data_file:
    pickle.dump(data, data_file)

serial_file_handler = SerialFileHandler("serijska", metaData)