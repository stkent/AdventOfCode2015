import re
import itertools


def compute_distance_mappings_from_file(input_file):
    locations = set()
    distance_mappings = {}

    for line in input_file:
        start_location = line.split(" ")[0]
        end_location = line.split(" ")[2]

        locations.add(start_location)
        locations.add(end_location)

        distance_between_locations = int(re.findall("\d+", line)[0])
        distance_mappings[(start_location, end_location)] = distance_between_locations
        distance_mappings[(end_location, start_location)] = distance_between_locations

    return locations, distance_mappings


if __name__ == "__main__":
    with open("input.txt") as input_file:
        (locations, distance_mappings) = compute_distance_mappings_from_file(input_file)

        path_lengths = {}

        for path in itertools.permutations(locations):
            segments = [(path[i], path[i + 1]) for i in range(0, len(locations) - 1)]
            segment_lengths = [distance_mappings[segment] for segment in segments]

            path_lengths[path] = sum(segment_lengths)

        print "The shortest path has length: " + str(min(path_lengths.values()))
        print "The longest path has length: " + str(max(path_lengths.values()))
