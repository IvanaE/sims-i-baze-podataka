class Knjiga():
    def __init__(self, naslov, ISBN, autor, zanr, broj_stranica, godina_izdavanja, broj_clanske_karte = None):
        super().__init__()
        self.naslov = naslov
        self.ISBN = ISBN
        self.autor = autor
        self.zanr = zanr
        self.broj_stranica = broj_stranica
        self.godina_izdavanja = godina_izdavanja
        self.broj_clanske_karte = broj_clanske_karte #osoba kod koje se nalazi trenutno