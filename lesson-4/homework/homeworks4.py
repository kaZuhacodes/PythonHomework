#4
import random

while True:
    target  = random.randint(1, 100)
    attempts = 0
    
    while attempts < 10:
        guess = int(input("Enter random number: "))
        attempts += 1
        if guess > target:
            print("Too high!")
        elif guess < target: 
            print("Too low!")
        else: 
            print("You guessed it right!")
            break
    if guess == target:
        break 
    
    restart = input("You lost. Want to play again?")
    if restart not in ["Y", "YES", "OK", "y", "yes", "ok"]:
        break
