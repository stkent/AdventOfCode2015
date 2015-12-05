import shared_code


with open("input.txt") as f:
    elf_instructions = f.readline()

    current_santa_location = (0, 0)
    coordinate_visit_counts = {current_santa_location: 1}

    for instruction in elf_instructions:
        current_santa_location = shared_code.update_current_location(current_santa_location, instruction)

        shared_code.increment_count_for_location(current_santa_location, coordinate_visit_counts)

    print len(coordinate_visit_counts)
