import unittest
import guess_number

class GuessSystemTest(unittest.TestCase):
    def test_return_4_different_random_numbers_list(self):
        numbers = guess_number.generate_4_random_numbers()
        self.assertEqual(len(set(numbers)), len(numbers))

    def test_return_different_4_random_numbers_list_when_called_2_times(self):
        self.assertNotEqual(guess_number.generate_4_random_numbers(), guess_number.generate_4_random_numbers())


if __name__ == '__main__':
    unittest.main()
