# Write a program for a tip calculator that tips 25% (because capitalism is bullshit and while tipping is capitalist af,
# workers unfortunately still need rely on tips to survive. So if you've got enough to go out to eat, you've got enough
# to tip 25%. Don't be a scumbag).

# i.e. If you go out to eat with 'p' people, the formula to calculate the tip would be as follows:
# tip = (total_bill / p) * 1.25

total_bill = float(input("What was the total cost of the bill?\n$"))
people = int(input("How many people ate?\n"))
tip = (total_bill / people) * 1.25
tip_per_person = tip / people

print(f"The total tip is ${round(tip, 2)}.\nThe amount each person pays is ${round(tip_per_person, 2)}")
