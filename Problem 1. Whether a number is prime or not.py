#Checking whether a number is prime or not.
def prime_finder(number):
    if number <= 1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


n = int(input("Enter a number: "))
if prime_finder(n):
    print("Prime.")
else:
    print("Not Prime.")
