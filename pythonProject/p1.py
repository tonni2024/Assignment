numbers = [5,10,5,20,10,12,7]
even = 0
odd = 0
for i in numbers:
    if i%2 == 0:
        even += i
    elif i%2 == 1:
        odd += i
print(f"Sum of even numbers: {even}\nSum of odd numbers: {odd}")

difference = even - odd

if difference < 1:
    even,odd = odd,even

print(f"Difference: {difference}")