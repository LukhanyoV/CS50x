# get the get_int function from cs50
from cs50 import get_int

# initialize variables
credit = sum_luhn = 0

# keep prompting until user gives credit card number greater than 0
while credit < 1:
    credit = get_int("Number: ")

# convert the credit card to string
credit = str(credit)

# get the length of the credit card
length = len(credit)

# apply luhn's algorithm
for i, v in enumerate(credit[::-1]):
    # check if should multiply number by 2 or not
    s = int(v) if i % 2 == 0 else int(v) * 2

    # add individual digits to total sum
    sum_luhn += (s // 10) + (s % 10)

# end of luhn algorightm

# check if credit card is valid
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
