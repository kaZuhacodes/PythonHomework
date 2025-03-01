#task1
def convert_cel_to_far(C):
    return round(C * 9/5 + 32, 2)

def convert_far_to_cel(F):
    return round((F - 32) * 5/9, 2)


C = float(input("Enter a temperature in degrees C: "))
f_result = convert_cel_to_far(C)
print(f"{C} degrees C = {f_result} degrees F")

F = float(input("Enter a temperature in degrees F: "))
c_result = convert_far_to_cel(F)
print(f"{F} degrees F = {c_result} degrees C")