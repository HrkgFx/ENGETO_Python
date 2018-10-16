# sachovnice 8x8
# moje noobacke reseni
pattern = [' ','#']
size_board = 8
odd_row = []
even_row = []

for i in range(size_board):
    if i % 2 == 0:
        odd_row.append(pattern[0])
    else:
        odd_row.append(pattern[1])
    if i % 2 == 0:
        even_row.append(pattern[1])
    else:
        even_row.append(pattern[0])

for x in range((size_board//2)):
    print(''.join(odd_row))
    print(''.join(even_row))

print(50*'-')

# systematictejsi reseni
size = 10
sym = ['#',' ']
desk = []

for row in range(size):
    line = []
    # print(r,'r')
    # print(row, 'row')
    for cell in range(size):
        i = (row+cell) % len(sym) # 0+0/2, 0+1/2
        line.append(sym[i])

    desk.append(''.join(line))

print('\n'.join(desk))

# FUNKCE
def show_board(size):
    index = 0

    for row in range(size):
        print()

        for col in range(size):
            index += 1
            char = '#' if index % 2 == 1 else ' '
            print(char, end='')
    print()

show_board(9)
