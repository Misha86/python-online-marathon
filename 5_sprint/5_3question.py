"""2 question 5 sprint"""


def divide(numerator, denominator):
    try:
        result = numerator/denominator
        return f"Result is {result}"
    except ZeroDivisionError:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
    except TypeError:
        return f"Value Error! You did not enter a number!"


if __name__ == '__main__':
    print(divide(10, 5))
    print(divide(5, 0))
    print(divide("25", 5))
    print(divide("abc", 9))



