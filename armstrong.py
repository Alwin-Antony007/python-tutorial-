n = int(input("Enter a number:"))

num = n
sum = 0

l = len(str(n))
while num>0:
    digit = num % 10
    
    sum = sum + digit ** l
    num = num //10

if sum == n :
    print(f"{n} is an Armstrong")
else:
    print(f"{n} is not an Armstrong")