# https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

import bs4 as bs
import urllib.request as req

sauce = req.urlopen('https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ').read()
soup = bs.BeautifulSoup(sauce,'lxml')

# # print(sauce)
# # print(soup)
#
# # zobrazi obsah daneho prvniho elementu jako string ale jen deti,jinak vraci None
# print(soup.h3.string)
# # vraci vsechen text vcetne mezer
# print(soup.h3.text)
#
# # najde vsechny h3 a ulozi je do listu
# print(soup.find_all('h3'))
#
# for header3 in soup.find_all('h3'):
#     print(header3.text)
#
# # # dostanes vsechen text na strance
# # print(soup.get_text())
#
# # vypise vsechny href tagy
# for url in soup.find_all('a'):
#     print(url.get('href'))


# vsechny h3 s class kraj v body rozdelene na text + url
body = soup.body
for h3 in body.find_all('h3', class_='kraj'):
    for url in h3.find_all('a'):
        print(url.text)
        print(url.get('href'))

# TABULKY

# table = soup.table
table = soup.find('table')
print(table)
table_rows = table.find_all('tr')
print(table_rows)

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)
