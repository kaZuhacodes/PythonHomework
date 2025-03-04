import os
import string
from collections import Counter

def get_text():
    if not os.path.exists("sample.txt"):  
        text = input("File not found. Enter a paragraph to create 'sample.txt':\n")
        with open("sample.txt", "w") as file:
            file.write(text)

def count_words():
    get_text()
    
    with open("sample.txt", "r") as file:
        text = file.read().lower()  
        text = text.translate(str.maketrans('', '', string.punctuation))  
        words = text.split()
    
    word_count = Counter(words)  
    return words, word_count

def save_report(word_count, total_words, top_n=5):
    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top Words:\n")
        for word, count in word_count.most_common(top_n):
            file.write(f"{word} - {count}\n")

def main():
    words, word_count = count_words()
    total_words = len(words)
    
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in word_count.most_common(5):
        print(f"{word} - {count} times")
    
    save_report(word_count, total_words)
    print("Word count report saved to 'word_count_report.txt'.")

main()
