#!/usr/bin/env python3



from bs4 import BeautifulSoup # type: ignore
# import lxml  # this is an just incase the website is using xml instead of html

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# soup = BeautifulSoup(contents, "lxml")  # this is just in case the website is using xml instead of html

print(soup.title)
print(soup.title.string)

# print(soup.prettify())   # indents html code to make more legible

print(soup.a)
print(soup.li)
print(soup.p)