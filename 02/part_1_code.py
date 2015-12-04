import shared_code


def get_wrapping_paper_area_for_dimensions(dimensions):
    surface_areas = [dimensions[0] * dimensions[1], dimensions[0] * dimensions[2], dimensions[1] * dimensions[2]]

    paper_area = 2 * sum(surface_areas) + surface_areas[0]

    return paper_area


parsed_dimensions = shared_code.get_parsed_dimensions()

total_wrapping_paper_area = sum([get_wrapping_paper_area_for_dimensions(dimensions) for dimensions in parsed_dimensions])

print "Total wrapping paper area: " + str(total_wrapping_paper_area)
