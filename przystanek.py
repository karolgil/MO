def roznica_czasow(czas_przyjazdu, czas_odjazdu):
    """
    Funkcja obliczajaca roznice czasow uwzgledniajac przy tym system 24-godzinny
    """
    if((czas_przyjazdu - czas_odjazdu) > 0):
        return abs(24 - czas_przyjazdu + czas_odjazdu)
    else:
        return abs(czas_odjazdu - czas_przyjazdu)

def funkcja_kary(czas_przyjazdu, czas_odjazdu, zakladany_czas_pobytu):
    realny_czas_pobytu = roznica_czasow(czas_przyjazdu, czas_odjazdu)
    return abs(realny_czas_pobytu - zakladany_czas_pobytu)
        
class Przystanek(object):
    """
    Klasa definiujaca kolejne etapy podrozy
    Przechowuje czasy przyjazu/odjazdu zwiazane z obecnym miastem i czas przybycia do nastepnego miasta
    """
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
        """
        Funkcja obliczajaca kare jako roznice, pomiedzy zakladanym czasem pobytu w danym miescie, a czasem realnie spedzonym dla danego rozwiazania
        """
        return funkcja_kary(self.czas_przyjazdu, self.czas_odjazdu, self.obecne_miasto.zakladany_czas_pobytu)
        
    def znajdz_najlepszy_odjazd(self):
        """
        Funkcja oblicza dla danego przystanku najlepszy mozliwy odjazd do kolejnego miasta, podejmujac decyzje poprzez minimalizacje funkcji
        kary dla konkretnej pary miast.
        """
        minimalna_roznica = 999999
        najlepszy_odjazd = None
        for mozliwy_odjazd in self.obecne_miasto.tablica_odjazdow[self.nastepne_miasto.nazwa]:
            obecna_roznica = funkcja_kary(self.czas_przyjazdu, mozliwy_odjazd.czas_rozpoczecia_podrozy, self.obecne_miasto.zakladany_czas_pobytu)
            if obecna_roznica <  minimalna_roznica:
                minimalna_roznica = obecna_roznica
                najlepszy_odjazd = mozliwy_odjazd
        return najlepszy_odjazd
                
        