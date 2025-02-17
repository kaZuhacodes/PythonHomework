string = input("Enter a string: ")
digit = any(char.isdigit() for char in string)

if digit:  
    print("Yes") 
else:
    print("No")
