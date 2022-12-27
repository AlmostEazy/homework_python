import unittest

from homework_9.temp import CustomError, division


class TestDivide(unittest.TestCase):

    def test_divide_equal(self):
        self.assertEqual(division(6, 2), 3)

    def test_divide_not_equal(self):
        self.assertNotEqual(division(6, 2), 5)

    def test_zero_divide(self):
        # self.assertRaises(CustomError, division, 6, 0)
        with self.assertRaises(CustomError):
            division(6, 0)

    def test_divide_not_none(self):
        self.assertIsNotNone(division(6, 2))
