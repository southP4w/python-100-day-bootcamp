# Write a program that flips a coin (heads or tails)

import random

side = random.randint(0, 1)
if side == 0:
    print("Heads")
else:
    print("Tails")
