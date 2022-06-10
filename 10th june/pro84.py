# Execute a String of Code in Python...

def execute_code():
   
    Code="""

def check_prime_no(num):

  for i in range(2, num):

     if (num % i) == 0:
        return "Not Prime" 

     else:
        return "Prime"

print(check_prime_no(12)) """

    exec(Code)

execute_code()