# import random
# import time
# import os.path
# from operator import itemgetter
#
# play_game = True
# while play_game:
#     print('AHOJ')
#     ############# result parts #############
#     #print row in all_results.txt
#     def row_table (top_score):
#         for index,value in enumerate(top_score):
#             print("|{0:^12}|{1:^12}|{2:^18}|".format(*top_score[index]))
#         print(t_line)
#
#     with open('all_results.txt') as rs:
#         result_line = rs.readlines()
#
#     # remove next line \n
#     result_line = [line.strip('\n') for line in result_line]
#
#     # convert to list from file - row is one item in list
#     to_list = [item.split(', ') for item in result_line]
#
#     # transform str to int on index 1 on attempts
#     for x in to_list[1:]:
#         x[1] = int(x[1])
#
#     #sort list by first index - attempts
#     top_score = sorted(to_list[1:], key=itemgetter(1))
#     #sort list by second index - time
#     top_time = sorted(to_list[1:], key=itemgetter(2))
#
#     #counting length header
#     len_header = len(("|{0:^12}|{1:^12}|{2:^18}|".format(*to_list[0])))
#
#     #horizontal table line
#     t_line = len_header * '-'
#
#     again = True
#     while again:
#         print("What do you want to do next?\n[A] - Play again, [R] - Show best results, [Q] - Quit Game")
#         what_next = input('Enter letter for your choice: ')
#
#         if what_next == 'Q' or 'q':
#             play_game = False
#             again = False
#
#         elif what_next == 'R' or 'r':
#
#             #header table
#             print()
#             print('{0:^46}'.format('TOP TEN SCORE BY ATTEMPTS'))
#             print(t_line)
#             print("|{0:^12}|{1:^12}|{2:^18}|".format(*to_list[0]))
#             print(t_line)
#             row_table(top_score)
#
#             print()
#             print('{0:^46}'.format('TOP TEN SCORE BY TIME'))
#             print(t_line)
#             print("|{0:^12}|{1:^12}|{2:^18}|".format(*to_list[0]))
#             print(t_line)
#             row_table(top_time)
#
#         elif what_next == 'A' or 'a':
#             again = False
#         else:
#             print('You are enter unknow choice. Try again.')
#             continue



# play_game = True
# while play_game:
#     print('AHOJ')
#     what_next = input('Enter letter for your choice: ')
#
#     if what_next == 'A':
#         print('A')
#         break
#     elif what_next == 'B':
#         print('B')
#     elif what_next == 'C':
#         print('C')
#         pass
#     elif what_next == 'D':
#         print('D')
#     else:
#         print('Zadal si sracku')

x = {'q','Q','r','R','a','A'}
print(x)
again = False
while not again:
    print("What do you want to do next?\n[A] - Play again, [R] - Show best results, [Q] - Quit Game")
    what_next = input('Enter letter for your choice: ')
    if what_next in x:
        if what_next == 'Q':
            play_game = True
            again = True
            print('CUS')

        elif what_next == 'R':
            print('R')
            # #header table
            # print()
            # print('{0:^46}'.format('TOP TEN SCORE BY ATTEMPTS'))
            # print(t_line)
            # print("|{0:^12}|{1:^12}|{2:^18}|".format(*to_list[0]))
            # print(t_line)
            # row_table(top_score)
            #
            # print()
            # print('{0:^46}'.format('TOP TEN SCORE BY TIME'))
            # print(t_line)
            # print("|{0:^12}|{1:^12}|{2:^18}|".format(*to_list[0]))
            # print(t_line)
            # row_table(top_time)

        elif what_next == 'A':
            again = False
        else:
            print('You are enter unknow choice. Try again.')
            continue
    else:
        print('Your enter is not correct. Try again.')
