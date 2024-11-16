# numbers = list(map(int,input("Enter numbers: ").split()))
# numbers = set(numbers)
# numbers = list(numbers)
# print(f"List without duplicates: {numbers}")
# summation = 0
# for i in numbers:
#     summation += i
# print(f"Sum of all items is : {summation}")
from idlelib.debugger_r import restart_subprocess_debugger

# my_dict = {"Name":"Tonni","Age":"25","phone":"01354335"}
# for key, val in my_dict.items():

# my_dict = {"Name":"Tonni","Age":25,"phone":"01354335"}
# for i in my_dict:
#     print(f"{i}:{my_dict[i]}")

# for key, val in my_dict.items():
#     print(f"{key}:{val}")

# my_dict = {"Student1":{"Name":"Tonni","Age":25,"phone":"01354335"},
#            "Student2":{"Name":"Shakila","Age":23,"phone":"034567"},
#            "Student3":{"Name":"Echo","Age":4,"phone":"3456787654"}
# }
# # print(my_dict["Student3"]["Name"])
# # print(my_dict["Student1"]["phone"])
# # print(my_dict["Student1"]["Age"])
# for st_serial, st_info in my_dict.items():
#     for key,val in st_info.items():
#         if val["Age"] > 20:
#             print(val["Name"])


# my_dict = {
#     "Student1": {"Name": "Tonni", "Age": 25, "Phone": "01354335"},
#     "Student2": {"Name": "Shakila", "Age": 23, "Phone": "034567"},
#     "Student3": {"Name": "Echo", "Age": 4, "Phone": "3456787654"}
# }
#
# # Loop through the dictionary and print names where age is greater than 20
# for student, details in my_dict.items():
#     if details["Age"] > 20:
#         print(details["Name"])


#problem 1: mathematical operations in list
# numbers = [5,10,5,20,10]
# n = int(input("Enter how many numbers you want in your list: "))
# numbers = []
# for i in range(n):
#     num = int(input(f"Enter the number {i+1}: "))
#     numbers.append(num)
# print(numbers)
# sum = 0
# for i in numbers:
#     sum += i
# avg = sum/len(numbers)
# print(f"Sum: {sum}, and average: {avg:.2f}")


#problem 2: Removing duplicate from list
#numbers = [5,10,5,20,10]
# n = int(input("Enter how many numbers you want in your list: "))
# numbers = []
# for i in range(n):
#     num = int(input(f"Enter the number {i+1}: "))
#     numbers.append(num)
# print(numbers)
# for item in numbers:
#     while numbers.count(item) > 1:
#         numbers.remove(item)
# print(numbers)


#problem 3: String operations
# text = input("Enter the string: ")
# low = text.lower()
# print(f"Lowercase: {low}")
# count = 0
# vowels = "aeiou"
# for i in low:
#     if i in vowels:
#         count += 1
# print(f"Number of vowels: {count}")
# list = list(text)
# list.reverse()
# reverse = "".join(list)
# print(f"Reversed string: {reverse}")
#print(f"Reversed string: {text[::-1]}")


# #problem 4: Finding prime number
# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# print(f"Prime numbers between {n1} and {n2}: ",end="")
# for i in range(n1,n2+1):
#     if i > 1:
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             print(f"{i}",end=" ")


#problem 5: Count characters in a list
# text = input("Enter a string: ")
# print(f"The string: {text}")
# upper = 0
# lower = 0
# digit = 0
# special = 0
# for i in text:
#     if i.isupper():
#         upper += 1
#     elif i.islower():
#         lower += 1
#     elif i.isdigit():
#         digit += 1
#     else:
#         special += 1
# print(f"Upper letters: {upper}\nLowercase letters: {lower}\nDigits: {digit}\nSpecial characters: {special}")


#problem 6: List flattening
# nested_list = [[1,2,3],[4,5],[6,7,8,9]]
# flattened_list = []
# for sublist in nested_list:
#     for item in sublist:
#         flattened_list.append(item)
# print(flattened_list)


#problem 7: Find the second largest number in a list
# numbers = [10,20,4,45,99]
# numbers.sort(reverse=True)
# print(numbers)
#
# # second_largest = []
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
#         print("Invalid input. Second largest numbers are all same.")


#problem 8: String compression
# string = "aaabbcc"
# print(string)
# compressed_string = ""
# count = 1
# for i in range(len(string)):
#     if i < len(string)-1 and string[i] == string[i+1]:
#         count += 1
#     else:
#         compressed_string += string[i] + str(count)
#         count = 1
# print(f"Compressed string: {compressed_string}")


#problem 9: Count words in a string
# string = "Hello world, this is a Python program."
# list = string.split(" ")
# count = len(list)
# print(f"Number of words: {count}")


#problem 10: Finding Palindrome in a list
# strings = ['radar','hello','level','world','madam','python']
# palin = []
# for i in strings:
#     lists = list(i)
#     lists.reverse()
#     word = "".join(lists)
#     if i == word:
#         palin.append(i)
# print(palin)


#problem 11: Find the lucky student

