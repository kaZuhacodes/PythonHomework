name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
if birth_year <= 2025:
    print("Your age is: ", 2025 - birth_year)
else:
    print("Incorrect year of birth!")

