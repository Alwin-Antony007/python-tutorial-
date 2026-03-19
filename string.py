str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = str1 + "" + str2
print("Concatenated String: ", result)

start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing: "))
sliced_str = result[start:end]
print("Sub String: ", sliced_str)