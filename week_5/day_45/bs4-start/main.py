from bs4 import BeautifulSoup
import requests

url = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
list_best_movies = response.text

soup = BeautifulSoup(list_best_movies, "html.parser")

titles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

movie_list = []
# movie_rank = []

# for mov in titles:
#     titles_text = mov.get_text().split(" ", 1)
#     if len(titles_text) > 1:
#         after_first_space = titles_text[1]
#     else:
#         after_first_space = ""
#     movie_list.append(after_first_space)
#
#     titles_rank = mov.get_text().split()[0]
#     movie_rank.append(titles_rank)

for movie in titles:
    movies_text = movie.get_text()
    movie_list.append(movies_text)

# movie_rank.reverse()
movie_list.reverse()
# print(movie_rank)
# print(movie_text)

with open("movieList.txt", "w", encoding="utf-8") as file:
    for item in movie_list:
        file.write(f"{item}\n")

# print(movie_list)