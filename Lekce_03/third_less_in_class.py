# print('Ahoj'[2]) #o
# print('Ahoj'[1:3]) #ho 3 index uz to nevypisuje
# print('Ahoj'[::2]) # [start,stop,step]
# print('Ahoj'[1:3:2]) #h [start,stop,step]
# print('Ahoj'[:-1]) #Aho - jde o krok zpet
# print('Ahoj'[::3]) #Aj
# print('Ahoj'[::-1]) #johA
# print('Ahoj jak se mas'[2:6:-1]) #''
# print('Ahoj jak se mas'[7:2:-1]) #kaj j
# print('Ahoj jak se mas'[8:1:-2]) # a o
# print([1,2,3,4,5,6,7,8,'ahoj','kocka'][8:1:-2]) #['ahoj',7,5,3]
#
# # help(str.isdecimal)
# print(print('ahoj')) #ahoj, None
#
#
# # name = 'Shawshank Redemption'
# # rating = 87
# # year = 1994
# # director = 'Frank Darabont'
# #
# #
# # cat = kocka
# # klic = slovo ktere
#
# # slovnik= {'name':'Shawshank Redemption', 'rating':{'csfd':98,'imbd':87}}
# slovnik= {'name':'Shawshank Redemption',
# 'rating':87,
# 'year':1994,
# 'director':'Frank Darabont'}
# print(slovnik)
#
# slovnik2 = dict(name = 'Forrest Gump', rating = 95, year = 1974, director = 'Frank Darabont')
# # print(slovnik2)
# #
# # print(slovnik2['year'])
#
# l1=[1,2,3,5]
# l1[-1]=4
# print(l1)
#
# slovnik['rating'] = 91
# print(slovnik)
#
# l1=[1,2,3,4]
# # l1[4]=5
# # # ERROR
# # print(l1)
#
# l1.append(5)
# print(l1)
#
# slovnik['ratig'] = 99
# print(slovnik)
#
# # del slovnik # smazani celeho slovniku
# # print (slovnik)
#
# del slovnik ['ratig'] # mazu tento klic
# print(slovnik)
#
# slovnik['starring'] = ['Tim Robbins', 'Morgan Freeman']
# slovnik['budget'] = 200
# print(slovnik)
#
# movies = {'DRAMA': slovnik, 'COMEDY': slovnik2}
# print(movies)
#
# categories=['DRAMA','COMEDY']
# print('We offers these categories:', categories ) #carka oddeluje ruzne druhy
# pick=input('Choose a category: ')
# print(movies[pick])


# SET - mnozina
A = set()
print(A)
print(bool(A))
#prvek v mnozine je unikatni a nezalezi na poradi
A=set('Hello')
print("A=set('Hello') and print(A) is ",A)

str1 = set('New York')
str2 = set('Yorkshire') # Y a y je rozdilne
str3 = set('Yellow')

# PRUNIK
print(str1 & str2)
print(str1.intersection(str2))

# ROZDIL
print(str1.difference(str2))
print(str1 - str2) # pismena ktere jsou ulozeny v STR1
print(str2 - str1)
print(str1 - str1)
print(str1 - str2 - str3)
print(str1.difference(str2, str3))

# Co je mimo prunik
print(str1 ^ str2)
print(str1.symmetric_difference(str2))

# UNION - sjednoceni
velka_mnozina = str1 | str2
print(velka_mnozina)

slov={'klic':'zamek'}
print(slov['klic'])
print(slov['klic1'])
print (slov.get('klic1'))
print (slov.update('klic1'))




# l1 = [1,2]
# l2 = l1
# l2.append(3)
# print(l1)
#
# # l2= l2 + [4]
# # print(l2)
#
# del l1[2]
# print(l2)
#
# del l1
# print(l2)
#
# l1 = [1,2]
# l2 = l1.copy()
# l2.append(3)
# print(l1)
# print(l2)
