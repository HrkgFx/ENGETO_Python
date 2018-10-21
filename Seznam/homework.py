import csv

def loader(name_csv):
    file = open (name_csv, encoding='utf8', newline='')
    reader = csv.reader(file, delimiter = ';')
    return reader

def reader (reader):
    for row in reader:
        print(row)

reader(loader('articles.csv'))
