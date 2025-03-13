# Your Student ID:230543011
# Your Name and Surname:Yağmur Çelikkaya
word = input("Enter a string: ")
print("Character frequencies: ")
charCount = {}
for i in word:
    charCount[i] = charCount.get(i, 0) + 1
for i in sorted(charCount):
    print(f"{i}: {charCount[i]}")

