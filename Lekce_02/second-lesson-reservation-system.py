destinations=['Prague','Wien','Brno','Svitavy','Zlín','Ostrava']
prices=[1000,1100,2000,1500,2300,3400]
discount_25=['Svitavy','Ostrava']
discount=0.75
line='-'
equal='='
board=79
lines=line*board
equals=equal*board

print(equals)
print('Welcome to our reservation system.')
print(lines)
print('''Our destinations:
    1 - Prague - 1 000 Kč
    2 - Wien - 1 100 Kč
    3 - Brno - 2 000 Kč
    4 - Svitavy - 1 500 Kč
    5 - Zlín - 2 300 Kč
    6 - Ostrava - 3 400 Kč   ''')
print(lines)
print('Our destinations with 25 % discount are Svitavy and Ostrava.')
print(equals)
selection_destination=input('Please enter the destination number to select:'))

#str.isdecimal() - pro ciselne hodnoty

if not 0 < selection_destination < len(destinations):
    print('We are sorry, but we can offer only those ' + str(len(destinations)) + ' destinations.')
else:
    destination = destinations[selection_destination-1]
    price = prices[selection_destination-1]
    if destination in discount_25:
        print('Lucky you! You have just earned 25% discount for your destination - ' + destination)
        input('Press ENTER to continue.')
        price *= 0.75


# if destination == 'Svitavy' or 'Ostrava':
#     price *= 0.75



print(equals)
print('registration'.upper())
print(lines)
print('In order to complete your reservations, please share few details about yourself with us.')
print(lines)
name=input('Please enter your name:')
print(lines)
surname=input('Please enter your surname:')
print(equals)
year_of_birth=input('Please enter your year of birth:')

if int(year_of_birth) > 2003:
    print('Sorry, but you are too young, for registration.')
else:
    print('Your age is ok.')

print(equals)
email=input('Please enter your email:')

# if not('@' in email and '.' in email):
#     print('Your email is not correct, missing @ or .')
# else:
#     print('Your email is ok.')

if not('@' in email and '.' in email):
    print('Your email is not correct, missing @ and .')
elif not '@' in email:
    print('Your email is not correct, missing @.')
elif not '.' in email:
    print('Your email is not correct, missing .')
else:
    print('Your email is correct.')

print(lines)
password=input('Please enter your password:')
print(equals)

if len(password) < 8:
    print('Your password is too short.')
elif password[0].isdigit() or password[-1].isdigit():
    print("Your password has number at the start or end.")
elif password.isdigit() or password.isalpha():
    print("Your password have only numbers and letters.")

else:
    print('Your password is ok.')



print('Thank you '+name+'.')
print('We have made your reservation to ' + destination)
print('The total price is '+ str(price) +' Kč')
print(equals)
