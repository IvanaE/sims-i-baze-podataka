class Clan():
    def __init__(self, ime, prezime, broj_clanske_karte, godina_rodjenja, knjige = []):
        super().__init__()
        self.ime = ime
        self.prezime = prezime
        self.broj_clanske_karte = broj_clanske_karte
        self.godina_rodjenja = godina_rodjenja
        self.knjige = knjige #istorijat