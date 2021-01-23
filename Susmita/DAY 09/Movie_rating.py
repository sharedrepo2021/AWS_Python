from imdb import IMDb


ia = IMDb()
# code = input("Enter the code of the movie:: ")
# get a movie
# movie = ia.get_movie(code)
# rating = movie.data['rating']
# print(movie)
# print(rating)
# print(movie.data)
#
# for key, value in movie.data.items():
#     print(key, value)
#
# # print the names of the directors of the movie
# print('Directors:')
# for director in movie['directors']:
#     print(director['name'])
#
# # print the genres of the movie
# print('Genres:')
# for genre in movie['genres']:
#     print(genre)
#
# # search for a person name
# # people = ia.search_person('Mel Gibson')
# # for person in people:
# #    print(person.personID, person['name'])
name = input("Enter the name of the movie:: ")

for m in ia.search_movie(name):
    movie = ia.get_movie(m.getID())
    print(movie.data['original title'], movie.data['rating'])
