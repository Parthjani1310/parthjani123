# Python program to extract IP address from file...

# importing the module
# import re

# # opening and reading the file
# with open('C:\Users\pj\Documents\GitHub\parthjani123\20th june\pro175.py') as fh:
#     fstring = fh.readlines()

# # declaring the regex pattern for IP addresses
# pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# # initializing the list object
# lst=[]

# # extracting the IP addresses
# for line in fstring:
#     lst.append(pattern.search(line)[0])

# # displaying the extracted IP addresses
# print(lst)

import re
blacklist = list(open("/home/asad/blackdb/blacklist", 'r').read().split('\n'))
logfile = list(open('/home/asad/logdb/snort.alert', 'r').read().split('\n'))
newip = []
for entry in logfile:
        ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', entry)
        for ip in ips:
            newip.append(ip)
newblist = blacklist + newip
with open("/home/asad/blackdb/blacklist", 'w+') as f:
        f.write('\n' .join(set(newblist))+'\n\n')
        f.close()
