'''
author = Engeto
'''
TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

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
garpike and stingray are also present.'''
]


# 1. Greet or welcome the user to the app
# 2. Ask the user for entering username and password
# 3. Check whether the password and username entered are among
# those registered.

# The registered username - password pairs:

# | USER |   PASSWORD  |
# -----------------------
# | bob  |     123     |
# | ann  |    pass123  |
# | mike | password123 |
# | liz  |    pass123  |

# If you consider this task difficult, then just check,
# whether the username and password entered are among
# the registered, without taking care of pairing them
# together.

credentials = {'bob': '123', 'ann': 'pass123',
                'mike': 'password123', 'liz': 'pass123'}

print('-' * 40)
print('Welcome to the app. Please log in:')

user = input('USERNAME: ')
password = input('PASSWORD: ')

if credentials.get(user) != password:
    print('ACCESS DENIED')
    print('Incorrect password or username')
    quit()


# 4. Ask the user to select among the three texts
# stored in the variable TEXTS.
print('-' * 40)
print('We have 3 texts to be analyzed.')

sel = int(input('Enter a number btw. 1 and 3 to select: '))

print('-' * 40)
text = TEXTS[sel-1]

dirty_words = text.split()


words = []

while dirty_words:
    word = dirty_words.pop()
    word = word.strip('.,:/;')
    if word: words.append(word)




# 5. Calculate the following statistics for the
# selected text:
#   - number of words in total
#   - number of words starting with capital letter
#   - number of uppercase words
#   - number of lowercase words
#   - number of numeric-only words (e.g. 100, not 100N)

print('There are ' + str(len(words)) + ' words in the selected text.')

titlecase = 0
lowercase = 0
uppercase = 0
numeric   = 0
counts    = {}
num_sum   = 0
i = 0
while i < len(words):

    if words[i].istitle():
        titlecase = titlecase + 1
    elif words[i].isupper():
        uppercase = uppercase + 1
    elif words[i].islower():
        lowercase = lowercase + 1
    elif words[i].isnumeric():
        numeric = numeric + 1
        num_sum = num_sum + float(words[i])

    l = len(words[i])
    counts[l] = counts.get(l,0) + 1

    i = i + 1

print('There are ' + str(titlecase) + ' titlecase words')
print('There are ' + str(uppercase) + ' uppercase words')
print('There are ' + str(lowercase) + ' lowercase words')
print('There are ' + str(numeric) + ' numeric strings')
print('-' * 40)

# 6. Create a bar chart depicting the frequencies
# of word lengths in the text. For example:

#  1 * 1
#  2 *********** 11
#  3 *************** 15
#  4 ********* 9
#  5 ********** 10


# In the above chart, there is one word of length 1,
# 11 words of length 2, 15 words of length 3 etc.

lengths = sorted(counts)

i= 0
while i < len(lengths):
    length = lengths[i]
    frequency = counts[length]

    if len(str(length)) == 1:
        str_len = ' ' + str(length)
    else:
        str_len = str(length)
    print(str_len, '*' * frequency, frequency)
    i = i + 1


# 7. Calculate the sum of all the numeric "words" in
# the given text. For example the sum for the string
# below would be 8500:

# "that rises sharply some 1000 feet above
# Twin Creek Valley to an elevation of more
# than 7500 feet above sea level. The butte
# is located just north of US 30N"
print('-' * 40)
print('If we summed all the numbers in this text we would get: ' + str(num_sum))
print('-' * 40)
