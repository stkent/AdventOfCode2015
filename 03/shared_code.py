import operator


def update_current_location(current_location, instruction):
    return tuple(map(operator.add, current_location,
                     {
                         "^": (0,  1),
                         ">": (1,  0),
                         "v": (0, -1),
                         "<": (-1, 0)
                     }[instruction]))


def increment_count_for_location(location, coordinate_visit_counts):
    if location not in coordinate_visit_counts:
        coordinate_visit_counts[location] = 0

    coordinate_visit_counts[location] += 1
