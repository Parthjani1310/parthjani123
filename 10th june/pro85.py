# String slicing in Python to rotate a string...

def rotate_string(s,d):
    Lfirst = s[0:d]
    Lsecond = s[d:]
    Rfirst = s[0: len(s)-d]
    Rsecond = s[len(s)-d : ]

    print ("Left rotation : ",(Lsecond+Lfirst))
    print("Right Rotation : ",(Rsecond+Rfirst))

string = input("Enter string : ")
d = 3

rotate_string(string,d)