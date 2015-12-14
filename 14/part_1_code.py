import shared_code


if __name__ == "__main__":
    with open("input.txt") as input_file:
        reindeer_dict = shared_code.get_parsed_input(input_file)
        distance_dict = {}

        for reindeer_name, reindeer_data in reindeer_dict.iteritems():
            (fly_speed, fly_time, rest_time) = reindeer_data

            distance_dict[reindeer_name] =\
                shared_code.compute_distance_traveled_in_time(
                    shared_code.RACE_TIME, fly_speed, fly_time, rest_time)

    print "The maximum distance traveled by a reindeer is: " + str(max(distance_dict.values())) + "km."
