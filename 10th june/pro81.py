# Replace multiple words with K....


string = " virat is best cricketer in the world"

print("The actul string is : "+str(string))

word_list = ["best","cricketer","world"]

replace_word = "k"

replaced_string = ' '.join([replace_word if i in word_list
        else i for i in string.split()])

print("String after multiple replace : "+ str(replaced_string))