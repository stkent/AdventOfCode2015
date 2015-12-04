import shared_code

parsed_instructions = shared_code.get_parsed_instructions()

current_floor = 0
instruction_count = 0
while current_floor >= 0:
    current_floor += parsed_instructions[instruction_count]
    instruction_count += 1

print "Instruction number that causes Santa to first enter basement: " + str(instruction_count)
