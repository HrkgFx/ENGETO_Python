import os, sys

# moje noob reseni
# os.mkdir('TestDir')

# s1 = open('s1.txt','w')
# s1.close()
# s2 = open('s2.txt','w')
# s2.close()
# s3 = open('s3.txt','w')
# s3.close()
# s4 = open('s4.txt','w')
# s4.close()

# slozka = os.getcwd()
# print(slozka)
#
# print(os.listdir())

slozka = 'TestDir'

try:
    os.mkdir(slozka)
except:
    OSError

for i in range(1,6):
    f = open('{}\s{}.txt'.format(slozka, i), 'w')
    f.close()

obsah = os.listdir(slozka)

print('Obsah slozky {} je: '.format(slozka))
for soubor in obsah:
    print(soubor)

    
