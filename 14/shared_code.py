import re
import math


RACE_TIME = 2503


def get_parsed_input(input_file):
    result = {}

    for line in input_file:
        name = re.match("(\w+)\s", line).group(0)
        (fly_speed, fly_time, rest_time) = [int(number) for number in re.findall("\d+", line)]
        result[name] = (fly_speed, fly_time, rest_time)

    return result


def compute_distance_traveled_in_time(number_of_seconds, fly_speed, fly_time, rest_time):
    fly_rest_cycle_time = fly_time + rest_time
    distance_traveled_per_fly_rest_cycle = fly_speed * fly_time
    number_of_complete_fly_rest_cycles = math.floor(number_of_seconds / fly_rest_cycle_time)
    distance_traveled = number_of_complete_fly_rest_cycles * distance_traveled_per_fly_rest_cycle

    extra_fly_time = number_of_seconds % fly_rest_cycle_time
    distance_traveled += fly_speed * min(fly_time, extra_fly_time)

    return distance_traveled
