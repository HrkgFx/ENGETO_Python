import csv

def line (char = '*', num = 50):
    line = num * str(char)
    print(line)

with open('example.csv', newline='', encoding='utf8') as f:
    reader = csv.reader(f)
# vypsani celeho csv
    for row in reader:
        print(row)

    line('-')
# vraci kurzor na 0
    f.seek(0)
#vraci jen 4 index na jednotlivych radcich coz je age
    ages_filtered = map(lambda x: x[3],reader)
    print(list(ages_filtered))

    line('-')
    f.seek(0)
    city_filtered = map(lambda x: x[4],reader)
    print(list(city_filtered))

    line('-')
# vypsani radku jen zen
    f.seek(0)
# filter creates a list of elements for which a function returns true.
    females = list(filter(lambda x: x[-1]=='Female',reader))
    print(females)

    line('-')
new_employee=['Mills','Amanda','Mills, Amanda', 41,'Leicester','Quality Assurance','Female']
with open('example2.csv', 'a', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(new_employee)

with open('example2.csv',newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

employees = [['Harris','Roy','Harris, Roy',22,'London','Junior Programmer','Male'],
            ['Chesterfield','Mark','Chesterfield, Mark',46,'Liverpool','SCRUM Master','Male'],
            ['Hammet','Sandra','Hammet, Sandra',48,'Liverpool','Designer','Female']]

with open('example2.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(employees)

with open('example.csv',newline='') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
