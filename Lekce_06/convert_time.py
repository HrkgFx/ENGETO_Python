Please enter your time: 17 : 35
Converted to English: 5 : 35 PM

while True:
    time = input('Please enter your time: ')
    hours, mins = time.split(':')
    hours = int(hours)

    if hours >= 12:
        eng_hours = hours - 12
        print('Converted time is: {}:{} PM'.format(eng_hours,mins))
    else:
        print('Converted time is: {}:{} AM'.format(hours,mins))


time = input('Please enter your time: ')

hours, mins = time.split(':')

# variable_name = expression1 if condition else expression2
adjusted_h = hours if int(hours)==12 else str(int(hours) % 12)

daytime = ['AM','PM'][int(hours)>=12]

print('Converted to English: ' + adjusted_h + ':' + mins + ' ' + daytime)
