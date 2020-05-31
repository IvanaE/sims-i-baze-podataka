class Predmet():
    def __init__(self, sifra_predmeta, naziv, broj_casova_nedeljno, broj_semestra, nastavnici=[]):
        super().__init__()
        self.sifra_predmeta = sifra_predmeta
        self.naziv = naziv
        self.broj_casova_nedeljno = broj_casova_nedeljno
        self.broj_semestra = broj_semestra
        self.nastavnici = nastavnici