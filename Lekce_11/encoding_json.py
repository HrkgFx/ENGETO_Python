import json

employee = {'Test': True, 'Job': 'Programmer', 'Age': 38, 'Full Name': 'Galagher, Fred', 'City': 'London', 'Surname': 'Galagher', 'Gender': 'Male', 'Name': 'Fred'}

data = json.dumps(employee)

print(data)
print(type(data))


emp = json.loads(data)
print(emp)
print(type(emp))

# prida mezery a novy radek pro lepsi cteni
data = json.dumps(emp,indent=4)
print(data)

#seradi json data
data = json.dumps(emp,indent=4,sort_keys=True)
print(data)
