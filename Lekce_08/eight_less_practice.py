# # leap year = /4 /400
# # not leap year = /100
#
# def is_leap(year):
#     if year % 4 == 0:
#         result = True
#         if year % 100 == 0:
#             result = False
#             if year % 400 == 0:
#                 result = True
#     else:
#         result = False
#     return result
#
# x = int(input('Zadej rok: '))
# print(is_leap(x))
#
# # 2 moje
# def leap_year(year):
#     result = True if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else False
#     return result
#
# while 1:
#     x = int(input('Enter the year: '))
#     print(leap_year(x))
#
# # Onra
# def is_leap(rok):
#     return (rok % 4 == 0 and rok % 100 !=0) or (rok % 400 == 0)
#
# # ENGETO RESULT 1:
# def is_leap(y):
#     if ((y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)):
#         return True
#     else:
#         return False
#
# # ENGETO RESULT 2:
# def is_leap(y):
#     return ((y % 400 == 0) or (y % 4 == 0 and y % 100 != 0))


# variable_name = expression1 if condition else expression2

# # 3.1
# city = input('What city do you live in? ')
# size = int(input('How many people live in your city? '))
# how = 'big' if size > 1000 else 'small'
# print('If there are %d people living in %s, the it is %s city' %(size,city,how))

# celsius = int(input('What is the current temperature?'))
# fahrenheit = celsius * (9/5) + 32
# print('{} degrees Celsius would be {} degrees Fahrenheit.'.format(celsius, fahrenheit))

# name = input('Your First Name: ')
# surname = input('Your Surname: ')
# greeting = 'Nice to meet you {1}, {0}.'
# print(greeting.format(name,surname))

# n = input('Your First Name: ')
# s = input('Your Surname: ')
# greeting = 'Nice to meet you {surname}, {name}.'
# print(greeting.format(name=n,surname=s))

# full_name = ('John', 'Smith')
# greeting = 'Nice to meet you {1}, {0}.'
# print(greeting.format(*full_name))
