"""3 question 4 sprint"""


class Employee:
    """
    Employee class, information about employees
    """

    def __init__(self, full_name=None, **kwargs):
        self.full_name = full_name
        self.__dict__.update(kwargs)
        self._split_full_name()

    def _split_full_name(self):
        names = ("_firstname", "_lastname")
        splitted_full_name = dict(zip(names, (self.full_name.split()))) if self.full_name else dict.fromkeys(names)
        self.__dict__.update(splitted_full_name)

    @property
    def name(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname


if __name__ == '__main__':
    john = Employee()
    mary = Employee("Mary Major", salary=120000)
    richard = Employee("Richard Roe", salary=110000, height=178)
    giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
    print(mary.lastname)
    print(richard.height)
    print(giancarlo.nationality)
    print(john.name)


