ON = "#"
OFF = "."


def animate_single_frame(state_matrix):
    result = []

    number_of_rows = len(state_matrix)
    number_of_columns = len(state_matrix[0])

    for row_index in range(0, number_of_rows):
        result_row = []

        for column_index in range(0, number_of_columns):
            neighbors = [state_matrix[row_index + i][column_index + j] for i in range(-1, 2) for j in range(-1, 2) if
                               abs(i) + abs(j) in [1, 2] and 0 <= row_index + i < number_of_rows and 0 <= column_index + j < number_of_columns]

            result_row.append(update_light_state(state_matrix[row_index][column_index], neighbors))

        result.append(result_row)

    return result


def update_light_state(initial_state, neighbors):
    number_of_lit_neighbors = len([neighbor for neighbor in neighbors if neighbor == ON])

    if initial_state == ON:
        return ON if number_of_lit_neighbors in [2, 3] else OFF
    if initial_state == OFF:
        return ON if number_of_lit_neighbors is 3 else OFF


if __name__ == "__main__":
    with open("part_1_input.txt") as input_file:
        state_matrix = []

        for line in input_file:
            state_matrix.append([char for char in line.strip("\n")])

        step_count = 0

        while step_count < 100:
            state_matrix = animate_single_frame(state_matrix)
            step_count += 1

        number_of_lit_lights = sum(sum([1 for light in row if light == ON]) for row in state_matrix)

        print str(number_of_lit_lights)
