banned_characters = ["i", "o", "l"]


def is_increasing_sequence(string):
    if len(string) == 0:
        return False

    ordinal_list = [ord(character) for character in string]
    ordinal_deltas = [ordinal_list[i + 1] - ordinal_list[i] for i in range(len(ordinal_list) - 1)]

    return len(filter(lambda d: d != 1, ordinal_deltas)) == 0


def contains_increasing_sequence_of_at_least_three_characters(string):
    for i in range(len(string) - 3):
        candidate_substring = string[i:i + 3]

        if is_increasing_sequence(candidate_substring):
            return True

    return False


def contains_at_least_two_distinct_pairs(string):
    number_of_distinct_pairs = 0

    index = 0
    while index < len(string) - 1:
        if string[index] == string[index + 1]:
            number_of_distinct_pairs += 1
            index += 2
        else:
            index += 1

    return number_of_distinct_pairs >= 2


def is_valid_password(string):
    if not contains_increasing_sequence_of_at_least_three_characters(string):
        return False

    for banned_character in banned_characters:
        if banned_character in string:
            return False

    if not contains_at_least_two_distinct_pairs(string):
        return False

    return True


def increment_character(character):
    return unichr(ord('a') + (ord(character) - ord('a') + 1) % (ord('z') - ord('a') + 1))


def increment_string(string):
    result_tail = []

    index = len(string) - 1
    while index >= 0:
        result_tail.insert(0, increment_character(string[index]))

        # If we didn't just wrap from z to a, we are done incrementing this string.
        if result_tail[0] != 'a':
            break
        else:
            index -= 1

    return string[0:index] + "".join(result_tail)


def compute_next_valid_password(string):
    while not is_valid_password(string):
        string = increment_string(string)

    return string


if __name__ == '__main__':
    # current_password = "hepxcrrq"
    current_password = "hepxxzaa"

    print "The next valid password for input " + current_password +\
          " is " + compute_next_valid_password(current_password)
