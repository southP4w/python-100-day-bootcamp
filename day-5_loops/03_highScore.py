# Write a program that prints the largest number in a list of numbers

nums = [3, 7, 2, 14, 28, 5, 11]

largest = nums[0]
for n in nums:
    if n > largest:
        largest = n

print(largest)
