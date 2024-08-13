#!/usr/bin/env python3


################################################################################################
# In late  2019, the US Court of Appeals denied LinkedIn's request to prevent
# HiQ, an analytics company, from scraping its data.

# The decision was a historic moment in the data privacy and data regulation
# era. It showed that any data that is 'PUBLICLY AVAILABLE AND NOT COPYRIGHTED' is 
# fair game for web scrapers/crawlers
################################################################################################




# This program goes through the specific website and determines the highest score 
# among the news titles of hacker news

import requests      # type: ignore
from bs4 import BeautifulSoup     # type: ignore



response = requests.get("https://news.ycombinator.com/")

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titles = soup.select(".titleline a")
links = soup.select(".titleline a")
scores = soup.select(".score")

title_list = []
link_list = []
score_list = []

for title in titles:
    if "." in title.text:
        continue
    title_list.append(title.text)

for link in links:
    if "?" in link.get("href"):
        continue
    link_list.append(link.get("href"))

for score in scores:
    points = score.getText()
    score_list.append(int(points.split()[0]))


max_score = max(score_list)
max_index = score_list.index(max_score)

print(f"""
{title_list[max_index]}\n
{link_list[max_index]}\n
{score_list[max_index]}\n
""")