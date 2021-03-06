# STRINGS
1/
# Create a python script named fullname.py that will perform the following actions:
#
# Store the string value 'Bob' inside the variable name.
# Print the information that value 'Bob' has been stored, for example: "Storing 'Bob' in name ..."
# Then store the string 'Marley' a variable surname.
# Print the information that value 'Marley' has been stored, for example: "Storing 'Marley' in surname ..."
# Lastly create a variable full_name, assign it the result of concatenation of values in variables name and surname and print the content of full_name to the terminal.

2/
# Create a python script named print_header.py that will perform the following actions:
# Print the following header to the terminal. The result lines should contain 20 equal signs - both upper and the lower. The result should look something like:
#
# ====================
# THIS IS THE HEADER
# ====================

3/
# Create a python script named get_day.py that will perform the following actions:
#
# Ask the user for the answer to the question:
# What is the name of the fourth day in a week?
# (The correct answer in Europe is Thursday)
#
# Print True or False to the terminal based on whether the answer has been correct or not.
# Your script should print True if the user provided any of the following values:
#
# Thursday, THURSDAY, thursday, tHursday etc.
# Example of running the script in terminal:
#
# ~/PythonBeginner/Lesson1 $ python get_day.py
# What is the name of the fourth day in a week? Thursday
# True
# ~/PythonBeginner/Lesson1 $ python get_day.py
# What is the name of the fourth day in a week? Wednesday
# False
# ~/PythonBeginner/Lesson1 $ python get_day.py
# What is the name of the fourth day in a week? THURsday
# True


4/
# Create a python script named word_length.py that will perform the following actions:
#
# Print out the length of the word 'quetzalcoatl' in a sentence similar to:
# quetzalcoatl is X characters long
# The placeholder X in the above string should be replaced by the actual length of the word.
#
# Example of running the script in terminal:
#
# ~/PythonBeginner/Lesson1$ python word_length.py
# quetzalcoatl is 12 characters long


5/
# Create a python script named str_slicing.py that will use indexing to:
#
# Extract the first five letters from the word 'tutorial'
#
# Print them to the terminal
#
# Extract the last five letters from the word 'approximation'
#
# Print them to the terminal
#
# Extract every third letter from the word 'approximation'
#
# Print them to the terminal
#
# Example of running the script in terminal:
#
# ~/PythonBeginner/Lesson1$ python str_slicing.py
# First five letters: tutor
# Last five letters: ation
# Every 3rd letter: aritn

6/
# Create a python script named change_case.py that will perform the following actions:
#
# ask the user for input
# transform all letters in the input into lowecase
# print the resulting lowercase string
# Example of running the script in terminal:
#
# ~/PythonBeginner/Lesson1 $ python change_case.py
# Enter something: Hello World
# Changed to lowercase: hello world

7.1/
# Create a python script named find_t.py that will perform the following actions:
#
# print out at what index is the first occurence of the letter 't' in the word 'quetzalcoatl'
# print out at what index is the last occurence of the letter 't' in the word 'quetzalcoatl'
# Example of running the script in terminal:
#
# ~/PythonBeginner/Lesson1 $ python find_t.py
# The first occurence of the letter "t" is at the index: 3
# The last occurence of the letter "t" is at index: 10

7.2/
# Create a python script named find_word.py that will perform the following actions:
#
# find the index of the first occurence of word 'nearly' in the sentence
# print out the message stating the position, where the word 'nearly' has been found
# "Today is forecast to be nearly the same temperature as yesterday"
#
# Example of running the script in terminal:
#
# ~/PythonBeginner/Lesson1 $ python find_word.py
# The first occurence of the word "nearly" is at the index: 24

8/
# Create a python script named clean_word.py that will perform the following actions:
# remove any of the below listed characters from the end and the beginning of the string '-hello-world. ,'
#
# ','
# '.'
# '-'
# ' '
# print the resulting string to the terminal
#
# Example of running the script in terminal:
#
# /Users/PythonBeginner/Lesson1$ python clean_word.py
# Original string: -hello-world. ,
# Cleaned string: hello-world

9/
# Create a python script named replace_name.py that will perform the following actions:
#
# In a variable store a string:
# 'Hello Bob! Name Bob is my prefered name.'
# Ask for the user to enter his/her name
# Replace all occurences of string 'Bob' with the name provided by the user
# Example of running the script in terminal:
#
# ~/PythonBeginner/Lesson1 $ python replace_name.py
# What is your name? Frank
# Hello Frank! Name Frank is my prefered name.

# LISTS
1/
# Create new lists
# Assign an empty list to the variable candidates
# Print the content of candidates to the terminal introducing it with the string: Candidates at the beginning:
# Create a list containing strings: 'Frank', 'Amy', 'John', 'Kate' and assign this list to the variable employees
# Print the content of employees to the terminal introducing it with the string: Employees at the beginning:
# Example of running the script:
#
# /Users/PythonBeginner/Lesson1$ python employees.py
# Candidates at the beginning: []
# Employees at the beginning: ['Frank', 'Amy', 'John', 'Kate']

2/
# Please, continue working with the file employees.py. Now, write a code that will perform the following actions:
#
# add new names 'Bob' and 'Ann' into the list candidates
# print the content of the variable candidates introduced by the string: Added new names to candidates:
# Example of running the script:
#
# /Users/PythonBeginner/Lesson1$ python employees.py
# Candidates at the beginning: []
# Employees at the beginning: ['Frank', 'Amy', 'John', 'Kate']
# Added new names to candidates: ['Bob', 'Ann']

3/
# Please, continue working with the file employees.py. Now, write a code that will perform the following actions:
#
# insert name 'Bob' stored in the variable candidates into the employees list at the index 1
# print the content of the variable employees introduced by the string: Added new names to employees:
# Example of running the script:
#
# /Users/PythonBeginner/Lesson1$ python employees.py
# Candidates at the beginning: []
# Employees at the beginning: ['Frank', 'Amy', 'John', 'Kate']
# Added new names to candidates: ['Bob', 'Ann']
# Added new names to employees: ['Frank', 'Bob', Amy', 'John', 'Kate']

4/
# Please, continue working with the file employees.py. Now, write a code that will perform the following actions:
#
# remove the string 'Bob' from the list candidates
# print the content of the variable candidates introduced by the string: Removed name from candidates:
# Example of running the script:
#
# /Users/PythonBeginner/Lesson1$ python employees.py
# Candidates at the beginning: []
# Employees at the beginning: ['Frank', 'Amy', 'John', 'Kate']
# Added new names to candidates: ['Bob', 'Ann']
# Added new names to employees: ['Frank', 'Bob', Amy', 'John', 'Kate']
# Removed Bob from candidates:  ['Ann']

5/
# Please, continue working with the file employees.py. Now, write a code that will perform the following actions:
#
# repeat the name 'Ann' 3 times inside the list candidates
# print the content of the variable candidates introduced by the string: Repeated name Ann in candidates:
# Example of running the script:
#
# /Users/PythonBeginner/Lesson1$ python employees.py
# Candidates at the beginning: []
# Employees at the beginning: ['Frank', 'Amy', 'John', 'Kate']
# Added new names to candidates: ['Bob', 'Ann']
# Added new names to employees: ['Frank', 'Bob', Amy', 'John', 'Kate']
# Removed name from candidates:  ['Ann']
# Repeated name Ann in candidates: ['Ann', 'Ann', 'Ann']

6/
# Please, continue working with the file employees.py. Now, write a code that will perform the following actions:
#
# merge the list candidates into the list employees
# print the content of the variable employees introduced by the string: Merged candidates with employees:
# Example of running the script:
#
# /Users/PythonBeginner/Lesson1$ python employees.py
# Candidates at the beginning: []
# Employees at the beginning: ['Frank', 'Amy', 'John', 'Kate']
# Added new names to candidates: ['Bob', 'Ann']
# Added new names to employees: ['Frank', 'Bob', 'Amy', 'John', 'Kate']
# Removed name from candidates:  ['Ann']
# Repeated name Ann in candidates: ['Ann', 'Ann', 'Ann']
# Merged candidates with employees: ['Frank', 'Bob', 'Amy', 'John', 'Kate', 'Ann', 'Ann', 'Ann']

7/
# Please, continue working with the file employees.py. Now, write a code that will perform the following actions:
#
# print out the name at the index 2 introduced by the string: At index 2 we have:
# print out the name at the last index introduced by the string: At index <index_num> we have:
# the placeholder <index_num> should be replaced by the index number of the last position in the list employees
#
# Example of running the script:
#
# /Users/PythonBeginner/Lesson1$ python employees.py
# Candidates at the beginning: []
# Employees at the beginning: ['Frank', 'Amy', 'John', 'Kate']
# Added new names to candidates: ['Bob', 'Ann']
# Added new names to employees: ['Frank', 'Bob', 'Amy', 'John', 'Kate']
# Removed name from candidates:  ['Ann']
# Repeated name Ann in candidates: ['Ann', 'Ann', 'Ann']
# Merged candidates with employees: ['Frank', 'Bob', 'Amy', 'John', 'Kate', 'Ann', 'Ann', 'Ann']
# At index 2 we have: Amy
# At index 7 we have:  Ann

8/
# Please, continue working with the file employees.py. Now, write a code that will perform the following actions:
#
# print out the names at the indices 2 to 5 introduced by the string: At indices 2 to 5 we have:
# Example of running the script:
#
# /Users/PythonBeginner/Lesson1$ python employees.py
# Candidates at the beginning: []
# Employees at the beginning: ['Frank', 'Amy', 'John', 'Kate']
# Added new names to candidates: ['Bob', 'Ann']
# Added new names to employees: ['Frank', 'Bob', 'Amy', 'John', 'Kate']
# Removed name from candidates:  ['Ann']
# Repeated name Ann in candidates: ['Ann', 'Ann', 'Ann']
# Merged candidates with employees: ['Frank', 'Bob', 'Amy', 'John', 'Kate', 'Ann', 'Ann', 'Ann']
# At index 2 we have: Amy
# At index 7 we have:  Ann
# At indices 2 to 5 we have:  ['Amy', 'John', 'Kate', 'Ann']

9/
# Please, continue working with the file employees.py. Now, write a code that will perform the following actions:
#
# print out every third string in employees introduced by the string: Every third member:
# Example of running the script:
#
# /Users/PythonBeginner/Lesson1$ python employees.py
# Candidates at the beginning: []
# Employees at the beginning: ['Frank', 'Amy', 'John', 'Kate']
# Added new names to candidates: ['Bob', 'Ann']
# Added new names to employees: ['Frank', 'Bob', 'Amy', 'John', 'Kate']
# Removed name from candidates:  ['Ann']
# Repeated name Ann in candidates: ['Ann', 'Ann', 'Ann']
# Merged candidates with employees: ['Frank', 'Bob', 'Amy', 'John', 'Kate', 'Ann', 'Ann', 'Ann']
# At index 2 we have: Amy
# At index 7 we have:  Ann
# At indices 2 to 5 we have:  ['Amy', 'John', 'Kate', 'Ann']
# Every third member: ['Frank', 'John', 'Ann']

10/
# Please, continue working with the file employees.py. Now, write a code that will perform the following actions:
#
# print the index, at which the string 'John' encounters itself in employees: John is at index:
# Example of running the script:
#
# /Users/PythonBeginner/Lesson1$ python employees.py
# Candidates at the beginning: []
# Employees at the beginning: ['Frank', 'Amy', 'John', 'Kate']
# Added new names to candidates: ['Bob', 'Ann']
# Added new names to employees: ['Frank', 'Bob', 'Amy', 'John', 'Kate']
# Removed name from candidates:  ['Ann']
# Repeated name Ann in candidates: ['Ann', 'Ann', 'Ann']
# Merged candidates with employees: ['Frank', 'Bob', 'Amy', 'John', 'Kate', 'Ann', 'Ann', 'Ann']
# At index 2 we have: Amy
# At index 7 we have:  Ann
# At indices 2 to 5 we have:  ['Amy', 'John', 'Kate', 'Ann']
# Every third member: ['Frank', 'John', 'Ann']
# John is at index: 3

11/
# Please, continue working with the file employees.py. Now, write a code that will perform the following actions:
#
# print how many times name 'Ann' can be found inemployees: The number of occurences of Ann:
# Example of running the script:
#
# /Users/PythonBeginner/Lesson1$ python employees.py
# Candidates at the beginning: []
# Employees at the beginning: ['Frank', 'Amy', 'John', 'Kate']
# Added new names to candidates: ['Bob', 'Ann']
# Added new names to employees: ['Frank', 'Bob', 'Amy', 'John', 'Kate']
# Removed name from candidates:  ['Ann']
# Repeated name Ann in candidates: ['Ann', 'Ann', 'Ann']
# Merged candidates with employees: ['Frank', 'Bob', 'Amy', 'John', 'Kate', 'Ann', 'Ann', 'Ann']
# At index 2 we have: Amy
# At index 7 we have:  Ann
# At indices 2 to 5 we have:  ['Amy', 'John', 'Kate', 'Ann']
# Every third member: ['Frank', 'John', 'Ann']
# John is at index: 3
# The number of occurences of Ann: 3
