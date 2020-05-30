class Student():
    def __init__(self, indeks, ime, prezime, datum, predmeti = []):
        super().__init__()
        self.indeks = indeks
        self.ime = ime
        self.prezime = prezime
        self.datum = datum
        self.predmeti = predmeti