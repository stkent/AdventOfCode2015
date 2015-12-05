import shared_code
import re


with open("input.txt") as f:
    elf_instructions = f.readline()
    grouped_elf_instructions = re.findall('..', elf_instructions)

    start_location = (0, 0)
    current_santa_location = start_location
    current_robo_santa_location = start_location
    coordinate_visit_counts = {start_location: 2}

    for grouped_instruction in grouped_elf_instructions:
        current_santa_location = shared_code.update_current_location(current_santa_location, grouped_instruction[0])
        current_robo_santa_location = shared_code.update_current_location(current_robo_santa_location, grouped_instruction[1])

        shared_code.increment_count_for_location(current_santa_location, coordinate_visit_counts)
        shared_code.increment_count_for_location(current_robo_santa_location, coordinate_visit_counts)

    print len(coordinate_visit_counts)
