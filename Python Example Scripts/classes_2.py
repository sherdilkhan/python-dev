
#define a class DOG



class dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age (self):
        return self.age

    def bark(self):
        print ('bark')
    def add(self, x):
        return x+1


dog1 = dog('tim',10)

dog2 = dog('tom', 12)

print (dog1.get_name())

print (dog2.get_age())





