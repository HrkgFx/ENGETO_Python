# print('3.1/')
# DAYS=['Monday' , 'Thuesday' , 'Wensday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday']
#
# day=input("Enter any name of a day in a week, I will return its number:")
# if day == "":
#     print('Not input provided.')
# day_num = DAYS.index(day) + 1 # list.index(to co hledame)
# print('The number ' + str(day) + ' is ' + str(day_num))

# s='Ahoj'.find('Y')
# print(s) # kdyz nenajde vrati -1


print('3.2/')

e1='mr.reilly@gmail.com'
e2='john55@yahoo.com'
e3='elgringo@atlas.sk'

at1=e1.find('@')
print(at1)
print(e1[0:at1+1]) #+1 mi vypisuje i zavinac, pridava znak navic
at2=e2.find('@')
print(e2[:at2])
at3=e3.find('@')
print(e3[:at3])

x1=e1.split('@') #oreze to podle zavinace
print(x1)
print(x1[0])

x2=e2.split('@') #oreze to podle zavinace
print(x2)
print(x2[0])

x3=e3.split('@') #oreze to podle zavinace
print(x3)
print(x3[0])
