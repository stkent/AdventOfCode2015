import hashlib

# noinspection SpellCheckingInspection
PUZZLE_INPUT = "yzbqklnj"

current_suffix_guess = 1
while True:
    candidate = PUZZLE_INPUT + str(current_suffix_guess)

    hash_function = hashlib.md5()
    hash_function.update(candidate)
    hash_output = hash_function.hexdigest()

    if hash_output.startswith("000000"):
        print "Smallest suffix: " + str(current_suffix_guess)
        break

    current_suffix_guess += 1
