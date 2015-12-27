def compute_next_code(current_code):
    return (252533 * current_code) % 33554393


def update_current_coordinates(current_coordinates):
    if current_coordinates[0] == 1:
        return current_coordinates[1] + 1, 1
    else:
        return current_coordinates[0] - 1, current_coordinates[1] + 1


if __name__ == "__main__":
    target_coordinates = (3010, 3019)
    current_coordinates = (1, 1)
    current_code = 20151125

    while True:
        current_coordinates = update_current_coordinates(current_coordinates)
        current_code = compute_next_code(current_code)

        if current_coordinates == target_coordinates:
            print "The code at", target_coordinates, "is", current_code
            break
