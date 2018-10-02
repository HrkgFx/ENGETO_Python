#1
print('1/')
name='Bob'
print('Var name is ' + name)
surname='Marley'
print('Var surname is ' + surname)
full_name=name+" "+surname
print('Var full_name is ' + full_name)
#2
print('2/')
print('*'*20)
print('This is header')
print('*'*20)
#3
print('3/')
week=['Monday' , 'Thuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday']
# day=input('What is the name of the fourth day in a week?')
# day=day.lower()
# day = input('What is the name of the fourth day in a week? ').lower()
# print(week[3].lower()==day)
#4
print('4/')
quetzalcoatl='quetzalcoatl'
print(quetzalcoatl + 'is ' + str(len(quetzalcoatl)) + 'characters long')
#4
print('4/')
word='tutorial'
print('First 5 letters from word ' + word + ' is ' + word[:5])
word='approximation'
wordlen=len(word)
print('Last 5 letters from word ' + word + ' is ' + word[wordlen-5:])
# last_five = 'approximation'[-5:]
print('Every 3rd letters from word ' + word + ' is ' + word[0:wordlen:3])
# every_third = 'approximation'[::3]
