# get the get_int function from cs50
from cs50 import get_int

# initialize height as 0
height = 0

# prompt the user to enter valid height
while height < 1 or height > 8:
    height = get_int("Height: ")

# use a loop to print out pyramid of given height
for i in range(1, height + 1):
    # print out spaces and hashes on the same line
    print(" " * (height - i) + "#" * i + "  " + "#" * i)
