import operator

OPERATOR_LIST = ["AND", "NOT", "OR", "LSHIFT", "RSHIFT"]


# Extracts symbolic equations from an input file.
def extract_symbolic_equations_from_file(input_file):
    result = {}

    for line in input_file:
        # Manipulate each line to separate LHS and RHS, and reverse so that equation reads left-to-right.
        reversed_equation = list(reversed(line.strip("\n").split(" -> ")))

        # Add each equation to the symbolic map.
        result[reversed_equation[0]] = reversed_equation[1].split(" ")

    return result


# Determines whether or not a given symbol can be converted to an integer.
def represents_int(symbol):
    try:
        int(symbol)
        return True
    except ValueError:
        return False


# Converts a list of expressions to a list of integers if possible; returns None otherwise.
def try_converting_expression_unknowns_to_ints(expression_unknowns, numeric_map):
    result = []

    for unknown in expression_unknowns:
        if represents_int(unknown):
            result.append(int(unknown))
        elif unknown in numeric_map.keys():
            result.append(numeric_map[unknown])
        else:
            return None

    return result


def apply_operator_to_expressions(expression_operator, numerical_expressions):
    if expression_operator == "AND":
        return numerical_expressions[0] & numerical_expressions[1]
    elif expression_operator == "NOT":
        return ~numerical_expressions[0]
    elif expression_operator == "OR":
        return numerical_expressions[0] | numerical_expressions[1]
    elif expression_operator == "LSHIFT":
        return operator.lshift(numerical_expressions[0], numerical_expressions[1])
    elif expression_operator == "RSHIFT":
        return operator.rshift(numerical_expressions[0], numerical_expressions[1])

    return None


def update_numeric_map_with_wholly_determined_values(symbolic_map, numeric_map):
    for symbol, expression in symbolic_map.iteritems():
        expression_unknowns = [element for element in expression if element not in OPERATOR_LIST]

        numerical_expression_values = try_converting_expression_unknowns_to_ints(expression_unknowns, numeric_map)

        if numerical_expression_values is None:
            continue

        expression_operators = [element for element in expression if element in OPERATOR_LIST]

        # ASSUMPTIONS: there is at most one operator in an expression; every expression is well-formed.
        number_of_operators = len(expression_operators)

        if number_of_operators == 0:
            numeric_map[symbol] = numerical_expression_values[0]
        elif number_of_operators == 1:
            evaluated_expression = apply_operator_to_expressions(expression_operators[0], numerical_expression_values)

            if evaluated_expression is not None:
                numeric_map[symbol] = evaluated_expression

    return numeric_map


def compute_signal_to_wire_a(input_file_name):
    # Define a map to hold numerical representations of all unknowns.
    numeric_map = {}

    with open(input_file_name) as input_file:
        # Define a map to hold symbolic forms of the equations we must solve.
        symbolic_map = extract_symbolic_equations_from_file(input_file)

        # Repeat while there are still symbols whose numerical value is unknown:
        while len(numeric_map) < len(symbolic_map):
            numeric_map = update_numeric_map_with_wholly_determined_values(symbolic_map, numeric_map)

    print "The signal provided to wire \"a\" is: " + str(numeric_map["a"])
