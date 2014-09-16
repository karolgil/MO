class AlgorytmEwolucyjny(object):
    def __init__(self, dlugosc_listy_rozwiazan=100, limit_iteracji_bez_poprawy=100):
        self.dlugosc_listy_rozwiazan = dlugosc_listy_rozwiazan
        self.lista_rozwiazan = self.wygeneruj_rozwiazania_poczatkowe(dlugosc_listy_rozwiazan)
        self.kolejnych_iteracji_bez_poprawy = 0
        self.limit_iteracji_bez_poprawy = limit_iteracji_bez_poprawy
        
    def wygeneruj_rozwiazania_poczatkowe(self):
        # return []
        pass
    
    def sortuj_liste_rozwiazan(self):
        self.lista_rozwiazan.sort(key=lambda x: x.kara_calej_trasy)
    
    def petla_algorytmu(self):
        while self.kolejnych_iteracji_bez_poprawy < self.limit_iteracji_bez_poprawy:
            self.iteracja_algorytmu()
        print(self.lista_rozwiazan[0])
    
    
    def iteracja_algorytmu(self):
        """turniej"""
        rozwiazanie_1 = self.losuj_rozwiazanie()
        rozwiazanie_2 = self.losuj_rozwiazanie()
        nowe_rozwiazanie = self.krzyzuj_kolejnosc_miast(rozwiazanie_1, rozwiazanie_2)
        if nowe_rozwiazanie.kara_calej_trasy < self.lista_rozwiazan[-1]:
            self.kolejnych_iteracji_bez_poprawy = 0
            self.lista_rozwiazan[-1] = nowe_rozwiazanie
            self.sortuj_liste_rozwiazan()
        else:
            self.kolejnych_iteracji_bez_poprawy += 1
       
    def losuj_rozwiazanie(self):
        return self.lista_rozwiazan[random.randrange(self.dlugosc_listy_rozwiazan)]
        
    def krzyzuj_kolejnosc_miast(self, rozwiazanie_1, rozwiazanie_2):
        """Krzyzowanie z porzadkowaniem (OX)
        L1 -> [A,B,C,D,E,F,Z]
        L2 -> [D,F,A,E,B,C,Z]
        pop:
        L1 -> [A,B,C,D,E,F]
        L2 -> [D,F,A,E,B,C]
        len = 4
        poszial = rand (0...len) [np. 4]
        pol_dlug = len/2 = 3
                    
        index       0 1 2 3 4 5
        dziecko -> [A,-,-,-,E,F]
        pol         3       1 2
        
        usunac A,E,F z L2
        L2 -> [D,F,A,E,B,C] => [D,B,C]
        
        polaczyc
        dziecko -> [A,D,B,C,E,F]
        
        dodac ostatni:
        dziecko -> [A,D,B,C,E,F,Z]
        """
        lista_miast_1 = rozwiazanie_1.wez_liste_miast()
        lista_miast_2 = rozwiazanie_2.wez_liste_miast()
        miasto_koncowe = lista_miast_1.pop()
        lista_miast_2.pop()
        
        dlugosc_trasy = len(lista_miast_1)
        pol_dlugosci = int(dlugosc_trasy/2)
        punkt_podzialu = random.randrange(dlugosc_trasy)
        
        lista_potomka = lista_miast_1
        for licznik in range(pol_dlugosci):
            indeks = (licznik + punkt_podzialu) % dlugosc_trasy
            lista_potomka[indeks] = '-'
        
        [lista_miast_2.remove(x) for x in lista_potomka if x != '-']
        for licznik in range(dlugosc_trasy - pol_dlugosci):
            indeks = lista_potomka.index('-')
            lista_potomka[indeks] = lista_miast_2.pop(0)
            
        lista_potomka.append(miasto_koncowe)    
        potomek = self.wygeneruj_rozwiazanie_na_podstawie_listy_miast(lista_potomka)
        return potomek
        
    def wygeneruj_rozwiazanie_na_podstawie_listy_miast(self, lista_miast):
        czas_przybycia_do_miasta = 0
        trasa = []
        for indeks, miasto in lista_miast.iteritems():
            if indeks + 1 == len(lista_miast):
                break
            nastepne_miasto = liasta_miast[indeks+1]
            przystanek = Przystanek(miasto, nastepne_miasto, czas_przybycia_do_miasta)
            trasa.append(przystanek)
            czas_przybycia_do_miasta = przystanek.czas_przybycia_do_nastepnego_miasta
        return Rozwiazanie(trasa)
                
            
            
        