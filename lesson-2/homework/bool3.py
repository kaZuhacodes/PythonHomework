num = int(input("Number: "))
if num >= 0:
    if num % 2 == 0:
        print("positive and even")
    else:
        print("positive but not even")
else:
    print("not positive")