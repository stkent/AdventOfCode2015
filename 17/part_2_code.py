import shared_code


def count_ways_to_divide(litres, container_sizes, current_container_count):
    for index in range(len(container_sizes)):
        container_size = container_sizes[index]

        if container_size == litres:
            global_container_counts.append(current_container_count + 1)
        elif container_size < litres:
            count_ways_to_divide(litres - container_size, container_sizes[index + 1:], current_container_count + 1)


if __name__ == "__main__":
    global_container_counts = []

    shared_code.CONTAINER_SIZES.sort()
    shared_code.CONTAINER_SIZES.reverse()
    print shared_code.CONTAINER_SIZES

    count_ways_to_divide(
        litres=shared_code.LITRES_OF_EGGNOG,
        container_sizes=shared_code.CONTAINER_SIZES,
        current_container_count=0)

    global_container_counts.sort()
    print global_container_counts
