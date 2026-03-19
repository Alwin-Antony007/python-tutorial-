def btd(n):

    decimal = 0
    temp = n 
    base = 1
    while temp > 0:
        digit = temp % 10
        temp = temp // 10
        decimal += digit * base
        base *= 2
    return decimal

print("Binary to Decimal Conversion")
n = int(input("Enter a binary number: "))
print(f"The decimal equivalent of binary {n} : {btd(n)}")