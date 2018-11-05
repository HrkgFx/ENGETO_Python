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

r = requests.get("https://example.com")
# print(r)
# print(r.text)


soup = BS(r.text, "html.parser")
print(soup)

# Selecting Element Directly by Tag Name
print(soup.p)
print(soup.a)
print(soup.body.contents)
print(len(soup.body.contents))
x = list(filter(lambda x: x != "\n",soup.body.contents))
print(x)
