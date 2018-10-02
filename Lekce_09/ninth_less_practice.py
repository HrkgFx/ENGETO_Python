# cislo = int('abc')
# if 1 < 2:
# while 1 < 2:
#     print(1)
#     print(3)
#      # print({1:1}[2])
#     print(1/'1')

# if :
#   x+1

def fn1(c):
    return 1 / c

def fn2(c1):
    return fn1(c1 - 1) + 2

print ('Ahoj')
if 1 < 2:
    print(3)
    # print(1/'1')
b = fn2(0)
# a = fn2(1)
# print(a)

while 1:
    vstup = input ('Zadej cislo: ')
    #zkus vykonat kod co mas u sebe
    try:
        cislo = int(vstup) # kde vznikla chyba rovno skace na except
        vysledek = 100 / cislo
    # except ValueError:
    #     print('Nezadal jsi cislo.')
    # except ZeroDivisionError:
    #     print('Nelze delit nulou.')

    except (ValueError, ZeroDivisionError): #je to TUPLE
        print('Blbost')
        raise # vyvola vyjimku, kterou odchytil

    else: # kdyz se provede try v pohode tak proved toto
        print('Výsledek je: ', vysledek)
        break

nasobek = cislo * 37
print(nasobek)

# finally:
#     print('Děkujeme za pouzivani aplikace.')

# BaseException #spadaji pod ni vsechny podminky a spada pod ni i Exception a CTRL + C
