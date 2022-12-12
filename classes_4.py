

class Dog:
    specie = 'Labrador Retriever'    #class attribute for Dog Class (same for all objects)
    def __init__(self, name, age):   #instance attributes for Dog Class (unique for all objects)
        self.name = name
        self.age = age


pup1 = Dog("puppy", 12) #lets instantiate an object from class Dog. Now this objects has all the attributes of class Dog


