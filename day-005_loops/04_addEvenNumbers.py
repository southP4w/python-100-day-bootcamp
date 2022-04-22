# Write a program that adds all the even numbers between 1 and 100, inclusive of both, using the range() function

all_evens = 0
for n in range(1, 101):
    if n % 2 == 0:
        all_evens += n
print(all_evens)
