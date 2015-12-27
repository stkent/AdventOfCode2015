import operator
import itertools


PACKAGE_WEIGHTS =\
    [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]


def compute_quantum_entanglement(package_weights):
    return reduce(operator.mul, package_weights)


def quantum_entanglement_comparator(group_1, group_2):
    return compute_quantum_entanglement(group_1) - compute_quantum_entanglement(group_2)


if __name__ == "__main__":
    for number_of_compartments in [3, 4]:

        group_size = sum(PACKAGE_WEIGHTS) / number_of_compartments

        current_smallest_group_size = 1

        while True:
            candidate_groups = itertools.combinations(PACKAGE_WEIGHTS, current_smallest_group_size)
            candidate_groups_of_desired_total = \
                [group for group in candidate_groups if sum(group) == group_size]

            if candidate_groups_of_desired_total:
                candidate_groups_of_desired_total.sort(cmp=quantum_entanglement_comparator)
                print "The minimum quantum entanglement for", number_of_compartments, "groups is", map(compute_quantum_entanglement, candidate_groups_of_desired_total)[0]
                break

            current_smallest_group_size += 1
