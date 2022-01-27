"""3 question 5 sprint"""


def check_odd_even(number):
    try:
        res = "Entered number is odd" if number % 2 else "Entered number is even"
        return res
    except TypeError:
        return "You entered not a number."


if __name__ == '__main__':
    print(check_odd_even(24))
    print(check_odd_even(19))
    print(check_odd_even(19))
    print(check_odd_even("19"))
