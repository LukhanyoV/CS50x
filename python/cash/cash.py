# get the get_float function from cs50
from cs50 import get_float

# coins available and their values
QUARTERS = 25
DIMES = 10
NICKELS = 5
PENNIES = 1

# get the user change
change = -1
while change < 0:
    change = get_float("Change: ")

# number of coins
coins = 0

# convert the floats to integers, easier to work with
# otherwise the floats go beyond the 2 decimal place of currencies when making calculations
change = int(change * 100) # hack

# calculate number of coins used
while change > 0:
    if QUARTERS <= change:
        change -= QUARTERS
    elif DIMES <= change:
        change -= DIMES
    elif NICKELS <= change:
        change -= NICKELS
    elif PENNIES <= change:
        change -= PENNIES

    # increment the number of coins by 1
    coins += 1

# display number of coins used
print(coins)
