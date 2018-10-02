'''
author = Robin Jancarik
'''
TEXTS = [
'''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''',

'''Ahoj, 123H, jak to dneska jde? CO?
400 jak se Mas 50?
'''
]

registered = {'bob' : '123',
            'ann' : 'pass123',
            'mike' : 'password123',
            'liz' : 'pass123'
}
separator_line = 86 * '-'

print(separator_line)
print('Welcome to the Text Analyzer application \nPlease login to system:')
print(separator_line)

while True:
    login = input('Login: ')
    password = input('Enter your password: ')
    if registered.get(login) != password:
        print('Wrong password or login, try again.')
        print(separator_line)
    elif registered.get(login) == password:
        print('Welcome to system.')
        break

print(separator_line)
print('We have 3 texts to be analyzed.')

#TRY/ELSE BYCH SE PROZATÍM VYHNUL
while True:
    try:
        while True:
            select = int(input('Select the text which would be analyzed. Enter a number between 1 and ' + str(len(TEXTS)) + ': '))
            if select not in range(1,len(TEXTS)+1):
                print('Select number is not between 1 - ' + str(len(TEXTS)) + ': ')
                print(separator_line)
            else:
                break
    except ValueError:
        print ('You are not entered number.')
        print(separator_line)
    else:
        break

print(separator_line)

# number of words in total
remove_lines = TEXTS[select - 1].splitlines()
# print(str(remove_lines))
#ZBYTEČNĚ SLOŽITÉ ODSTRAŇOVÁNÍ 'TOXICKÝCH' ZNAKŮ
remove_lines = ' '.join(remove_lines)
remove_lines = remove_lines.replace(",","")
remove_lines = remove_lines.replace(".","")
remove_lines = remove_lines.replace("?","")
remove_lines = remove_lines.replace("!","")
remove_lines = remove_lines.replace("''","")
remove_lines = remove_lines.replace("(","")
remove_lines = remove_lines.replace(")","")
remove_lines = remove_lines.replace("[","")
remove_lines = remove_lines.replace("]","")
remove_lines = remove_lines.replace("/","")
remove_lines = remove_lines.replace('<',"")
remove_lines = remove_lines.replace('>',"")
remove_lines = remove_lines.replace('$',"")
remove_lines = remove_lines.replace('',"")
remove_lines = remove_lines.replace('''""''',"")
# print(remove_lines)
individual_words = remove_lines.split(" ")
# print(individual_words)
number_words = len(remove_lines.split(" "))
print('There are ' + str(number_words) + ' words in the selected text.')

#VŠECHNY ANALYTICKÉ SMYČKY SE DAJÍ SLOUČIT DO JEDNÉ

# number of words starting with capital letter
#NEMUSÍŠ VYMÝŠLET SLOŽITÝ ALGORITMUST, NA ROZPOZNÁNÍ TOHOTO EXISTUJE METODA .istitle
start = 0
num_upp_words = 0
while start < number_words:
    if individual_words[start][0].isupper():
        start += 1
        num_upp_words += 1
    else:
        start += 1

print('There are ' + str(num_upp_words) + ' words starting with capital letter in the selected text.')

# number of uppercase words
start = 0
num_upp_words = 0
while start < number_words:
    if individual_words[start].isupper():
    # if individual_words[start].isupper() and individual_words[start].isalpha():
        start += 1
        num_upp_words += 1
    else:
        start += 1
print('There are ' + str(num_upp_words) + ' uppercase words in the selected text.')

# number of lowercase words
start = 0
num_low_words = 0
while start < number_words:
    if individual_words[start].islower():
        start += 1
        num_low_words += 1
    else:
        start += 1
print('There are ' + str(num_low_words) + ' lowercase words in the selected text.')

# number of numeric-only words (e.g. 100, not 100N)
start = 0
num_dig = 0
while start < number_words:
    if individual_words[start].isdigit():
        start += 1
        num_dig += 1
    else:
        start += 1
print('There are ' + str(num_dig) + ' numeric strings in the selected text.')
print(separator_line)

# Bar chart depicting the frequencies of word lengths

freq_word = []
start = 0
while start < number_words:
    freq_word.append(len(individual_words[start]))
    start += 1

# print(individual_words)
# print(freq_word)

num_dict = {}
start = 0
while start < number_words:
    #TOTO ŘEŠÍ METODA .get KTERÉ MŮŽEŠ JAKO DRUHÝ ARGUMENT DÁT HODNOTU, KTERÁ SE PŘIŘADÍ KE KLÍČI, KTERÝ SE SNAŽÍŠ ZÍSKAT A JEŠTĚ NEEXISTUJE.
    if freq_word[start] in num_dict.keys():
        num_dict[freq_word[start]] += 1
        start += 1
    else:
        num_dict[freq_word[start]] = 1
        start += 1

# print (num_dict)

start = 1
# print(num_dict.get(start))
while start < 44: #SEM BY ŠLO TU HORNÍ HRANICI ZADÁVAT NĚJAK DYNAMICKY
    if start in num_dict.keys():
        key = num_dict.get(start)
        stars = int(key) * '*'
        print(str(start) + ' ' + str(stars) + ' ' + str(key))
        start += 1
    else:
        start += 1

print(separator_line)

# TOTO SE OPĚT DÁ ZAHRNOUT DO JEDNÉ VELKÉ SMYČKY, KDE SE BUDE ANALYZOVAT VŠECHNO NAJEDNOU
# Calculate the sum of all the numeric "words" in the given text
start = 0
num_dig = 0
while start < number_words:
    if individual_words[start].isdigit():
        num_dig += int(individual_words[start])
        start += 1
    else:
        start += 1
print('If we summed all the numbers in this text we would get: ' + str(num_dig))
print(separator_line)
