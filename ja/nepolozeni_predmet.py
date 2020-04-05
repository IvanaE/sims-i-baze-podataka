from predmet import Predmet


class NepolozeniPredmet(Predmet):
    def __init__(self, id,  naziv, silabus, broj_pokusaja=1):
        super().__init__(id, naziv, silabus)
        self.broj_pokusaja = broj_pokusaja