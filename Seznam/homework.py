import csv

def loader(name_csv):
    file = open (name_csv, encoding='utf8', newline='')
    reader = csv.reader(file, delimiter = ';')
    return list(reader)

def reader (reader, x = None):
    for row in reader[:x]:
        print(row)

reader(loader('articles.csv'),10)
reader(loader('videos.csv'),10)

# art = loader('articles.csv')
# print(art[:10])

# int_view = [int(x) for x in art[3]

# art.sort(key = lambda x : x[3])
# print(art)
