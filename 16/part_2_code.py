import shared_code
import operator


with open("input.txt") as input_file:
    for sue_number, sue_data in shared_code.parse_input_file(input_file).iteritems():

        is_real_sue = True
        for stat, measured_stat_value in shared_code.THE_REAL_SUE_STATS.iteritems():
            if stat in sue_data.keys():
                this_sue_stat_value = int(sue_data[stat])

                if stat == "cats" or stat == "trees":
                    comparison_operator = operator.gt
                elif stat == "pomeranians" or stat == "goldfish":
                    comparison_operator = operator.lt
                else:
                    comparison_operator = operator.eq

                if not comparison_operator(this_sue_stat_value, measured_stat_value):
                    is_real_sue = False

        if is_real_sue:
            print "Sue " + str(sue_number) + " is the real Sue."
