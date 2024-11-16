string = input("Enter the string: ")

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
removed_punctuation = ""
for i in string:
    if i not in punctuation:
        removed_punctuation += i
print(f"String after removing punctuation: {removed_punctuation}")

lower_case = removed_punctuation.lower()
print(f"Lowercase: {lower_case}")

vowels = "aeiou"
count = 0
for i in removed_punctuation:
    if i in vowels:
        count += 1
print(f"Number of vowels: {count}")

lists = list(lower_case)
lists.reverse()
reversed_str = "".join(lists)
print(f"Reversed string: {reversed_str}")