
#problem 2
# mylist = [5,10,5,20,10]
# print("The list is: ",mylist)
# convert = set(mylist)
# result = list(convert)
# print("List after removing duplicates: ",result)
#or
# for i in mylist:
#     while 1 < mylist.count(i) :
#         mylist.remove(i)
# print(mylist)


#problem 3
# text = "Tonni"
# vowel = "aeiouAEIOU"
# vowel_count = 0
# for char in text:
#     if char in vowel:
#         vowel_count += 1
# print(text)
# print(f"Lowercase: {text.lower()}")

# text2 = list(text)
# reverse1 = text2.reverse()
# reverse2 = "".join(text2)
# print(reverse2)

# print(f"Reversed string: {text[::-1]}")
# print("Number of vowels in the string: ",vowel_count)


#problem 4
# n1 = int(input("Enter the starting number: "))
# n2 = int(input("Enter the ending number: "))
# for i in range(n1,n2+1):
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)

# nested_list = [[1,2,3],[4,5,6],[7,8,9]]
# flattened_list = []
# for sublist in nested_list:
#     for item in sublist:
#         flattened_list.append(item)
# print(flattened_list)


#finding second largest number
# numbers = list(map(int, input("Enter a list of numbers: ").split(" ")))
# numbers.sort(reverse=True)
# if len(numbers) < 2:
#     print("List must contain at least two numbers.")
# else:
#     largest = numbers[0]
#     second_largest = None
#     for num in numbers:
#         if num < largest:
#             second_largest = num
#             break
#     if second_largest is not None:
#         print(f"Second largest number: {second_largest}")
#     else:
#         print("There is no second largest number, all elements are the same.")

#problem 8: string compression
# string = "aaabbbbcc"
# compressed_str = ""
# count = 1
# for i in range(len(string)):
#     if i < len(string)-1 and string[i] == string[i+1]:
#         count += 1
#     else:
#         compressed_str += string[i] + str(count)
#         count = 1
# print(f"Compressed string is: {compressed_str}")


#problem 10: finding palindrome in list
# strings = ['radar','hello','level','world','madam','python']
# palin = []
# for i in strings:
#     if i == i[::-1]:
#         palin.append(i)
# print(f"Palindrome in the list: {palin}")


#problem 11: lucky student
# num_students = int(input("Enter the number of students: "))
# names = []
# tokens = []
# scores = []
#
# for i in range(num_students):
#     details = input(f"Enter the name, token number, and score of the student {i+1}: ")
#     name, token, score = details.split()
#     names.append(name)
#     tokens.append(int(token))
#     scores.append(int(score))
#
# for i in range(num_students):
#     token = tokens[i]
#     if token > 1:
#         for j in range(2,token):
#             if token%j == 0:
#                 break
#         else:
#             print(f"Name: {names[i]}, score: {scores[i]}")


#problem 12: removing punctuation marks
# string = "Hello, World! How's it going?"
# punc = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
# result = ""
# for char in string:
#     if char not in punc:
#         result += char
# print(result)