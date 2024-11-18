"""Define a Pet Class:
Create private properties: owner_first_name, owner_last_name, pet_id, pet_name, and pet_type.
Set a default value for pet_type as "Dog".
Implement getter and setter methods for all properties.
Include a class variable vet_name set to the name of your veterinary office.
Add a method display_pet_info to print all details of the pet and owner.
Create Pet Objects:
Instantiate at least three pet objects with different details.
Show the use of setter methods for at least one pet object.
Implement Property Existence Check:
Write a function check_property that uses hasattr() to verify if a
property exists in a pet object.
Display Information:
Use display_pet_info to print details for each pet.
Show examples of check_property being used on various properties and pets.
Deliverables
Source code for the Pet class and a script demonstrating its functionality uploaded to GitHub.
Hand in the link to your code on Canvas. """


class Pet:  # class for pet (customer?) information,

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        # instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    def get_owner_first_name(self):
        return self.__owner_first_name

    def get_owner_last_name(self):
        return self.__owner_last_name

    def get_pet_id(self):
        return self.__pet_id

    def get_pet_name(self):
        return self.__pet_name

    def get_pet_type(self):
        return self.__pet_type

# owner_first_name, owner_last_name, pet_id, pet_name, pet_type <ease of copy paste
    def set_owner_first_name(self, value):
        self.__owner_first_name = value

    def set_(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value

    def set_pet_name(self, value):
        self.__pet_name = value

    def set_pet_type(self, value):
        self.__pet_type = value

# owner_first_name, owner_last_name, pet_id, pet_name, pet_type <for ease of copy paste
    def pet_info(self):  # prints the info
        print(f"{self.__owner_first_name}, {self.__owner_last_name}, {
              self.__pet_id}, {self.__pet_name}, {self.__pet_type}")

    def display_pet_details(self):  # another way to display
        print("Pet Details:", vars(self))


def main():  # sets (customer?) info in the class
    james_lawleit = Pet("James", "Lawleit", "009827", "Joey", "Cat")
    james_lawleit.set_pet_name("Zoey")

    carrie_shooop = Pet("Carrie", "Shooop", "008998", "Biggie")

    jarna_klarna = Pet("Jarna", "Klarna", "009877", "Polly", "Parrot")

    james_lawleit.pet_info()
    carrie_shooop.display_pet_details()
    jarna_klarna.display_pet_details()

    return james_lawleit
    return carrie_shooop  # i tried a few other methods to transfer these over
    return jarna_klarna  # i dont know if there is an easier/ more efficient way but this
    # worked for me, I looked back at my dictionaries and just putting james_lawleit = main
    # didn't work quite right, it just passed false for the has attr


def check_property():  # checks properties
    james_lawleit = main()
    carrie_shooop = main()
    jarna_klarna = main()
    print(hasattr(james_lawleit, "_Pet__pet_name"))
    print(hasattr(carrie_shooop, "_Pet__business_card"))
    print(hasattr(jarna_klarna, "_Pet__pet_id"))
    print(hasattr(carrie_shooop, "_Pet__pet_name"))


main()
check_property()
