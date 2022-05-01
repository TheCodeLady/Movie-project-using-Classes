class Actors():
    """
    a class to set and get details of actors
    Attribute: first_name, surname, gender and date_of_birth
    Methods: a set method for each of the attributes
             a get method for each of the attributes
    """

    def __init__(self, first_name, surname, gender, date_of_birth):
        self.first_name = first_name
        self.surname = surname
        self.gender = gender
        self.date_of_birth = date_of_birth

    """
    a constructor of the actors class 
    to create an object of each attribute
    """

    def set_first_name(self, first_name):
        self.first_name = first_name
    """
    a method to set the first name
    """

    def set_surname(self, surname):
        self.surname = surname
    """
    a method to set the surname
    """

    def set_gender(self, gender):
        self.gender = gender
    """
    a method to set the gender
    """

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    """
    a method to set the date of birth
    """

    def get_first_name(self):
        return self.first_name

    """
    a method to retrieve the first name
    """

    def get_surname(self):
        return self.surname

    """
    a method to retrieve the surname
    """

    def get_gender(self):
        return self.gender

    """
    a method to retrieve the gender
    """

    def get_date_of_birth(self):
        return self.date_of_birth
    """
    a method to retrieve the date of birth
    """
