import shared_code


with open("input.txt") as input_file:
    for sue_number, sue_data in shared_code.parse_input_file(input_file).iteritems():

        is_real_sue = True
        for stat, measured_stat_value in shared_code.THE_REAL_SUE_STATS.iteritems():
            if stat in sue_data.keys() and not int(sue_data[stat]) == measured_stat_value:
                is_real_sue = False

        if is_real_sue:
            print "Sue " + str(sue_number) + " is the real Sue."
