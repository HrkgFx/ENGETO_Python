#2.1.
# numbers = range(1,101)
#
# for num in numbers:
#     if num % 15 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)

# 2.2
# size = 10
# sym = ['#',' ']
# desk = []
#
# for r,row in enumerate(range(size)): #generuju radej (index a hodnotu na indexu)
#     line = []
#
#     for c,cell in enumerate(range(size)):   #generuje bunku
#         i = (r+c)%len(sym)
#         line.append(sym[i])
#
#     desk.append(''.join(line))
#
# print('\n'.join(desk))
#
# # enumerate - tuple - index a ta vec
# a,b = (1,2)
# print(a)
# print(b)
#
# a, *b = (1, 2, 3)
# a, *b = (1, 'kocka', 'asd')
# print(a)
# print(b)
#
# *a, b, c = (1,2,3,4)
# print(a)
# hodi se na list v listu a v tom budu mit [[1,2,3],['asd',2,3],['ddgdgs',2,'p']]


# list_setu = [{1,2,3},{'asd',2,3},{'ddgdgs',2,'p'}]
# x = set.intersection(*list_setu) #
# print(x)
# set('dsafasfasf')
#
#
# # a, b = [1,2]
# #
# # q = input() # zavorky jsou spoustec funkce volani funkce - call funkce
# # print(input)
#
# #vytvareni funkce
#
# def nova_funkce(parametr, number):   #do zavorek pisu parametry(promene, do kterych dava programator argumenty) funkce #kdyz ji volam, tak ji predavam argumenty
#     results = 0
#     for num in parametr:
#         results += num
#     # print(results * number)
#     return results * number # zajisti co funkce vraci
#
# # nova_funkce([1, 2, 3], 2)
#
# # a = sum()
#
# # ve funkci mohou byt nepovinne parametry
#
# # nova_funkce('[]', {1,2,3})
# # ERROR
# print(nova_funkce({1,2,3},2)) #vypise se mi 12 a 12 - nejdrive se vypise prvni funkce a nasledne druha funkce

# str = 'tohle je string'
# print(str(123))
# ERROR protoze jsem si prepsal funkci prevody na string


# def dvakrat(input):
#     print(input)
#     a = input('Vnitrni')
#     print(a)
# b = input('Vnejsi')
#
# dvakrat(b)
# ERROR

# def dvakrat(input):
#     print(input)
# b = input('Vnejsi')
#
# dvakrat(b)
# input('Funkce uz probehla')

# def zdvoj(string):

# def secti (lst, cislo): # secti je jen sipka ktera ukazuje kam, lst a cislo je objekt
#     vysledek = 0
#     for i in lst:
#         vysledek += i
#
#     return vysledek * cislo
#
# sum_list = secti
# dvanact = secti({1,2,3},2) # dava co tam funkce vraci a proto s tim muzu dale pracovat, kvuli tomu jde retazit funkce
#
# print(sum_list)
# print(dvanact)
#
# # OBJEKT je neco si python musi pamatovat (vse co ma v sobe) - objekt je to, co je ulozeno v promennych
#
# cele_cislo = int
# print(cele_cislo('1'))
#
# # vysledky funkci vraci jen hodnoty, proto je mozno je retezit


# DOBROVOLNY ARGUMENT
def postupny_print(povinny,*neco):    # * urcuje, ze je to dobrovolny parametr (uklada se jako tuple)
    print(f'Toto je povinne: {povinny}')
    for cast in neco:
        print(cast)
    # print(neco) # vytiskne se to jako tuple

postupny_print(1,2,35,4556,4)

a, *b = 1, 2, 3, 5, 6 # zbytek se uklada jako list
print(a,b)

def nekolikrat(string, kolik=2):  # nastaveni defaultni hodnoty pres = neco
    vysledek = ''
    for pismeno in string:
        vysledek += kolik * pismeno
    return vysledek

# print(nekolikrat('Ahoj', 5))
#
# print(nekolikrat(kolik=3, string='BAF'))

lst =[('ahoj',2),('BAF',4),('_-',8)]
for tupl in lst:
    # print(nekolikrat(tupl[0], tupl[1]))
    print(nekolikrat(*tupl))



# JINY SOUDEK

print('tex\\\\\\t')
