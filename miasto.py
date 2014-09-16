class Miasto(object):
    def __init__(self, nazwa, zakladany_czas_pobytu, tablica_odjazdow):
        self.nazwa = nazwa.lower()
        self.zakladany_czas_pobytu = zakladany_czas_pobytu
        self.tablica_odjazdow = tablica_odjazdow