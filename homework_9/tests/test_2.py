import unittest

from homework_9.temp import sum_numbers


class TestSum(unittest.TestCase):

    def test_sum_numbers_equal(self):
        self.assertEqual(sum_numbers("1"), 123)

    def test_sum_numbers_not_equal(self):
        self.assertNotEqual(sum_numbers(1), 123)

    def test_sum_numbers_instance(self):
        self.assertIsInstance(sum_numbers("1"), int)

    def test_sum_numbers_not_instance(self):
        self.assertNotIsInstance(sum_numbers("1"), str)
