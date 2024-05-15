# get the get_string function from cs50
from cs50 import get_string

# prompt the user for text
text = get_string("Text: ")

# initialize variables
n_letters = n_words = n_sentences = 0

# count letter, words and sentences in text
for c in text:
    # check if is a letter
    if c.isalpha():
        n_letters += 1

    # check if is a space
    elif c.isspace():
        n_words += 1

    # check for end of sentence
    elif c == "!" or c == "." or c == "?":
        n_sentences += 1

# correct number of words
n_words += 1
# if number of senteces has the value of 0
# set the value as 1
n_sentences = n_sentences or 1

# calculate the averages
L = (n_letters / n_words) * 100
S = (n_sentences / n_words) * 100

# use Coleman-Liau index formula
index = round(0.0588 * L - 0.296 * S - 15.8)

# check the reader grade
if index < 1:
    print("Before Grade 1")
elif index > 0 and index < 16:
    print(f"Grade {index}")
else:
    print("Grade 16+")
