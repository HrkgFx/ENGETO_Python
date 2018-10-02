# 8.1
# inpt = input('Hello, please write your numbers and press enter to confirm: ')
# nums = inpt.split(',')
# result = []
#
# for num in nums:
#     num = int(num.strip())
#     result.append(num)
#
# print('List:', result)

# 8.2
# numbers = [369, 22, 321, 64221, 5657, 8321]
# sums = []
#
# for num in numbers:
#     num_str = str(num)
#     sums.append(0)
#     # print(f'sums is {sums}')
#     # print(f'num_str is {num_str}')
#     for digit in num_str:
#         print(f'digit is {digit}')
#         print(f'sums[-1] is {sums[-1]}')
#         print(10*'-')
#         sums[-1] = sums[-1] + int(digit)
# print(sums)

# 8.3
# vowels = 'aeiouy'
# consonants = 'bcdfghjklmnpqrstvwxz'
# counts = {'cons':0,'vows':0}
# sentence = 'a speech sound that is produced by comparatively open configuration of the vocal tract'
#
# for letter in sentence:
#     if letter.isalpha():
#         if letter.lower() in vowels:
#             counts['vows'] = counts['vows'] + 1
#         else:
#             counts['cons'] = counts['cons'] + 1
#
# print(f"No. consonants: {counts['cons']} | No. vowels: {counts['vows']}")

# 8.4
# start = int(input('START: '))
# stop = int(input('STOP: '))
# divisor = int(input ('DIVISOR: '))
#
# output = []
#
# if divisor:
#     for num in range(start,stop+1):
#         if num % divisor == 0:
#             output.append(num)
#     print(f'Numbers in range({start},{stop}) divisible by {divisor}: {output}')
# else:
#     print('Cannot divide by zero')

# 8.5
# sentence = 'It was a bright, sunny day in May, and the church bell was just ringing'
# letters={}
#
# for letter in sentence:
#      letters.setdefault(letter, 0) #dict.setdefault(key, default=None)
#      letters[letter] = letters[letter] + 1
# print(letters)

# 8.6
# inp = input('Enter the number: ')
# if int(inp) % 2 == 0:
#     print('Even')
# else:
#     print('Odd')
#
# num = int(input('Please, enter a number: '))
# result = 'EVEN' if num % 2 == 0 else 'ODD'
# print(result)

# 8.7
# 65341345251
# number = input('Enter the number: ')
# iteration = 0
#
# while len(number) > 1:
#     iteration += 1
#     temp = 0
#     for num in number:
#         temp += int(num)
#     number = str(temp)
#
# print (f'Results is: {number} and number of iteration is: {iteration} ')

# num = input('Enter any integer number: ')
# count_iterations = 0
# while len(num) > 1:
#     count_iterations += 1
#     nums = list(num)
#     temp = 0
#
#     while nums:
#         temp = temp + int(nums.pop())
#         num = str(temp)
#
# print('Result: ' + num + ' | No. Iterations: ' + str(count_iterations))

# 8.8
# nums = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]
# dict_counts = {}
#
# for num in nums:
#     dict_counts.setdefault(num, 0)
#     dict_counts[num] += 1
#     print(type(dict_counts[num]))
# print(dict_counts)
#
# # DETERMINE EACH COLUMN'S LENGTH
# col1_width = len(' Item |') + 2
# col2_width = len(' Count ') + 2
#
# for k,v in dict_counts.items():
#
#     k_len = len(str(k)) + 2
#     v_len = len(str(v)) + 2
#
#     if k_len > col1_width:
#         col1_width = k_len
#
#     if v_len > col2_width:
#         col2_width = v_len
#
# # PRINT THE RESULTING TABLE
# print(' Item '.ljust(col1_width) + '|' + 'Count'.center(col2_width))
# print('='* (col1_width +col2_width))
#
# ordered_data = sorted(dict_counts, key = dict_counts.get, reverse=True)
#
# for category in ordered_data:
#     print(' ' +str(category).ljust(col1_width) + '|' + str(dict_counts[category]).center(col2_width))

# 8.9
sentence = '''The Czech Republic also known as Czechia, is a nation state in Central Europe
bordered by Germany to the west, Austria to the south, Slovakia to the east and Poland to the
northeast.[12] The Czech Republic covers an area of 78,866 square kilometres (30,450 sq mi) with
mostly temperate continental climate and oceanic climate. It is a unitary parliamentary republic,
has 10.5 million inhabitants and the capital and largest city is Prague, with over 1.2 million residents.
The Czech Republic includes the historical territories of Bohemia, Moravia, and Czech Silesia.'''

words = sentence.split()
fletters = []
lenghts = []

for word in words:
    lenghts.append(len(word))
    fletters.append(word[0])
    # print(lenghts)
    # print(fletters)

result_string = ''

while fletters:
    lenw = lenghts.pop(0)

    if lenw >= len(fletters):
        result_string = result_string + ''.join(fletters)
        fletters.clear()
    else:
        result_string = result_string + ''.join(fletters[:lenw]) + ' '
        del fletters[:lenw]

print (result_string)


print(10 in range(10))
