def dimensions_parser(raw_dimensions):
    return sorted([int(raw_dimension) for raw_dimension in raw_dimensions.strip("\n").split("x")])


def get_parsed_dimensions():
    result = []

    with open("input.txt") as f:
        for line in f:
            raw_dimensions = str(line)

            result.append(dimensions_parser(raw_dimensions))

    return result
