# Count the Number of matching characters in a pair of string....

def count(a,b):
    char_of_a=set(a)
    char_of_b=set(b)
    common_char= char_of_a & char_of_b
    print("commoon character: ",len(common_char))

a = input("Enter first string:")
b = input("Enter second string:")
count(a,b)

# def count(s1, s2):
#     char_of_s1=set(s1)
#     char_of_s2=set(s2)    
#     common_char= char_of_s1 & char_of_s2
#     print("Matching Characters: ",len(common_char))
# s1="abgfhij2@1"
# s2="@1khgabop"
# count(s1,s2)