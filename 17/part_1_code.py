import shared_code


def count_ways_to_divide(litres, container_sizes):
    result = 0

    for index in range(len(container_sizes)):
        container_size = container_sizes[index]

        if container_size == litres:
            result += 1
        elif container_size < litres:
            result += count_ways_to_divide(litres - container_size, container_sizes[index + 1:])

    return result


if __name__ == "__main__":
    shared_code.CONTAINER_SIZES.sort()
    shared_code.CONTAINER_SIZES.reverse()

    number_of_combinations = count_ways_to_divide(
        litres=shared_code.LITRES_OF_EGGNOG,
        container_sizes=shared_code.CONTAINER_SIZES)

    print "There are " + str(number_of_combinations) + " combinations available."
