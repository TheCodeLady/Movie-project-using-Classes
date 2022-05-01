from actors import Actors


class ActorsList():

    """
    a class to store details of actors imported from the Actors class
    Attributes: a dictionary to hold the details
    Methods: actor_collection to update the dictionary
             remove_actor to remove an actor by the first name
             calculate_no_of_actor to get the number within the dictionary
             return_actor_details to return details of an actor by the actors first name
    """

    def __init__(self, collections_of_actor={}):
        self.collections_of_actor = collections_of_actor

    """
    constructor to create an object of the ActorList class
    with a dictionary object that will be assesed by other method
    in the class to store collection of actors
    """

    def actors_collection(self, actors_dict: dict):
        self.collections_of_actor.update(actors_dict)

    """
    class method to update the dictionary 
    object with actor details
    """

    def remove_actor(self, first_name):
        place_holder = []
        for key, value in self.collections_of_actor.items():
            if first_name == value.get_first_name():
                place_holder.append(key)
        if len(place_holder) == 1:
            self.collections_of_actor.pop(place_holder[0])
        elif len(place_holder) > 1:
            print("Multiple actor with same first name found")
            if input("Would you like to continue with the removal? Y/N").upper() == 'Y':
                for item in place_holder:
                    self.collections_of_actor.pop(item)

    """
    a method to remove an actor from the 
    collection by the actor's first name
    using a for loop and conditional statements
    """

    def calculate_no_of_actor(self):

        return len(self.collections_of_actor)

    """
    method to calculate and return
    number of actor in the collection
    """

    def return_actor_details(self, first_name):
        name_holder = []
        for key, value in self.collections_of_actor.items():
            if first_name == value.get_first_name():
                name_holder.append({"First name": value.get_first_name(),
                                    "surname": value.get_surname(),
                                    "Gender": value.get_gender(),
                                    "Date of Birth": value.get_date_of_birth()})
        return name_holder

    """
    a method to loop through the collection
    extract details one after the other, store in a temporary list 
    and return the details of all the actors
    """
