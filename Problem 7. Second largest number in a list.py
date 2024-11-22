#finding second largest number in a list
def second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) < 2:
        return "Enter at least two numbers."
    else:
        largest = nums[0]
        second_largest = None
        for i in nums:
            if i < largest:
                second_largest = i
                break
    return second_largest

numbers = list(map(int,input("Enter numbers separated by space: ").split()))
result = second_largest_num(numbers)
if result is not None:
    print(f"Second largest number: {result}")
else:
    print("Invalid input. Second largest numbers are all same.")


