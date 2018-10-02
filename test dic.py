# x={3: 2, 1: 2, 6: 1}
#
# print('Toto ' + str(x.get(3)))
#
# start = 1
# while start < 10:
#     print(start)
#     if start in x.keys():
#         key = x.get(start)
#         stars = int(key) * '*'
#         print(str(start) + ' ' + str(stars) + ' ' + str(key))
#         start += 1
#     else:
#         start += 1

# print(round(233.03, -2)) #zaokrouhluje na desitky, -1 na stovky, pokud pridam rad, tak dle radu

city = input('What city do you live in? ')
size = int(input('How many people live in your city? '))
how = 'big' if size > 1000 else 'small'
print('If there are %d people living in %s, the it is %s city' %(size,city,how))
