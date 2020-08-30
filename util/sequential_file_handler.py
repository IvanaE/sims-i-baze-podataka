from os import path
import pickle

from PySide2.QtCore import QDir

from util.data_handler import DataHandler

class SequentialFileHandler(DataHandler):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.data = []
        self.key = self.model.metaModel.key

    def getPath(self):
        return QDir.currentPath() + '/data/' + self.model.dataSource + '.Seq'

    def get_all(self):
        return self.data

    def save(self):
        with open(self.getPath(), 'wb') as data_file:
            pickle.dump(self.model.data, data_file)

    def load_data(self):

        if path.exists(self.getPath()) == False:
            return

        with open(self.getPath(), 'rb') as dfile:
            self.data = pickle.load(dfile)

    def binary_search(self, id, start, end):

        while start <= end:

            mid = start + (end - start) // 2

            # Check if x is present at mid
            if getattr(self.data[mid], (self.key)) == id:
                return mid

                # If x is greater, ignore left half
            elif getattr(self.data[mid], (self.key)) < id:
                start = mid + 1

            # If x is smaller, ignore right half
            else:
                end = mid - 1

        return None  # nismo pronasli

    def get_one(self, id):
        index = self.binary_search(id, 0, (len(self.data)))

        if index == None:
            return None

        return self.data[index]

    def find_location_for_insert(self, obj):

        for i in range(len(self.data)):
            if getattr(self.data[i], (self.key)) > getattr(obj, (self.key)):
                return i
        return None

    def insert(self, obj):

        index = self.binary_search(obj[self.key], 0, (len(self.data)))

        if index != None:
            return

        location = self.find_location_for_insert(obj)
        if (location == None):
            self.data.append(obj)
        else:
            self.data.insert(location - 1, obj)

    def edit(self, obj):
        index = self.binary_search(id, 0, (len(self.data)))

        if index == None:
            return None

        self.data[index] = obj

    def delete_one(self, obj):
        keyValue = obj[self.key]
        oldObj = self.get_one(keyValue)
        self.data.remove(oldObj)

    def insert_many(self, list):

        for item in list:
            self.insert(item)