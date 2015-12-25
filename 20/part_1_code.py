import math


PUZZLE_INPUT = 29000000


def find_unique_factors(n):
    result = set()

    candidate = 1

    while candidate <= math.ceil(math.sqrt(n)):
        if n % candidate == 0:
            result.add(candidate)
            result.add(n / candidate)

        candidate += 1

    return result


def find_sum_of_unique_factors(n):
    return sum(find_unique_factors(n))


def compute_number_of_presents_delivered(n):
    return 10 * find_sum_of_unique_factors(n)


if __name__ == "__main__":
    house_number = 1

    while True:
        presents_delivered_to_house = compute_number_of_presents_delivered(house_number)

        if presents_delivered_to_house >= PUZZLE_INPUT:
            print "House number: ", house_number
            break

        house_number += 1