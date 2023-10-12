import unittest
from lab2.lab2 import min_length


class MinLengthTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(min_length(10, 4, [1, 2, 3, 4, 5, 10, 30, 40, 60, 90]), 29)

    def test2(self):
        self.assertEqual(min_length(7, 4, [15, 20, 40, 80, 90, 120, 177]), 40)

    def test_3(self):
        self.assertEqual(min_length(10, 4, [1000, 1570, 1890, 2000, 2187, 2300, 3000, 3333, 3799, 4000]), 1000)


if __name__ == '__main__':
    unittest.main()
