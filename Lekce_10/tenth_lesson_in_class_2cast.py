import os # slouzi k manipulaci s operacnim systemem
import sys #

# import muj_modul
# os.path # manipulace se souborama a cestama

print(os.listdir()) # vraci list, ktery je soucasti souboru
print(os.listdir('__pycache__')) # vraci obsah dane slozky

# os.mkdir('Test') # vytvori slozku s nazvem
if 'Test' in os.listdir():
    print('Je tam!')

# f = open('novy.txt','w') #vytvorim soubor
# f.close()


# os.path.isdir(path) # vraci True / False
# os.path.isfile(path)

# print(os.path.isdir('novy.txt'))
# print(os.path.isfile('novy.txt'))
#
# print(os.getcwd())
#
# x = os.getcwd()
# print(x)
#
# os.path.join(os.getcwd(),'DIR1') #slouci dve cesty do jedne
#
# if __name__ == '__main__':

slozka = os.getcwd()
print(slozka)
cwd = os.getcwd().split('\\')
cwd.insert(1,os.sep) # importuju chybejici \ kvuli ceste
print(list(cwd))

x = os.path.join(*cwd)
print(list(os.sep))
print(x)
# print(os.path.isdir'muj_modul.py')

os.system('dir') # lze pouzivat systemove prikazy
os.system('mkdir test3')


# sys
print(sys.platform) # urceni platformy (mac vraci dark :D)
sys.exit() #SystemExit vyvolava chybu pres try except se muzu zeptat jestli chce opravdu zavrit

# argumenty skriptu jmeno_skriptu.py 1 2 3 4
# python jmeno_skriptu.py 1 2 3 4 --- automatizovane spousteni skriptu, kdyz jim je potreba neco predavat
# print(sys.argv) vypise list

#pip install nazev modulu
