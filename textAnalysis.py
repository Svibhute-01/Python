text = input("Enter your paragraph: ")

words = text.split()
word_count = len(words)

space_count = text.count(' ')

word_freq = {}
for word in words:
    word = word.lower().strip(".,!?")  # clean punctuation
    word_freq[word] = word_freq.get(word, 0) + 1

top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:3]

vowel_count = sum(1 for char in text.lower() if char in 'aeiou')

print("\n--- Text Analysis Result ---")
print("Total number of words:", word_count)
print("Total number of spaces:", space_count)
print("Number of vowels:", vowel_count)

print("\nWord Frequencies:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

print("\nTop 3 most frequent words:")
for word, freq in top_words:
    print(f"{word}: {freq}")