import unittest
import code


class Tests(unittest.TestCase):

    def test_validity_check_with_first_example_input(self):
        self.assertFalse(code.is_valid_password("hijklmmn"))

    def test_validity_check_with_second_example_input(self):
        self.assertFalse(code.is_valid_password("abbceffg"))

    def test_validity_check_with_third_example_input(self):
        self.assertFalse(code.is_valid_password("abcddgjk"))

    def test_validity_check_with_good_password(self):
        self.assertTrue(code.is_valid_password("ddabcee"))

    def test_next_password_calculator_with_first_example_input(self):
        self.assertEqual(code.compute_next_valid_password("abcdefgh"), "abcdffaa")

    def test_next_password_calculator_with_second_example_input(self):
        self.assertEqual(code.compute_next_valid_password("ghijklmn"), "ghjaabcc")

    def test_incrementing_a(self):
        self.assertEqual(code.increment_character("a"), "b")

    def test_incrementing_z(self):
        self.assertEqual(code.increment_character("z"), "a")
