from data_handler import DataHandler
import json
import pickle

class SerialFileHandler(DataHandler):
    def __init__(self, filepath, meta_filepath):
        super().__init__()
        self.filepath = filepath
        self.meta_filepath = meta_filepath
        self.data = []
        self.metadata = {}
        self.load_data()

    def load_data(self):
        with open((self.filepath), 'rb') as dfile:
            self.data = pickle.load(dfile)

        with open(self.meta_filepath) as meta_file:
            self.metadata = json.load(meta_file)

    def get_one(self, id):
        for d in self.data:
            if getattr(d, (self.metadata["key"])) == id:
                return d
        return None
    def get_all(self):
        return self.data()
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