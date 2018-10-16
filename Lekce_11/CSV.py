import csv

# f = open ('table1.csv')
# print(f.read())
# f.close()

# # vraci mi to radky jednotlive radky, neni soucasti moduu csv
# f = open ('table1.csv')
# for i in f:
#     print(i)    # i je string
# f.close()


f = open ('table1.csv')
ctecka = csv.reader(f, delimiter = ';')

for radek in ctecka:
    print(radek)
f.close()
