#!/usr/bin/env python3


################################################################################################
# In late  2019, the US Court of Appeals denied LinkedIn's request to prevent
# HiQ, an analytics company, from scraping its data.

# The decision was a historic moment in the data privacy and data regulation
# era. It showed that any data that is 'PUBLICLY AVAILABLE AND NOT COPYRIGHTED' is 
# fair game for web scrapers/crawlers
################################################################################################

import requests     # type: ignore
from bs4 import BeautifulSoup     # type: ignore

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
# print(movie_titles[::-1]) # to reverse the order of the list

# for n in range(len(movie_titles) - 1, -1, -1):  # we could alternatively use a forloop to print the list in reverse
#     print(movie_titles[n])



with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")