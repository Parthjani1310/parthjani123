# Python program to read file word by word...


# with open('C:\\Users\\pj\\Documents\\GitHub\\parthjani123\\20th june\\pj123.txt','r') as file:
# 	for line in file:		
# 		for word in line.split():	
# 			print(word)

with open('pj123.txt','r') as file:
	for line in file:		
		for word in line.split():	
			print(word)