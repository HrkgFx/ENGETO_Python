# 1 /First of all, the computer will generate a 4-digit secret number. The digits must be all different.
# 2/ Then, in turn, the user tries to guess their computer's number. The computer prompts the user for a number
# and after the input has been received, the computer responds with the number of matching digits.
# 3/ If the matching digits are in their right positions, they are "bulls", if in different positions, they are "cows".
# Bonus
# Extend the functionality of the program as you wish. For example
# Counting time it took to guess the number
# Count the number of guesses and store them in a file and at the end depict user's stats (the best player etc.)


import random
import time
import os
import os.path
from operator import itemgetter


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

play_game = False
while not play_game:
    line = 78 * '-'
    print(line)
    print("|{0:^76}|".format("Ahoj!") + "\n" + "|{0:^76}|".format("Bylo vygenerováno číslo s 4 různými čísly.") + "\n" + "|{0:^76}|".format("Když je číslice v čísle na správném místě je to BÝK, jinak jako KRÁVA."))
    print(line)
    name = input('Zadej svoje jméno: ')
    # generate searching number
    gen_num = generate_4num()
    # print('Generated number is:',gen_num)

    result = [0,0]
    attempts = 0

    # create file with header if file not exists
    if not os.path.exists('all_results_cz.txt'):
        with open('all_results_cz.txt', mode = 'a') as tab_header:
            table = tab_header.write(f'Jméno, Počet pokusů, Čas uhodnutí\n')

    # start counting time
    start = time.time()
    while result[0] != 4:
        #transfer string input to list with int - map(function, iterables)
        try:
            user_number = list(map(int, input('Zadej 4 rozdílné čísla: ')))
            attempts += 1
            if len(user_number) != len(gen_num):
                print(line)
                print("Nezadal jsi 4 místné číslo. Zkus to znovu.")
                print(line)
            elif len(user_number) == len(set(user_number)):
                result = compare_num(gen_num, user_number)
                print(f'Býci {result[0]} a Krávy {result[1]}')
                print(line)
            else:
                print(line)
                print('Číslo obsahuje stejné číslice. Zkus to znovu.')
                print(line)
        except ValueError:
            print(line)
            print("Nezadal jsi číslo, zkus to znovu.")
            print(line)

    #score results
    if attempts == 1:
        score = 'Jsi bůh býků a krav!'
    elif attempts <= 10:
        score = 'Úžasné'
    elif attempts <= 15:
        score = 'Dobré'
    elif attempts <= 20:
        score = 'Průměrné'
    elif attempts > 20:
        score = 'Nic moc :('

    #merged list numbers to string numbers
    look_num = ''.join(str(i) for i in gen_num)
    elapsed_time = time.time() - start
    # transform to time hours:minutes:seconds
    r_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

    # adding results to file
    with open('all_results_cz.txt', mode = 'a') as ap_f:
        complete_results = ap_f.write(f'{name}, {attempts}, {r_time}\n')

    print(f"{score}, uhodl jsi číslo {look_num} v {attempts} pokusech! \nČas pro nalezení čísla je {r_time}")
    print(line)

    ############# result parts #############
    #print row in all_results.txt
    def row_table (top_score):
        '''
        Generate table from nested list with 3 items in list
        '''
        for index,value in enumerate(top_score):
            if index < 10:
                print("|{0:^12}|{1:^12}|{2:^18}|".format(*top_score[index]))
            else: break
        print(t_line)

    with open('all_results_cz.txt') as rs:
        result_line = rs.readlines()

    # remove next line \n
    result_line = [line.strip('\n') for line in result_line]

    # convert to list from file - row is one item in list
    to_list = [item.split(', ') for item in result_line]

    # transform str to int on index 1 on attempts
    for x in to_list[1:]:
        x[1] = int(x[1])

    #sort list by first index - attempts
    top_score = sorted(to_list[1:], key=itemgetter(1))
    #sort list by second index - time
    top_time = sorted(to_list[1:], key=itemgetter(2))

    #counting length header
    len_header = len(("|{0:^12}|{1:^12}|{2:^18}|".format(*to_list[0])))
    #horizontal table line
    t_line = len_header * '-'

    #loop for menu after game
    again = False
    while not again:
        #set of choices in menu
        choices = {'a','r','q','A', 'R', 'Q'}
        print("Co chceš dělat dál?\n[A] - Hrej znovu, [R] - Ukaž nejlepší výsledky (TOP 10), [Q] - Ukonči hru")
        what_next = input('Zadej písmeno pro volbu: ').lower()
        if what_next in choices:
            #quit game
            if what_next == 'q':
                play_game = True
                again = True
                break
            #print best results
            elif what_next == 'r':
                #header table top by attempts
                print()
                print('{0:^46}'.format('TOP 10 hráčů, dle pokusů'))
                print(t_line)
                print("|{0:^12}|{1:^12}|{2:^18}|".format(*to_list[0]))
                print(t_line)
                row_table(top_score)
                #header table top by time
                print()
                print('{0:^46}'.format('TOP 10 hráčů, dle času'))
                print(t_line)
                print("|{0:^12}|{1:^12}|{2:^18}|".format(*to_list[0]))
                print(t_line)
                row_table(top_time)
            #play again
            elif what_next == 'a':
                again = True
                # clear screen for windows
                os.system('cls')
                # clear screen for linux
                # os.system('clear')
            else:
                print('Neznámí vstup. Zkus to znovu.')
                continue
        else:
            print('Nezadal jsi určené písmena. Zkus to znovu.')
