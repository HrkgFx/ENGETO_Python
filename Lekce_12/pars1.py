import requests
import bs4
from pprint import pprint as pp

# a = int(1) #instruktor ktery vytvari objekt
# trida BeautifulSoup()

# (co chci prochazet - string s HTML, jak to chceme prochazet - 'html.parser')


getr = requests.get('https://httpbin.org')

soup = bs4.BeautifulSoup(getr.text, 'html.parser')

# pp(soup.a)
# pp(soup.b)
# pp(soup.p)
# pp(soup.body.contents) #vytahne veci, co ma primo pod sebou

# children = soup.body.children
# for child in children:
#     print(child)
#     print(20*'-')
#
# print(40*'*')
#
# descendants = soup.body.descendants
# for desc in descendants:
#     print(desc)
#     print(20*'-')

children = soup.body.children

pp(soup.find_all('a'))
pp(soup.find_all(href = "https://github.com/rochacbruno/flasgger"))
pp(soup.find_all(href = "https://github.com/rochacbruno/flasgger")[0].contents)
pp(soup.find_all(href = "https://github.com/rochacbruno/flasgger")[0].contents[0])


# for odkaz in soup.find_all('a'):
#     print (odkaz.contents)

for odkaz in soup.find_all('a'):
    if 't' in odkaz.contents[0]:
        print (odkaz.contents)
