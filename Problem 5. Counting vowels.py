#counting vowels in a string
text = input("Enter a string: ").lower()

vowels = "aeiou"

count = 0

for i in text:
    if i in vowels:
        count += 1
print(f"Number of vowels: {count}")

