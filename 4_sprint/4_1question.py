"""1 question 4 sprint"""


class Employee:
    """
    Employee class, information about employees
    """

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @staticmethod
    def from_string(s):
        firstname, lastname, salary = s.split('-')
        return Employee(firstname, lastname, int(salary))


if __name__ == '__main__':
    emp1 = Employee("Mary", "Sue", 60000)
    emp2 = Employee.from_string("John-Smith-55000")
    print(emp1.firstname)
    print(emp1.salary)
    print(emp2.firstname)


