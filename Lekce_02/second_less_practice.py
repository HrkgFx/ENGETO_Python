line = 22 * '*'
#3.3
print('#3.3')
text1 = 'Hello'
text2 = text1 * 5
list1 = list(text1)
list2 = [text1] + list(text2)

print('text1 ' + str(text1) + ' is ' + str(len(text1)) + ' chars length')
print('text2 = text1 * 5 is' + str(text2) + ' is ' + str(len(text2)) + ' chars length')
print('list1 = list(text1) is ' + str(list1) + ' is ' + str(len(list1)) + ' chars length')
print('list2 = [text1] + list(text2) is ' + str(list2) + ' is ' + str(len(list2)) + ' chars length')

# r=len(input('Zadej retezec 4 - 6 znaku dlouhy: '))
# if r >6:
#     print('Too long.')
# elif r<4:
#     print('Too short.')
# else:
#     print('This is ok.')

#3.4
print('\n#3.4')

city = 'New York'
# result1 = 'ew' in city
print(city)
if 'ew' in city:
    print("'ew' is in city")
else:
    print("'ew' is not in city")

name = ['Helga','Herta','Helmut']
# result2 = 'Helmi' in names
print(name)
if 'Helga' in name:
    print("'Helga' is in name")
else:
    print("'Helga' is not in name")

#3.5
print('\n#3.5')
r=0
print(str(r) + " - bool(" + str(r) + ") is " + str(bool(r)))
r=0.0
print(str(r) + " - bool(" + str(r) + ") is " + str(bool(r)))
r=''
print(str(r) + " - bool(" + str(r) + ") is " + str(bool(r)))
r=[]
print(str(r) + " - bool(" + str(r) + ") is " + str(bool(r)))
r=False
print(str(r) + " - bool(" + str(r) + ") is " + str(bool(r)))
r=None
print(str(r) + " - bool(" + str(r) + ") is " + str(bool(r)))
print(line)
#7.1
print('7.1.')
my_str = 'pPython'
result = ''

if my_str.istitle():
    result = 'Titlecased'
else:
    result = 'Not titlecased'
print(result)

my_str = 'Python'
result = 'Titlecased' if my_str.istitle() else 'Not titlecased'
print(result)
