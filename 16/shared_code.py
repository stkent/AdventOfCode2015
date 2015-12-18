import re


THE_REAL_SUE_STATS = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


def parse_input_file(input_file):
    result = {}

    for line in input_file:
        sue_number = re.findall("\d+", line)[0]

        sue_data_list = re.sub("Sue \d+: ", "", line.strip("\n")).split(", ")

        # noinspection PyTypeChecker
        sue_data = dict(item.split(":") for item in sue_data_list)

        result[sue_number] = sue_data

    return result
