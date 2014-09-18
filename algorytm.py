from pustemiasto import PusteMiasto
from przystanek import Przystanek
from rozwiazanie import Rozwiazanie
from miasto import Miasto
from itertools import permutations
import random

class AlgorytmEwolucyjny(object):
    """
    Klasa przechowujaca wszystkie funkcje zwiazane z dzialaniem algorytmu 
    np. obslugujaca glowna petle czy definiujaca sposob krzyzowania rodzicow"""
    def __init__(self, plik_z_miastami="miasta.data", plik_z_rozkladem="rozklady_jazdy.data", dlugosc_listy_rozwiazan=100, limit_iteracji_bez_poprawy=100):
        """
        Parametry:
        * plik_z_miastami - plik przechowujacy liste miast, ktore chcemy odwiedzic
        * plik_z_rozkladem - plik przechowujacy rozklad jazdy
        * dlugosc_listy_rozwiazan - liczba najlepszych wynikow przechowywanych w pamieci
        * limit_iteracji_bez_poprawy - liczba iteracji zakonczonych porazka(wygenerowaniem rozwiazania gorszego), po ktorych algrytm wyjdzie  z petli glownej
        """
        self.dlugosc_listy_rozwiazan = dlugosc_listy_rozwiazan
        self.miasto_poczatkowe = None
        self.lista_rozwiazan = self.wygeneruj_rozwiazania_poczatkowe(plik_z_miastami, plik_z_rozkladem)
        self.kolejnych_iteracji_bez_poprawy = 0
        self.limit_iteracji_bez_poprawy = limit_iteracji_bez_poprawy
        
    def wypisz_liste_rozwiazan(self):
        print("\n".join([str(x) for x in self.lista_rozwiazan]))
        
    def wygeneruj_rozwiazania_poczatkowe(self, plik_miasta, plik_rozklad):
        """
        funkcja zwraca liste losowo wygenerowanych Rozwiazan,
        dlugosc listy jest rowna atrybutowi dlugosc_listy_rozwiazan
        format zwracanych danych:
        A->B->C->D->A
        A->C->B->D->A
        A->B->D->C->A
        """
        lista_miast = []
        with open (plik_miasta, 'r') as plik_z_miastami:
            for linia in plik_z_miastami:
                data = linia.split()
                lista_miast.append(Miasto(data[0],float(data[1]),plik_rozklad))
                
        self.miasto_poczatkowe = lista_miast.pop(0)
        
        tablica_wszystkich_permutacji_miast = list(permutations(lista_miast))
        tablica_wszystkich_permutacji_miast = [list(permutacja) for permutacja in tablica_wszystkich_permutacji_miast]
        for permutacja in tablica_wszystkich_permutacji_miast:
            permutacja.append(self.miasto_poczatkowe)
            permutacja.insert(0,self.miasto_poczatkowe)
            
        rozwiazania_poczatkowe = []
        for indeks in range(self.dlugosc_listy_rozwiazan):
            random_indeks = random.randrange(len(tablica_wszystkich_permutacji_miast))
            rozwiazania_poczatkowe.append(self.wygeneruj_rozwiazanie_na_podstawie_listy_miast(tablica_wszystkich_permutacji_miast[random_indeks]))
        return rozwiazania_poczatkowe
        
    def sortuj_liste_rozwiazan(self):
        """sortuj rozwiazania od najlepszego do najgorszego"""
        self.lista_rozwiazan.sort(key=lambda x: x.kara_calej_trasy)
    
    def petla_algorytmu(self):
        """Krzyzuj rozwiazania, az nie dostaniemy lepszego wyniku przez n=limit_iteracji_bez_poprawy iteracji"""
        while self.kolejnych_iteracji_bez_poprawy < self.limit_iteracji_bez_poprawy:
            self.iteracja_algorytmu()
    
    def iteracja_algorytmu(self):
        """Losuje dwa rozwiazania i dokonuje na nich operacji krzyzowania
        Po znalezieniu lepszego rozwiazania zeruje licznik i sortuje tablice rozwiazan"""
        rozwiazanie_1 = self.losuj_rozwiazanie()
        rozwiazanie_2 = self.losuj_rozwiazanie()
        nowe_rozwiazanie = self.krzyzuj_kolejnosc_miast(rozwiazanie_1, rozwiazanie_2)
        if nowe_rozwiazanie.kara_calej_trasy < self.lista_rozwiazan[-1].kara_calej_trasy:
            self.kolejnych_iteracji_bez_poprawy = 0
            self.lista_rozwiazan[-1] = nowe_rozwiazanie
            self.sortuj_liste_rozwiazan()
        else:
            self.kolejnych_iteracji_bez_poprawy += 1
       
    def losuj_rozwiazanie(self):
        """Zwroc losowe rozwiazanie z listy rozwiazan"""
        return self.lista_rozwiazan[random.randrange(self.dlugosc_listy_rozwiazan)]
        
    def krzyzuj_kolejnosc_miast(self, rozwiazanie_1, rozwiazanie_2):
        """
        Metoda generujaca nowe rozwiazanie na podstawie 2 istniejacych
        
        Algorytm na przykladzie:
        Krzyzowanie z porzadkowaniem (OX)
        Zakladamy, ze:
        * X - miasto poczatkowe (i koncowe)
        * A...F - miasta ktore chcemy odwiedzic
        * Lista1 -> [X,A,B,C,D,E,F]
        * Lista2 -> [X,D,F,A,E,B,C]
        * Listy sa rownej dlugosci, zawieraja te same miasta i kazde miasto wystepuje tylko raz
        
        Procedura:
        1. Usun miasto poczatkowe
        L1 -> [A,B,C,D,E,F]
        L2 -> [F,D,A,E,B,C]
        
        2. Okresl
        N - dlugosc kazdej listy - dla naszego przykladu 6
        P - punkt podzialu = losowaliczba z zakresu 0 do N - zalozmy 4
        Npol = polowa dlugosci listy zaokraglajac w dol - dla nas 3
        
        3. Stworz dziecko jako kopie L1
        dziecko = [A,B,C,D,E,F]
        
        4. usun Npol elementow z dziecka, zaczynajac od P
        indeks      0 1 2 3 4 5
        dziecko -> [-,B,C,D,-,-]
        Npol        3       1 2
        
        5. Usun z L2 element,ktore sa juz zawarte w dziecku (B,C,D)
        L2 = [F,A,E]
        
        6. Uzupelnij puste miejsca dziecka zawartoscia L2 
        dziecko -> [-,B,C,D,-,-]
        +
        L2      -> [F,      A,E]
        =
        dziecko -> [F,B,C,D,A,E]
        
        7. Dodaj na poczatek i koniec listy miasto startowe (X)
        dziecko -> [X,F,B,C,D,A,E,X]
        
        8. Wugeneruj rozwiazanie na podstawie dziecka
        """
        lista_miast_1 = rozwiazanie_1.wez_liste_miast()
        lista_miast_2 = rozwiazanie_2.wez_liste_miast()
        
        #1.
        lista_miast_1.pop(0)
        lista_miast_2.pop(0)
        
        #2.
        dlugosc_trasy = len(lista_miast_1)
        pol_dlugosci = int(dlugosc_trasy/2)
        punkt_podzialu = random.randrange(dlugosc_trasy)
        
        #3.
        lista_potomka = lista_miast_1
        
        #4.
        for licznik in range(pol_dlugosci):
            indeks = (licznik + punkt_podzialu) % dlugosc_trasy
            lista_potomka[indeks] = PusteMiasto()
        
        #5.
        for miasto in lista_potomka:
            if miasto in lista_miast_2:
                lista_miast_2.remove(miasto)
        
        #6.
        for licznik in range(dlugosc_trasy - pol_dlugosci):
            indeks = lista_potomka.index(PusteMiasto())
            lista_potomka[indeks] = lista_miast_2.pop(0)
        #7.    
        lista_potomka.insert(0,self.miasto_poczatkowe)
        lista_potomka.append(self.miasto_poczatkowe)
        
        #8.
        potomek = self.wygeneruj_rozwiazanie_na_podstawie_listy_miast(lista_potomka)
        return potomek
        
    def wygeneruj_rozwiazanie_na_podstawie_listy_miast(self, lista_miast):
        """Zwraca obiekt klasy Rozwiazanie dla podanej listy miast"""
        czas_przybycia_do_miasta = 0
        trasa = []
        for indeks, miasto in enumerate(lista_miast[:-1]):
            nastepne_miasto = lista_miast[indeks+1]
            przystanek = Przystanek(miasto, nastepne_miasto, czas_przybycia_do_miasta)
            trasa.append(przystanek)
            czas_przybycia_do_miasta = przystanek.czas_przybycia_do_nastepnego_miasta
        return Rozwiazanie(trasa)
                
            
            
        