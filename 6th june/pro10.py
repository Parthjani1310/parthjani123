def Fibonacci(n):
   if n<0:
      print("Fibbonacci can't be computed")
   # First Fibonacci number
   elif n==1:
      return 0
   # Second Fibonacci number
   elif n==2:
      return 1
   else:
      return Fibonacci(n-1)+Fibonacci(n-2)

n=10
print(Fibonacci(n))