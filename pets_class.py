class Mammal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        """
        Returns:
            str: contains the name and age of the dog
        """
        return '{0} is {1}'.format(self.name, self.age)


class Dog(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.is_hungry = True

    def eat(self):
        """
        Sets an instance variable is_hungry to False

        Returns:
            bool: True if hungry, False otherwise
        """
        self.is_hungry = not self.is_hungry
        return self.is_hungry

    def walk(self):
        """
        Returns:
            str: Indicating that the dog is walking
        """
        return "{} is walking".format(self.name)


class Pets:
    species = 'mammals'

    def __init__(self, **kwargs):
        self.number_of_dogs = len(kwargs)
        self.mammals = kwargs

    def get_number_of_dogs(self):
        """
        Returns:
            str: indicating the number of dog added 
        """
        return "I have {} dogs".format(self.number_of_dogs)

    def display_mammals(self):
        """
        Loops through a list of dogs and prints out every dog
        name with its age
        """
        for dog in self.mammals.values():
            print("{0} is {1}".format(dog.name, dog.age))

    def get_species(self):
        """
        Retruns:
            str: indicating that all dogs are mammals
        """
        return "And they are all {}, of cource".format(self.species)

    def feed_dogs(self):
        """
        Loops through a list of dogs and feeds them

        Returns:
            str: indicating that all have been fed
        """
        for dog in self.mammals.values():
            dog.eat()
        return "My dogs are not hungry"

    def walk(self):
        """
        Loops through a list of dogs and make them walk
        """
        for dog in self.mammals.values():
            print("{} is walking".format(dog.name))


"""
Create 3 dog instances and assign them to an 
instance of the Pets class
"""
pets = Pets(
    tom=Dog('Tom', 6),
    fletcher=Dog('Fletcher', 7),
    larry=Dog('Larry', 9)
)

#  Display output
print(pets.get_number_of_dogs())
pets.display_mammals()
print(pets.get_species())
print(pets.feed_dogs())
pets.walk()
