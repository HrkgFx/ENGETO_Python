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

line('-')
with open('example2.csv',newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

line('-')
employees = [['Harris','Roy','Harris, Roy',22,'London','Junior Programmer','Male'],
            ['Chesterfield','Mark','Chesterfield, Mark',46,'Liverpool','SCRUM Master','Male'],
            ['Hammet','Sandra','Hammet, Sandra',48,'Liverpool','Designer','Female']]

with open('example2.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(employees)

line('-')
with open('example.csv', newline='') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

line('-')
file = open('example.csv',newline='')
reader = csv.DictReader(file)

print(next(reader))
print(next(reader))
print(next(reader))
print(next(reader))
print(next(reader))

line('-')
new_employee = {'Job': 'Programmer', 'Age': 38, 'Full Name': 'Galagher, Fred', 'City': 'London', 'Surname': 'Galagher', 'Gender': 'Male', 'Name': 'Fred'}
file = open('example.csv' ,'a+', newline='')
file.seek(0)
header = next(file)
print(header)

line('-')
header = header.strip('\r\n').split(',')
print(header)

line('-')
writer = csv.DictWriter(file,header)
writer.writerow(new_employee)

reader = csv.reader(file)
for row in reader:
    print(row)

new_employees = [{'Job': 'Programmer', 'Age': 35, 'Full Name': 'Murphy, John', 'City': 'London', 'Surname': 'Murphy', 'Gender': 'Male', 'Name': 'John'},
                {'Job': 'Supervisor', 'Age': 26, 'Full Name': 'Higgins, Mary', 'City': 'Leicester', 'Surname': 'Higgins', 'Gender': 'Female', 'Name': 'Mary'}]
writer.writerows(new_employees)

line('-')
file.seek(0)
for row in reader:
    print(row)
