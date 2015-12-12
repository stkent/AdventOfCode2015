import unittest
import part_1_code


class Part1Tests(unittest.TestCase):

    def test_sum_with_first_example_input(self):
        self.assertEquals(part_1_code.compute_sum("[1,2,3]"), 6)

    def test_sum_with_second_example_input(self):
        self.assertEquals(part_1_code.compute_sum("{\"a\":2,\"b\":4}"), 6)

    def test_sum_with_third_example_input(self):
        self.assertEquals(part_1_code.compute_sum("[[[3]]]"), 3)

    def test_sum_with_fourth_example_input(self):
        self.assertEquals(part_1_code.compute_sum("{\"a\":{\"b\":4},\"c\":-1}"), 3)

    def test_sum_with_fifth_example_input(self):
        self.assertEquals(part_1_code.compute_sum("{\"a\":[-1,1]}"), 0)

    def test_sum_with_sixth_example_input(self):
        self.assertEquals(part_1_code.compute_sum("[-1,{\"a\":1}]"), 0)

    def test_sum_with_seventh_example_input(self):
        self.assertEquals(part_1_code.compute_sum("[]"), 0)

    def test_sum_with_eighth_example_input(self):
        self.assertEquals(part_1_code.compute_sum("{}"), 0)
