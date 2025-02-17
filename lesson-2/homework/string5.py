vowels = "aeiouAEIOU"
string=str(input ("String: "))
vowel_count=0
for char in string:
    if char in vowels:
        vowel_count+=1
print(f'There are {vowel_count} vowels in {string}')