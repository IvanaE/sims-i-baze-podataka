from predmet import Predmet


class PolozeniPredmet(Predmet):
    def __init__(self, id, naziv, silabus, ocena=6):
        super().__init__(id, naziv, silabus)
        self.ocena = ocena