"""create the Pet Class:
Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
Implement get and set methods for each of these attributes.
Add a method called print_details that prints the details of the pet.
Create Instances:
Create three objects of the Pet class with different kinds, breeds, and names.
Call the print_details method for each object that you created
Demonstrate a Special Method or Function:
Choose three of the following and demonstrate its use with the Pet class instances:
__name__: Display the name of the class.
type(): Show the class used to instantiate a pet object.
__module__: Return the module name in which the Pet class is defined.
__bases__: Display the base classes of the Pet class (if any).
getattr(): Use it to access an attribute of a Pet instance.
isinstance(): Check if an instance is of the Pet class."""


class Pet:
    def __init__(self, kind, breed, name, temperment):  # creating  atributes
        self.__kind = kind
        self.__breed = breed
        self.__name = name
        self.__temperment = temperment

    def get_kind(self):
        return self.__kind

    def get_breed(self):
        return self.__breed

    def get_name(self):
        return self.__name

    def get_temperment(self):
        return self.__temperment

    def set_kind(self, value):
        self.__kind = value

    def set_breed(self, value):
        self.__breed = value

    def set_breed(self, value):
        self.__name = value

    def set_name(self, value):
        self.__temperment = value

    def print_details(self):  # prints the info
        print(f"{self.__kind}, {self.__name}, {
              self.__breed}, {self.__temperment}")


def main():
    ken_moray_0876 = Pet("Lizard", "Godzilla", "Chameleon",
                         "Skiddish, Standoff-ish")
    kary_name_0990 = Pet("Dog", "Zim", "German Shephard", "Gentle, Friendly")
    winston_lang_0012 = Pet("Cat", "Princess", "Persian", "Cat.")

    ken_moray_0876.print_details()
    kary_name_0990.print_details()
    winston_lang_0012.print_details()

    jim_bean_9099 = Pet("Turtle", "Monster", "Snapping", "Aggressive")
    print(type(jim_bean_9099))

    print(getattr(jim_bean_9099, '_Pet__temperment'))  # mangled

    print(isinstance(jim_bean_9099, Pet))

    print(Pet.__name__)

    print(Pet.__module__)

    print(Pet.__bases__)


main()
