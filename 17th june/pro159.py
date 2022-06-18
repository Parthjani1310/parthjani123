# Python program to get Current Time...

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time is :", current_time)


 