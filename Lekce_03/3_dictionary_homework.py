text='It was a bright, sunny day in May, and the church bell was just ringing'
letters={}

for letter in text:
    letters.setdefault(letter, 0)
    letters[letter] = letters[letter] + 1

print(letters)


data = {'user1': 'password1',
        'Marek': '1234',
        'Danko': 'qwert'}

# we want to ask user for username and password
Username    = str(input('Please enter the username: '))
Password    = str(input('Please enter the password: '))

# two conditions for evaluating the inputs
if data.get(Username) != Password:
    print('Password or username is wrong')

elif data.get(Username) == Password:
    print('Permission granted')
