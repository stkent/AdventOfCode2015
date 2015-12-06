import re


def method_for_instruction():
    if line.startswith("turn off"):
        return lambda x: max(x - 1, 0)
    elif line.startswith("toggle"):
        return lambda x: x + 2
    elif line.startswith("turn on"):
        return lambda x: x + 1
    else:
        return lambda x: x


light_brightness_matrix = {}

for i in range(1000):
    for j in range(1000):
        light_brightness_matrix[(i, j)] = 0

with open("input.txt") as f:
    for line in f:
        stripped_coordinates = re.match("[\D]*(\d+),(\d+)[\D]*(\d+),(\d+)", line)

        method_to_apply = method_for_instruction()

        for i in range(int(stripped_coordinates.group(1)), int(stripped_coordinates.group(3)) + 1):
            for j in range(int(stripped_coordinates.group(2)), int(stripped_coordinates.group(4)) + 1):
                light_brightness_matrix[(i, j)] = method_to_apply(light_brightness_matrix[(i, j)])

    lit_light_brightness = 0

    for light_brightness in light_brightness_matrix.values():
        lit_light_brightness += light_brightness

    print "Total brightness of lit lights: " + str(lit_light_brightness)
