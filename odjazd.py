class Odjazd(object):
    def __init__(self, miasto_poczatkowe, miasto_koncowe, czas_rozpoczecia_podrozy, czas_trwania_podrozy):
        self.miasto_poczatkowe = miasto_poczatkowe
        self.miasto_koncowe = miasto_koncowe
        self.czas_rozpoczecia_podrozy = czas_rozpoczecia_podrozy
        self.czas_trwania_podrozy = czas_trwania_podrozy
        
    def __str__(self):
        return " ".join([self.miasto_poczatkowe, self.miasto_koncowe, self.czas_rozpoczecia_podrozy, self.czas_trwania_podrozy])