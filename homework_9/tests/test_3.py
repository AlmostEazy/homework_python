import unittest

from temp import my_func


class TestPow(unittest.TestCase):

    def test_pow_equal(self):
        self.assertEqual(my_func(2, -2), 0.25)

    def test_pow_not_equal(self):
        self.assertNotEqual(my_func(2, -2), 4)

    def test_pow_true(self):
        self.assertTrue(my_func(2, -2))

    def test_pow_err(self):
        with self.assertRaises(ZeroDivisionError):
            my_func(0, -2)

    def test_pow_instance(self):
        self.assertIsInstance(my_func(2, -2), float)

    def test_pow_not_instance(self):
        self.assertNotIsInstance(my_func(2, -2), str)

    def test_is_not(self):
        self.assertIsNot(2, -2)

    def test_pow_not_none(self):
        self.assertIsNotNone(my_func(2, -2))
