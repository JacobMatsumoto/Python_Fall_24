"""Now, let's practice using tuples. Imagine you're planning the classes
 for a programming certificate. You need to list out six classes. Here's what you need to do:

Create a tuple named programming_classes with these classes: 'Intro to Python',
'Advanced Python', 'Database Essentials', 'Web Development Basics', 
'Data Structures in Python', 'Web Design Fundamentals'.
Write a program that uses a for loop to print each class in the tuple.
Use the len function to print how many classes are in the tuple.
Make sure to use a main function for this program.
Try this out, and you'll get a good grasp of how tuples work in Python!"""


def main():#main is the primary function for this program listing the items in the tuple and counting them
    programming_classes = ('Intro to Python', 'Advanced Python', 'Database Essentials', 
                           'Web Development Basics', 'Data Structures in Python',
                           'Web Design Fundamentals')
    for classes in programming_classes: #I found you can't use "class" after the for here, 
        #I'm not sure what causes this but I'm guessing it has to do with something 
        # else important being named class.
        print(classes)
    number_of_classes = len(programming_classes) #obtaining length
    print(f"There are {number_of_classes} classes ")

main() #forgot this -.-
