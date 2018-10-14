############### IF na jeden radek (Ternary conditional operator) ###############
# variable_name = expression1 if condition else expression2
variable = condition_is_true if condition else condition_is_false
hour = 14
day_time = 'Morning' if hour < 12 else 'Afternoon'
print(f'{hour} is {day_time}')

# Another more obscure and not widely used example involves tuples.
variable = (if_test_is_false, if_test_is_true)[test]

nice = True
personality = ("mean", "nice")[nice == False]
print("The cat is", personality)
# Output: The cat is mean

############### FOR na jeden radek ###############
list_variable = [x for x in iterable]

number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)

shark_letters = [letter * 2 for letter in 'shark']
print(shark_letters)
