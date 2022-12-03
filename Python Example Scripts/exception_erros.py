
# how to handle exceptions or errors in pyhton program. Very important


try:
    age = int (input ('enter age:> '))
    income = 20000
    risk = income/age
    print (age)

# define possible exceptions that can be caused by user input

except ZeroDivisionError:
    print('age can never b zero')   
except ValueError:
    print("invalid Value")





