import re


# Returns a function of three variables: instruction_index, register_value, and offset.
perform_instruction = lambda instruction_name, instruction_index, register_value, offset: {
    "hlf": lambda instruction_index, register_value, offset: (instruction_index + 1, register_value / 2),
    "tpl": lambda instruction_index, register_value, offset: (instruction_index + 1, register_value * 3),
    "inc": lambda instruction_index, register_value, offset: (instruction_index + 1, register_value + 1),
    "jmp": lambda instruction_index, register_value, offset: (instruction_index + offset, register_value),
    "jie": lambda instruction_index, register_value, offset: (instruction_index + (offset if register_value % 2 == 0 else 1), register_value),
    "jio": lambda instruction_index, register_value, offset: (instruction_index + (offset if register_value == 1 else 1), register_value)
}[instruction_name](instruction_index, register_value, offset)


if __name__ == "__main__":
    with open("input.txt") as input_file:
        parsed_instructions = []

        for line in input_file:
            parsed_instructions.append(line.strip())


        for initial_register_values in [{"a": 0, "b": 0}, {"a": 1, "b": 0}]:
            instruction_index = 0

            while instruction_index < len(parsed_instructions):
                instruction_to_execute = parsed_instructions[instruction_index]
                # print "Processing instruction #" + str(instruction_index) + ":", instruction_to_execute

                instruction_name = instruction_to_execute[:3]

                raw_instruction_register = re.search("\s[ab]", instruction_to_execute)
                instruction_register = raw_instruction_register.group(0).strip() if raw_instruction_register else None
                current_register_value = initial_register_values[instruction_register] if instruction_register else None

                raw_offset = re.search("[+-]\d+", instruction_to_execute)
                offset = int(raw_offset.group(0)) if raw_offset else None

                (updated_instruction_index, updated_register_value) = perform_instruction(
                        instruction_name, instruction_index, current_register_value, offset)

                instruction_index = updated_instruction_index

                if instruction_register:
                    initial_register_values[instruction_register] = updated_register_value

                # print "Resulting register values:", register_values

            print "For initial register values", initial_register_values, "the value in register b when the program completes is:", initial_register_values["b"]
