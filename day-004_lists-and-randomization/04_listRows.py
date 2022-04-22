row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
grid = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
while position > str(33) or position < str(11):
    position = input("Please enter a number between 11 and 33, inclusive of both: ")

row = int(position[0])
col = int(position[1])

grid[row - 1][col - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
