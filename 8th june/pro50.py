# sort the first list using second list....

first_list = ["A","B","C","D","E","F"]
second_list = ['1','2','3','4','5','6']

zipped_pairs = zip(first_list,second_list)

sorted_pairs = sorted(zipped_pairs)

result = [item[1] for item in sorted_pairs]

print(result)