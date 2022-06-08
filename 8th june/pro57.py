# Get kth column in matrix...

input_list = [[6,4,7], [10,2,5], [6,13,17]]

k = 1

print("The original list is : "+str(input_list))

# Using list comprehension

ele = [i[k] for i in input_list]

print("The Kth column of matrix using list comprehension : "+str(ele))


# Using zip()
ele1 = list(zip(*input_list))

print("The Kth column of matrix using zip() : "+str(ele1[k]))