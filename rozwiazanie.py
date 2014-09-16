class Rozwiazanie(object):
    def __init__(self, trasa):
        self.trasa = trasa
        self.kara_calej_trasy = oblicz_funkcje_kary_calej_trasy()
        
    def oblicz_funkcje_kary_calej_trasy(self):
        return sum([przystanek.kara for przystanek in trasa])
        
    def wez_liste_miast(self)
        return [przystanek.obecne_miasto for przystanek in self.trasa]
        
    