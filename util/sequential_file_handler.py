from util.file_handler import FileHandler
import json
import pickle


class SequentialFileHandler():
    def __init__(self, path, meta_path):
        super().__init__()
        self.meta_path = meta_path
        self.path = path
        self.metadata = {}
        self.data = []
        self.load_data()

    def load_data(self):
        with open((self.path), 'rb') as dfile:
            self.data = pickle.load(dfile)

        with open(self.meta_path) as meta:
            self.metadata = json.load(meta)

    def binary_search(self, id):
        bot = 0
        top = len(self.data)-1
        while bot <= top:
            mid = (top+bot)//2
            key = self.metadata["key"]
            if self.data[mid][key] == id:
                return mid
            elif self.data[mid][key] < id:
                bot = mid+1
            else:
                top = mid - 1
        return None

    def get_one(self,id):

        index = self.binary_search(id)
        
        return self.data[index]
            
            
    def get_all(self):
        return self.data

    def insert(self, id, obj):


        top = len(self.data)-1
        found = False
        biggest = True
        bot = 0

        while bot <= top:

            mid = (top+bot)//2
            
            key = self.metadata["key"]

            if self.data[mid][key] == id:
                found = True
                break
            elif self.data[mid][key] > id:
                self.data.insert(mid, obj)
                biggest = False
                break
            else:
                bot = mid + 1
                
        if found == False and biggest == True:
            self.data.insert(mid+1, obj)
        
        if found == False:
            with open(self.file_path, 'wb') as f:
                pickle.dump(self.data, f)
        

    def insert_many(self, objects):

        for obj in objects:
            key = obj[self.metadata["key"]]
            self.insert(key, obj)

        with open(self.file_path, 'wb') as f:
            pickle.dump(self.data, f)


    def edit(self, id, value):
        index = self.binary_search(id)
        self.data[index] = value

        with open(self.file_path, 'wb') as f:
            pickle.dump(self.data, f)

    def delete_one(self, id):

        index = self.binary_search(id)
        if index is not None:
            self.data.remove(self.data[index])
            with open(self.file_path, 'wb') as data:
                pickle.dump(self.data, data)


    def print_all(self):
        lista = self.get_all()


    def save(self):
        with open(self.file_path, 'wb') as data:
            pickle.dump(self.data, data)
