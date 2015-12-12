import unittest
import part_2_code


class Part2Tests(unittest.TestCase):

    def test_sum_with_first_example_input(self):
        self.assertEquals(part_2_code.compute_sum("[1,2,3]"), 6)

    def test_sum_with_second_example_input(self):
        self.assertEquals(part_2_code.compute_sum("[1,{\"c\":\"red\",\"b\":2},3]"), 4)

    def test_sum_with_third_example_input(self):
        self.assertEquals(part_2_code.compute_sum("{\"d\":\"red\",\"e\":[1,2,3,4],\"f\":5}"), 0)

    def test_sum_with_fourth_example_input(self):
        self.assertEquals(part_2_code.compute_sum("[1,\"red\",5]"), 6)
