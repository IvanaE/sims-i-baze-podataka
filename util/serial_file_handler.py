from util.file_handler import FileHandler
import json
import pickle


class SerialFileHandler():
    def __init__(self, path, meta_path):
        super().__init__()
        self.meta_path = meta_path
        self.path = path
        self.data = []
        self.metadata = {}
        self.load_data()


    def load_data(self):
        try:
            with open((self.path), 'rb') as dfile:
                self.data = pickle.load(dfile)

        except EOFError as e:
            self.data = []

        with open(self.meta_path) as meta:
            self.metadata = json.load(meta)

    def get_one(self,id):
        for i in self.data:
            if getattr(i, (self.metadata["key"])) == id:
                return i

        return None
            
    def get_all(self):

        return self.data

    def insert(self, obj):
        self.data.append(obj)
        with open(self.file_path, 'wb') as f:
            pickle.dump(self.data, f)

    def insert_many(self, objects):
        for obj in objects:
            self.data.append(obj)

        with open(self.file_path, 'wb') as f:
            pickle.dump(self.data, f)


    def edit(self, id, value):
        found = False
        index = 0
        for i in self.data:
            if getattr(i, (self.metadata["key"])) == id:
                
                self.data[index] = value
                found = True
            else:
                index += 1


        else:
            with open(self.file_path, 'wb') as data_file:
                pickle.dump(self.data, data_file)


    def delete_one(self, id):

        for i in self.data:
            if i[self.metadata["key"]] == id:
                self.data.remove(i)

        with open(self.file_path, 'wb') as data:
            pickle.dump(self.data, data)

    def delete_all(self):
        for i in self.data:
            self.data.remove(i)

        with open(self.file_path, 'wb') as data:
            pickle.dump(self.data, data)


    def print_all(self):
        lista = self.get_all()


    def save(self):
        with open(self.file_path, 'wb') as data:
                pickle.dump(self.data, data)
    
