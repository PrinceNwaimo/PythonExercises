import unittest
from Credit_card_validator import even_double_digits,odd_digits


class TestCredit_card_validator(unittest.TestCase):

    def test_even_double_digits(self):
        self.assertEqual(even_double_digits("5399834432138592"), 49)
        self.assertEquals(even_double_digits("12324342727"), 22)

    def test_odd_digits(self):
        self.assertEqual(odd_digits("1111111111111"), 7)
        self.assertEquals(odd_digits("3333333333333"), 21)


if __name__ == '__main__':
    unittest.main()
