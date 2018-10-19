import csv

# f = open ('table1.csv')
# print(f.read())
# f.close()

# # vraci mi to radky jednotlive radky, neni soucasti moduu csv
# f = open ('table1.csv')
# for i in f:
#     print(i)    # i je string
# f.close()

# pozor na nazev souboru, kdybych dal csv.py tak to nefunguje

f = open ('table1.csv')
ctecka = csv.reader(f, delimiter = ';')

for radek in ctecka:
    print(radek)
f.close()

print('*'*55)

nf = open('table2.csv', 'w', newline = '') # novy radek je prazdny string
radek = [7, '', 9]
radek2 = [10, 11,'' ]

zapis = csv.writer(nf, delimiter = ';')
# zapis.writerow(radek)
# zapis.writerow(radek2)
zapis.writerows([radek, radek2])
nf.close()

print('*'*55)

nf = open('table2.csv')
ctecka2 = csv.reader(nf, delimiter = ';')

for radek in ctecka2:
    print(radek)
nf.close()

nf = open('table2.csv')
ctecka2 = csv.reader(nf, delimiter = ';')
sloupec1 = []
for radek in ctecka2:
    sloupec1.append(radek[0]) #info o prvnim sloupci
nf.close()

print('*'*55)

print(sloupec1)


nf = open('table2.csv')
ctecka2 = csv.reader(nf, delimiter = ';')
sloupce = {}

for radek in ctecka2:
    for i, polozka in enumerate(radek):
        # sloupce[i].append(polozka)
        # sloupce[i] = sloupce[i] + [polozka]

        sloupce[i] = sloupce.get(i, []) + [polozka] #get vraci none a proto rikam co mi to ma vratit misto None
nf.close()

# print(sloupce)

# 7,'',9,12
# 10,11,'',13
# 0, 1, 2, 3 - index sloupce
#
# for radek in ctecka2:
# [7,'',9,12] dostanu z prvniho pruchodu
# klic[0] = [] +[7]
#
# {0:7, 1:'', 2:9, 3: 12} - chci dostat po prvnim pruchodu



print(sloupce)
# sloupce = {1:[], 2:[]}
# sloupce.get(3) # vraci NoNe
