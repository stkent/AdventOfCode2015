import re
import functools
import operator


def parse_ingredients_from_file(input_file):
    result = {}

    for line in input_file:
        ingredient_name = re.match("(\w+):", line).group(1).lower()
        ingredient_properties = re.findall("-?\d+", line)

        result[ingredient_name] = {
            "capacity": int(ingredient_properties[0]),
            "durability": int(ingredient_properties[1]),
            "flavor": int(ingredient_properties[2]),
            "texture": int(ingredient_properties[3]),
            "calories": int(ingredient_properties[4])
        }

    return result


def compute_cookie_score_for_combo(ingredient_dict, ingredient_quantities, calorie_restriction=None):
    if not sum(ingredient_quantities.values()) == 100:
        return 0

    if not len(ingredient_dict) == len(ingredient_quantities):
        return 0

    score_dict = {}

    for contributing_score_component in ["flavor", "capacity", "texture", "durability"]:
        component_score = 0

        for ingredient, ingredient_properties in ingredient_dict.iteritems():
            component_score += ingredient_quantities[ingredient] * ingredient_properties[contributing_score_component]

        score_dict[contributing_score_component] = max(0, component_score)

    if calorie_restriction:
        calories = 0

        for ingredient, ingredient_properties in ingredient_dict.iteritems():
            calories += ingredient_quantities[ingredient] * ingredient_properties["calories"]

        if not calories == calorie_restriction:
            return 0

    return functools.reduce(operator.mul, score_dict.values())


if __name__ == "__main__":
    with open("input.txt") as input_file:
        ingredient_dict = parse_ingredients_from_file(input_file)

        max_score = 0

        for sugar in range(1, 101):
            for sprinkles in range(1, 101):
                for candy in range(1, 101):
                    for chocolate in range(1, 101):
                        cookie_score = compute_cookie_score_for_combo(
                            ingredient_dict, {
                                "sugar": sugar,
                                "sprinkles": sprinkles,
                                "candy": candy,
                                "chocolate": chocolate}, calorie_restriction=500)

                        max_score = max(max_score, cookie_score)

        print "The maximum cookie score is: " + str(max_score)
