"""2 question 8 sprint"""
import unittest


def divide(num_1, num_2):
    return float(num_1)/num_2


class DivideTest(unittest.TestCase):

    def test_zero_division(self):
        self.assertEqual(divide(2, 2), 1)
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_value_first_attr(self):
        with self.assertRaises(ValueError):
            divide("abc", 2)

    def test_type_second_attr(self):
        with self.assertRaises(TypeError):
            divide(1, "2")


if __name__ == '__main__':
    unittest.main()


