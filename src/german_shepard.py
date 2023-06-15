"""from dog import Dog


class GermanShepard(Dog):
    pass
    # TODO: override the walk() method"""

#####################################################
from dog import Dog

class GermanShepard(Dog):
    def walk(self):
        # Call the walk() method of the parent class (Dog)
        super().walk()
        # Print the specific behavior of German Shepards while walking or running
        print("German Shepards show their beautiful fur while running.")
