from knjiga import Knjiga
from clan import Clan
import pickle
from sequential_file_handler import SequentialFileHandler

data = []
data.append(Knjiga("Prva knjiga", 1, "Marko Markovic", "Putokaz", "432", 1952, None))
data.append(Knjiga("Druga knjiga", 2, "Marko Markovic", "Istorija", "432", 1992, None))
data.append(Knjiga("Treca knjiga", 3, "Pera Peric", "Biografija", "45", 2007, None))
data.append(Knjiga("Cetvrta knjiga", 4, "Marko Markovic", "Autobiografija", "645", 1921, None))
data.append(Knjiga("Peta knjiga", 5, "Stanko Markovic", "Horor", "231", 1953, None))
data.append(Knjiga("Sesta knjiga", 6, "Marko Milovanovic", "Putokaz", "553", 1952, None))

n_data = []
n_data.append(Clan("Pera", "Peric", 1, 1994))
n_data.append(Clan("Milica", "Peric", 2, 2005))
n_data.append(Clan("Pera", "Nenadovic", 3, 1977))
n_data.append(Clan("Nenad", "Stankovic", 4, 1994))
n_data.append(Clan("Branko", "Stevanovic", 5, 1988))
n_data.append(Clan("Stevan", "Brankovic", 6, 1994))




with open("knjiga_data", 'wb') as data_file:
    pickle.dump(data, data_file) #koristimo pickle da bismo serijalizovali u binarnu datoteku

with open("clan_data", 'wb') as data_file:
    pickle.dump(n_data, data_file)

sequential_file_handler = SequentialFileHandler("knjiga_data", "knjiga_metadata.json") #pri instanciranju samo prosledimo putanje do datoteka sa podacima i sa metapodacima
#ovo bi se moglo smanjiti na jedan argument za konstrukciju filehandler-a, ukoliko uvedemo neku konvenciju za imenovanje datoteka

print(sequential_file_handler.get_one(3).naslov)

sequential_file_handler.insert(Knjiga("Dvadeseta knjiga", 20, "Marko Milovanovic", "Putokaz", "553", 1952, None))

print(sequential_file_handler.get_one(20))

#clan_file_handler = SequentialFileHandler("clan_data", "clan_metadata.json")

#print(clan_file_handler.get_one("14").ime)


    
