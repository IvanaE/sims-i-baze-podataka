class Predmet():
    def __init__(self, sifra_predmeta, naziv, broj_nedeljnih_casova, smer, broj_semestra, nastavnici=[]):
        super().__init__()
        self.sifra_predmeta = sifra_predmeta
        self.naziv = naziv
        self.broj_nedeljnih_casova = broj_nedeljnih_casova
        self.smer = smer
        self.broj_semestra = broj_semestra
        self.nastavnici = nastavnici
