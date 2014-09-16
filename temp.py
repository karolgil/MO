from miasto import Miasto
from algorytm import AlgorytmEwolucyjny

alg = AlgorytmEwolucyjny()

plik = "rozklady_jazdy.data"

krakow = Miasto("krakow", 8, plik)
warszawa = Miasto("warszawa", 10, plik)
gdansk = Miasto("gdansk", 5, plik)
wroclaw = Miasto("wroclaw", 2, plik)
soncz = Miasto("soncz", 7, plik)
poznan = Miasto("poznan", 7, plik)
rzeszow = Miasto("rzeszow", 5, plik)

lista_miast = [krakow, warszawa, gdansk, wroclaw,poznan, rzeszow, soncz]

# print "\n\n".join([str(x) for x in lista_miast])

print alg.wygeneruj_rozwiazanie_na_podstawie_listy_miast(lista_miast)