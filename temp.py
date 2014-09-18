from algorytm import AlgorytmEwolucyjny

alg = AlgorytmEwolucyjny()
alg.sortuj_liste_rozwiazan()
alg.petla_algorytmu()

print("Najlepsze znalezione rozwiazanie:")
print(alg.lista_rozwiazan[0])