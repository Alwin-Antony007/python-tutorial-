amount = int(input("Enter inital investment amount: "))
rate = float(input("Enter annual interest rate (in %): "))
years = int(input("Enter number of years for investment: "))

print("Year     Amount")
for i in range(years):
    amount = amount + (amount * rate / 100)
    print(f"{i+1}       {amount:.2f}")