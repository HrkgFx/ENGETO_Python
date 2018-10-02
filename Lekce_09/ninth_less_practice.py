# cislo = int('abc')
# if 1 < 2:
# while 1 < 2:
#     print(1)
#     print(3)
#      # print({1:1}[2])
#     print(1/'1')

# if :
#   x+1

print ('Ahoj')
if 1 < 2:
    print(3)
    # print(1/'1')


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

    else: # kdyz se provede try v pohode tak proved toto
        print('Výsledek je: ', vysledek)
        break

nasobek = cislo * 37
print(nasobek)

# finally:
#     print('Děkujeme za pouzivani aplikace.')
