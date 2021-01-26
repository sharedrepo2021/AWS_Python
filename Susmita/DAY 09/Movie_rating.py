from imdb import IMDb


ia = IMDb()
class Movie:
    def __init__(self):
        self.name = None

    def get_input(self):
        self.name = input("Enter the name of the movie:: ")

        for m in ia.search_movie(self.name):
            movie = ia.get_movie(m.getID())
            print(movie.data['original title'], movie.data['rating'])


if __name__ == '__main__':
    m = Movie()
    m.get_input()

