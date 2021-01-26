from imdb import IMDb

moviesDB = IMDb()
top = moviesDB.get_top250_movies()
bottom = moviesDB.get_bottom100_movies()
print("Top 10 Movies")
print('\n')
movieinfolist = []
print("Top", top)

for i in range(len(top[0:10])):
    id = top[i].movieID
    series = moviesDB.get_movie(id)
    rating = series.data['rating']
    print(i)
    print("Name of the Movie", top[i])
    print("Movie Rating", rating)

