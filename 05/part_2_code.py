def contains_repeated_but_non_overlapping_pair(string):
    for i in range(len(string) - 3):
        candidate_pair = string[i:i+2]

        if candidate_pair in string[i+2:]:
            return True

    return False


def contains_repeated_letter_separated_by_single_char(string):
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            return True

    return False


def is_nice(string):
    return contains_repeated_but_non_overlapping_pair(string)\
           and contains_repeated_letter_separated_by_single_char(string)


with open("input.txt") as f:
    counter = 0

    for line in f:
        if is_nice(line):
            counter += 1

    print "There are " + str(counter) + " nice strings."
