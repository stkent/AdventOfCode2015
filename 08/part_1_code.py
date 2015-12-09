import re

PLACEHOLDER_STRING = "P"

with open("input.txt") as input_file:

    characters_of_code = 0
    string_characters = 0
    input_file_lines = []

    for line in input_file:
        # ASSUMPTION: every line in the input file ends with a newline character.
        trimmed_line = line[:-1]

        no_escaped_slashes_line = trimmed_line.replace("\\\\", PLACEHOLDER_STRING)
        no_escaped_quotes_line = no_escaped_slashes_line.replace("\\\"", PLACEHOLDER_STRING)
        no_hexcode_line = re.sub("\\\\x..", PLACEHOLDER_STRING, no_escaped_quotes_line)

        characters_of_code += len(trimmed_line)

        # ASSUMPTION: every string in the input file starts and ends with double quotes.
        string_characters += (len(no_hexcode_line) - 2)

        input_file_lines.append(trimmed_line)

    print "The character count difference is: " + str(characters_of_code - string_characters)
