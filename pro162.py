# Python program to convert time from 12 hour to 24 hour format...

import datetime


def timeconvert(str1):
      if str1[-2:] == "AM" and str1[:2] == "12":
         return "00" + str1[2:-2]
      elif str1[-2:] == "AM":
         return str1[:-2]
      elif str1[-2:] == "PM" and str1[:2] == "12":
         return str1[:-2]
      else:
        return str(int(str1[:2]) + 12) + str1[2:8]
dt=datetime.datetime.now()
print("Conversion Of Time ::",timeconvert(dt.strftime("%H:%M:%S")))