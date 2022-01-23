"""3 question 4 sprint"""


class Employee:
    """
    Employee class, information about employees
    """

    def __init__(self, full_name=None, **kwargs):
        self.full_name = full_name
        self.__dict__.update(kwargs)

    def _split_full_name(self):
        if self.full_name:
            spited_full_name = dict(zip(("firstname", "lastname"), (self.full_name.split())))
            return spited_full_name
        return None

    @property
    def name(self):
        return self._split_full_name().get('firstname')

    @property
    def lastname(self):
        return self._split_full_name().get('lastname')


if __name__ == '__main__':
    john = Employee("John Doe")
    mary = Employee("Mary Major", salary=120000)
    richard = Employee("Richard Roe", salary=110000, height=178)
    giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
    print(mary.lastname)
    print(richard.height)
    print(giancarlo.nationality)
    print(john.name)


