#multiplication table of a number from 1 to 10
n = int(input("Enter a number: "))

i = 1
while i <= 10:
    multiplication = i*n
    print(f"{n} x {i} = {multiplication}")
    i += 1
