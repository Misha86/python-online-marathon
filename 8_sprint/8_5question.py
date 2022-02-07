"""5 question 8 sprint"""
import unittest
from unittest.mock import patch, PropertyMock


class Worker2:
    data = {
        (0, 1001): {"percents": 0, "rest_taxes": 0},
        (1001, 3001): {"percents": 0.1, "rest_taxes": 0},
        (3001, 5001): {"percents": 0.15, "rest_taxes": 200},
        (5001, 10001): {"percents": 0.21, "rest_taxes": 500},
        (10001, 20001): {"percents": 0.30, "rest_taxes": 1550},
        (20001, 50001): {"percents": 0.40, "rest_taxes": 4550},
        (50001, pow(10, 20)): {"percents": 0.47, "rest_taxes": 16550.47}
    }

    def __init__(self, name, salary=0):
        self.name = name
        self._salary = self.validate_salary(salary)

    @classmethod
    def validate_salary(cls, salary):
        if salary < 0:
            raise ValueError
        else:
            return float(salary)

    def get_tax_value(self):
        taxes = 0
        for key, value in self.data.items():
            if self.salary in range(*key):
                subtraction = self.salary - key[0] if self.salary != key[0] else 1
                taxes += value["percents"]*subtraction + value['rest_taxes']
                break
        return float(taxes)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = self.validate_salary(value)


class Worker:

    data = [
        ((1001,), 0),
        ((1001, 3001), 0.1),
        ((3001, 5001), 0.15),
        ((5001, 10001), 0.21),
        ((10001, 20001), 0.30),
        ((20001, 50001), 0.40),
        ((50001, 10**10), 0.47)
    ]

    def __init__(self, name, salary=0):
        self.name = name
        self._salary = float(self.validate_salary(salary))

    @classmethod
    def validate_salary(cls, salary):
        if salary < 0:
            raise ValueError
        else:
            return salary

    def get_tax_value(self):
        taxes = 0
        if self.salary > 1000:
            for i, value in enumerate(self.data[1:], 1):
                current_percents = value[1]
                prev_percents = self.data[i-1][1]
                current_start_range = value[0][0]
                prev_start_range = self.data[i - 1][0][0]
                calculate = prev_percents * (current_start_range - prev_start_range)
                if self.salary not in range(*value[0]):
                    taxes += calculate
                else:
                    subtraction = self.salary - current_start_range if self.salary != current_start_range else 1
                    taxes += current_percents * subtraction + calculate
                    break
        return float(round(taxes) if self.salary >= 100000 else taxes)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = self.validate_salary(value)


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Misha", 100000)

    @unittest.expectedFailure
    def test_validate_salary(self):
        self.worker.salary = -1000

    def test_salary_property(self):
        self.assertEqual(self.worker.salary, 100000)

    def test_get_tax_value(self):
        self.assertEqual(self.worker.get_tax_value(), 40050.0)

    def test_salary_property_mock(self):
        with patch('__main__.Worker.salary', new_callable=PropertyMock) as mock_salary:
            mock_salary.return_value = 1000
            self.assertEqual(self.worker.salary, 1000)

    def tearDown(self) -> None:
        self.worker = None


if __name__ == '__main__':
    # worker = Worker("Misha", 100000)
    # print(worker.get_tax_value())
    #
    unittest.main()



