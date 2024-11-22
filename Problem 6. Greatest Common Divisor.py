#gcd of two numbers
def gcd_finder(a,b):
    while b != 0:
        a, b = b, a%b
    return a

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

result = gcd_finder(n1,n2)
print(f"The GCD of {n1} and {n2} is: {result}")
