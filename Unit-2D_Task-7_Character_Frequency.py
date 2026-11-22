text = input("Enter a string: ")
char = input("Enter a character: ")

count = 0

for ch in text:
    if ch == char:
        count += 1

print("Character Frequency:", count)