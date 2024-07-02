import requests
from bs4 import BeautifulSoup

movie_endpoint = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(movie_endpoint)
movie_content = response.text

soup = BeautifulSoup(movie_content, 'html.parser')

movie_list = soup.find_all(name="h3", class_="title")
movie_list.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_list:
        file.write(f"{movie.getText()}\n")

