def roznica_czasow(czas1, czas2):
    return abs(czas2-czas1)

class Przystanek(object):
    def __init__(self, obecne_miasto, nastepne_miasto, czas_przyjazdu):
        """
        obecne_miasto, nastepne_miasto -> obiekt miasto
        """
        self.obecne_miasto = obecne_miasto
        self.nastepne_miasto = nastepne_miasto
        self.czas_przyjazdu = czas_przyjazdu
        self.odjazd = self.znajdz_najlepszy_odjazd()
        self.czas_odjazdu = self.odjazd.czas_rozpoczecia_podrozy
        self.czas_przybycia_do_nastepnego_miasta = self.czas_odjazdu + self.odjazd.czas_trwania_podrozy
        self.kara = self.wylicz_funkcje_kary_dla_przystanku()
        
    def __str__(self):
        return str(self.kara)
        
    def wylicz_funkcje_kary_dla_przystanku(self):
        return roznica_czasow(self.czas_odjazdu, self.obecne_miasto.zakladany_czas_pobytu)
        
    def znajdz_najlepszy_odjazd(self):
        minimalna_roznica = 999999
        najlepszy_odjazd = None
        for mozliwy_odjazd in self.obecne_miasto.tablica_odjazdow[self.nastepne_miasto.nazwa]:
            obecna_roznica = roznica_czasow(mozliwy_odjazd.czas_rozpoczecia_podrozy, self.obecne_miasto.zakladany_czas_pobytu)
            if obecna_roznica <  minimalna_roznica:
                minimalna_roznica = obecna_roznica
                najlepszy_odjazd = mozliwy_odjazd
        return najlepszy_odjazd
                
        