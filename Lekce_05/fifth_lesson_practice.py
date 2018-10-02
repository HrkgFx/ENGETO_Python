line = 28 * '*'
sep = 28 * '-'

# 3.3
names = ['Jakub', 'Jana', 'Petr', 'Klara', 'Jirina', 'Jaroslav']
totallen = 0

for name in names:
    if name.startswith('J'):
        lenght=len(name)
        totallen += lenght
        print(f'Name {name} has {lenght} chars')

print(f'Sum of lenght name is {totallen} chars.')
print(line)

#3.4
# for item in 1234567:
#     print(item)
# ERROR
for item in 'abcdefghi':
    print(item)
print(line)

for item in (1,2,3,4,5):
    print(item)
print(line)

for item in {1,2,3,4,5}:
    print(item)
print(line)

for item in {'name': 'Bob', 'age': 23, 'job':'plumber'}:
    print(item)
print(line)

#3.5
r = range(5)
print(f'print is r = range(5) is {r}')
for x in r:
    print(x)
print(line)

r = range(2,6)
print(f'print is r = range(2,6) is {r}')
for x in r:
    print(x)
print(line)

r = range(2,9,2)
print(f'print is r = range(2,9,2) is {r}')
for x in r:
    print(x)
print(line)

r = range(4,0,-1)
print(f'print is r = range(4,0,-1) is {r}')
for x in r:
    print(x)
print(line)

r = range(8,1,-2)
print(f'print is r = range(8,1,-2)) is {r}')
for x in r:
    print(x)
print(line)

# We usually use range() in for loop, to generate numbers later used as indexes: (Not very Pythonic)
names = ['Helmut', 'Helga', 'Harold', 'Hammet', 'Hetfield']
for index in range(len(names)):
    print(names[index])
print(line)

for name in names:
    print(name)
print(line)

for i in range(0,len(names),2):
    print(i,names[i])
print(line)

# vytiskne kazde druhe cislo
# enumerate(iterable, start=0)
# The enumerate() method adds counter to an iterable and returns it. The returned object is a enumerate object.
# You can convert enumerate objects to list and tuple using list() and tuple() method respectively.

numbers = [321,45,32,12,54]
for index, number in enumerate(numbers):
    if index % 2 == 0:
        print(number, ':', number**2)
print(line)
# SAMPLE 1
# grocery = ['bread', 'milk', 'butter']
# enumerateGrocery = enumerate(grocery)
#
# print(type(enumerateGrocery))
# print(list(enumerateGrocery))

# SAMPLE 2
# grocery = ['bread', 'milk', 'butter']
#
# for item in enumerate(grocery):
#   print(item)

# # 3.10
# text = '''
# Situated about 10 miles west of Kemmerer,
# Fossil Butte is a ruggedly impressive
# topographic feature that rises sharply
# some 1000 feet above Twin Creek Valley
# to an elevation of more than 7500 feet
# above sea level. The butte is located just
# north of US 30N and the Union Pacific Railroad,
# which traverse the valley.'''
# print(text)
# print(line)
#
# search_word = input('Enter search word: ')
#
# # 0/
# words = text.split()
# # print(words)
# found = False
#
# for i,word in enumerate(words):
#     word = word.strip(';,._/:')
#     if word == search_word:
#         found = True
#         position = i + 1
#
# if found:
#     print(f'Position searched word is: {position}')
# else:
#     print('NO SUCH WORD')
#
#
# # 3.12
# 1/
# words = text.split()
# position = -1
# for i,word in enumerate(words):
#     word = word.strip(';,._/:')
#     if word == search_word:
#         position = i + 1
#         print('POSITION: ' + str(position))
#         break
#
# if position == -1:
#     print('NO SUCH WORD')

# 2/
# words = text.split()
# for i,word in enumerate(words):
#     word = word.strip(';,._/:')
#     if word == search_word:
#         position = i + 1
#         # print('POSITION: ' + str(position))
#         print(f'Position searched word is: {position}')
#
# else:
#     print('NO SUCH WORD')

# CORRECT RESULTS
text = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''
print(text)
# print(line)

search_word = input('Enter search word: ')
positions = []
words = text.split()
for i,word in enumerate(words):
    word = word.strip(';,._/:')
    if word == search_word:
        position = i + 1
        positions.append(position)
        print(f'Position searched word is: {position}')

if not positions:
    print('NO SUCH WORD')


# 3.13
employee = {'f_name':'John', '_name':'Smith','age': 23, 'job':'plumber'}

print(f'Dictionary employee: {employee}')

print('for k in employee:\n\tprint(k)')
print(sep)
for k in employee:
    print(k)
print(line)

print('for k in employee.keys():\n\tprint(k)')
print(sep)
for k in employee.keys():
    print(k)
print(line)

print('for v in employee.values():\n\tprint(v)')
print(sep)
for v in employee.values():
    print(v)
print(line)

print('for k,v in employee.items():\n\tprint(k,v)')
print(sep)
for k,v in employee.items():
    print(k,v)
print(line)

# 3.14
data = [['ID','Name', 'Price', 'Amount', 'Supplier'],
        ['321','Ibalgin', 40.50, 2841, 'Zentiva'],
        ['534','Paralen', 19.90, 3229, 'Zentiva'],
        ['327','Smecta', 68.00, 2709, 'Sipsen'],
        ['242','Uniclophen', 76.00, 476, 'UNIMED']]



total_price = 0
amount = 0
num_items = 0
eshop = {}
header = data[0][1:]

for row in data[1:]:
    # 1/ What is the total price of our inventory?
    total_price += row[2] * row[3]

    # 2/ What is the total amount of items in our warehouse?
    amount += row[3]

    # 3/ How many items do we have from the company called Zentiva?
    if row[4] == 'Zentiva':
        num_items += row[3]

    # 4/ Let's transfer the above table into a dictionary of dictionaries. How would we do that?
    id = row[0]
    eshop[id] = {}
    for i,item in enumerate(row[1:]):
        key = header[i]
        eshop[id].update({key: item})

print(f'Total price is: {total_price}')
print(f'Total amount of items is: {amount}')
print(f'Data have {num_items} Zentiva items.')
print(f'Dictionary is: {eshop}')

# 3.16
size = 10
sym = ['+','-']
desk = []

for r,row in enumerate(range(size)):
    line = []
    for c,cell in enumerate(range(size)):
        line.append(sym[(r+c)%len(sym)])
    desk.append(''.join(line))

print('\n'.join(desk))



# # 3.18
# # our training table - in case we do not want to insert new
# # rows and columns at the beginning
# table = [['Name','Age','Email'],
#          ['bob', '23', 'bob@abc.com'],
#          ['ann', '25', 'ann@abc.com'],
#          ['fred', '43', 'fred@abc.com']]
#
# while True:
#
#     print('-'*40)
#     print('What do we want to do? Enter the number')
#     print('''
#     1-Create table | 2-Insert new row | 3-Insert new column |
#     4-Update a cell | 5-Column Total | 6-Row Total |
#     7-Print Table | 8-Export do List of Dicts |
#     ''')
#     selection = int(input('OPTION: '))
#     print('-'*40)
#
#     # user wants to create a table
#     if selection == 1:
#         table = []
#         print('Enter header names separated by comma (e.g. Name,Age,Email)')
#         header = input()
#         table.append(header.split(','))
#
#     # user wants to insert a new row
#     elif selection == 2:
#         where = int(input('ROW NUMBER: '))
#         print('Enter the comma separated values (e.g. Bob,23,bob@abc.com): ')
#         row = input().split(',')
#         if  0 < where < len(table):
#             table.insert(where, row)
#         elif where >= len(table):
#             table.append(row)
#
#     # user wants to insert a new column
#     elif selection == 3:
#         col_name = input('COLUMN NAME: ')
#         table[0].append(col_name)
#
#         for i,row in enumerate(table[1:]):
#             val = input('ENTER VALUE: ' + '|'.join(row) + '|')
#             table[i+1].append(val)
#
#     # user wants to update a cell
#     elif selection == 4:
#         row_num = int(input('ROW NUMBER: '))
#         col_num = int(input('COLUMN NUMBER: '))
#         if row_num in range(len(table)) and \
#            col_num in range(len(table[0])):
#            val = input('VALUE (current value: ' + table[row_num][col_num] + '):')
#            table[row_num][col_num] = val
#         else:
#             print('No such row or column')
#
#     # user wants to calculate the total sum of numbers in a column
#     elif selection == 5:
#         total = 0
#         print('Select the column name')
#         print('|'.join(table[0]))
#         col_name = input()
#         if col_name in table[0]:
#             col_num = table[0].index(col_name)
#
#             for row in table:
#                 if row[col_num].isnumeric():
#                     total += int(row[col_num])
#             print('COLUMN TOTAL FOR ' + col_name + ': ' +str(total))
#         else:
#             print('No column named ' + col_name)
#
#     # user wants to calculate the total sum of numbers in a row
#     elif selection == 6:
#         total = 0
#         print('Select the row number in range 1 to ' + str(len(table[0])))
#         row_num = int(input())
#
#         if 0<row_num < len(table[0]):
#             for cell in table[row_num]:
#                 if cell.isnumeric():
#                     total+=int(cell)
#             print('ROW TOTAL FOR ROW #' + str(row_num) + ': ' +str(total))
#
#     # user wants to print table contents - can select which rows
#     elif selection == 7:
#         start = int(input('FROM ROW: '))
#         end = int(input('TILL ROW: '))
#         skip=1
#         if input('Skip rows? [y/n]: ')=='y':
#             skip = input('How many? (2 for every second etc.): ')
#
#         start = 0 if start not in range(len(table)) else start
#         end = len(table) if end>len(table) else end
#
#         print('-'*40)
#         for num in range(start,end,skip):
#             row = table[num]
#             print(' | '.join(row))
#
#     # user wants to export the table (list of lists) into a dictionary
#     elif selection == 8:
#         data = []
#         for row in table[1:]:
#             d = {}
#             for i,header in enumerate(table[0]):
#                 d[header] = row[i]
#             data.append(d)
#
#         print(data)
#
#
#     print('-'*40)
#     repeat = input('Press enter to repeat or q to quit: ')
#
#     if repeat == 'q':
#         break


# 9.2
some_string = 'For loops support iteration protocol'
for index, char in enumerate(some_string):
    if index % 2 == 0:
        char = char.upper()
    print(char, end = '')
