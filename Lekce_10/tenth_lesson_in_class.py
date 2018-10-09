# # 2.1
# def int_conver(*items): # jedna hvezdicka vraci tuple
#     nums = []
#     for i in items:
#         try:
#             nums.append(int(i))
#         except ValueError:
#             pass
#     return nums
#
# print(int_conver('Hello', '23','12', 'Bob', 'new', '4312','5'))

import math #ten soubor se spusti - takze pokud by byla nejaka akce v tom importu, tak projde cely math a zeptal by se me na tu akci
from math import pi
from math import floor as fl
# from math import pi, floor # naimportuje jen dane veci z tohoto modulu
# from math import * # naimportuje uplne vsechno, ale nedoporucuje se, protoze si tim zaseru promenne
# from math import pi as picko # prejmenujes si to jak potrebus
# import cesta/muj_modul
# globalni promenne - math a odkazujes se na ty soubory co jsou tam

print(globals())

r = int(input('Zadej polomer: '))
# vysledek = r**2*math.pi
vysledek = r**2*pi
print(vysledek)
print('{0:.5}'.format(vysledek))
print(math.floor(vysledek)) # zaokrouhleni dolu
print(math.ceil(vysledek)) # zaokrouhleni nahoru

x = 13//2 # flor division
print(x)
