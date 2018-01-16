import unittest
from compare_number import CompareNumber


class CompareNumberTest(unittest.TestCase):
    def setUp(self):
        self.answer = '1234'

    def test_return_4A0B_when_1234(self):
        self.assertEqual(CompareNumber.compare(self.answer, '1234'), '4A0B')

    def test_return_3A0B_when_1235(self):
        self.assertEqual(CompareNumber.compare(self.answer, '1235'), '3A0B')

    def test_return_0A4B_when_4321(self):
        self.assertEqual(CompareNumber.compare(self.answer, '4321'), '0A4B')

    def test_return_2A4B_when_1243(self):
        self.assertEqual(CompareNumber.compare(self.answer, '1243'), '2A2B')

    def test_return_0A0B_when_5678(self):
        self.assertEqual(CompareNumber.compare(self.answer, '5678'), '0A0B')

    def test_return_1A1B_when_1378(self):
        self.assertEqual(CompareNumber.compare(self.answer, '1378'), '1A1B')



if __name__ == '__main__':
    unittest.main()