#!/usr/bin/env python3


################################################################################################
# In late  2019, the US Court of Appeals denied LinkedIn's request to prevent
# HiQ, an analytics company, from scraping its data.

# The decision was a historic moment in the data privacy and data regulation
# era. It showed that any data that is 'PUBLICLY AVAILABLE AND NOT COPYRIGHTED' is 
# fair game for web scrapers/crawlers
################################################################################################





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