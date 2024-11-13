"""Class Creation: Design a class named Person that includes the following data: 
name, address, age, and phone number.
Accessor and Mutator Methods: Write get and set methods for each piece of data. 
These methods allow you to access and change the data safely.
Creating Instances: Write a program that creates three instances (objects) of the Person class
. Use one instance for your made-up information
 and the other two for imaginary friends or family members.
Display Data: Print out the information stored in each instance.
 Ensure the output is formatted and easy to read."""


class Person:
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number

    def set_name(self, value):
        self.__name = value

    def set_address(self, value):
        self.__address = value

    def set_age(self, value):
        self.__age = value

    def set_phone_number(self, value):
        self.__phone_number = value

    def person_info(self):
        print(f"{self.__name}, {self.__address},{
              self.__age},{self.__phone_number}")

    def person_details(self):
        print("Person's Details:", vars(self))


def main():
    jacob = Person('Jacob Matsumoto', '1510 Shelton Ln.',
                   23, "(1)224-600-3024")
    jacob.person_info()
    jacob.person_details()

    amanda = Person('Amanda Matsumoto', '1510 Shelton Ln.',
                    44, '(1)224-383-4627')
    amanda.person_info()
    amanda.person_details()

    rich = Person('Richard Racila', '1667 richmond Ct.', 43, '(1)224-600-3927')
    rich.person_info()
    rich.person_details()


main()
