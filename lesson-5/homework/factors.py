#task3
factors = int(input("Enter a positive integer:"))
for factor in range(1, factors+1):
    if factors % factor == 0:
       print(f"{factor} is a factor of {factors}")

