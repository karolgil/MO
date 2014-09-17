import copy

class Rozwiazanie(object):
    def __init__(self, trasa):
        self.trasa = trasa
        self.kara_calej_trasy = self.oblicz_funkcje_kary_calej_trasy()
        
    def oblicz_funkcje_kary_calej_trasy(self):
        return sum([przystanek.kara for przystanek in self.trasa])
        
    def wez_liste_miast(self):
        return [przystanek.obecne_miasto for przystanek in self.trasa]
    
    def __str__(self):
        return str(self.kara_calej_trasy) #+ "\n".join([str(przystanek) for przystanek in self.trasa])
        
    