students = ['Adam, Baker','Chelsea, Archer',
            'Marcus, Archer','Oliver, Cook',
            'Alex, Dyer', 'Sandra, Turner',
            'Ann, Fisher', 'Glenn, Hawkins',
            'Samuel, Baker','Clara, Slater',
            'Tyler, Hunt', 'Alex, Smith',
            'Clara, Woodman','Abraham, Mason',
            'Marcus, Sawyer','Alex, Glover',
            'Glenn, Cook','Clara, Fisher',
            'Alfred, Dyer', 'Curt, Head',
            'Oliver, Slater','Alex, Mason',
            'Tyler, Fisher','Ann, Parker',
            'Samuel, Hawkins', 'Ann, Woodman',
            'Sandra, Slater', 'Curt, Dyer']

# Our task is to extract an overview of what unique names and surnames do we have in the class.

names = set()
surnames = set()

while students:
    name, surname = [1,2,3]
    #students.pop().split(', ')
    names.add(name)
    surnames.add(surname)

print('Unique names:')
print(names)
print('Unique surnames:')
print(surnames)



# nums = [ 386, 462, 47, 418, 907, 344, 236, 375, 823,
#         566, 597, 978, 328, 615, 953, 345, 399, 162,
#         758, 219, 918, 237, 412, 566, 826, 248, 866,
#         950, 626, 949, 687, 217, 815, 67, 104, 58, 512,
#         24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
#         742, 717, 958,743, 527]
#
# odd=[]
# even=[]
# count_odd=0
# count_even=0
#
# while nums:
#     number = nums.pop()
#     if number % 2:
#         odd.append(number)
#         count_odd =
#     else:
#         even.append(number)
#
# print(odd)
# print(even)
