
from movies import Movies


class MovieList:

    """
     a class to store details of movies imported from the Movies class
    Attributes: a dictionary to hold the movies details
    Methods: movie_list_dictionary to update the dictionary
             find_movie to search for a movie with either it's title, genre or 
             release date remove_movie to remove a movie by it's title
             calculate_no_of_movies to get the number within the dictionary

    """

    def __init__(self, movie_dictionary ={}):
        self.movie_dictionary = movie_dictionary

    """
    constructor to create an object of the MoviesList class
    with a dictionary object that will be assesed by other method
    in the class to store collection of movies
    """

    def movies_list_dictionary(self, movie_list: dict):

        self.movie_dictionary.update(movie_list)

    """
    class method to update the dictionary 
    object with details of movies
    """

    def find_movie(self, title: str = None, genre: str = None, release_date: str = None):
        found_movie_list = {}
        for key, value in self.movie_dictionary.items():
            if title is None:
                if genre is None:
                    if release_date is None:
                        continue
                    elif release_date == value.get_release_date():
                        found_movie_list[key] = value
                elif genre == value.get_genre():
                    if release_date is None:
                        found_movie_list[key] = value
                    elif release_date == value.get_release_date():
                        found_movie_list[key] = value
            elif title == value.get_title():
                if genre is None:
                    if release_date is None:
                        found_movie_list[key] = value
                    elif release_date == value.get_release_date():
                        found_movie_list[key] = value
                elif genre == value.get_genre():
                    if release_date is None:
                        found_movie_list[key] = value
                    elif release_date == value.get_release_date():
                        found_movie_list[key] = value
        return found_movie_list

    """
    a method to loop through the collection of movies using for loops 
    and nested if statements,
    extract a movie based on either the title, genre or 
    release date, store in a temporary place holder 
    and return the details of the movie found
    """

    def remove_movies(self, title: str):
        self.movie_dictionary = {key: value for key, value in self.movie_dictionary.items(
        ) if value.get_title() != title}

    """
    a method to remove a movie based on it's title from the 
    collection
    using a dictionary comprehension
    """

    def calculate_no_of_movies(self):
        return len(self.movie_dictionary)
    """
    method to calculate and return
    number of movies in the collection
    """
