"""2 question 3 sprint"""


def create(s):
    return lambda ss: s == ss


if __name__ == '__main__':
    olha = create("Olha")
    res = olha("Olha")
    print(res)
