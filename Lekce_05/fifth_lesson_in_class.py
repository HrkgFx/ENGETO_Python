# # pro neco v necem najdi
# for pismeno in 'abcde':
#     print(pismeno)
#
line=(9*'*')
#
# for pismeno in 'abcde'[2:5]:
#     print(pismeno)


# nums = ['421',867,65, '93', 45, 82]
# i = 0
# result = 0
#
# while i < len(nums):
#     result = result + int(nums[i])
#     i = i + 1
# print(str(result))

# for x in nums:
#     result = result + int(x)
# print(str(result))



# names = ['Jakub', 'Jana', 'Petr', 'Klara', 'jaja']
#
# for cokoliv in names:
#     if cokoliv[0]  =='J' or cokoliv[0]  =='j':
#         print(cokoliv)

# for item in 1234567:
#     print(item)
# ERROR

# for item in 'abcdefghi':
#     print(item)

# for item in (1,2,3,4,5):
#     print(item)

# for item in {1,2,3,4,5}:
#     print(item)

# for item in {'name': 'Bob', 'age': 23, 'job':'plumber'}:
#     print(item)
# # tento zapis vypisuje jen klice
#
#
# r = range(9)
# print(r)
#
# for p in range(11):
#     print(p)
# # vypisuje jen do 10ky
#
# r = range(4,0,-1)
# for coko in r:
#     print(coko)
#
# x = [1,2,3,4,5,6][1:4]
# print(x)
#
# print(line)
#
# y = range(2, 5)
# for z in y:
#     print(z)
#
# print(line)
#
# u = range(1, 11, 2)
# for o in u:
#     print(o)
#
# print(line)
#
# r=range(1,7)[1:4]
# print(r)
# print(r[0])
#
# x=range(4, 0)
# print(x)
# for o in x:
#     print(o)
# #nic tam není
#
#
# names = ['Helmut', 'Helga', 'Harold', 'Hammet', 'Hetfield']
#
# for index in range(len(names)):
#     print(names[index])
#
#
# for i in range(0,len(names),2):
#     print(i,names[i])
#
#
# numbers = [321,45,32,12,54]
# for index, number in enumerate(numbers):
#     if index % 2 == 0:
#         print(number, ':', number**2)

# enumerate - svaze hodnoty s indexem


# text = '''
# Situated about 10 miles west of Kemmerer,
# Fossil Butte is a ruggedly impressive
# topographic feature that rises sharply
# some 1000 feet above Twin Creek Valley
# to an elevation of more than 7500 feet
# above sea level. The butte is located just
# north of US 30N and the Union Pacific Railroad,
# which traverse the valley.'''
#
# target = input('SEARCH WORD: ')
#
# words = text.split()
# found = False
# for i,word in enumerate(words):
#     word = word.strip(';,._/:') #maze znaky ktere predame dokud nenarazi na jiny ,.p.e s:/ - maze veci jen na okrajich stringu
#     if word == target:
#         found = True
#         position = i + 1
#
# if found:
#     print('POSITION: ' + str(position))
# else:
#     print('NO SUCH WORD')


# if
# break

# if
# continue



# nums = ['421',867,65, '93', 45, 82]
# result = 0
#
# for x in nums:
#     if type(x) == int:
#     # if not type(x) == int:
#     #     continue
#         result = result + int(x)
#
# print(result)
#
#
#
# nums = ['421',867,65, '93', 45, 82]
# result = 0
#
# for x in nums:
#     if not type(x) == int:
#         continue
#     result = result + x
#
# print(result)
#
# # vypsani vsech lichych cisel
# a = range(20)
# for x in a:
#     if x % 2 == 0:
#         continue
#     print(x)
#
#
# print(line)
#
# a = range(20)
# search = 20
#
# for x in a:
#     if x == search:
#         print('Nasel jsem cilo ', x)
#         break
#     else:
#         print(x*2)
# else:
#     print('Nenašel jsem.')

# views in dictionaries

slovnik = {'A':1, 'B':2, 'C':3}
klice = slovnik.keys()
hodnoty = slovnik.values()
oboje = slovnik.items()

print(klice, hodnoty, oboje)
print(list(klice))
print(list(klice)[1])
print(list(hodnoty))
print(list(oboje))
print(list(oboje)[0])
print(list(oboje)[0][1]) #hodnota v tuplu na 0 indexu a hodnota na 1 indexu v tuplu

print(line)

for hodnota in hodnoty:
    print(hodnota)

#ERROR
# for par in hodnoty:
#     print(par[0])

print(line)

for par in oboje:
    for vec in par:
        print(vec)
