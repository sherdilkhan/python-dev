

# define a Class footprint
class Engineer:
    def __init__(self, name, field) -> None:  #this method is always called when an object is created (its constructor method)
        print('Hey! an Object is created')
        self.name = name
        self.field = field
    def info(self):
        print(f'My name is {self.name} and i am a/an {self.field}') # self is ref.  to current instance

# create an object from above Class or footprint

a = Engineer('sumair', 'Mechanical Engineer')
b = Engineer('Sherdil', 'ELectrical Engineer')


a.info()
b.info()












