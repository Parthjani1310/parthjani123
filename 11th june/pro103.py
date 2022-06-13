# Print anagrams together in Python using List and Dictionary...

def  allAnagram(input):

    dict= {}

    for strval in input:

        key = ''.join(sorted(strval))

        if key in dict.keys():
            dict[key].append(strval)
        else:
            dict[key]=[]
            dict[key].append(strval)

            output = " "
            for key,value in dict.items():
                output= output + ''.join(value)+''
                return output

if __name__=="__main__":
    input = ['cat','dog','tac','god','act']
    print (allAnagram(input))