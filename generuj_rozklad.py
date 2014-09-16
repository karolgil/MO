from itertools import permutations

def generuj_rozklad():
	with open("miasta.data", 'r') as handler_do_pliku:
		miasta = []
		polaczenia = []
		for linia in handler_do_pliku:
			miasta.append(str(linia))
			polaczenia = permutations(miasta)
			data = list(map("".join, itertools.permutations(miasta)))
			print(data)
generuj_rozklad()