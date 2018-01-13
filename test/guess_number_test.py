import unittest
import guess_number


class GuessSystemTest(unittest.TestCase):
    def test_return_4_different_random_numbers_list(self):
        numbers = guess_number.generate_4_random_numbers()
        self.assertEqual(len(set(numbers)), len(numbers))

    def test_return_different_4_random_numbers_list_when_called_2_times(self):
        self.assertNotEqual(guess_number.generate_4_random_numbers(), guess_number.generate_4_random_numbers())

    def test_return_false_when_input_is_12345(self):
        self.assertEqual(guess_number.is_input_legal("12354"), (False, guess_number.INPUT_LENGTH_ERROR))

    def test_return_false_when_input_is_12ab(self):
        self.assertEqual(guess_number.is_input_legal("12ab"), (False, guess_number.INPUT_NOT_NUMBERS))

    def test_return_true_when_input_is_1234(self):
        self.assertEqual(guess_number.is_input_legal("1234"), (True, guess_number.INPUT_LEGAL))


class CalculateResultTest(unittest.TestCase):
    def setUp(self):
        self.ACTUAL_NUMBER = '1234'

    def test_return_4A0B_when_1234(self):
        self.assertEqual(guess_number.calculate_result('1234', self.ACTUAL_NUMBER), (4, 0))

    def test_return_3A0B_when_1235(self):
        self.assertEqual(guess_number.calculate_result('1235', self.ACTUAL_NUMBER), (3, 0))


if __name__ == '__main__':
    unittest.main()
