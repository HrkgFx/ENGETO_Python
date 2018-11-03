# # 1/
# class Dice:
#     """
#     Class present dice.
#     """
#     def __init__(self):
#         self.num_side = 6
#
# cube = Dice()
# print(cube.num_side)

class Kostka:
    """
    Class present dice.
    """
    def __init__(self, pocet_sten=6):
        self.__pocet_sten = pocet_sten
        # __ znaci soukromy atribut (read_only)

    def vrat_pocet_sten(self):
        """
        Vrati pocet sten kostky
        """
        return self.__pocet_sten

    def hod(self):
        """
        Vrati cislo od 1 do poctu sten na kostce
        """
        import random as _random
        return _random.randint(1,self.__pocet_sten)

kostka = Kostka()
print(kostka.vrat_pocet_sten())


sestistenka = Kostka()
desetistenka = Kostka(10)

print('sestistenka', sestistenka.vrat_pocet_sten())
print('desetistenka', desetistenka.vrat_pocet_sten())

print(sestistenka)
