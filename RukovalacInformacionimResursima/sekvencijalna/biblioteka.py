class Biblioteka:
    def __init__(self, naziv, adresa, godina_osnivanja, knjige=[]):
        super().__init__()
        self.naziv = naziv
        self.adresa = adresa
        self.godina_osnivanja = godina_osnivanja
        self.knjige = knjige