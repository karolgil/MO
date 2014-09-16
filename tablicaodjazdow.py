class TablicaOdjazdow(object):
    def __init__(self, slownik_odjazdow):
        """
        k moga byc rozne dla poszczegolnych miast 
        slownik_odjazdow = {
            "MiastoA" : [odjazd1_do_A, odjazd2_do_A, ... , odjazdk_do_A],
            "MiastoB" : [odjazd1_do_B, odjazd2_do_B, ... , odjazdk_do_B],
             ...
            "Miaston" : [odjazd1_do_n, odjazd2_do_n, ... , odjazdk_do_n]
        }
        """
        self.slownik_odjazdow = slownik_odjazdow