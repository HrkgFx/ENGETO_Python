import requests
from bs4 import BeautifulSoup as BS

# https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

main_req = requests.get('https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ')
# print(main_req)
# print(main_req.text)


main = BS(main_req.text, "html.parser")
# print(main)

# print(main)

print(main.h3.a.contents)
print(len(main.h3.a))

for child in main.children:
    print(child)

regions = main.find_all('h3')
print(regions)
