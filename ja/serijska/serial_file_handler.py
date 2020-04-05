from data_handler import DataHandler
import json
import pickle  # koristimo pickle za serijalizaciju i deserijalizaciju objekata

class SerialFileHandler(DataHandler):
    def __init__(self, filepath, meta_filepath):
        super().__init__()
        self.filepath = filepath
        self.meta_filepath = meta_filepath
        self.data = []
        self.metadata = {}
        self.load_data()

    def load_data(self):
        #učitavanje podataka
        with open((self.filepath), 'rb') as dfile:
            self.data = pickle.load(dfile)
        #učitavanje metapodataka
        with open(self.meta_filepath) as meta_file:
            self.metadata = json.load(meta_file)

    def get_one(self, id):
        for d in self.data:  # za serijsku datoteku moramo proći linearno kroz sve slogove kada tražimo
            # ako se poklopi ključna kolona, koju dobavljamo iz metapodataka sa zadatim podatkom
            if getattr(d, (self.metadata["key"])) == id:
                return d
        return None

    def get_all(self):
        return self.data

    def insert(self, obj):
        self.data.append(obj)
        with open(self.filepath, 'wb') as f:
            pickle.dump(self.data, f)

    def delete_one(self, id):
        for d in self.data:
            if getattr(d, (self.metadata["key"])) == id:
                self.data.remove(d)
        with open(self.metadata, 'wb') as f:
            pickle.dump(self.data, f)

    def edit(self, id, new_value):
        for d in self.data:
            if getattr(d, (self.metadata["key"])) == id:
                index_elementa = self.data.index(d)
                self.data[index_elementa] = new_value
        self.save_to_file()
    
    def save_to_file(self):
        with open(self.filepath, "wb") as sfile:
            pickle.dump(self.data, sfile)

    def insert_many(self, lista):
        for i in lista:
            self.insert(i)
        self.save_to_file()
