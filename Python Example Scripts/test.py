# script.py

def my_function():
    print("Function inside script.py")
    

if __name__ == "__main__":
    print("This code runs when script.py is executed directly as the main program.")
    my_function()
else:
    print("This code runs when script.py is imported as a module into another script.")
