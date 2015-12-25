import math


PUZZLE_INPUT = 29000000


def find_factor_pairs(n):
    result = []

    candidate = 1

    while candidate <= math.sqrt(n):
        if n % candidate == 0:
            result.append((candidate, n / candidate))
            result.append((n / candidate, candidate))

        candidate += 1

    return result


def find_unique_values(list_of_tuples):
    added_values = set()
    return [ factor for factor_pair in list_of_tuples for factor in factor_pair
             if not factor in added_values and not added_values.add(factor)]


def find_factor_pairs_with_bounded_multiplicity(n, max_multiplicity):
    result = []

    factor_pairs = find_factor_pairs(n)

    for factor_pair in factor_pairs:
        if factor_pair[1] <= max_multiplicity:
            result.append(factor_pair)

    return result


def compute_number_of_presents_delivered(n):
    factors_with_bounded_multiplicity = find_unique_values(find_factor_pairs_with_bounded_multiplicity(n, 50))
    sum_of_factors_with_bounded_multiplicity = sum(factors_with_bounded_multiplicity)

    return 11 * sum_of_factors_with_bounded_multiplicity


if __name__ == "__main__":
    house_number = 1

    while True:
        presents_delivered_to_house = compute_number_of_presents_delivered(house_number)
        # print house_number, presents_delivered_to_house

        if presents_delivered_to_house >= PUZZLE_INPUT:
            print "House number: ", house_number
            break

        house_number += 1