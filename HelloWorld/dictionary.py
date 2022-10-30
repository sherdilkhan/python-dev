
#dicitonary is useful in naming different vairables names

# lets define a numbers dictionary as below

number_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
}



numbers = input("enter a number: ")

for number in numbers:
    print (number_mapping.get(number))
