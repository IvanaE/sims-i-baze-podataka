from knjiga import Knjiga
from clan import Clan
import pickle
from sequential_file_handler import SequentialFileHandler

data = []
metaModel = None

with open("sekvencijalna", 'wb') as data_file:
    pickle.dump(data, data_file) #koristimo pickle da bismo serijalizovali u binarnu datoteku

sequential_file_handler = SequentialFileHandler("sekvencijalna", metaModel) #pri instanciranju samo prosledimo putanje do datoteka sa podacima i sa metapodacima
#ovo bi se moglo smanjiti na jedan argument za konstrukciju filehandler-a, ukoliko uvedemo neku konvenciju za imenovanje datoteka

