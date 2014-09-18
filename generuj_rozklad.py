from itertools import permutations
from random import randint

def generuj_rozklad():
    """
    Funkcja generuje na podstawie listy miast losowe godziny polaczen pomiedzy nimi, wyznaczajac od 1 do 4 polaczen w kazda strone kazdego dnia
    """
    with open("miasta.data", 'r') as handler_do_pliku:
        miasta = []
        polaczenia = []
        for linia in handler_do_pliku:
            miasta.append(str(linia.split()[0]))
        polaczenia = permutations(miasta)
        permutacje = list(map(" ".join, permutations(miasta, 2)))
        with open("rozklady_jazdy.data", 'w') as handler_do_pliku:
            for trasa in permutacje:
                for _ in range(randint(1,4)):
                    linia_do_pliku = " ".join([str(trasa),str(randint(1,23)),str(randint(1,5))])
                    handler_do_pliku.write(linia_do_pliku + "\n")
        
generuj_rozklad()