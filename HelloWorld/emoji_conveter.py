


# emoji conevertr function

def emoji_converter(message):

    words = message.split (' ')  # this will split the charater string into a list with multiple words based on space bar

    #lets define an emoji dictionary

    emojis = {
        ":)" : "😊 ",
        ":(" : "😔 "
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


input_text  = input ('> ')  

# lets call the emoji converter function 
#  
print (emoji_converter(input_text))