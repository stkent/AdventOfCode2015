import shared_code


def compute_number_of_presents_delivered(n):
    return 10 * shared_code.find_sum_of_unique_factors(n)


if __name__ == "__main__":
    house_number = 1

    while True:
        presents_delivered_to_house = compute_number_of_presents_delivered(house_number)

        if presents_delivered_to_house >= shared_code.PUZZLE_INPUT:
            print "House number: ", house_number
            break

        house_number += 1