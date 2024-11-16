# making list, its sum, avg
# n = int(input("Enter the value of n: "))
# numbers = []
# for i in range(n):
#     num = int(input(f"Enter value {i+1}: "))
#     numbers.append(num)
# print(numbers)
# sum = 0
# for i in numbers:
#     sum += i
# avg = sum/len(numbers)
# print(f"sum: {sum}, and avg: {avg:.2f}")
from string import punctuation
from zipfile import stringEndArchive64Locator

from unicodedata import digit

#removing duplicates
# n = int(input("Enter the value of n: "))
# numbers = []
# for i in range(n):
#     num = int(input(f"Enter the number {i+1}: "))
#     numbers.append(num)
# print(numbers)
# i = 0
# while i < len(numbers):
#     num = numbers[i]
#     while numbers.count(num) > 1:
#         numbers.remove(num)
#     i += 1
# print(numbers)


#string operations
# string = input("Enter the string: ")
# low = string.lower()
# print(f"Lowercase: {low}")
# vowels = "aeiou"
# count = 0
# for i in low:
#     if i in vowels:
#         count += 1
# print(f"Number of vowels: {count}")
# lists = list(string)
# lists.reverse()
# reversed = "".join(lists)
# print(f"Reversed: {reversed}")


#prime number
# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# print(f"The prime numbers are: ",end="")
# for i in range(n1,n2+1):
#     if i > 1:
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             print(f"{i}",end=" ")


#counting characters
# string = input("Enter the string: ")
# upper = 0
# lower = 0
# digits = 0
# special = 0
# for letter in string:
#     if letter.isupper():
#         upper += 1
#     elif letter.islower():
#         lower += 1
#     elif letter.isdigit():
#         digits += 1
#     else:
#         special += 1
# print(f"Upper: {upper}\nLower: {lower}\nDigit: {digits}\nSpecial: {special}")


#list flattened
# nested_list = [[1,2,3],[4,5],[6,7,8,9]]
# flattened_list = []
# for sublist in nested_list:
#     for item in sublist:
#         flattened_list.append(item)
# print(flattened_list)


#second largest
# numbers = [10,20,4,45,99]
# numbers.sort(reverse=True)
# if len(numbers) < 2:
#     print("Enter at least two numbers.")
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
#         print("Invalid")


#string compression
# string = "aaabbcc"
# compressed_string = ""
# count = 1
# for i in range(len(string)):
#     if i < len(string)-1 and string[i] == string[i+1]:
#         count += 1
#     else:
#         compressed_string += string[i] + str(count)
#         count = 1
# print(f"The compressed string is: {compressed_string}")


#cound words in a string
# string = "Hello world, this is a Python program"
# lists = string.split(" ")
# count = len(lists)
# print(count)


#palindrome
# strings = ['radar','hello','level','world','madam','python']
# print(f"Palindromes in the list: ",end="")
# for word in strings:
#     lists = list(word)
#     lists.reverse()
#     reversed = "".join(lists)
#     if word == reversed:
#         print(word,end=" ")


#lucky student
# n = int(input("Enter how many students you want to add: "))
# names = []
# tokens = []
# scores = []
# for i in range(n):
#     details = input(f"Enter name, token, score for {i+1}: ")
#     name, token, score = details.split()
#     names.append(name)
#     tokens.append(int(token))
#     scores.append(int(score))
# print(f"name: {names}, token: {tokens}, scores: {scores}")
#
# for i in range(n):
#     token = tokens[i]
#     if token > 1:
#         is_prime = True
#         for j in range(2,token):
#             if token%j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(f"name: {names[i]}, scores:{scores[i]}")


#remove punctuation
# string = "Hello, World! How's it going?"
# w_punct = ""
# punctuation = "!@#$%^&*(){}[]:\"<>?/.,';\\~`"
# for i in string:
#     if i not in punctuation:
#         w_punct += i
# print(w_punct)