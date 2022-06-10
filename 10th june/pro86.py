# String slicing in Python to check if a string can become empty by recursive deletion...

def solve (s,t):
   
    while len(s)>0:
   
        position = s.find(t)
        if position == -1:
            break

        s = s.replace(t,"",1)
    