def instruction_parser(x):
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0


def get_parsed_instructions():
    with open("input.txt") as f:
        raw_instructions = str(f.readline())

        parsed_instructions = [instruction_parser(x) for x in raw_instructions]

        return parsed_instructions
