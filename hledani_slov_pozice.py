text = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''
print(text)
# print(line)

search_word = input('Enter search word: ')
positions = []
words = text.split()
for i,word in enumerate(words):
    word = word.strip(';,._/:')
    if word == search_word:
        position = i + 1
        positions.append(position)
        print(f'Position searched word is: {position}')

if not positions:
    print('NO SUCH WORD')
