# get the get_int function from cs50
from cs50 import get_int

# initialize variables
credit = sum_luhn = 0
mod = 10
div = 1

# keep prompting until user gives credit card number greater than 0
while credit < 1:
    credit = get_int("Number: ")

# keeps track of how many numbers iterated over
count = 0

# get the length of the credit card
length = len(str(credit))

# apply luhn's algorithm
#pa
while count < length:
    # get the current number
    current = (credit % mod) // div

    # check to double number or not
    # before adding to sum
    if count % 2:
        current *= 2
        if current > 9: # add first and last digits seperately
            sum_luhn += (current % 10) + (current // 10)
        else:
            sum_luhn += current
    # add number to sum without doubling it
    else:
        sum_luhn += current
    mod *= 10
    div *= 10
    count += 1
# end of luhn algorightm

# check if credit card is valid
credit = str(credit) # convert the credit card to string
if  sum_luhn % 10 == 0:
    # check if visa and correct length
    if (length == 13 or length == 16) and credit[0] == "4": # validate length
        print("VISA")

    # check if valid mastercard and correct length
    elif length == 16 and (int(credit[0:2]) >= 51 and int(credit[0:2]) <= 55):
        print("MASTERCARD")

    # check if amex and correct length
    elif length == 15 and (credit[0:2] == "34" or credit[0:2] == "37"):
        print("AMEX")

    # passed the luhn algorith but not recognised
    else:
        print("INVALID")

# faiiled the mod 10 check
else:
    print("INVALID")
