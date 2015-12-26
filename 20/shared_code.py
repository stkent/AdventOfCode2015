import math


PUZZLE_INPUT = 29000000


def find_unique_values(list_of_tuples):
    added_values = set()
    return [ value for a_tuple in list_of_tuples for value in a_tuple
             if not value in added_values and not added_values.add(value)]


def find_factor_pairs(n):
    result = []

    candidate = 1

    while candidate <= math.sqrt(n):
        if n % candidate == 0:
            result.append((candidate, n / candidate))
            result.append((n / candidate, candidate))

        candidate += 1

    return result


def find_unique_factors(n):
    return find_unique_values(find_factor_pairs(n))


def find_sum_of_unique_factors(n):
    return sum(find_unique_factors(n))


def find_factor_pairs_with_bounded_multiplicity(n, max_multiplicity):
    result = []

    factor_pairs = find_factor_pairs(n)

    for factor_pair in factor_pairs:
        if factor_pair[1] <= max_multiplicity:
            result.append(factor_pair)

    return result