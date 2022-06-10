# Dictionary and counter in Python to find winner of election...

from collections import Counter

def winner(input):

    votes = Counter(input)

    dict = {}

    for value in votes.values():

        dict[value]=[]

    for (key,value) in votes.items():
        dict[value].append(key)

    maxvote = sorted(dict.keys(),reverse=True)[0]

    if len(dict[maxvote])>1:
        print (sorted(dict[maxvote])[0])
    else:
        print (dict[maxvote][0])

if __name__=="__main__":
    input=['jay','jinal','parth','akshay',
            'parth','jay','jigar','parth',
            'akshay']

    winner(input)        