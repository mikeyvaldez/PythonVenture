#!/usr/bin/env python3

################################################################################################
# In late  2019, the US Court of Appeals denied LinkedIn's request to prevent
# HiQ, an analytics company, from scraping its data.

# The decision was a historic moment in the data privacy and data regulation
# era. It showed that any data that is 'PUBLICLY AVAILABLE AND NOT COPYRIGHTED' is 
# fair game for web scrapers/crawlers
################################################################################################



from bs4 import BeautifulSoup # type: ignore
# import lxml  # this is an just incase the website is using xml instead of html

with open("website.html") as file:  # interact with html file
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')  # creates a variable for html parser
# soup = BeautifulSoup(contents, "lxml")  # this is just in case the website is using xml instead of html

# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())   # indents html code to make more legible

# print(soup.a)
# print(soup.li)
# print(soup.p)


# -----------------------

# all_anchour_tags = soup.find_all(name="a")   # finds all anchor tags and puts them in a list
# print(all_anchour_tags)

# --------------------------

all_anchour_tags = soup.find_all(name="a") 
# for tag in all_anchour_tags:
#     # print(tag.getText()) # grabs the text of the anchor tag
#     print(tag.get("href"))


heading = soup.find(name="h1", id="name")
print(heading)


section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")   # this piece is looking for a <p> tag that is sitting inside of an <a> tag
print(company_url)

name = soup.select_one(selector="#name")  # finds an id by name
print(name)




headings = soup.select(".heading")
print(headings)

















