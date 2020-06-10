from os import path
import pickle

from sekvencijalna.data_handler import DataHandler


class SequentialFileHandler(DataHandler):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.data = []
        
    def save(self):
        with open(self.model.dataSource + '.Sequential', 'wb') as data_file:
           pickle.dump(self.model.data, data_file) 
    
    def load_data(self):

        if path.exists(self.model.dataSource + '.Sequential') == False:
            return

        with open((self.model.dataSource + '.Sequential'), 'rb') as dfile:
            self.data = pickle.load(dfile)

    def get_one(self, id):
        for d in self.data:
            if getattr(d, (self.metadata["key"])) == id:
                return d
        return None

    def get_all(self):
        return self.data

    def insert(self, obj):
        self.data.append(obj)
        with open(self.filepath, 'wb') as f:
            pickle.dump(self.data, f)

    def edit(self, obj):
        keyValue = obj[self.model.metaModel.key]
        oldObj = self.get_one(keyValue)
        index = self.data.index(oldObj)
        self.data[index] = obj

    def insertList(self, list):

        for item in list:
            self.insert(item)

    def delete(self, obj):
        keyValue = obj[self.model.metaModel.key]
        oldObj = self.get_one(keyValue)
        self.data.remove(oldObj)    

    
