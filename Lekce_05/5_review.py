# 1/
sentence = input('Write sentence:')

if sentence[:9] == 'However, ':
    print (sentence)
else:
    print ('However, ' + str(sentence[0].lower()) + str(sentence[1:]))

# 2/
sentence = input ('Enter the text: ')
word = input('Enter search word: ')

print('The searched word starts at index ' + str(sentence.find(word)) + '.' )
# print(sentence[6])

# 3/
nums = ['421',867,65, '93', 45, 82]
i = 0
result = 0

while i < len(nums):
    result = result + int(nums[i])
    i = i + 1

print(str(result))

# 4/
letter = input('Please enter a letter: ')
vowels = list('aeiouy')

if type(letter) == str and len(letter)==1:
    print(letter in vowels)
