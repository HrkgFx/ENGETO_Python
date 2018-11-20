# $ pip install requests

import requests
from bs4 import BeautifulSoup as BS

# response = requests.get('https://httpbin.org')
# print(response)
# print(response.status_code)
# print(response.text)

# # return JSON
# response = requests.get('https://httpbin.org/get')
# print(response.status_code)
# print(response.text)
# print(response.json())
#
# d = response.json()
# print(d['origin'])
#
#
# response = requests.post('http://httpbin.org/post', data = {'my_message':'Hello'})
# print(response)
# print(response.text)
# print(response.json())

# # $ pip install beautifulsoup4
# # modul for parsing webpages


# # 1/ using methods, that will gather the target items (find(), find_all(), select(), etc) for us
# # 2/ looping across the document tree structure (tag, children, descendands, parents, siblings, etc.)
line = 50*'-'

r = requests.get("https://example.com")
# print(r)
# print(r.text)


soup = BS(r.text, "html.parser")
print(soup)
print(line)

# Selecting Element Directly by Tag Name
print(soup.p)
print(line)

print(soup.a)
print(line)

print(soup.body.contents)
print(line)

print(len(soup.body.contents))
print(line)

x = list(filter(lambda x: x != "\n",soup.body.contents))
print(x)
print(line)

for child in soup.body.children:
    print(child)

for i,descendant in enumerate(soup.div.descendants):
    print('DESCENDANT {}: {}'.format(i,descendant))

# To move among the sibling elements, we can use next_sibling, previous_sibling, next_siblings and previous_siblings attributes.

soup.find_all('p')
soup.find_all(charset="utf-8")
soup.find_all(attrs={"content":"text/html; charset=utf-8",'http-equiv':"Content-type"})
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


html = "<div class='red' id='bob'>This is the first div</div><div class='green'>This is the second div</div>"
small_soup = BS(html,"html.parser")
small_soup.find_all(has_class_but_no_id)
