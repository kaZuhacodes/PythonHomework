string = input("Enter a string: ")
vowels = "aeiouAEIOU"
for vowel in vowels:
    string = string.replace(vowel, "")
print(string)