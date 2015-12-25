import shared_code
import re


if __name__ == "__main__":
    with open("replacements_input.txt") as replacements_input_file:
        substitutions = []

        for line in replacements_input_file:
            characters_to_replace = re.search("^\w+", line)
            characters_to_insert = re.search("\w+$", line)

            substitutions.append((characters_to_replace.group(0), characters_to_insert.group(0)))

        viable_molecules = shared_code.generate_all_viable_molecules_after_single_replacement(shared_code.INITIAL_MOLECULE, substitutions)

        print "The number of molecules that can be generated is: " + str(len(viable_molecules))
