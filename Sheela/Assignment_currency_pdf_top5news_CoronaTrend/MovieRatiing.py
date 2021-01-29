from imdb import IMDb
import imdb
import json


class Movierating():
    def __init__(self):
        self.moviesDB = IMDb()

    def topbottommovies(self):
        top = self.moviesDB.get_top250_movies()
        bottom = self.moviesDB.get_bottom100_movies()
        print("*************Top 10 Movies*********************************")
        movieinfolist = []
        for i in range(len(top[0:10])):
            id = top[i].movieID
            series = self.moviesDB.get_movie(id)
            rating = series.data['rating']
            print(i+1, "Name of the Movie :", top[i])
            print("Movie Rating", rating)
        print("***************************************************************")
        print("********************Bottom 10 Movies************************")
        for i in range(len(bottom[0:10])):
            id = bottom[i].movieID
            series = self.moviesDB.get_movie(id)
            rating = series.data['rating']
            print(i+1, "Name of the Movie :", bottom[i])
            print("Movie Rating", rating)

    def specificmovie(self, moviename):
        search = self.moviesDB.search_movie(moviename)
        movieid = search[0].movieID
        series = self.moviesDB.get_movie(movieid)
        rating = series.data['rating']
        print("Name of the Movie :", moviename)
        print("Rating", rating)

if __name__ == '__main__':

    print("***************Movie Rating*****************************")

    option_movie = {
        1: 'Top & Bottom 10 Movie Rating',
        2: 'Specific Movie Rating',
        3: 'Exit'
    }
    print(json.dumps(option_movie, indent=4))
    while True:

        movierating = Movierating()
        choice = input("Enter your choice: ")
        if choice == "1":
            movierating.topbottommovies()
        elif choice == "2":
            moviename = input("Enter the movie name to get the rating: ")
            movierating.specificmovie(moviename)
        elif choice == "3":
            break
        else:
            print("Invalid choice!! Give numbers specified in the options")


