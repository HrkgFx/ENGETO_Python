print('1/')
candidates=[]
print('Candidates at the beginning: ' + str(candidates))
employees=['Frank','Amy','John','Kate']
print('Employees at the beginning: ' + str(employees))

print('2/')
candidates=candidates + ['Bob','Ann']
print('Added new names to candidates: '+ str(candidates))
# print("Added new names to candidates: ['Bob', 'Ann']")

print('3/')
# pridani polozky do listu seq[index,item]=item
employees[1:1]=candidates[0:1]
# employees[1:1] = ['Bob']
print('Added new names to employees: ' + str(employees))

print('4/')
cand0=candidates[0]
del candidates[0]
print('Removed ' + cand0 + ' from candidates: '+str(candidates))
# candidates.remove('Bob')
# print('Removed Bob from candidates: ' + str(candidates))

print('5/')
candidates=candidates*3
print('Repeated name ' + str(candidates[0]) + ' in candidates: ' + str(candidates))

print('6/')
employees.extend(candidates)
# employees= employees + candidates
print('Merged candidates with employees: ' + str(employees))

print('7/')
print('At index 2 we have: ' + str(employees[2]))
# print('At index 2 we have: ' + employees[2])
print('At index ' + str(len(employees)-1) + ' we have: ' + str(employees[-1]))
# last_index = len(employees) - 1
# print('At index ' + str(last_index) + " we have: " employees[last_index])

print('8/')
# the main catch here is to remember that when slicing, the stop index has to be one higher than the index we want to be actually included in the result subsequence
print('At indices 2 to 5 we have: ' + str(employees[2:6]))

print('9/')
print('Every third member: ' + str(employees[::3]))

print('10/')
print('John is at index: ' + str(employees.index('John')))
# john_pos = employees.index('John')
# print('John is at index: ' + str(john_pos)

print('11/')
print('The number of occurences of Ann: '+ str(employees.count('Ann')))
# ann_count = employees.count('Ann')
# print('The number of occurences of Ann: ' + str(ann_coun))
