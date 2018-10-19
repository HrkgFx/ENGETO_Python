import csv

file = open ('articles.csv', encoding='utf8')
reader = csv.reader(file, delimiter = ';')

for row in reader:
    print(row)
file.close()
