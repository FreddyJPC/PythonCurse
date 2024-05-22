def count_words(text):
    words = text.split()
    return len(words)

text = input("Enter a text string: ")
word_count = count_words(text)
print("Number of words:", word_count)