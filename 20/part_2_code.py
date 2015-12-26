import shared_code


def compute_number_of_presents_delivered(n):
    factors_with_bounded_multiplicity = shared_code.find_unique_values(
            shared_code.find_factor_pairs_with_bounded_multiplicity(n, 50))
    sum_of_factors_with_bounded_multiplicity = sum(factors_with_bounded_multiplicity)

    return 11 * sum_of_factors_with_bounded_multiplicity


if __name__ == "__main__":
    house_number = 1

    while True:
        presents_delivered_to_house = compute_number_of_presents_delivered(house_number)

        if presents_delivered_to_house >= shared_code.PUZZLE_INPUT:
            print "House number: ", house_number
            break

        house_number += 1