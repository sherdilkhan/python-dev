

class Dog:
    specie = 'Labrador Retriever'            #class attribute for Dog Class (same for all objects)
    def __init__(self, name, age):           #instance attributes for Dog Class (unique for all objects)
        self.name = name
        self.age = age
    
    def __str__(self):      #to print an object, this will give details of that object in a "pythonic Way" rather than "<__main__.Dog object at 0x00aeff70>"
        return f"my name is {self.name} and i am {self.age} years old"


    def introduce(self):                    #instance method for Dog Class
        return f"My Name is: {self.name}"
    
    def speak(self, sound):                 #instance method for Dog Class
        return f"i can scare you with my: {sound}"


pup1 = Dog("puppy", 12) #lets instantiate an object from class Dog. Now this objects has all the attributes of class Dog


print (pup1.name)
print (pup1.age)
print (pup1.specie)

pup1.specie = 'husky'  #class attributes can be changed dynamically
pup1.age = 8           #instance attributes can also be chnaged dynamically

print (pup1.specie)
print (pup1.age)

print (pup1.introduce())
print (pup1.speak('Bow Bow'))

print (pup1)

#The key takeaway here is that:
# Custom objects are mutable by default. 
# An object is mutable if it can be altered dynamically. 
# For example, lists and dictionaries are mutable, but strings and tuples are immutable.