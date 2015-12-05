import shared_code


def ribbon_length_for_dimensions(dimensions):
    wrap_ribbon_length = 2*(dimensions[0] + dimensions[1])
    bow_ribbon_length = reduce(lambda x, y: x*y, dimensions, 1)
    total_ribbon_length = wrap_ribbon_length + bow_ribbon_length

    return total_ribbon_length


parsed_dimensions = shared_code.get_parsed_dimensions()

total_wrapping_paper_area = sum([ribbon_length_for_dimensions(dimensions) for dimensions in parsed_dimensions])

print "Total ribbon length: " + str(total_wrapping_paper_area)
