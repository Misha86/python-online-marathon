"""4 question 3 sprint"""


def divisor(num):
    for i in range(1, num + 1):
        if num % i == 0:
            yield i
    while True:
        yield None


if __name__ == '__main__':
    three = divisor(3)
    print(next(three))
    print(next(three))
    print(next(three))
    print(next(three))

