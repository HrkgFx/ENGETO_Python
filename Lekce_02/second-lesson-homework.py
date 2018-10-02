# 1/
# age=int(input('How old are you? '))
# year=2018-age
# print('You were propably born in ' + str(year) + '.')

# 2/
number=(input('Please enter the number of day:'))
DAYS=['Monday' , 'Thuesday' , 'Wensday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday']

if not number:
    print('Not input provided.')
elif number not in ['1','2','3','4','5','6','7']:
    print('Enter only number please.')
elif number > len(DAYS):
    print("I don't know how many days your universe, but in mine we have 7 days :)")
elif number == 0:
    print("I don't know how many days in your universe, but in mine we have 7 days :)")
else:
    day=DAYS[number-1]
    print('The day on ' + str(number) + ' is ' + day)
