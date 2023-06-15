"""from animal import Animal

class Dog(Animal):
    pass
    #TODO create a constructor for Dog, with 4 legs and 2 eyes!

    #TODO override the breathe() method!

    #TODO override the walk() method!"""

###########################################################

from animal import Animal

class Dog(Animal):
    def __init__(self):
        # Call the constructor of the parent class (Animal) with 4 legs and 2 eyes
        super().__init__(4, 2)

    def breathe(self):
        # Call the breathe() method of the parent class (Animal)
        super().breathe()
        # Print the specific behavior of dogs while breathing
        print("Dogs love to breathe with their mouths open.")

    def walk(self):
        # Call the walk() method of the parent class (Animal)
        super().walk()
        # Print the specific behavior of dogs while walking or running
        print("Dogs love to run.")

