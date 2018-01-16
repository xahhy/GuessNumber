import unittest
from answer_generator import AnswerGenerator


class AnswerGeneratorTest(unittest.TestCase):
    def test_return_4_length_string(self):
        result = AnswerGenerator.generate()
        self.assertEqual(len(result), 4)

    def test_return_4_numbers_string(self):
        result = AnswerGenerator.generate()
        self.assertEqual(result.isdigit(), True)

    def test_return_2_different_random_string_when_called_2_times(self):
        random_number_1 = AnswerGenerator.generate()
        random_number_2 = AnswerGenerator.generate()
        self.assertNotEqual(random_number_1, random_number_2)

    def test_return_number_string_should_not_contain_same_number(self):
        result = AnswerGenerator.generate()
        result_set = set(result)
        self.assertEqual(len(result), len(result_set))


if __name__ == '__main__':
    unittest.main()
