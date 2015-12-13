import re
import itertools


def compute_happiness(seating_order, happiness_dict):
    result = 0

    for i in range(len(seating_order)):
        first_guest = seating_order[i]
        second_guest = seating_order[(i + 1) % len(seating_order)]

        result += happiness_dict[(first_guest, second_guest)]
        result += happiness_dict[(second_guest, first_guest)]

    return result


with open("input.txt") as input_file:
    guest_list = set()
    happiness_dict = {}

    for line in input_file:
        # Replace instances of "lose" with negation.
        line = re.sub("lose ", "-", line)

        guest_tuple = (line.split(" ")[0], line.split(" ")[-1].strip(".\n"))

        for guest in guest_tuple:
            guest_list.add(guest)

        happiness_delta = int(re.findall("-?\d+", line)[0])
        happiness_dict[guest_tuple] = happiness_delta

    seating_order_happiness_levels = {}
    for seating_order in itertools.permutations(guest_list):
        happiness = compute_happiness(seating_order, happiness_dict)

        seating_order_happiness_levels[seating_order] = happiness

    print "Maximum happiness level: " + str(max(seating_order_happiness_levels.values()))
