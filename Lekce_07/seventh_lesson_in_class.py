def secti(lst, cislo):
    vysledek = 0
    # a = a + 3 #pristup vs prirazeni
    # a.append(1)
    global a # prepise a = 10 na 35 urci ji jako globalni promennou
    a = 35
    for i in lst:
        vysledek += i #+ c nemuzu brat c z nizsi def funkce
    # print(a)
    def uvnitr():
        # c = 3
        print(vysledek)   # pro tuto funkci je toto globalni promena prebira si ji z nadrazene funkce
    uvnitr()
    return vysledek*cislo

# a = 5
sum_list = secti
# a = []
a = 10
dvanact = secti({1,2,3},2)
# print(vysledek) # ERROR protoze promena neni definovana - jen v definici funkce jako lokalni promenna
print(a)
# print(sum_list)
# print(dvanact)



# namespaces - pytlik s propojenim a hodnotama
#
# lokalni
# - vsechny promenne ktere muzu pouzit jen na omezenem pisecku (napr. funkce definice)
#
# Globalni

def ahoj():
    x = 5

print(globals())
print(locals())


# --------------------PART 2--------------------
# spopes
from pprint import pprint as pp
def vnejsi():
    c = None
    a = [1,2,3]
    def vnitrni():
        f = 'jsem uvnitr funkce vnejsi'
        print('Global vnitrni: ')
        pp(globals())
        print('Local vnitrni: ')
        pp(locals())
    vnitrni()
    print('Global vnejsi: ')
    pp(globals())
    print('Local vnejsi: ')
    pp(locals())
    # pass        # preskakuje obsah funkce
a = 1
b = 'abc'
vnejsi()
print('Globals:')
pp(globals())

# global_namespaces = globals()



# def nazev(jmeno, rok = 2018, *nepoviny):
def nazev(jmeno, *nepoviny, rok = 2018):
    print(jmeno)
    print(nepoviny) # vypise tupple
    # pass
    # return jmeno + str(rok)

# nazev('Robin',1,2,3,4,5,2, rok = 2019) #zmenim rok na 2019 ze ho priradim roku
#
# a, *b = 1,2,3,4,5
# print(a)
# print(b)
# slovnik = dict(klic = 'hodnota', klic2 = 2)
#
# def nazev(**dobrovolne):        #** ukladaji klic = hodnota a dobrovolny bude mit promennou typu slovnik
#     print(dobrovolne)
# slovnik = nazev(klic = 'hodnota', klic2 = 2)
# print(slovnik)          #vypise se None
#
#
#
# def nazev(poviny1,**dobrovolne):        #** ukladaji klic = hodnota a dobrovolny bude mit promennou typu slovnik
# # nelze za **neco davat dalsi parametry
#     print(poviny1)
#     print(dobrovolne)
#     # print(poviny2)
#
# slovnik = nazev('kocka', klic = 'hodnota')
# print(slovnik)          #vypise se None


# def nazev(poviny1, d = 1, *dobrovolne, cislo): # spatny zapis defaultni promenne davat az nakonec
# # nelze za **neco davat dalsi parametry
#     print(poviny1)
#     print(d)
#     print(dobrovolne)
#     print(cislo)
#
# slovnik = nazev('kocka', 'hodnota', cislo = 3)
# slovnik = nazev(d=2, poviny1 = 'kocka', cislo = 3)
# print(slovnik)          #vypise se None


def nazev(**dobrovolny): #- ** je ulozen jako dict
    print(dobrovolny)
    return(dobrovolny)
x = nazev(d = 2)
print(x)

def nazev(*dobrovolny): #- ** je ulozen jako dict
    print(dobrovolny)
    return(dobrovolny)
x = nazev("d",2,3,5)
print(x)
