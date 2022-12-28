import unittest

from temp import n_list


class TestList(unittest.TestCase):

    def test_list_in(self):
        my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
        self.assertIn(10, n_list(my_list))
