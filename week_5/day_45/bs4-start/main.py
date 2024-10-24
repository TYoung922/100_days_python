from bs4 import BeautifulSoup
import requests

url = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
list_best_movies = response.text

soup = BeautifulSoup(list_best_movies, "html.parser")

titles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

movie_list = []

for movie in titles:
    movies_text = movie.get_text()
    movie_list.append(movies_text)

movie_list.reverse()

with open("movieList.txt", "w", encoding="utf-8") as file:
    for item in movie_list:
        file.write(f"{item}\n")

# print(movie_list)