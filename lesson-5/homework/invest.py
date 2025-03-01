#task2
def invest(amount, rate, years):
    amount  = float(amount)
    rate = float(rate)
    years = int(years)
    for year in range(1, (years+1)):
        amount *= (1 + rate)
        print(f"Year {year}: ${amount:.2f}")
    


amount = input("Enter the principal amount: ")
rate = input("Enter the annual rate of return: ")
years = input("Enter the number of years: ")

invest(amount, rate, years)
