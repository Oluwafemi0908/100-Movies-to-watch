import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

movies = [movie.getText() for movie in soup.select(".article-title-description__text .title")]
movies_list = []
for num in range(99, -1, -1):
    movies_list.append(movies[num])

print(movies)
print(movies_list)

with open("Top movies.txt", "w", encoding="utf-8") as file:
    for movie in movies_list:
        file.write(movie + "\n")
