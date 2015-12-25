import shared_code
import re


def reduce_molecule(current_molecule, inverted_substitutions, current_replacements_count):
    reduced_molecules = shared_code.generate_all_viable_molecules_after_single_replacement(current_molecule, inverted_substitutions)
    most_reduced_molecule = sorted(reduced_molecules, key=lambda x: len(x))
    new_replacements_count = current_replacements_count + 1

    if most_reduced_molecule is "e":
        # If reduced_molecule is 'e', we are done searching the chain.
        global_replacement_counts.add(new_replacements_count)
    else:
        reduce_molecule(most_reduced_molecule, inverted_substitutions, new_replacements_count)


if __name__ == "__main__":
    with open("replacements_input.txt") as replacements_input_file:
        global_replacement_counts = set()

        inverted_substitutions = []

        for line in replacements_input_file:
            characters_to_replace = re.search("\w+$", line)
            characters_to_insert = re.search("^\w+", line)

            inverted_substitutions.append((characters_to_replace.group(0), characters_to_insert.group(0)))

        reduce_molecule(shared_code.INITIAL_MOLECULE, inverted_substitutions, 0)
        print "Minimum number of steps to generate molecule 'e':", min(global_replacement_counts)
