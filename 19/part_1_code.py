import re


initial_molecule = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"


if __name__ == "__main__":
    with open("replacements_input.txt") as replacements_input_file:
        substitutions = []
        generated_molecules = set()

        for line in replacements_input_file:
            replaced_characters = re.search("^\w+", line)
            replacing_characters = re.search("\w+$", line)

            substitutions.append((replaced_characters.group(0), replacing_characters.group(0)))

        for substitution in substitutions:
            for match in re.finditer(substitution[0], initial_molecule):
                generated_molecule = initial_molecule[:match.start()] + substitution[1] + initial_molecule[match.start() + len(substitution[0]):]
                generated_molecules.add(generated_molecule)

        print "The number of molecules that can be generated is: " + str(len(generated_molecules))