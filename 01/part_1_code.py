import shared_code

parsed_instructions = shared_code.get_parsed_instructions()

delivery_floor = sum(parsed_instructions)

print "Delivery floor: " + str(delivery_floor)
