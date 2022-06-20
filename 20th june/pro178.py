# Python Program to validate an IP address using ReGex...

import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def check(Ip):

	if(re.search(regex, Ip)):
		print("Valid Ip address")
		
	else:
		print("Invalid Ip address")
	

# Driver Code
if __name__ == '__main__' :
	
	# Enter the Ip address
	Ip = "192.168.35.14"
	
	# calling run function
	check(Ip)

	
