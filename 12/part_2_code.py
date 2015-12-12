import re


def compute_sum(string):
    print string

    for match in re.finditer(":\"red\"", string):
        object_start_index = match.span()[0]
        object_end_index = match.span()[1] - 1

        # The object we are looking to ignore may itself contain
        # other (nested) objects, so we need to account for those
        # by tracking these brace counts:
        number_of_left_braces_to_find = 1
        number_of_right_braces_to_find = 1

        while number_of_left_braces_to_find > 0:
            object_start_index -= 1

            if string[object_start_index] == "{":
                number_of_left_braces_to_find -= 1

            if string[object_start_index] == "}":
                number_of_left_braces_to_find += 1

        while number_of_right_braces_to_find > 0:
            object_end_index += 1

            if string[object_end_index] == "}":
                number_of_right_braces_to_find -= 1

            if string[object_end_index] == "{":
                number_of_right_braces_to_find += 1

        string = string[:object_start_index] + re.sub("\d", "0", string[object_start_index:object_end_index + 1]) + string[object_end_index + 1:]

    print string

    return sum([int(n) for n in re.findall("-?\d+", string)])


if __name__ == "__main__":
    with open("input.txt") as input_file:
        input_string = input_file.readline()

        print "Total sum of numbers in structure: " + str(compute_sum(input_string))
