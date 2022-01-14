"""6 question 1 sprint"""


def order(a):
    """
    Check list order
    :param a: list
    :return: str
    """
    if 1 < len(a) < 100 and len(a) == len(set(a)):
        if a == sorted(a):
            return "ascending"
        elif a == sorted(a, reverse=True):
            return "descending"
    else:
        return "not sorted"



if __name__ == '__main__':
    expression = [1, 7, 0, 4, 8, 1]
    res = order(expression)
    print(res)


