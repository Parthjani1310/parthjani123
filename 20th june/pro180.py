# Python program to find files having a particular extension using RegEx...

import re 

def search(ip_file):

    for fnames in ip_file: 

        search_ext = re.search("\.txt$", fnames) 

        if search_ext: 
            print("File with extension .txt is:", fnames) 

ip_file = ["py.html", "python.xml", "py.rar", "py.txt", "python.jpg"]

search(ip_file)
