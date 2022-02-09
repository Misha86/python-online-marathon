"""4 question 8 sprint"""
import unittest


class TriangleNotValidArgumentException(Exception):

    def __init__(self, message="Not valid arguments"):
        self.message = message

    def __str__(self):
        return self.message


class TriangleNotExistException(Exception):

    def __init__(self, message="Can`t create triangle with this arguments"):
        self.message = message

    def __str__(self):
        return self.message


class Triangle:

    def __init__(self, sides):
        self._sides = self.check_triangle_exist(self.validate_args(sides))

    def get_area(self):
        a, b, c = self.sides
        p = sum(self.sides)/2
        S = (p * (p-a) * (p-b) * (p-c))**0.5
        return S

    @classmethod
    def validate_args(cls, sides):
        if not isinstance(sides, (list, tuple)) or len(sides) != 3 or any([isinstance(i, str) for i in sides]):
            raise TriangleNotValidArgumentException
        else:
            return sides

    @classmethod
    def check_triangle_exist(cls, sides):
        a, b, c = sides
        if any((a <= 0, b <= 0, c <= 0, a + b <= c, a + c <= b, b + c <= a)):
            raise TriangleNotExistException
        return sides

    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, value):
        self._sides = self.check_triangle_exist(self.validate_args(value))


class TriangleTest(unittest.TestCase):
    valid_test_data = [
        ((3, 4, 5), 6.0),
        ((10, 10, 10), 43.30),
        ((6, 7, 8), 20.33),
        ((7, 7, 7), 21.21),
        ((50, 50, 75), 1240.19),
        ((37, 43, 22), 406.99),
        ((26, 25, 3), 36.0),
        ((30, 29, 5), 72.0),
        ((87, 55, 34), 396.0),
        ((120, 109, 13), 396.0),
        ((123, 122, 5), 300.0)
    ]

    not_valid_triangle = [
        (1, 2, 7),
        (1, 1, 2),
        (7, 7, 15),
        (100, 7, 90),
        (17, 18, 35),
        (127, 17, 33),
        (145, 166, 700),
        (1000, 2000, 1),
        (717, 17, 7),
        (0, 7, 7),
        (-7, 7, 7)
    ]

    not_valid_arguments = [
        ('3', 4, 5),
        ('a', 2, 3),
        (7, "str", 7),
        ('1', '1', '1'),
        'string',
        (7, 2),
        (7, 7, 7, 7),
        'str',
        10,
        ('a', 'str', 7)
    ]

    def setUp(self):
        self.triangle = Triangle([3, 4, 5])

    def test_valid_data(self):
        for data in self.valid_test_data:
            self.triangle.sides = data[0]
            with self.subTest(data=data):
                self.assertAlmostEqual(self.triangle.get_area(), data[1], delta=0.01)

    def test_not_exist_triangle(self):
        for data in self.not_valid_triangle:
            with self.subTest(data=data):
                with self.assertRaises(TriangleNotExistException):
                    self.triangle.sides = data

    def test_invalid_args(self):
        for data in self.not_valid_arguments:
            with self.subTest(data=data):
                with self.assertRaises(TriangleNotValidArgumentException):
                    self.triangle.sides = data

    def test_get_area(self):
        self.assertEqual(self.triangle.get_area(), 6.0)

    def tearDown(self) -> None:
        self.triangle = None


if __name__ == '__main__':
    triangle = Triangle([3, 4, 5])
    print(triangle.get_area())

    unittest.main(verbosity=2)
