import random

#
# values = range(1,101)
#
# for num in values:
#     if num % 3 == 0 and num % 5 == 0: #elif num % 15 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)

a,b,c = [1,2,3]
print(a)
print(b)
print(c)
a,b,c = 1,2,3
print(a)
print(b)
print(c)

letter1, letter2, letter3, letter4 = 'John'
print(letter1)
print(letter2)
print(letter3)
print(letter4)

name, surname = 'Rob', '28'
print(name, surname)

a,b,c = range(3)
print(a)
print(b)
print(c)

d = {'name':'John', 'surname':'Snow'}
jmeno, prijmeni = d
print (jmeno)
print(prijmeni)
#vytiskne klice

jmeno, prijmeni = d.values()
print (jmeno)
print(prijmeni)
#vytiskne hodnoty

jmeno, prijmeni = d.items()
print (jmeno)
print(prijmeni)
#vytiskne vytiskne klic,hodnota

name1, rest = 'Hans', ('Helmut', 'Gerhard')

print(name1)
print(rest)

((a,b),c,) = ('Mo','re')
print(a)

first, *rest = range(10)
print(first)
print(rest)
# * rozbaluje zbyvajici hodnoty do listu

first, *rest = d
print(first)
print(rest)

first,*mid, last = range(10)
print(first)
print(mid)
print(last)


a,*b,c,d = 1,2,3
print(a,b,c,d)
# vrati prazdny list


*a,='abcd'
print(a)
# carka dava informaci o tom, ze vraci list / tuple

# addition	a += b	a = a + b
# subtraction	a -= b	a = a - b
# multiplication	a *= b	a = a * b
# true division	a /= b	a = a / b
# floor division	a //= b	a = a // b
# modulo	a %= b	a = a % b
# power	a **= b	a = a ** b


def add_two(a,b):
    return a + b

print(add_two(10,30))

def repeat_char(char, num_repetitions):
    return char * num_repetitions

print(repeat_char('*',48))


def max(sequence):
    max_item = sequence[0] #bere prvni hodnotu z listu

    for item in sequence[1:]:
        if max_item < item:
            max_item = item

    return max_item

print(max([0,1,2,3,5,65,4,15,897,23]))


def all_title(words):

    for word in words:

        if not word.istitle():
            return False

    print('Bye')
    return True

print(all_title(['Bob','Frank','mike', 'John']))


def show_board(size):
    index = 0

    for row in range(size):
        print()

        for col in range(size):
            index += 1
            char = '#' if index % 2 == 1 else ' '
            print(char, end='')
    print()

print(show_board(15))


def sum_range(from_num,to_num):
    result = 0
    for number in range(from_num, to_num):
        result += number
    return result

print(sum_range(3,10))


result = all([True, False, True, True])
print(result)


def to_kilograms(weight):
    return weight * 0.45

def to_meters(height):
    return height * 0.025

def bmi(weight, height):
    return to_kilograms(weight) / to_meters(height) **2


print(random.randrange(1,100))
print(random.random())
print(random.uniform(1, 100))

lst = [45, 21, 53, 1, 213, 43, 42, 85]
random.shuffle(lst)
print(lst)
random.shuffle(lst)
print(lst)


words = ['hello', 'new', 'write', 'car', 'notebook']
print(words)
word = random.choice(words)
guess = input('Guess the word: ')
result = 'guessed' if guess == word else 'not guessed'
print(result)
print(word)

# random.randrange(start,stop,step)
# random.randint(start,stop)
# random.sample(population, k)

ids = ['X5235', 'X6752']
id = random.randint(1000, 9999)
if 'X' + str(id) not in ids: ids.append('X' + str(id))
print(ids)
