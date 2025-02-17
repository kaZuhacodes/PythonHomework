num = int(input("Number 1: "))
if num % 3 == 0:
    if num % 5 == 0:
        print("divisible")
    else:
        print("not divisible")
else:
    print("not divisible")