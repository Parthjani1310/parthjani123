# Python program to Count Uppercase, Lowercase, special character and numeric values using Regex...

def count_chars(str):
    upper_ctr,lower_ctr,numeric_ctr,special_ctr = 0,0,0,0

    for i in range(len(str)):
        if str[i] >= 'A' and str[i] <= 'Z' :upper_ctr += 1
        elif str[i] >= 'a' and str[i] <= 'z' :lower_ctr += 1
        elif str[i] >= '0' and str[i] <= '9' :numer_ctr += 1
        else :
            special_ctr += 1
            return upper_ctr,lower_ctr,numeric_ctr,special_ctr 

str = "@pj1310.com"
u, l, n, s = count_chars(str)
print ("\nUpper case is : ",u)
print ("\nLpper case is : ",l)
print ("\nNumber case is : ",n)
print ("\nSpecial character case is : ",s)
