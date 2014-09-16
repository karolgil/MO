from odjazd import Odjazd

class Miasto(object):
    def __init__(self, nazwa, zakladany_czas_pobytu, plik_z_odjazdami):
        self.nazwa = nazwa.lower()
        self.zakladany_czas_pobytu = zakladany_czas_pobytu
        self.tablica_odjazdow = []
        self.tablica_odjazdow = pobierz_tablice_odjazdow(plik_z_odjazdami)
        
    def pobierz_tablice_odjazdow(self, plik_z_odjazdami):
        with open(plik_z_odjazdami, 'r') as handler_do_pliku:
            for linia in handler_do_pliku:
                dane_odjazdu = linia.split()
                if dane_odjazdu[0].lower() == self.nazwa:
                    self.tablica_odjazdow.append(Odjazd(dane_odjazdu[0],dane_odjazdu[1],dane_odjazdu[2],dane_odjazdu[3]))
        