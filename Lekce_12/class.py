# json vs slovnik
# "" vs ''
# 'klic'  vs klic
# true, false vs True, False
# null vs None


# slovnik = {1:'a', 2:'b'}
# klice = slovnik.keys()
# print(type(klice))
# klice[1]


import requests
from pprint import pprint as pp

# vytvori requests
getr = requests.get('https://httpbin.org')
print(getr.status_code)
print(50*'-')
#co jsem dostal
pp(getr.text)


getr = requests.post('https://httpbin.org', data = {1:2})

print(getr.status_code)
print(50*'-')
#co jsem dostal
pp(getr.text)
