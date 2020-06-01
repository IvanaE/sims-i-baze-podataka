from data_handler import DataHandler
import json
import pickle

class SequentialFileHandler(DataHandler):
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
            self.data = pickle.load(dfile) #koristimo pickle za deserijalizaciju podataka

        #učitavanje metapodataka
        with open(self.meta_filepath) as meta_file:
            self.metadata = json.load(meta_file)  

    def binary_search(self, id, start, end):
        
        while start <= end: 
  
            mid = start + (end - start)//2; 
          
        # Check if x is present at mid 
            if getattr(self.data[mid], (self.metadata["key"])) == id: 
                return mid 
  
        # If x is greater, ignore left half 
            elif getattr(self.data[mid], (self.metadata["key"])) < id: 
                start = mid + 1
  
        # If x is smaller, ignore right half 
            else:
                end = mid - 1

        return None #nismo pronasli


    def get_one(self, id):
        #TODO sta ako vrati None?
        return self.data[self.binary_search(id, 0, (len(self.data)))]

    def find_location_for_insert(self, obj):
        #TODO alternativni način dobavljanja? (binarna pretraga)
        for i in range(len(self.data)):
            if getattr(self.data[i], (self.metadata["key"])) > getattr(obj, (self.metadata["key"])):
                return i
        return None

    def insert(self, obj):
        #TODO proveriti da li podatak postoji vec u datoteci
        #trazimo indeks koji je poslednji manji od naseg
        location = self.find_location_for_insert(obj)
        if(location == None):
            self.data.append(obj)
        else:
            self.data.insert(location-1, obj)

        
        

    
