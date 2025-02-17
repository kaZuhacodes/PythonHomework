sentence = input("Enter a sentence:")
words = sentence.split()
l = [word[0] for word in words]
acronym = ''.join(l)
print(acronym)
