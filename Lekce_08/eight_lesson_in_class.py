# jmeno = input('Zadej jmeno: ')
# prijmeni = input('Zadej prijmeni: ')

# print(f'Ahoj moje jmeno je: {jmeno} a prijmeni: {prijmeni}.')
# print('Ahoj moje jmeno je: {} a prijmeni: {}.'.format(jmeno, prijmeni))
# print('Ahoj moje jmeno je: %s' %jmeno)
#
# print('Ahoj moje jmeno je: {1} a prijmeni: {0}.'.format(jmeno, prijmeni))

jmeno = ['Robin', 'Jancarik'] # nebo tuple
print('Ahoj moje jmeno je: {1:^9.5} a prijmeni: {0:#>20}.'.format(*jmeno))

# {index,:, vyplnovy znak, zarovnani, znamenko, sirku, ,, ., presnost}

# index
# vyplnovy znak - sirka se nam vyplni danym znakem pokud neni zadan tak je to mezera
# zarovnani - < > ^ - levo, pravo, stred
# znamenko nejde udelat u stringu
# sirka - 10 prazdnych znaku (nebo vyplnovy znak)
# , dlouhe cislo oddeluje mi to po 1 000
# . - urcuje tu presnost
# presnost, kolik muze zabirat znaku

print('Mam toto cislo: {:$^ 10}'.format(1000))
print('Mam toto cislo: {:$^10}'.format(-1000))
print('Mam toto cislo: {:$^+10}'.format(1000))
print('Mam toto cislo: {:$^10.4}'.format(1000.0))
print('Mam toto cislo: {:$^10.5}'.format(1000.34))
print('Mam toto cislo: {:$^10,.11}'.format(100044554.34))

# {'vec' : cena}
# ==========
# |vec|cena|
# ==========

# %s - string
# %d - cislo
sablona1 = '| %s | %d |' % ('rohlik', 2)
# print('| %s | %d |' % (2, 'rohlik')) ERROR rohlik neni cislo

l1 = ['rohlik',2.698]
sablona2 = '| {1:*^10} | {0:.2} |'.format(20.486523248, 'rohlik') #pocita pocet cifer ne desetinne mista
sablona3 ='| {:*^10} | {:.2} |'.format(*l1)
print(sablona1)
print(sablona2)
print(sablona3)

sablona4 = '| {vec} | {cena}|'.format(cena = 2.3, vec ='rohlik')
# sablona4 = '| {vec} | {cena} | {} |'.format(cena = 2.3, vec ='rohlik', 30) #ERROR nevi kam priradit 30ku

sablona5 = '| {vec} | {cena}|'.format(cena = 2.3, vec ='rohlik', kolik = 30)

slovnik = dict(vec = 'rohlik', cena = 2.985, kolik = 30)

sablona6 = '| {vec} | {cena}|'.format(**slovnik)
# sablona6 = '| {} | {}|'.format(slovnik) #TUPLE OF RANGE
print(sablona6)
sablona7 = '| {} | {} | {} |'.format(*slovnik) #dostanu jen klice slovniku
print(sablona7)


# SOUBORY
#OTEVRENI SOUBORU PRO CTENI
soubor = open('C:\\Users\\ASUS-R\\PythonBeginner\\Lekce_08\\text.txt')
print(soubor.tell())     # kde je kurzor
obsah = soubor.read()    # cte soubor do konce a vraci jako jeden string
print(obsah)
print(soubor.tell())
soubor.seek(86)         # odkud ma zacit v souboru cist
obsah2 = soubor.read()
print(soubor.tell())
soubor.close()
print(obsah2)

#WIN
# C:\\
# LINUX
# /  #root


#OTEVRENI SOUBORU PRO ZAPIS
soubor_zapis = open ('text2.txt', 'w') #mod zapisu 'w', pokud neexistuje, tak se soubor vytvori
string = 'Hovno hori!'
soubor_zapis.write(string)
# print(soubor_zapis.read()) # nelze cist v zapisu
# soubor_zapis.seek(0)
# soubor_zapis.write('FANTOMAS')
soubor_zapis.close()
# pridani textu na konec souboru
soubor_pridat = open ('text2.txt', 'a') # mod pridani 'a' jako append
soubor_pridat.write(' FANTOMAS!')
soubor_pridat.close()

# r+ read + zapis
# w+ write + read
# a+ append + read

soubor_zapis3 = open ('text3.txt', 'a+')
string = 'Je to tu, tadada '
soubor_zapis3.write(string)
soubor_zapis3.seek(0)
print(soubor_zapis3.read())
soubor_zapis3.close()

soubor_ctenip = open ('text4.txt', 'r+')
string = 'aktivista'
soubor_ctenip.write(string)
soubor_ctenip.seek(0)
soubor_ctenip.write('NAKARY')
soubor_ctenip.seek(0)
print(soubor_ctenip.read())
soubor_ctenip.close()


soubor = open('C:\\Users\\ASUS-R\\PythonBeginner\\Lekce_08\\text.txt')
for i in soubor:
    print(i, '\n')
    # print(soubor.tell())
soubor.close()


# for i in 123:
#     print(i)

# iterator
a = iter('asdsadasgsdgds')
print(next(a))              #
print(next(a))              #
print(next(a))              #
print(next(a))              #
print(next(a))              #
print(next(a))              #
print(next(a))              #
print(next(a))              #


s = open('text.txt')
print(next(s))
print(next(s))
print(next(s))
print(next(s))

a = [1, 2, 3]
ai = iter(a)
print(ai)
ai2 = iter(ai)
print(ai2)

# LIST od 1 - 100 bez cisel delitelnych 32
# h = []
# for i in range(1,101):
#     if i % 32 !=0:
#         h.append()

l2 = [i for i in range(1,101)]              # co se ma ukladat do listu, for a pak podminka if
l1 = [i for i in range(1,101) if i % 32 !=0]
print(l2)
print(l1)

l1 = (i for i in range(1,101) if i % 32 !=0) # z kulatych zavorek je generator
print(type(l1))

# A - vnorene slovnik
