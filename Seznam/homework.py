import csv
from pprint import pprint as pp

def loader(name_csv):
    file = open (name_csv, encoding='utf8', newline='')
    reader = csv.reader(file, delimiter = ';')
    return list(reader)

def reader (reader, x = None):
    for row in reader[:x]:
        print(row)

def dictLoader(name_csv):
    file = open (name_csv, encoding='utf8', newline='')
    reader = csv.DictReader(file, delimiter = ';')
    return list(reader)

#reader(loader('articles.csv'),10)
a = dictLoader('articles.csv')#[:11]
b = sorted(a, key= lambda x: int(x['Zobrazení']))
pp(b)


# art = loader('articles.csv')
# print(art[:10])

# int_view = [int(x) for x in art[3]

# art.sort(key = lambda x : x[3])
# print(art)
