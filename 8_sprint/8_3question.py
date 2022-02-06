"""2 question 8 sprint"""
import unittest


def quadratic_equation(a, b, c):
    d = b**2 - 4*a*c
    try:
        if d > 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            return x1, x2
        elif d == 0:
            x = -b / (2 * a)
            return x
        else:
            return None
    except ZeroDivisionError:
        print('error')


class QuadraticEquationTest(unittest.TestCase):

    def test_discriminant_positive(self):
        self.assertEqual(quadratic_equation(2, 1, -1), (0.5, -1.0))

    def test_discriminant_equal_zero(self):
        self.assertEqual(quadratic_equation(1, -4, 4), 2.0)

    def test_discriminant_negative(self):
        self.assertEqual(quadratic_equation(4, 1, 2), None)

    def test_exception_type_error(self):
        with self.assertRaises(TypeError):
            quadratic_equation(0, 0, "0")


if __name__ == '__main__':
    print(quadratic_equation(2, 1, -1))
    print(quadratic_equation(1, -4, 4))
    print(quadratic_equation(4, 1, 2))
    quadratic_equation(0, 0, 0)
    # unittest.main()


