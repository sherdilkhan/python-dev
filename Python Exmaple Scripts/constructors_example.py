
#let define a new type Person with a method called talk() and an attribute name.


#let go

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print (f"Hi. I am {self.name}")

#let create an object with constructor with an attribute called name

person1 = Person("Sherdil")
person1.talk()

#lets create anothet object

person2 = Person("Sarah")
person2.talk()

