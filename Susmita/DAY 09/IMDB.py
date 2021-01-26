# importing the module
import imdb


def search_movie(movie_name):
    # searching the name
    search = ia.search_movie(name)
    print("Movie names matched are:")
    # loop for printing the name and id
    for i in range(len(search)):
        try:
            # getting the id
            id = search[i].movieID
            series = ia.get_movie(search[i].movieID)
            # getting rating of the series
            rating = series.data['rating']
            cast = series.data['cast']
            # printing the object i.e name
            print("Movie name: ", series)
            cast_crew = ''
            # print the rating
            print("Rating of the movie: ", rating)
            count = 0
            for i in range(len(cast)):
                if count == 0:
                    cast_crew += str(cast[i])
                else:
                    cast_crew += "," + str(cast[i])
                count += 1
            print("cast crew of the movie: ", cast_crew)
        except:
            print("Movie name: ", series, "No Rating found")


try:
    ia = imdb.IMDb()
    name = input("Enter the movie name: ")
    search_movie(name)
except Exception as e:
    print(e)