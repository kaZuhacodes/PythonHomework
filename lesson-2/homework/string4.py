palindrome = input("Enter a word: ")
if palindrome == palindrome[::-1]:
    print("This is a palindrome")
else:
    print("This is not a palindrome")