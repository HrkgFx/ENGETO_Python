# 1 /First of all, the computer will generate a 4-digit secret number. The digits must be all different.
# 2/ Then, in turn, the user tries to guess their computer's number. The computer prompts the user for a number
# and after the input has been received, the computer responds with the number of matching digits.
# 3/ If the matching digits are in their right positions, they are "bulls", if in different positions, they are "cows".

import random
import time
import os.path

def generate_4num():
    '''
    generate random number (4 length) to the list with different numbers (0 - 9)
    '''
    four_num = []
    while len(four_num) < 4:
        num = random.randint(0,9)
        if num not in four_num:
            four_num.append(num)
    return (four_num)


def compare_num(gen_num, user_num):
    '''
    compare two number with with same length
    gen_num = searching number
    user_num = input from user
    '''
    bulls, cows = [0,0]
    for i in range(len(gen_num)):
        for j in range(len(user_num)):
                #kdyz se indexy a hodnoty na indexech rovnaji pricti k bulls +1
            if (i == j) and (gen_num[i] == user_num[j]):
                bulls += 1
                #kdyz se indexy nerovnaji a hodnoty rovnaji pricti k bulls +1
            elif (i != j) and (gen_num[i] == user_num[j]):
                cows += 1
            else:
                pass
    return bulls, cows


print("Hi there!\nI've generated a random 4 different digit number for you.\nLet's play a Bulls and Cows game.")
name = input('Enter your name: ')
# generate searching number
gen_num = generate_4num()
# print('Generated number is:',gen_num)

line = 66 * '-'
result = [0,0]
attempts = 0

# create file with header if file not exists
if not os.path.exists('all_results.txt'):
    with open('all_results.txt', mode = 'a') as tab_header:
        table = tab_header.write(f'Name, Number of attempts, Searching time\n')

# start counting time
start = time.time()
while result[0] != 4:
    #transfer string input to list with int - map(function, iterables)
    try:
        user_number = list(map(int, input('Enter a 4 digits number with different numbers: ')))
        attempts += 1
        if len(user_number) != len(gen_num):
            print(line)
            print("Your entered number didn't has 4 digits. Try again.")
            print(line)
        elif len(user_number) == len(set(user_number)):
            result = compare_num(gen_num, user_number)
            print(f'BULLS {result[0]} and COWS {result[1]}')
            print(line)
        else:
            print(line)
            print('You are enter number which contain same digits. Try it again.')
            print(line)
    except ValueError:
        print(line)
        print("You didn't enter number. Try it again.")
        print(line)

if attempts = 1:
    score = 'You are GOD of all Cow and Bulls'
elif attempts <= 10:
    score = 'Amazing'
elif attempts <= 15:
    score = 'Good'
elif attempts <= 20:
    score = 'Average'
elif attempts > 20:
    score = 'Not so good'

look_num = ''.join(str(i) for i in gen_num)
elapsed_time = time.time() - start
r_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

with open('all_results.txt', mode = 'a') as ap_f:
    complete_results = ap_f.write(f'{name}, {attempts}, {r_time}\n')

print(f"{score}, you've guessed number {look_num} in {attempts} guesses! Guessed time for number is {r_time}")



# variable_name = expression1 if condition else expression2

# results = list(map(int, results))

# x = list(str(1235443545548484355435434455))
# print(x)

# import random
#
# def compare_numbers(number, user_guess):
#     cowbull = [0,0] #cows, then bulls
#     for i in range(len(number)):
#         if number[i] == user_guess[i]:
#             cowbull[1]+=1
#         else:
#             cowbull[0]+=1
#     return cowbull
#
# if __name__=="__main__":
#     playing = True #gotta play the game
#     number = str(random.randint(0,9999)) #random 4 digit number
#     guesses = 0
