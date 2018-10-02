destinations=['Prague','Wien','Brno','Svitavy','Zlín','Ostrava']
prices=[1000,1100,2000,1500,2300,3400]
discount_25=['Svitavy','Ostrava']
discount=0.75
line='-'
equal='='
board=79



print(equal*board)
print('Welcome to our reservation system.')
print(line*board)
print('''Our destinations:
    1 - Prague - 1 000 Kč
    2 - Wien - 1 100 Kč
    3 - Brno - 2 000 Kč
    4 - Svitavy - 1 500 Kč
    5 - Zlín - 2 300 Kč
    6 - Ostrava - 3 400 Kč   ''')
print(line*board)
print('Our destinations with 25 % discount are Svitavy and Ostrava.')
print(equal*board)
selection_destination=int(input('Please enter the destination number to select:'))

destination = destinations[selection_destination-1]
price = prices[selection_destination-1]

print(equal*board)
name=input('Please enter your name:')
print(line*board)
surname=input('Please enter your surname:')
print(equal*board)
year_of_birth=input('Please enter your year of birth:')
print(equal*board)
email=input('Please enter your email:')
print(line*board)
password=input('Please enter your password:')
print(equal*board)
print('Thank you '+name+'.')
print('We have made your reservation to ' + destination)
print('The total price is '+ str(price) +' Kč')
print(equal*board)

7/8/2018
# print(destinations)
# print(prices)
# print(discount_25)
#
# selection=4
# destination_4=(destinations[selection-1])
# price_4=(prices[selection-1]*discount)
#
# print('We have made your reservation to '+ destination_4)
# print('Price is ' + str(int(price_4))+' Kč.')
#
# age = int(input('What is your age: '))
# print(age)


# print(destinations,prices,discount_25)
#
# cara="-"*10
#
# mojeDestinace=destination[3]
# mojeCena=price[3]*0.75
# print("Vybral sis: ", mojeDestinace," - ", int(mojeCena), " Kc")
#
#
# print(int('12')+3)
# print ('assd'+str(3))
# print(type(mojeCena)) # rekne co to je za datovy typ
#
# jmeno=input('Zadej jmeno: ')
# vek=int (input('Zadej vek: '))
# print(jmeno)
# print(vek)
# print(type(vek))
