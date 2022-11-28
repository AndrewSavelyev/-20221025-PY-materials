#Чем отличаются позиционные аргументы от именных?
#A simple function.

# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print “My favorite movie is named {name}”.
name_of_my_favorite_movie = "The Fountain"
def favorite_movie(name):
    print(f'My favorite movie is named {name}')

favorite_movie(name_of_my_favorite_movie)
