str = input("Enter text : ")
rev=""

for i in str:
    rev = i + rev

if str == rev:
    print(f"{str} is a palindrome")
else:   
    print(f"{str} is not a palindrome")

fh="" 
sh=""
for i in range(len(str)//2):
    fh = fh + str[i]

for i in range(len(str)//2, len(str)):
    sh = sh + rev[i]

if fh == sh:
    print(f"{str} is a symmetric")
else:
    print(f"{str} is not a symmetric")

