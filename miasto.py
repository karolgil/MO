from odjazd import Odjazd

class Miasto(object):
    def __init__(self, nazwa, zakladany_czas_pobytu, plik_z_odjazdami):
        self.nazwa = nazwa.lower()
        self.zakladany_czas_pobytu = zakladany_czas_pobytu
        self.tablica_odjazdow = {}
        self.pobierz_tablice_odjazdow(plik_z_odjazdami)
        
    def __str__(self):
        return self.nazwa
        
    def __cmp__(self, other):
        if self.nazwa == other.nazwa:
            return 0
        return 1
        
    def pobierz_tablice_odjazdow(self, plik_z_odjazdami):
        with open(plik_z_odjazdami, 'r') as handler_do_pliku:
            for linia in handler_do_pliku:
                linia = linia.lower()
                dane_odjazdu = linia.split()
                if dane_odjazdu[0] == self.nazwa:
                    if dane_odjazdu[1] not in self.tablica_odjazdow.keys():
                        self.tablica_odjazdow[dane_odjazdu[1]] = []
                    odj = Odjazd(dane_odjazdu[0],dane_odjazdu[1],float(dane_odjazdu[2]),float(dane_odjazdu[3]))
                    self.tablica_odjazdow[dane_odjazdu[1]].append(odj)