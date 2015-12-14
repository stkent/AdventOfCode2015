import shared_code


if __name__ == "__main__":
    with open("input.txt") as input_file:
        reindeer_dict = shared_code.get_parsed_input(input_file)
        leading_count_dict = {}

        for instant in range(1, shared_code.RACE_TIME + 1):
            instant_distance_dict = {}

            for reindeer_name, reindeer_data in reindeer_dict.iteritems():
                (fly_speed, fly_time, rest_time) = reindeer_data

                instant_distance_dict[reindeer_name] =\
                    shared_code.compute_distance_traveled_in_time(
                        instant, fly_speed, fly_time, rest_time)

            print instant_distance_dict

            all_leading_reindeer = [reindeer for reindeer in instant_distance_dict.keys()
                                    if instant_distance_dict[reindeer] == max(instant_distance_dict.values())]

            for leading_reindeer in all_leading_reindeer:
                if leading_reindeer not in leading_count_dict:
                    leading_count_dict[leading_reindeer] = 1
                else:
                    leading_count_dict[leading_reindeer] += 1

    print leading_count_dict
    print sum(leading_count_dict.values())

    print "The maximum point score for a reindeer is: " + str(max(leading_count_dict.values()))
