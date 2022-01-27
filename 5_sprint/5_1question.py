"""1 question 5 sprint"""


class MyError(Exception):
    """Raise exception for negative numbers"""

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"You input negative number: {self.data}. Try again."


def check_positive(number):
    try:
        float_number = float(number)
        if float_number > 0:
            return f"You input positive number: {float_number}"
        else:
            raise MyError(float_number)
    except ValueError:
        return "Error type: ValueError!"
    except MyError as m:
        return m


# class MyError(Exception):
#     """Raise exception for negative numbers"""
#     pass
#
#
# def check_positive(number):
#     try:
#         float_number = float(number)
#         if float_number > 0:
#             return f"You input positive number: {float_number}"
#         else:
#             raise MyError(f"You input negative number: {float_number}. Try again.")
#     except ValueError:
#         return "Error type: ValueError!"
#     except MyError as m:
#         return m


if __name__ == '__main__':
    print(check_positive(10))
    print(check_positive(-10))
    print(check_positive(11))
    print(check_positive('112'))
    print(check_positive('abc'))



