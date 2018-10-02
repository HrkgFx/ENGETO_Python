# #3
# # 2.0
#
# films = {'name': 'Shawsank Redeption',
#          'rating': 87,
#          'year': 1994,
#          'director': 'Frank Darabont'}
#
# print('Films is ' + str(films))
#
# films.update(staring =['Tim Robbins', 'Morgan Freeman'])
# films.update(budget = 200)
#
# print('Films is ' + str(films))
#
#
# # films.popitem()
# # print('Films is ' + str(films))
# # del films['budget']
# # print('Films is ' + str(films))
#
# films.pop('budget')
# print('Films is ' + str(films))
#
# movies={}
# movies.update(DRAMA=films)
# print('Movies is ' + str(movies))
#
# print('\nWe can currently offer: ')
#
# list_movies=list(movies)
# # print(list_movies)
# print(list_movies)
#
# genre=input('What genre are you interested in? ')
# print('\nHERE IT GOES')
# print(movies[genre])
#
# movies.clear()
# print('\nDatabase has been ERASED')
# print(movies)



# 4.7
my_db = {   'Name' : 'Robin Jancarik',
            'Age' : 32,
            'Address' : {'Street' : 'Novobohdalecka',
                'Street #' : '1484/18',
                'City' : 'Praha 10',
                'ZIP' : '110 00',
                'State' : 'Czech republic'
            },
            'Job': {'Job title' : 'System admin',
                    'Level' : 3}

}

print(my_db)
print(my_db['Address']['State'])
print(my_db['Job']['Level'])
print('My adress is: ' + my_db['Address']['Street'] + ' ' + my_db['Address']['Street #'] + ', ' + my_db['Address']['City'] + ' ' + my_db['Address']['ZIP'] + ', ' + my_db['Address']['State'])

print(my_db.get('Address'))
print(my_db.get('Salary','Chybí'))
print(my_db.get('Salary',0))
print(my_db.get('birth',"0.0.0000"))
print(my_db.get('age',0))

# 4.7
my_db.update({'Performance': {'Q1': 1, 'Q2':1, 'Q3':2, 'Q4':1}})
print(my_db['Performance'])
my_db.update(Name ='Rob H. Jancarik')
print(my_db)
my_db.update({'manager' : 'Samuel, Hunt'})
print(my_db)
del my_db['manager']
print(my_db)


# 5.2
my_set = set()
print(type(my_set))
my_set = frozenset()
print(type(my_set))
my_set = {'John', 'Rob'}
print(my_set)

print(set('Popocatepetl'))

s = set([1,2,4,2,5,6,4,3,3,'a'])
print(s)

print('\nUnion - sjednocení')
union=set('Hello') | set('Yellow') | set ('Fellow')
print(union)
union=set('Hello').union(set('Yellow'),set ('Fellow'))
print(union)

print('\nDifference - rozdíl')
difference=set('Hello') - set('Yellow') - set('Fellow')
print(difference)
difference=set('Hello').difference(set('Yellow'),set ('Fellow'))
print(difference)

print('\nSymmetric Difference - obsahuje prvky, které nejsou v jejich průniku')
symmetric_difference=set('Hello') ^ set('Yellow')
print(symmetric_difference)
symmetric_difference=set('Hello').symmetric_difference(set('Yellow'))
print(symmetric_difference)

print('\nIntersection - Průnik')
intersection=set('Hello') & set('Yellow') & set('Fellow')
print(intersection)
intersection=set('Hello').intersection(set('Yellow'),set ('Fellow'))
print(intersection)

subset=set('Hello') <= set('Yellow H')
print(subset)
subset=set('Hello') >= set('Yellow H')
print(subset)

subset=set('Hello').issubset(set('Yellow H'))
print(subset)

disjoint=set((1,2,3,4)) & set((6,7,8))
print(disjoint)
d=len({1,2,3,4} & {6,7,8})
print(d)
disjoint={1,2,3,4}.isdisjoint({6,7,8})
print(disjoint)

col=5 in {1,6,13,54,21,654,10,5}
print(col)

col=len({5,1,5,6,7,7})
print(col)

names = {'Marcus', 'Alex'}
names.add('Oliver')
print(names)

names2 = {'Marcus', 'Oliver', 'Alex'}
names2.add('Oliver')
print(names2)

names.discard('Oliver')
print(names)


# colors = ['green', 'blue', 'black', 'red', 'red', 'yellow', 'blue', 'grey', 'black' , 'red', 'green']
# color_counts = {}
#
# while colors:
#     color = colors.pop()
#
#     if color not in color_counts:
#         color_counts[color]=0
#
#     color_counts[color] = color_counts[color] + 1
#     print(color)
#     print(color_counts)
