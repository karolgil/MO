class Rozwiazanie(object):
    """
    Klasa przechowujaca propozycje podrozy
    Przechowuje kolejnosc przystankow i wartosc funkcji kary
    """
    def __init__(self, trasa):
        """trasa - lista Przystankow [A,B,C,D] - bez punktu startowego na koncu
        Lista nie zawiera w sobie Przystanku koncowego, bo obiekt Przystanek zawiera informacje o kolejnym miescie podrozy, 
        a po powrocie do punktu startowego nigdzie jux nie jedziemy"""
        self.trasa = trasa
        self.kara_calej_trasy = self.oblicz_funkcje_kary_calej_trasy()
        
    def oblicz_funkcje_kary_calej_trasy(self):
        return sum([przystanek.kara for przystanek in self.trasa])
        
    def wez_liste_miast(self):
        """Zwraca lise miast -> [A,B,C,D] - bez miasta startowego na koncu"""
        return [przystanek.obecne_miasto for przystanek in self.trasa]
    
    def __str__(self):
        return "Kara = " + str(self.kara_calej_trasy)+"\nKolejnosc miast:\n" + "\n".join([miasto.nazwa for miasto in self.wez_liste_miast()])
        
    