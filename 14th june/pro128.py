# Python – Convert Nested Tuple to Custom Key Dictionary...

from re import sub


tuple = ((15,'jash',2),(9,'my',4),(8,'great',18))

print("The original tuple : " +str(tuple))

keys = ['key','value','id']

res = [{key : val for key,val in zip(keys,sub)}
            for sub in tuple]

print("The converted dictionary : "+str(res))