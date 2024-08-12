#!/usr/bin/env python3


from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page)
print(response.text)