"""4 question 5 sprint"""


class ToSmallNumberGroupError(Exception):
    """Exception class for numbers less 10"""
    def __init__(self, *args):
        self.message = args[0] if args else f"No message for exception {self.__class__.__name__}"

    def __str__(self):
        return self.message


def check_number_group(number):
    try:
        int_number = int(number)
        if int_number > 10:
            return f"Number of your group {int_number} is valid"
        else:
            raise ToSmallNumberGroupError("We obtain error:Number of your group can't be less than 10")
    except ValueError:
        return "You entered incorrect data. Please try again."
    except ToSmallNumberGroupError as small_number:
        return small_number


if __name__ == '__main__':
    print(check_number_group(4))
    print(check_number_group(59))
    print(check_number_group("25"))
    print(check_number_group("abc"))
