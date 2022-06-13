# Python Counter to find the size of largest subset of anagram words...

from collections import Counter

def maxAnagramsize(input):

    input = input.split("")

    for i in range(0,len(input)):
        input[i]=''.join(sorted(input[i]))

    freqDict = Counter(input)

    print(max(freqDict.values()))

if __name__ == "__main__":
    
    input = 'ant magenta magnate tan gnamate'
    maxAnagramSize(input)