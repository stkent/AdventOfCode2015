import re


def compute_sum(string):
    return sum([int(n) for n in re.findall("-?\d+", string)])


if __name__ == "__main__":
    with open("input.txt") as input_file:
        input_string = input_file.readline()

        print "Total sum of numbers in structure: " + str(compute_sum(input_string))
