# Counting the frequencies in a list using dictionary in Python...

# def countFreq(li):

#     freq = {}

#     for item in list:
#         if (item in freq):
#             freq[item] += 1
#         else:
#             freq[item] = 1

#         print[freq]

# li = [1,1,3,5,2,1,3,2,6,4]
# countFreq(li)

def CountFreq(li):
    freq = {}
    for item in li:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    print(freq) 
li =[1, 1, 3, 2, 6, 5, 3, 1, 3, 3, 1, 4, 6, 4, 4, 2, 2, 2, 2]
CountFreq(li)