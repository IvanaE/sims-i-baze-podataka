from data_handler import DataHandler
import json
import pickle #koristimo pickle za serijalizaciju i deserijalizaciju objekata

class SerialFileHandler(DataHandler):
    def __init__(self, filepath, metaModel):
        super().__init__()
        self.filepath = filepath
        self.metaModel = metaModel
        self.data = []
        self.metadata = {}
        self.load_data()
    
    def load_data(self):
        #učitavanje podataka
        with open((self.filepath), 'rb') as dfile:
            self.data = pickle.load(dfile) #koristimo pickle za deserijalizaciju podataka

        #učitavanje metapodataka
        with open(self.meta_filepath) as meta_file:
            self.metadata = json.load(meta_file)  

    def get_one(self, id):
        for d in self.data: #za serijsku datoteku moramo proći linearno kroz sve slogove kada tražimo
            if getattr(d, (self.metadata["key"])) == id: #ako se poklopi ključna kolona, koju dobavljamo iz metapodataka sa zadatim podatkom
                return d
        return None

    def get_all(self):
        return self.data()

    def insert(self, obj):
        self.data.append(obj)
        with open(self.filepath, 'wb') as f:
            pickle.dump(self.data, f)

    #TODO implementirati edit, delete, insert_many (za ubacivanje više objekata odjednom, preko neke kolekcije)
    #TODO kreirati funkciju za ispis svih studenata, sa predmetima i nastavnicima, kao što piše u zadatku
    # ta funkcija ne treba da bude unutar ove klase, nego da se koriste file handleri za sva 3 entiteta da bi se ovo postiglo
    # u odvojenoj skripti

    



    

        

