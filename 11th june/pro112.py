# Python dictionary, set and counter to check if frequencies can become same...
from collections import Counter
def check_all_same(my_input):
    my_dict = Counter (my_input)

    input_2 = list(set(my_dict.values()))
    if len(input_2)>2:
        print("The frequencies are not same")
    elif len(input_2)==2 and input_2[1]- input_2[0]>1:
        print("The frequencies are not same")
    else:
        print("The frequencies are same")

my_str = input("Enter Values : ")
print("The string is : ")
print(my_str)
check_all_same(my_str)