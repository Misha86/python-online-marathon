"""5 question 8 sprint"""
import unittest

#
# s0 = 0                                                                                                                                        # 1000 - 0 %
# s1= 0.1*(1001 - 1000)                                                                                                                # 1001 - 3000 - 10 %
# s_4000 = 0.1*(3001 - 1001)                                                                                           # 3001 - 5000 - 15 %
# s_6000 = 0.15*(5001 - 3001) + 0.1*(3001 - 1001)                                                                      # 5001 - 10000 - 21 %
# s_12000 = 0.21*(10001 - 5001) + 0.15*(5001 - 3001) + 0.1*(3001 - 1001)                                              # 10001 - 20000 - 30 %
# s_12000 = 0.3 * (20001 - 10001) + 0.21 * (10001 - 5001) + 0.15 * (5001 - 3001) + 0.1 * (3001 - 1001)                                       # 20001 - 50000 - 40 %
# s_12000 = 0.40 * (50000 - 20001) + 0.3 * (20001 - 10001) + 0.21 * (10001 - 5001) + 0.15 * (5001 - 3001) + 0.1 * (3001 - 1001)              # 20001 - 50000 - 40 %
# #                                                                                                                                          # 50000 - 47 %


class Worker:
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
        self._salary = float(self.validate_salary(salary))

    @classmethod
    def validate_salary(cls, salary):
        if salary < 0:
            raise ValueError
        else:
            return salary

    def get_tax_value(self):
        taxes = 0
        for key, value in self.data.items():
            if self.salary in range(*key):
                differens = self.salary - key[0] if self.salary != key[0] else 1
                taxes += value["percents"]*differens + value['rest_taxes']
                break
        return float(taxes)

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

    def tearDown(self) -> None:
        self.worker = None


if __name__ == '__main__':
    worker = Worker("Misha", 2000)
    print(worker.get_tax_value())

    unittest.main()


