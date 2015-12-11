import itertools


def look_and_say(current_sequence):
    result = []

    for digit, group in itertools.groupby(current_sequence):
        group_length = len(list(group))
        result.append("{}{}".format(group_length, digit))

    return ''.join(result)


initial_sequence = "1321131112"
number_of_repetitions = 50

current_sequence = initial_sequence
counter = 0

while counter < number_of_repetitions:
    current_sequence = look_and_say(current_sequence)

    counter += 1

print "After " + str(number_of_repetitions) + " repetitions, the sequence " +\
      initial_sequence + " is transformed into a sequence of length " +\
      str(len(current_sequence)) + " characters."
