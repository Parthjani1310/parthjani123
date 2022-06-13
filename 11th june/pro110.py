# Convert a list of Tuples into Dictionary...

def convert(tup,di):
    di = dict(tup)
    return di

tups = [("Aadi",50),("Maya",36),("Yash",52),("Jay",68)]
dictionary = {}
print(convert(tups,dictionary))
