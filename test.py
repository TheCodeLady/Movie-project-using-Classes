from movies import Movies
from movieslist import MovieList
from actors import Actors
from actorlist import ActorsList

oo7 = Movies("Spectre", 2015, "Action", "26-Oct-2015")
actions = MovieList({"oo7": oo7})
JamesBond = Actors("James", "Bond", "Male", "02-Mar-1968")
all_actors = ActorsList({"JamesBond": JamesBond})

"""
creating instances of the 4 classes
while passing in arguments
"""

print(oo7.get_title())
print(oo7.get_year())
print(oo7.get_genre())
print(oo7.get_release_date())
print(oo7.random_id)


print(all_actors.calculate_no_of_actor())
print(all_actors.return_actor_details("James"))
print(all_actors.remove_actor("James"))
print(all_actors.calculate_no_of_actor())

"""
statements to call movie
object method to retrieve the movie object details

statement to call movieslist object 
method to get the number of movies in it's collection

statement to call actorlist object method to 
get the details of the actor 

statement to call actorslist object 
method to get the number of actors in it's collection
before calling the remove method

statement to call the actorlist object method 
to remove the detials of the actor passed to it

statement to call actorslist object 
method to get the number of actors in it's collection

statement to retrieve the movie ID that randomly generates

"""
