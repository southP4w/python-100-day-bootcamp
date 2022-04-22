# Write a program that prints the average of five numbers (using a For Loop)

heights = [120, 135, 128, 142, 117]

total_height = 0
for h in heights:
    total_height += h
avg_height = total_height / len(heights)

print(avg_height)
