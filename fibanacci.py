n = int(input("Enter a number n to find its Fibonacci series up to n terms: "))

def fibanacci(n):
   if n == 0:
       return 0
   elif n == 1:
       return 1
   else:
        return fibanacci(n-1) + fibanacci(n-2)
   

print(fibanacci(n))