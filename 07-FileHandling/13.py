movie_titles = ["John Wick", "Star Wars", "Uncharted", "Indiana Jones", "Taxi"]
file = open("movies.txt", 'a')
for movie in movie_titles:
    file.write(movie+"\n")
file.close()