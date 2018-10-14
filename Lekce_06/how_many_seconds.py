# the number of hours can be represented by the numbers between 0 and 12
# the number of minutes can be represented by the numbers between 0 and 59
# the AM and PM flag should signal, whether it is afternoon (PM) or morning (AM)
# For example, if input is 3900, then 3900 seconds have passed since midnight So the program should prin 1:05 AM.

def add_zero(time):
    if len(str(time)) == 1:
        time = "0" + str(time)
    return time

seconds = int(input('Please enter the number of seconds since midnight: '))

hours,remain_sec = divmod(seconds,3600) #return number and remain
minutes,sec  = divmod(remain_sec,60)
eng_time = hours if hours == 12 else hours % 12
am_pm = 'AM' if hours <= 12 else 'PM'



eng_time864 = add_zero(eng_time)
minutes = add_zero(minutes)
sec = add_zero(sec)

print(f"It's: {eng_time}:{minutes}:{sec} {am_pm}")
