#!/usr/bin/env python3

# extracts titles of the hyper links for the website


from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore

response = requests.get("https://news.ycombinator.com/")

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titles = soup.select(".titleline a")

for title in titles:
    if "." in title.text:
        continue
    print(title.text)