# wap a program to count frequency of each character in a string

str = input("Enter a string: ")

dict = {}

stri = str.lower()

for i in stri:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)