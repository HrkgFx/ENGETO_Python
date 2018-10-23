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

# vytvori requests
getr = requests.get('https://httpbin.org')
print(getr.status_code)

#co jsem dostal
print(getr.text)
