# STRINGS
1/
name = 'Bob'
print("Storing 'Bob' in name ...")
surname = 'Marley'
print("Storing 'Marley' in surname ...")
full_name = name + " " + surname
print(full_name)

2/
print("=" * 20)
print('THIS IS THE HEADER')
print("=" * 20)

3/
# - in order user's input can be comparable with our word 'Thursday', it will be the best if we changed users input into lowercase (line 2)
# - subsequently we print the result of comparison operation among lowercase user input and our lowercase "thursday" (the result will be True or False)
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = input('What is the name of the fourth day in a week? ')
day = day.lower()
print(day == days[3].lower())

# Little advice - make your code shorter. We can ask for user input and convert it into lower case on one line:
day = input('What is the name of the fourth day in a week? ').lower()

4/
# to find out the length of a string, we can use len() function and store it inside a variable word_length
# once we have the length calculated, we can print our result sentence
# in the result sentence we have to perform concatenation
# concatenation can be however performed only among sequenes of the same data type
# word_length is however an integer and therefore we have to use the function str() to convert it into a string (line 2)
word_length = len('quetzalcoatl')
print('quetzalcoatl is ' + str(word_length) + ' characters long')

5/
# We will have to use slicing for the first two operations and for the last one, we will have to specify the third argument called step inside the square brackets:
# Extract the first five letters from the word 'tutorial' (line 1)
# Extract the last five letters from the word 'approximation' (line 3)
# Extract every third letter from the word 'approximation' (line 5)

first_five = 'tutorial'[:5]
print('First five letters: ' + first_five)

last_five = 'approximation'[-5:]
print('Last five letters: ' + last_five)

every_third = 'approximation'[::3]
print('Every 3rd letter: ' + every_third)

6/
# When asking for user input, we can immediately convert it to the lowercase using lower() method
# Subsequently we concatenate the lowercased input with the string 'Changed to lowercase: '
user_input = input('Enter something: ').lower()
print('Changed to lowercase: ' + user_input)

7.1/
# we can use it to find the first occurence of a subtring
# in our case, the subtring is letter 't'
# the method find starts its search from the left side of the string. If we wanted to find the last occurence, we would have to use its sibling rfind, which starts its search from the oposite (right) side of the string
# both find and rfind return a number. Therefore if we want to concatenate it with another string, we have to convert it into a string (lines 4 and 5)
word = 'quetzalcoatl'
first_t = word.find('t')
last_t = word.rfind('t')
print('The first occurence of the letter "t" is at the index: ' + str(first_t))
print('The last occurence of the letter "t" is at index: ' + str(last_t))

7.2/
# here we are not searching for a single letter, but for a substring "nearly"
# despite this difference, we still can use find() method
sentence = "Today is forecast to be nearly the same temperature as yesterday"
position = sentence.find('nearly')
print('The first occurence of the word "nearly" is at the index: ' + str(position))

8/
# the operation we are about to perform is called stripping and Python provides a method with such name `str.strip'
# inside the parentheses of the strip() method we have write a string of characters we want to erase from the beginning and the end of the stripped string
# word = '-hello-world. ,'
cleaned = word.strip("-,. ")
print('Original string: ' + word)
print('Cleaned string: ' + cleaned)

9/
# to replace one string for another, we can use the str.replace() method
# the first input into this method is the target substring we want to repalce and the second is the string we want to insert instead
original = 'Hello Bob! Name Bob is my prefered name.'
name = input('What is your name? ')
new = original.replace('Bob', name)
print(new)

# LISTS
1/
candidates = []
employees = ['Frank', 'Amy', 'John', 'Kate']
print('Candidates at the beginning: ' + str(candidates))
print('Employees at the beginning: ' + str(employees))

2/
# let's use the concatenation + between two lists - candidates and ['Bob', 'Ann']
# concatenation extends the list on the right side of the expression
# the result should be stored back into a variable candidates
candidates = candidates + ['Bob', 'Ann']
print("Added new names to candidates: ['Bob', 'Ann']")

3/
# insertion into a list is performed on list slices
# the trick is in that the start and the stop index of the slice have to be equal, if we do not want to erase anything from the original list
# here we want to insert 'Bob' at the index 1 so the insertion command will look like the one on line 9
# on line 10 we have to convert the list employees into a string in order we can perform the concatenation (+) operation
employees[1:1] = ['Bob']
print('Added new names to employees: ' + str(employees))

4/
# to remove an item from a list, we can use the list.remove() method
# we just pass it the item we want to remove and the method takes care of everything
candidates.remove('Bob')
print('Removed Bob from candidates: ' + str(candidates))

5/
# currently the list candidates contains only one item
# we can repeat this item 3 times by using the multiplication * symbol
# the resut has to be stored back into the candidates variable
# again we have to convert candidates into a string in order we can concatenate it with another string
candidates = candidates * 3
print('Repeated name Ann in candidates: ' + str(candidates))

6/
# To merge two lists, we should again use concatenation operation +
# employees = employees + candidates
print('Merged candidates with employees: ' + str(employees))

7/
# we retrieve an item at index 2 as employees[2]
# the trickier part however is to determine the last index, which equal to the length of the sequence - 1 (line 22)
# when concatenating the resulting string, all items have to be strings or converted to strings
print('At index 2 we have: ' + employees[2])
last_index = len(employees) - 1
print('At index ' + str(last_index) + " we have: " employees[last_index])

8/
# the main catch here is to remember that when slicing, the stop index has to be one higher than the index we want to be actually included in the result subsequence
# therefore to retrieve items at indices 2 to 5 we need to slice employees with [2:6]
print('At indices 2 to 5 we have: ' +  str(employees[2:6]))

9/
# to extract every n-th item from a sequence, we need to specify the step inside the square brackets
# we also want to apply striding to the whole sequence, therefore we do not specify start and stop parameters
print('Every third member: ' + str(employees[::3]))

10/
# Python implements list.index() method for lists, which we can use to determine, at which index an item encounters itself
# we write the value of the searched item inside the parentheses
john_pos = employees.index('John')
print('John is at index: ' + str(john_pos))

11/
# to calculate the number of occurences of an item in a list or string or tuple, we can use count() method
# again inside parentheses, we have to specify, what item we want to count
ann_count = employees.count('Ann')
print('The number of occurences of Ann: ' + str(ann_coun))

12/
# If you completed all previous tasks, check our complete solution below. :)

candidates = []
employees = ['Frank', 'Amy', 'John', 'Kate']
print('Candidates at the beginning: ' + candidates)
print('Employees at the beginning: ' + employees)

candidates = candidates + ['Bob', 'Ann']
print("Added new names to candidates: ['Bob', 'Ann']")

employees[1:1] = 'Bob'
print('Added new names to employees: ' + str(employees))

candidates.remove('Bob')
print('Removed Bob from candidates: ' + str(candidates))

candidates = candidates * 3
print('Repeated name Ann in candidates: ' + str(candidates))

employees = employees + candidates
print('Merged candidates with employees: ' + str(employees))

print('At index 2 we have: ' + employees[2])
last_index = len(employees) - 1
print('At index ' + str(last_index) + " we have: " employees[last_index])

print('At indices 2 to 5 we have: ' str(employees[2:6])

print('Every third member: ' + str(employees[::3]))

john_pos = employees.index('John')
print('John is at index: ' + str(john_pos))

ann_count = employees.count('Ann')
print('The number of occurences of Ann: ' + str(ann_count))
