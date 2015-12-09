with open("input.txt") as input_file:

    characters_of_code = 0
    string_characters = 0
    input_file_lines = []

    for line in input_file:
        # ASSUMPTION: every line in the input file ends with a newline character.
        trimmed_line = line[:-1]

        escaped_quotes_line = trimmed_line.replace("\\", "\\\\")
        escaped_slashes_line = escaped_quotes_line.replace("\"", "\\\"")

        characters_of_code += len(trimmed_line)

        # ASSUMPTION: every manipulated string needs to start and end with double quotes.
        string_characters += (len(escaped_slashes_line) + 2)

        input_file_lines.append(trimmed_line)

    print "The character count difference is: " + str(string_characters - characters_of_code)
