import csv
import sys


def main():

    # TODO: Check for command-line usage
    argv = sys.argv  # arguments
    argc = len(argv)  # arguments count

    # check for sufficient number of arguments
    if argc != 3:
        print("Usage: python3 dna.py [database file] [sequence file]")
        return

    # TODO: Read database file into a variable
    rows = []
    # open the file in read mode
    with open(argv[1], "r") as db:
        reader = csv.DictReader(db)  # open the csv file
        for row in reader:
            # append each row of the table in my rows list
            rows.append(row)

    # TODO: Read DNA sequence file into a variable
    sequence = ""
    # open the file in read mode
    with open(argv[2], "r") as seq:
        # read the sequence from the file and strip out trailing white spaces
        sequence = seq.read().strip()

    # TODO: Find longest match of each STR in DNA sequence
    # get list of subsequences
    # i dont want to hardcode them cause two database check for different number of things
    subsequences = list(rows[0].keys())[1:]

    # store the subsequence with its highest value as a key-value-pair in a dictionary
    anon_sequence = {}
    for subsequence in subsequences:
        # in anon_sequence store key of sequence set its value to be highest count sequence
        anon_sequence[subsequence] = longest_match(sequence, subsequence)

    # TODO: Check database for matching profiles
    for row in rows:
        # keep count of how many subsequences matched
        count = 0
        # check the values of each key in the dictionary
        for subsequence in subsequences:
            # match of the sequence given to one in the database
            if int(row[subsequence]) == anon_sequence[subsequence]:
                count += 1
        # if the number of subsequences in the database that matched
        # matched with the anon person sequence
        # then the person was found
        if len(subsequences) == count:
            print(row["name"])
            return

    # no match found
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
