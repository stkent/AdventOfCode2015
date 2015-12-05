def contains_at_least_three_vowels(string):
    vowels = [char for char in string if char in ['a', 'e', 'i', 'o', 'u']]

    return len(vowels) >= 3


def contains_at_least_one_letter_twice_in_a_row(string):
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return True

    return False


def contains_no_blacklisted_strings(string):
    for blacklisted_string in ['ab', 'cd', 'pq', 'xy']:
        if blacklisted_string in string:
            return False

    return True


def is_nice(string):
    return contains_at_least_three_vowels(string)\
            and contains_at_least_one_letter_twice_in_a_row(string)\
            and contains_no_blacklisted_strings(string)


with open("input.txt") as f:
    counter = 0

    for line in f:
        if is_nice(line):
            counter += 1

    print "There are " + str(counter) + " nice strings."
