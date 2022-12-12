

class Dog:
    specie = 'Labrador Retriever'    #class attribute for Dog Class (same for all objects)
    def __init__(self, name, age):   #instance attributes for Dog Class (unique for all objects)
        self.name = name
        self.age = age


pup1 = Dog("puppy", 12) #lets instantiate an object from class Dog. Now this objects has all the attributes of class Dog


print (pup1.name)
print (pup1.age)
print (pup1.specie)

pup1.specie = 'husky'  #class attributes can be changed dynamically
pup1.age = 8           #instance attributes can also be chnaged dynamically

print (pup1.specie)
print (pup1.age)