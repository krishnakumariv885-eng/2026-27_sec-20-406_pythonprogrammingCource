# Word Frequency using Dictionary

# Taking input from user
text = input("Enter a sentence: ")

# Splitting sentence into words
words = text.split()

# Creating an empty dictionary
frequency = {}

# Counting word frequency
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Displaying word frequency
print("\nWord Frequency:")

for word, count in frequency.items():
    print(word, ":", count)