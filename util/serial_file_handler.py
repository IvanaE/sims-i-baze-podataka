from os import path
import pickle

from PySide2.QtCore import QDir

from util.data_handler import DataHandler

class SerialFileHandler(DataHandler):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.key = self.model.metaModel.key
        self.data = []

    def getPath(self):
        return QDir.currentPath() + '/data/' + self.model.dataSource + '.Serial'

    def save(self):
        with open(self.getPath(), 'wb') as data_file:
            pickle.dump(self.model.data, data_file)

    
    def load_data(self):

        if path.exists(self.getPath()) == False:
            return

        with open(self.getPath(), 'rb') as dfile:
            self.data = pickle.load(dfile)

    def get_one(self, id):
        for d in self.data:
            if getattr(d, (self.key)) == id:
                return d
        return None

    def get_all(self):
        return self.data

    def insert(self, obj):
        self.data.append(obj)
        with open(self.getPath(), 'wb') as f:
            pickle.dump(self.data, f)

    def edit(self, obj):
        keyValue = obj[self.key]
        oldObj = self.get_one(keyValue)
        index = self.data.index(oldObj)
        self.data[index] = obj

    def insert_many(self, list):

        for item in list:
            self.insert(item)

    def delete_one(self, obj):
        keyValue = obj[self.key]
        oldObj = self.get_one(keyValue)
        self.data.remove(oldObj)



    

        

