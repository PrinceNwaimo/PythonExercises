import unittest
from Credit_card_validator.CardValidator import even_double_digits


class TestCredit_card_validator(unittest.TestCase):

    def test_even_double_digits(self):
        self.assertEqual(even_double_digits("5399834432138592"), 49)
        self.assertEquals(even_double_digits("12324342727"), 22)


if __name__ == '__main__':
    unittest.main()
