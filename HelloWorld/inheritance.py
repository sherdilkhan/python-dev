
# reusability of a class
#e.g.

class Mammal:
    def walk(self):
        print ("walk")

# lets inherite a class from Mammal

class Dog (Mammal):
    pass

# lets inherite a class from Mammal

class Cat (Mammal):
    pass
# as can be seen, both classes have same method but defined seperately in two classes.
# to avoid this. we will create a class with any name like "Mammal" with walk method.
# then inherite this method to creat Dog and Cat classes. Go to the top to see this class.

# now creat dog object

dog1 = Dog()
dog1.walk()